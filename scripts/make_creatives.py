"""
Kat9ad les creatives dyal kol post men les tsawer li f posts/<n>/ :
  ready/<n>/carousel/01.jpg ...   -> Instagram + Facebook (ga3 les tsawer, 4:5)
  ready/<n>/video.mp4             -> TikTok + Instagram Reel + Facebook video (9:16)
  ready/<n>/pin.jpg               -> Pinterest (2:3)

Kol post khasso post.json (smiya, prix, lien, text dyal vidéo...). Chouf README.md.

Usage:
  python scripts/make_creatives.py            # ga3 les posts li ma 3endhomch ready/
  python scripts/make_creatives.py 3 7        # ghir posts 3 w 7
  python scripts/make_creatives.py --force 1  # 3awed 9ad post 1
"""
import json
import math
import os
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "posts"
READY = ROOT / "ready"
ASSETS = ROOT / "assets"
LOGO = ASSETS / "logo.png"

# Brand (lidpet-styles-v2.css)
CREAM = (243, 234, 215)
INK = (22, 22, 22)
WHITE = (255, 255, 255)
GOLD = (228, 161, 27)
GOLD_DARK = (143, 98, 11)

FONT_BLACK = str(ASSETS / "fonts" / "Poppins-Black.ttf")
FONT_BOLD = str(ASSETS / "fonts" / "Poppins-Bold.ttf")
FONT_REG = str(ASSETS / "fonts" / "Poppins-Regular.ttf")

IMG_EXT = (".png", ".jpg", ".jpeg", ".webp")
FPS, VW, VH = 30, 1080, 1920


def font(path, size):
    return ImageFont.truetype(path, size)


def nat(name):
    stem = Path(name).stem
    return (int(stem) if stem.isdigit() else 10**6, name.lower())


def load_config(folder: Path) -> dict:
    cfg = json.loads((folder / "post.json").read_text(encoding="utf-8"))
    cfg.setdefault("skip_images", [])
    return cfg


def images_of(folder: Path, cfg: dict):
    names = [f.name for f in folder.iterdir() if f.suffix.lower() in IMG_EXT]
    names = [n for n in names if n not in cfg["skip_images"]]
    order = cfg.get("image_order")
    if order:
        return [n for n in order if n in names] + sorted([n for n in names if n not in order], key=nat)
    # lifestyle (png) 9bel mockups (jpg), b ra9m
    return sorted(names, key=lambda n: (0 if n.lower().endswith(".png") else 1, nat(n)))


def mockups_of(folder, cfg):
    """Tsawer dyal les couleurs: men post.json ("mockups"), ola ga3 les .jpg li machi f les scenes."""
    if cfg.get("mockups"):
        return cfg["mockups"]
    used = {sc["image"] for sc in cfg["video"]["scenes"]}
    return [n for n in images_of(folder, cfg) if n.lower().endswith(".jpg") and n not in used]


def load(folder, name):
    return Image.open(folder / name).convert("RGB")


def logo(width):
    lg = Image.open(LOGO).convert("RGBA")
    return lg.resize((width, int(lg.height * width / lg.width)), Image.LANCZOS)


def logo_badge(width):
    """Logo 3la badge cream bach yban 7ta f tsawer k7lin ola m3emrin."""
    lg = logo(width)
    px, py = width // 7, width // 12
    badge = Image.new("RGBA", (lg.width + px * 2, lg.height + py * 2), (0, 0, 0, 0))
    ImageDraw.Draw(badge).rounded_rectangle((0, 0, badge.width - 1, badge.height - 1),
                                            radius=badge.height // 2, fill=CREAM + (235,))
    badge.paste(lg, (px, py), lg)
    return badge


def text_center(draw, cx, y, text, fnt, fill):
    l, t, r, b = draw.textbbox((0, 0), text, font=fnt)
    draw.text((cx - (r - l) // 2 - l, y - t), text, font=fnt, fill=fill)


def fit_font(draw, text, path, size, max_w):
    while size > 20:
        f = font(path, size)
        l, _, r, _ = draw.textbbox((0, 0), text, font=f)
        if r - l <= max_w:
            return f
        size -= 2
    return font(path, size)


# ---------------- Carousel (Instagram / Facebook) ----------------

def make_carousel(folder, cfg, out):
    """Ga3 les tsawer kif homa, f 4:5 (Instagram kay9ṭe3 kolchi 3la format dyal l'awla)."""
    d = out / "carousel"
    d.mkdir(parents=True, exist_ok=True)
    for old in d.glob("*.jpg"):
        old.unlink()
    for i, name in enumerate(images_of(folder, cfg)[:10], 1):
        canvas = Image.new("RGB", (1080, 1350), CREAM)
        im = ImageOps.contain(load(folder, name), (1080, 1350), Image.LANCZOS)
        canvas.paste(im, ((1080 - im.width) // 2, (1350 - im.height) // 2))
        canvas.save(d / f"{i:02d}.jpg", quality=92)


# ---------------- Pinterest pin ----------------

def make_pin(folder, cfg, out):
    W, H = 1000, 1500
    imgs = images_of(folder, cfg)
    hero_name = cfg.get("pin_hero") or cfg["video"]["scenes"][0]["image"]
    mockups = mockups_of(folder, cfg)[:4]
    img = Image.new("RGB", (W, H), CREAM)
    hero = load(folder, hero_name)
    hz = cfg.get("pin_hero_zoom", 1.0)  # >1 kay9ṭe3 text li deja f tswira
    if hz > 1:
        cw, ch = hero.width / hz, hero.height / hz
        hero = hero.crop(((hero.width - cw) / 2, (hero.height - ch) / 2, (hero.width + cw) / 2, (hero.height + ch) / 2))
    img.paste(ImageOps.fit(hero, (W, 860), Image.LANCZOS, centering=(0.5, 0.3)), (0, 0))
    d = ImageDraw.Draw(img)
    lg = logo_badge(130)
    img.paste(lg, (36, 32), lg)
    l1, l2 = cfg["headline"]
    text_center(d, W // 2, 895, l1, fit_font(d, l1, FONT_BLACK, 68, W - 80), INK)
    text_center(d, W // 2, 985, l2, fit_font(d, l2, FONT_BLACK, 52, W - 80), GOLD_DARK)
    text_center(d, W // 2, 1062, cfg["pin_subtitle"], fit_font(d, cfg["pin_subtitle"], FONT_REG, 28, W - 80), INK)
    tile, gap = 220, 20
    x0 = (W - (tile * len(mockups) + gap * (len(mockups) - 1))) // 2
    for i, n in enumerate(mockups):
        img.paste(ImageOps.fit(load(folder, n), (tile, tile), Image.LANCZOS, centering=(0.5, 0.42)),
                  (x0 + i * (tile + gap), 1120))
    label = f"{cfg['price']}  ·  Shop at lidpet.store"
    f = font(FONT_BLACK, 34)
    l, t, r, b = d.textbbox((0, 0), label, font=f)
    bw, bh = r - l + 56, b - t + 28
    x, y = (W - bw) // 2, H - 118
    d.rounded_rectangle((x, y, x + bw, y + bh), radius=bh // 2, fill=GOLD)
    d.text((x + 28 - l, y + 14 - t), label, font=f, fill=INK)
    img.save(out / "pin.jpg", quality=92)


# ---------------- Video (TikTok / Reels) ----------------

def ease_out_back(t):
    t = min(max(t, 0.0), 1.0)
    return 1 + 2.70158 * (t - 1) ** 3 + 1.70158 * (t - 1) ** 2


def caption_box(lines, highlight=(), size=74):
    """Style dyal TikTok: blocs byad, ktaba k7la, kelmat mohimmin b gold."""
    f = font(FONT_BLACK, size)
    probe = ImageDraw.Draw(Image.new("RGB", (8, 8)))
    # ila kan ster twil bzaf, nsghrou l'font
    while max(probe.textlength(ln, font=f) for ln in lines) > VW - 160 and size > 40:
        size -= 4
        f = font(FONT_BLACK, size)
    pad_x, pad_y, gap = 32, 14, 10
    rows = []
    for ln in lines:
        l, t, r, b = probe.textbbox((0, 0), ln, font=f)
        rows.append((ln, r - l, b - t, l, t))
    bw = max(w for _, w, _, _, _ in rows) + pad_x * 2
    bh = sum(h + pad_y * 2 for _, _, h, _, _ in rows) + gap * (len(rows) - 1)
    box = Image.new("RGBA", (bw, bh), (0, 0, 0, 0))
    d = ImageDraw.Draw(box)
    hl = {w.lower() for w in highlight}
    y = 0
    for ln, w, h, l, t in rows:
        x = (bw - (w + pad_x * 2)) // 2
        d.rounded_rectangle((x, y, x + w + pad_x * 2, y + h + pad_y * 2), radius=22, fill=WHITE)
        cx = x + pad_x - l
        for word in ln.split(" "):
            color = GOLD if word.strip(".,?!:").lower() in hl else INK
            d.text((cx, y + pad_y - t), word, font=f, fill=color)
            cx += probe.textlength(word + " ", font=f)
        y += h + pad_y * 2 + gap
    return box


def paste_pop(frame, box, t_local, center_y, delay):
    p = (t_local - delay) / 0.28
    if p <= 0:
        return
    s = 0.6 + 0.4 * ease_out_back(p)
    b = box.resize((max(1, int(box.width * s)), max(1, int(box.height * s))), Image.BILINEAR)
    if p < 1:
        b.putalpha(b.getchannel("A").point(lambda a: int(a * min(1, p * 1.4))))
    frame.paste(b, ((VW - b.width) // 2, int(center_y - b.height / 2)), b)


def zoom(img, t, z0, z1, pan, anchor=(0.5, 0.5)):
    """anchor = fin kaykoun l'centre dyal zoom (0..1). 0.3 = l'jiha lisriya / l'fo9."""
    z = z0 + (z1 - z0) * t
    cw, ch = VW / z, VH / z
    cx = cw / 2 + anchor[0] * (VW - cw) + pan[0] * t * (VW - cw) / 2
    cy = ch / 2 + anchor[1] * (VH - ch) + pan[1] * t * (VH - ch) / 2
    return img.resize((VW, VH), Image.BILINEAR, box=(cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2))


def video_scenes(folder, cfg):
    """Scenes men post.json -> video.scenes. Kol scene: image, top (text fo9), bottom (text lta7t)."""
    fill = lambda n, fy, fx=0.5: ImageOps.fit(load(folder, n), (VW, VH), Image.LANCZOS, centering=(fx, fy))
    v = cfg["video"]
    scenes = []
    pans = [(0, -0.3), (0.3, 0), (0, 0.2), (-0.3, 0)]
    for i, sc in enumerate(v["scenes"]):
        caps = []
        if sc.get("top"):
            caps.append((caption_box(sc["top"], sc.get("highlight", [])), 0.1, 0.15))
        if sc.get("bottom"):
            caps.append((caption_box(sc["bottom"], sc.get("highlight", [])), 0.8 if sc.get("top") else 0.2, 0.74))
        # "zoom": [debut, fin] > 1 kay9ṭe3 l'text li deja mktoub 3la tswira (fo9 w lta7t)
        z = tuple(sc.get("zoom", [1.0, 1.12]))
        scenes.append(dict(img=fill(sc["image"], sc.get("focus", 0.35), sc.get("focus_x", 0.5)), dur=sc.get("seconds", 3.8),
                           pan=(0, 0) if z[0] > 1.05 else pans[i % 4], caps=caps, z=z,
                           anchor=(sc.get("zoom_x", 0.5), sc.get("zoom_y", 0.5))))
        if i == v.get("colors_after", 1):
            mockups = mockups_of(folder, cfg)[:6]
            label = caption_box([v.get("colors_text", "Pick your color")], ["color"])
            for n in mockups:
                scenes.append(dict(img=fill(n, 0.45), dur=0.9, pan=(0, 0), caps=[(label, -1, 0.16)], z=(1.04, 1.04)))
    scenes.append(dict(end=True, dur=3.5))
    return scenes


def end_card(cfg, tl):
    frame = Image.new("RGB", (VW, VH), CREAM)
    d = ImageDraw.Draw(frame)
    lg = logo(440)
    frame.paste(lg, ((VW - lg.width) // 2, 470), lg)
    text_center(d, VW // 2, 790, cfg["short_name"], fit_font(d, cfg["short_name"], FONT_BLACK, 80, VW - 120), INK)
    text_center(d, VW // 2, 905, cfg["price"], font(FONT_BLACK, 124), GOLD)
    s = 1 + 0.05 * math.sin(tl * 2 * math.pi * 1.5)
    btn = caption_box(["Link in bio"], (), 70)
    btn = btn.resize((int(btn.width * s), int(btn.height * s)), Image.BILINEAR)
    frame.paste(btn, ((VW - btn.width) // 2, 1160), btn)
    text_center(d, VW // 2, 1340, "lidpet.store", font(FONT_BOLD, 50), INK)
    return frame


def make_video(folder, cfg, out):
    path = out / "video.mp4"
    ff = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{VW}x{VH}",
         "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "21",
         "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(path)],
        stdin=subprocess.PIPE)
    lg = logo_badge(180)
    for si, s in enumerate(video_scenes(folder, cfg)):
        n = int(s["dur"] * FPS)
        for k in range(n):
            t, tl = k / max(1, n - 1), k / FPS
            if s.get("end"):
                frame = end_card(cfg, tl)
            else:
                frame = zoom(s["img"], t, s["z"][0], s["z"][1], s["pan"], s.get("anchor", (0.5, 0.5))).convert("RGB")
                for box, delay, yfrac in s["caps"]:
                    if delay < 0:
                        frame.paste(box, ((VW - box.width) // 2, int(VH * yfrac - box.height / 2)), box)
                    else:
                        paste_pop(frame, box, tl, VH * yfrac, delay)
                frame.paste(lg, (56, 110), lg)
            if k < 3 and si > 0 and s["dur"] > 1:
                frame = Image.blend(frame, Image.new("RGB", (VW, VH), WHITE), 0.5 - k * 0.16)
            ff.stdin.write(frame.tobytes())
    ff.stdin.close()
    if ff.wait() != 0:
        raise RuntimeError("ffmpeg fshl f " + str(folder))


def build(folder: Path):
    cfg = load_config(folder)
    out = READY / folder.name
    out.mkdir(parents=True, exist_ok=True)
    make_carousel(folder, cfg, out)
    make_pin(folder, cfg, out)
    make_video(folder, cfg, out)
    print(f"[ok] {folder.name}: carousel + pin + video")


def main(argv):
    force = "--force" in argv
    wanted = [a for a in argv if not a.startswith("--")]
    folders = sorted([p for p in POSTS.iterdir() if p.is_dir()], key=lambda p: nat(p.name))
    for f in folders:
        if wanted and f.name not in wanted:
            continue
        if not (f / "post.json").exists():
            print(f"[skip] {f.name}: ma kaynch post.json")
            continue
        if (READY / f.name / "video.mp4").exists() and not force:
            continue
        build(f)


if __name__ == "__main__":
    main(sys.argv[1:])
