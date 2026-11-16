"""
Kayzid 2 posts dyal Noël l'automation:
  22 = Santa Paws ornament (l'produit li 3lih l'ad daba), 23 = Merry Christmas Ya Filthy Cat Hoodie (Product 17).

Usage:
  python scripts/seed_xmas_posts.py "<Desktop Product 17 folder>" "<session ornament/ads/src folder>" "<session ornament/ads folder>"
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ORN_URL = "https://lidpet.store/products/santa-paws-personalized-pet-ornament"
CAT_URL = "https://lidpet.store/products/merry-christmas-ya-filthy-cat-hoodie-funny-cat-christmas-sweatshirt"

POSTS = {
    "22": {
        "files": {  # repo name -> (folder key, source file)
            "1.jpg": ("orn_src", "m2.jpg"),   # cadeau + sapin
            "2.jpg": ("orn_src", "m1.jpg"),   # produit sur blanc
            "3.jpg": ("orn_src", "m3.jpg"),   # bureau
            "4.jpg": ("orn_src", "m4.jpg"),   # suspendu
            "5.jpg": ("orn_ads", "ad-square-names-1080.jpg"),
        },
        "cfg": {
            "priority": 9,
            "kind": "gear",
            "board": "Pet Christmas Gifts",
            "product": "Santa Paws Personalized Pet Ornament",
            "short_name": "Santa Paws Ornament",
            "price": "$22",
            "url": ORN_URL,
            "headline": ["SANTA PAWS", "WITH THEIR NAME"],
            "pin_subtitle": "Personalized paw ornament · Free US shipping",
            "mockups": ["1.jpg", "5.jpg", "3.jpg", "4.jpg"],
            "pin_hero": "1.jpg",
            "video": {
                "fit": True,
                "scenes": [
                    {"image": "1.jpg", "fit": False, "top": ["The gift every pet mom"], "bottom": ["will hang every year"],
                     "highlight": ["every", "year"], "seconds": 4.0, "focus": 0.45},
                    {"image": "2.jpg", "top": ["Their name."], "bottom": ["Their ornament."], "highlight": ["name.", "ornament."]},
                    {"image": "3.jpg", "fit": False, "top": ["One for your pup,"], "bottom": ["one for a friend"],
                     "highlight": ["pup,", "friend"], "focus": 0.5},
                ],
                "colors_after": 9,
            },
            "caption": "Every pet deserves a spot on the tree. \U0001F384\U0001F43E\n\n"
                       "Santa Paws is a paw-shaped Christmas ornament personalized with your dog's or cat's name.\n\n"
                       "\U0001F43E Their name, printed just for them\n"
                       "\U0001F69A FREE US shipping\n"
                       "\U0001F381 Buy 2, save 15% · 3+, save 20%\n\n"
                       "Order by Dec 5 for Christmas delivery. Shop: link in bio · lidpet.store\n\n"
                       "#christmasornament #personalizedornament #petornament #dogornament #catornament "
                       "#giftfordogmom #giftforcatlovers #petparent #christmasgift #lidpet",
            "tiktok_caption": "Their name. Their ornament. \U0001F384\U0001F43E Link in bio "
                              "#christmasornament #dogmom #catmom #lidpet",
            "pin_title": "Santa Paws Personalized Pet Ornament – Dog & Cat Name Christmas Ornament 2026",
            "pin_description": "Paw-shaped metal Christmas ornament personalized with your pet's name. "
                               "Free US shipping, buy 2 save 15%. A sweet gift for dog and cat lovers. Shop at lidpet.store.",
        },
    },
    "23": {
        "files": {
            "1.png": ("p17", "Cozy Christmas Couple in Matching Cat Hoodies.png"),
            "4.jpg": ("p17", "unisex-heavy-blend-hoodie-red-front-6abe61f9cc2fb.jpg"),
            "5.jpg": ("p17", "unisex-heavy-blend-hoodie-sand-front-6abe61f9cc33b.jpg"),
            "6.jpg": ("p17", "unisex-heavy-blend-hoodie-ash-front-6abe61f9cbe29.jpg"),
            "7.jpg": ("p17", "unisex-heavy-blend-hoodie-graphite-heather-front-6abe61f9cc37b.jpg"),
            "8.jpg": ("p17", "unisex-heavy-blend-hoodie-navy-front-6abe61f9cc2ab.jpg"),
        },
        "cfg": {
            "priority": 8,
            "kind": "apparel",
            "board": "Pet Christmas Gifts",
            "product": "Merry Christmas Ya Filthy Cat Hoodie",
            "short_name": "Ya Filthy Cat Hoodie",
            "price": "$43.99",
            "url": CAT_URL,
            "headline": ["MERRY CHRISTMAS", "YA FILTHY CAT"],
            "pin_subtitle": "Funny cat Christmas hoodie · 5 colors · S–5XL",
            "mockups": ["4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg"],
            "pin_hero": "1.png",
            "video": {
                "scenes": [
                    {"image": "1.png", "top": ["Matching for Christmas"], "bottom": ["(the cat approves)"],
                     "highlight": ["Christmas", "approves)"], "seconds": 4.0, "focus": 0.35},
                    {"image": "4.jpg", "fit": True, "top": ["Merry Christmas,"], "bottom": ["ya filthy cat"],
                     "highlight": ["filthy", "cat"]},
                    {"image": "5.jpg", "fit": True, "bottom": ["Cat lovers,", "this one's for you"], "highlight": ["Cat"]},
                ],
                "colors_after": 1,
            },
            "caption": "Merry Christmas, ya filthy cat. \U0001F384\U0001F431\n\n"
                       "The most honest Christmas message in any house with a cat in it. Warm fleece, low standards, unconditional love.\n\n"
                       "\U0001F43E Cozy hoodie in 5 colors · S–5XL\n"
                       "\U0001F43E Matching his & hers Christmas look\n"
                       "\U0001F43E A gift every cat lover will actually wear\n\n"
                       "Shop now: link in bio · lidpet.store\n\n"
                       "#catlover #catsofinstagram #christmashoodie #funnycat #catmom #catdad "
                       "#christmasgift #giftforcatlovers #matchingoutfits #lidpet",
            "tiktok_caption": "Merry Christmas, ya filthy cat \U0001F384\U0001F431 Link in bio "
                              "#cattok #christmas #catlover #lidpet",
            "pin_title": "Merry Christmas Ya Filthy Cat Hoodie – Funny Cat Christmas Sweatshirt",
            "pin_description": "Funny Christmas hoodie for cat lovers. 5 colors, sizes S–5XL. "
                               "A matching couple gift for Christmas. Shop at lidpet.store.",
        },
    },
}


def main():
    src = {"p17": Path(sys.argv[1]), "orn_src": Path(sys.argv[2]), "orn_ads": Path(sys.argv[3])}
    for n, spec in POSTS.items():
        if (ROOT / "done" / n).exists():
            print(f"skip {n}: deja f done/")
            continue
        dst = ROOT / "posts" / n
        dst.mkdir(parents=True, exist_ok=True)
        for name, (key, fname) in spec["files"].items():
            shutil.copy2(src[key] / fname, dst / name)
        cfg = spec["cfg"]
        used = set(cfg["mockups"]) | {cfg["pin_hero"]} | {s["image"] for s in cfg["video"]["scenes"]}
        missing = used - {f.name for f in dst.iterdir()}
        if missing:
            sys.exit(f"post {n}: ma kaynach {sorted(missing)}")
        (dst / "post.json").write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"ok post {n}: {cfg['product']}")


if __name__ == "__main__":
    main()
