"""
Kaypposti l'post jay (awal dossier f posts/) f Instagram, Facebook, Pinterest w TikTok.

Kol plateforme katkhdem GHIR ila les secrets dyalha kaynin (chouf README.md).
Status dyal kol plateforme kayttsejjel f posts/<n>/status.json: ila wa7da fshlat,
run jay kay3awed ghir hiya, machi les autres.

DRY_RUN=1 -> kaybyyen chno ghadi ydir bla ma yposti walo.
"""
import base64
import json
import os
import shutil
import sys
import time
from pathlib import Path
from urllib.parse import quote

import requests

ROOT = Path(__file__).resolve().parent.parent
POSTS, READY, DONE = ROOT / "posts", ROOT / "ready", ROOT / "done"

env = os.environ.get
DRY = env("DRY_RUN", "0") == "1"
REPO = env("GITHUB_REPOSITORY", "")
BRANCH = env("BRANCH", "main")
RECYCLE = env("RECYCLE", "1") == "1"

GRAPH = "https://graph.facebook.com/v21.0"
FB_TOKEN, FB_PAGE_ID, IG_USER_ID = env("PAGE_ACCESS_TOKEN", ""), env("FB_PAGE_ID", ""), env("IG_USER_ID", "")

PIN_API = "https://api.pinterest.com/v5"
PIN_APP_ID, PIN_APP_SECRET = env("PINTEREST_APP_ID", ""), env("PINTEREST_APP_SECRET", "")
PIN_REFRESH, PIN_TOKEN = env("PINTEREST_REFRESH_TOKEN", ""), env("PINTEREST_ACCESS_TOKEN", "")
PIN_BOARD = env("PINTEREST_BOARD_ID", "")

TT_API = "https://open.tiktokapis.com/v2"
TT_KEY, TT_SECRET, TT_REFRESH = env("TIKTOK_CLIENT_KEY", ""), env("TIKTOK_CLIENT_SECRET", ""), env("TIKTOK_REFRESH_TOKEN", "")
# inbox = katwsel l TikTok k draft (nta tclicki Post f l'app). direct = katposti bou7dha (khass app mvalidiya).
TT_MODE = env("TIKTOK_MODE", "inbox")


def nat(name):
    return (int(name) if name.isdigit() else 10**6, name)


def raw_url(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    return f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{quote(rel)}"


def check(r, what):
    try:
        data = r.json()
    except Exception:
        data = {"raw": r.text[:500]}
    # Meta: {"error": {"code": 190, ...}} on failure. TikTok: {"error": {"code": "ok"}} on success.
    err = data.get("error") if isinstance(data, dict) else None
    bad_err = isinstance(err, dict) and err.get("code") not in (None, "ok")
    if r.status_code >= 400 or bad_err or (isinstance(err, str) and err):
        raise RuntimeError(f"{what}: HTTP {r.status_code} {json.dumps(data)[:500]}")
    return data


# ---------------- Instagram + Facebook (Meta Graph API) ----------------

def graph(method, path, **params):
    params["access_token"] = FB_TOKEN
    r = requests.request(method, f"{GRAPH}/{path}", data=params if method == "POST" else None,
                         params=params if method == "GET" else None, timeout=120)
    return check(r, path)


def ig_wait(cid, tries=90, delay=5):
    for _ in range(tries):
        code = graph("GET", cid, fields="status_code").get("status_code")
        if code == "FINISHED":
            return
        if code == "ERROR":
            raise RuntimeError(f"Instagram container {cid} ERROR")
        time.sleep(delay)
    raise RuntimeError(f"Instagram container {cid} timeout")


def instagram_carousel(images, caption):
    kids = [graph("POST", f"{IG_USER_ID}/media", image_url=raw_url(i), is_carousel_item="true")["id"] for i in images[:10]]
    for k in kids:
        ig_wait(k)
    c = graph("POST", f"{IG_USER_ID}/media", media_type="CAROUSEL", children=",".join(kids), caption=caption)["id"]
    ig_wait(c)
    return graph("POST", f"{IG_USER_ID}/media_publish", creation_id=c)


def instagram_reel(video, caption):
    c = graph("POST", f"{IG_USER_ID}/media", media_type="REELS", video_url=raw_url(video),
              caption=caption, share_to_feed="true")["id"]
    ig_wait(c, tries=150)
    return graph("POST", f"{IG_USER_ID}/media_publish", creation_id=c)


def facebook_photos(images, caption):
    ids = [graph("POST", f"{FB_PAGE_ID}/photos", url=raw_url(i), published="false")["id"] for i in images]
    params = {"message": caption}
    for n, pid in enumerate(ids):
        params[f"attached_media[{n}]"] = json.dumps({"media_fbid": pid})
    return graph("POST", f"{FB_PAGE_ID}/feed", **params)


def facebook_video(video, caption):
    return graph("POST", f"{FB_PAGE_ID}/videos", file_url=raw_url(video), description=caption)


# ---------------- Pinterest (API v5) ----------------

def pinterest_token():
    if PIN_REFRESH and PIN_APP_ID and PIN_APP_SECRET:
        auth = base64.b64encode(f"{PIN_APP_ID}:{PIN_APP_SECRET}".encode()).decode()
        r = requests.post(f"{PIN_API}/oauth/token", headers={"Authorization": f"Basic {auth}"},
                          data={"grant_type": "refresh_token", "refresh_token": PIN_REFRESH}, timeout=60)
        return check(r, "pinterest token")["access_token"]
    return PIN_TOKEN


def pinterest_pin(image, cfg):
    token = pinterest_token()
    body = {"board_id": PIN_BOARD, "title": cfg["pin_title"][:100], "description": cfg["pin_description"][:500],
            "link": cfg["url"], "alt_text": cfg["pin_title"][:500],
            "media_source": {"source_type": "image_url", "url": raw_url(image)}}
    r = requests.post(f"{PIN_API}/pins", headers={"Authorization": f"Bearer {token}"}, json=body, timeout=120)
    return check(r, "pinterest pin").get("id")


# ---------------- TikTok (Content Posting API) ----------------

def tiktok_token():
    r = requests.post(f"{TT_API}/oauth/token/", headers={"Content-Type": "application/x-www-form-urlencoded"},
                      data={"client_key": TT_KEY, "client_secret": TT_SECRET, "grant_type": "refresh_token",
                            "refresh_token": TT_REFRESH}, timeout=60)
    data = check(r, "tiktok token")
    if data.get("refresh_token") and data["refresh_token"] != TT_REFRESH:
        print("  [warn] TikTok 3ṭa refresh_token jdid: beddel TIKTOK_REFRESH_TOKEN f GitHub Secrets.")
    return data["access_token"]


def tiktok_video(video, caption):
    token = tiktok_token()
    size = video.stat().st_size
    if TT_MODE == "direct":
        url = f"{TT_API}/post/publish/video/init/"
        body = {"post_info": {"title": caption[:2200], "privacy_level": "PUBLIC_TO_EVERYONE",
                              "disable_comment": False, "disable_duet": False, "disable_stitch": False},
                "source_info": {"source": "FILE_UPLOAD", "video_size": size, "chunk_size": size, "total_chunk_count": 1}}
    else:
        url = f"{TT_API}/post/publish/inbox/video/init/"
        body = {"source_info": {"source": "FILE_UPLOAD", "video_size": size, "chunk_size": size, "total_chunk_count": 1}}
    r = requests.post(url, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json; charset=UTF-8"},
                      json=body, timeout=60)
    data = check(r, "tiktok init")["data"]
    up = requests.put(data["upload_url"], data=video.read_bytes(), timeout=600,
                      headers={"Content-Type": "video/mp4", "Content-Range": f"bytes 0-{size - 1}/{size}"})
    if up.status_code >= 300:
        raise RuntimeError(f"tiktok upload: HTTP {up.status_code} {up.text[:300]}")
    return data.get("publish_id")


# ---------------- Main ----------------

def enabled():
    return {
        "instagram_carousel": bool(FB_TOKEN and IG_USER_ID),
        "instagram_reel": bool(FB_TOKEN and IG_USER_ID),
        "facebook_photos": bool(FB_TOKEN and FB_PAGE_ID),
        "facebook_video": bool(FB_TOKEN and FB_PAGE_ID),
        "pinterest_pin": bool(PIN_BOARD and (PIN_TOKEN or (PIN_REFRESH and PIN_APP_ID and PIN_APP_SECRET))),
        "tiktok_video": bool(TT_KEY and TT_SECRET and TT_REFRESH),
    }


def next_folder():
    ready = lambda p: (p / "post.json").exists() and (READY / p.name / "video.mp4").exists()
    folders = sorted([p for p in POSTS.iterdir() if p.is_dir() and ready(p)], key=lambda p: nat(p.name))
    if folders:
        return folders[0]
    done = sorted([p for p in DONE.iterdir() if p.is_dir()], key=lambda p: nat(p.name))
    if RECYCLE and done and not DRY:
        print(f"posts/ khawya: kanrj3o {len(done)} posts men done/ w nbdaw men l'awal")
        for d in done:
            (d / "status.json").unlink(missing_ok=True)
            shutil.move(str(d), str(POSTS / d.name))
        return next_folder()
    return None


def main():
    folder = next_folder()
    if not folder:
        print("Ma kayn ta post wajed (khass post.json + ready/<n>/video.mp4).")
        return
    cfg = json.loads((folder / "post.json").read_text(encoding="utf-8"))
    out = READY / folder.name
    carousel = sorted((out / "carousel").glob("*.jpg"))
    video, pin = out / "video.mp4", out / "pin.jpg"
    print(f"Post {folder.name}: {cfg['product']}")

    steps = {
        "instagram_carousel": lambda: instagram_carousel(carousel, cfg["caption"]),
        "instagram_reel": lambda: instagram_reel(video, cfg["caption"]),
        "facebook_photos": lambda: facebook_photos(carousel, cfg["caption"]),
        "facebook_video": lambda: facebook_video(video, cfg["caption"]),
        "pinterest_pin": lambda: pinterest_pin(pin, cfg),
        "tiktok_video": lambda: tiktok_video(video, cfg.get("tiktok_caption", cfg["caption"])),
    }
    on = enabled()
    if not any(on.values()) and not DRY:
        print("7ta plateforme ma mconnectiya mazal (zid les secrets f GitHub). Walo ma tposta.")
        return
    status_file = folder / "status.json"
    st = json.loads(status_file.read_text()) if status_file.exists() else {}
    ok = True
    for name, fn in steps.items():
        if not on[name]:
            print(f"  [off ] {name} (ma kaynch secrets)")
            continue
        if st.get(name):
            print(f"  [skip] {name} deja tposta")
            continue
        print(f"  [run ] {name}")
        if DRY:
            continue
        try:
            res = fn()
            st[name] = True
            status_file.write_text(json.dumps(st, indent=2))
            print(f"  [ok  ] {name}: {res}")
        except Exception as e:
            ok = False
            print(f"  [FAIL] {name}: {e}", file=sys.stderr)

    if DRY:
        print("DRY RUN: walo ma tposta.")
        return
    if ok:
        status_file.unlink(missing_ok=True)
        shutil.move(str(folder), str(DONE / folder.name))
        print(f"Kml: post {folder.name} -> done/")
    else:
        print("Chi plateforme fshlat: ghadi n3awdo ghir hiya f run jay.")
        sys.exit(1)


if __name__ == "__main__":
    main()
