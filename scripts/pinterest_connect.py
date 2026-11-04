"""
Kayrbeṭ Pinterest b l'automation (kaykhdem f PC dyalk, machi f GitHub).

1. Kay7ell Pinterest f browser: nta kat3ṭi l'accès l l'app dyalk.
2. Kayjib refresh token + kaybyyen les boards dyalk.
3. Kayzid les secrets f GitHub (PINTEREST_APP_ID, PINTEREST_APP_SECRET,
   PINTEREST_REFRESH_TOKEN, PINTEREST_BOARD_ID) bla ma ybanou f l'écran.
4. --demo: kay9ad board + pin dyal tjriba f Pinterest SANDBOX (l vidéo demo).

App ID w App secret kayt9raw men fichier .env (machi men chat):
  PINTEREST_APP_ID=...
  PINTEREST_APP_SECRET=...

Usage:
  python scripts/pinterest_connect.py --env "C:\\path\\text.env" --repo owner/repo [--demo]
"""
import argparse
import base64
import http.server
import secrets as pysecrets
import subprocess
import sys
import threading
import urllib.parse
import webbrowser

import requests

REDIRECT = "http://localhost:8085/"
SCOPES = "boards:read,boards:write,pins:read,pins:write,user_accounts:read"
API = "https://api.pinterest.com/v5"
SANDBOX = "https://api-sandbox.pinterest.com/v5"


def read_env(path):
    vals = {}
    for line in open(path, encoding="utf-8-sig"):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            vals[k.strip()] = v.strip().strip('"').strip("'")
    return vals


def get_code(app_id):
    state = pysecrets.token_urlsafe(16)
    box = {}

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            if q.get("state", [""])[0] != state:
                self.send_response(400); self.end_headers(); self.wfile.write(b"Bad state"); return
            box["code"] = q.get("code", [""])[0]
            box["error"] = q.get("error", [""])[0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<h2>Lidpet: Pinterest connecté ✅</h2><p>Rje3 l terminal.</p>".encode())

        def log_message(self, *a):
            pass

    srv = http.server.HTTPServer(("localhost", 8085), Handler)
    threading.Thread(target=srv.handle_request, daemon=True).start()
    url = "https://www.pinterest.com/oauth/?" + urllib.parse.urlencode({
        "client_id": app_id, "redirect_uri": REDIRECT, "response_type": "code",
        "scope": SCOPES, "state": state})
    print("7ell Pinterest f browser... (ila ma t7ellch, copier had l'lien):\n" + url + "\n")
    webbrowser.open(url)
    while "code" not in box and "error" not in box:
        threading.Event().wait(0.5)
    srv.server_close()
    if not box.get("code"):
        sys.exit(f"Pinterest refusa: {box.get('error')}")
    return box["code"]


def token_request(app_id, secret, data):
    auth = base64.b64encode(f"{app_id}:{secret}".encode()).decode()
    r = requests.post(f"{API}/oauth/token", headers={"Authorization": f"Basic {auth}"}, data=data, timeout=60)
    if r.status_code >= 400:
        sys.exit(f"Token error: HTTP {r.status_code} {r.text[:300]}")
    return r.json()


def set_secret(repo, name, value):
    subprocess.run(["gh", "secret", "set", name, "-R", repo], input=value.encode(), check=True,
                   stdout=subprocess.DEVNULL)
    print(f"  ✓ GitHub secret {name}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--demo", action="store_true")
    a = ap.parse_args()

    env = read_env(a.env)
    app_id, secret = env.get("PINTEREST_APP_ID"), env.get("PINTEREST_APP_SECRET")
    if not app_id or not secret:
        sys.exit("Zid PINTEREST_APP_ID w PINTEREST_APP_SECRET f " + a.env)

    code = get_code(app_id)
    tok = token_request(app_id, secret, {"grant_type": "authorization_code", "code": code,
                                         "redirect_uri": REDIRECT, "continuous_refresh": "true"})
    access, refresh = tok["access_token"], tok.get("refresh_token", "")
    H = {"Authorization": f"Bearer {access}"}

    me = requests.get(f"{API}/user_account", headers=H, timeout=60).json()
    print(f"\nConnecté: @{me.get('username')} ({me.get('account_type')})")

    if a.demo:
        print("\nDemo (SANDBOX): kan9ad board w pin dyal tjriba...")
        b = requests.post(f"{SANDBOX}/boards", headers=H, json={"name": "Lidpet Gifts (demo)"}, timeout=60)
        print("  board:", b.status_code, b.json().get("name", b.text[:200]))
        board_id = b.json().get("id")
        pin = requests.post(f"{SANDBOX}/pins", headers=H, timeout=120, json={
            "board_id": board_id, "title": "Good Mood Sponsored By My Dog Tee – Funny Dog Lover Shirt",
            "description": "A funny, soft cotton tee for dog people. Shop at lidpet.store.",
            "link": "https://lidpet.store/products/unisex-t-shirt-13",
            "media_source": {"source_type": "image_url",
                             "url": f"https://raw.githubusercontent.com/{a.repo}/main/ready/1/pin.jpg"}})
        print("  pin:", pin.status_code, pin.json().get("id", pin.text[:300]))
        print("  (Hada pin dyal tjriba f SANDBOX, machi visible f Pinterest.)")

    boards = requests.get(f"{API}/boards", headers=H, params={"page_size": 50}, timeout=60).json().get("items", [])
    print("\nLes boards dyalk:")
    for i, bd in enumerate(boards, 1):
        print(f"  {i}. {bd['name']}")
    board_id = ""
    if boards:
        pick = input("\nRa9m dyal board fin ytposṭaw les pins (Enter = 1): ").strip() or "1"
        board_id = boards[int(pick) - 1]["id"]
    else:
        print("Ma kayn 7ta board: dir board f Pinterest w 3awed.")

    print("\nKanzid les secrets f GitHub...")
    set_secret(a.repo, "PINTEREST_APP_ID", app_id)
    set_secret(a.repo, "PINTEREST_APP_SECRET", secret)
    if refresh:
        set_secret(a.repo, "PINTEREST_REFRESH_TOKEN", refresh)
    else:
        set_secret(a.repo, "PINTEREST_ACCESS_TOKEN", access)
    if board_id:
        set_secret(a.repo, "PINTEREST_BOARD_ID", board_id)
    print("\nSalina ✅")


if __name__ == "__main__":
    main()
