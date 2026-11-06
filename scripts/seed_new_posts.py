"""
Kayzid designs jdad (Desktop folders 6, 11, 13) l l'automation b7al posts 19, 20, 21.

Usage:
  python scripts/seed_new_posts.py "C:\\Users\\user\\Desktop\\lidpet\\products images\\New folder\\Automation-posts"
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TAGS_DOG = "#doglover #dogsofinstagram #dogparent #petparent #lidpet"
TAGS_CAT = "#catlover #catsofinstagram #catparent #petparent #lidpet"

POSTS = {
    # dossier f Desktop -> post f repo
    "19": {
        "src": "6",
        "priority": 6,
        "kind": "apparel",
        "board": "Pet Christmas Gifts",
        "product": "Merry Christmas From Our Pack To Yours Hoodie",
        "short_name": "Pack Christmas Hoodie",
        "price": "$43.99",
        "url": "https://lidpet.store/products/merry-christmas-from-our-pack-to-yours-hoodie-dog-cat-christmas-sweatshirt",
        "headline": ["MERRY CHRISTMAS", "FROM OUR PACK"],
        "pin_subtitle": "Dog & cat Christmas hoodie · 5 colors · S–5XL",
        "mockups": ["4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg"],
        "pin_hero": "9.png",
        "video": {
            "scenes": [
                {"image": "9.png", "top": ["Christmas photo"], "bottom": ["with the whole pack"],
                 "highlight": ["pack"], "seconds": 4.0, "focus": 0.45},
                {"image": "6.jpg", "fit": True, "top": ["Merry Christmas"], "bottom": ["from our pack to yours"],
                 "highlight": ["pack"]},
                {"image": "4.jpg", "fit": True, "bottom": ["Dog & cat lovers", "this one's for you"],
                 "highlight": ["Dog", "cat"]},
            ],
            "colors_after": 1,
        },
        "caption": "Merry Christmas from our pack to yours. 🎄🐶🐱\n\n"
                   "The cozy hoodie for the family photo, the tree, and every movie night until New Year.\n\n"
                   "🐾 Soft, warm hoodie in 5 colors · S–5XL\n"
                   "🐾 Made for dog and cat lovers\n"
                   "🐾 A Christmas gift they will actually wear\n\n"
                   "Shop now: link in bio · lidpet.store\n\n"
                   "#christmashoodie #christmasgift #giftfordoglovers #giftforcatlovers #doglover #catlover "
                   "#petparent #dogsofinstagram #catsofinstagram #lidpet",
        "tiktok_caption": "Christmas photo with the whole pack 🎄🐶🐱 Link in bio "
                          "#christmas #doglover #catlover #lidpet",
        "pin_title": "Merry Christmas From Our Pack To Yours Hoodie – Dog & Cat Christmas Sweatshirt",
        "pin_description": "Cozy Christmas hoodie for dog and cat lovers. 5 colors, sizes S–5XL. "
                           "A perfect Christmas gift for pet parents. Shop at lidpet.store.",
    },
    "20": {
        "src": "11",
        "priority": 1,
        "kind": "apparel",
        "board": "Pet Parent Gifts",
        "product": "Cat Mom Club Oversized Tee",
        "short_name": "Cat Mom Club Tee",
        "price": "$25.99",
        "url": "https://lidpet.store/products/cat-mom-oversized-tee",
        "headline": ["CAT MOM", "CLUB"],
        "pin_subtitle": "Oversized garment-dyed tee · 5 colors · S–3XL",
        "mockups": ["3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg"],
        "pin_hero": "2.png",
        "video": {
            "scenes": [
                {"image": "2.png", "top": ["Life is better"], "bottom": ["with cats."],
                 "highlight": ["cats."], "seconds": 4.0, "focus": 0.4},
                {"image": "5.jpg", "fit": True, "top": ["Official member:"], "bottom": ["Cat Mom Club"],
                 "highlight": ["Club"]},
                {"image": "3.jpg", "fit": True, "bottom": ["Soft oversized fit", "washed colors"],
                 "highlight": ["oversized"]},
            ],
            "colors_after": 1,
        },
        "caption": "Welcome to the Cat Mom Club. 🐱💕\n\n"
                   "Membership rules: your cat is the boss, and life is better with cats.\n\n"
                   "🐾 Oversized garment-dyed tee in 5 washed colors · S–3XL\n"
                   "🐾 Soft, relaxed fit for every day\n"
                   "🐾 A sweet gift for the cat lover in your life\n\n"
                   "Shop now: link in bio · lidpet.store\n\n"
                   "#catmom #catlover #catsofinstagram #catparent #oversizedtee #giftforcatlovers "
                   "#crazycatlady #petparent #catlife #lidpet",
        "tiktok_caption": "Life is better with cats 🐱 Cat Mom Club, link in bio "
                          "#catmom #cattok #catlover #lidpet",
        "pin_title": "Cat Mom Club Oversized Tee – Life Is Better With Cats Shirt",
        "pin_description": "Oversized garment-dyed tee for cat moms. 5 washed colors, sizes S–3XL. "
                           "A cute gift for cat lovers. Shop at lidpet.store.",
    },
    "21": {
        "src": "13",
        "priority": 1,
        "kind": "apparel",
        "board": "Pet Parent Gifts",
        "product": "Does Not Fetch Does Not Come When Called Tee",
        "short_name": "Does Not Fetch Tee",
        "price": "$25.99",
        "url": "https://lidpet.store/products/does-not-fetch-does-not-come-when-called-t-shirt-funny-cat-owner-tee",
        "headline": ["DOES NOT FETCH", "DOES NOT COME"],
        "pin_subtitle": "Funny cat owner tee · 4 colors · XS–2XL",
        "mockups": ["5.jpg", "6.jpg", "7.jpg", "8.jpg"],
        "pin_hero": "2.png",
        "video": {
            "scenes": [
                {"image": "2.png", "top": ["My cat:"], "bottom": ["does not fetch."],
                 "highlight": ["fetch."], "seconds": 4.0, "focus": 0.4},
                {"image": "6.jpg", "fit": True, "top": ["Does not come"], "bottom": ["when called."],
                 "highlight": ["called."]},
                {"image": "8.jpg", "fit": True, "bottom": ["Still the best", "roommate ever"],
                 "highlight": ["best"]},
            ],
            "colors_after": 1,
        },
        "caption": "Does not fetch. Does not come when called. Still perfect. 🐱\n\n"
                   "For everyone who lives with a cat who has other plans.\n\n"
                   "🐾 Soft cotton tee in 4 colors · XS–2XL\n"
                   "🐾 For cat owners with a sense of humor\n"
                   "🐾 An easy gift for any cat lover\n\n"
                   "Shop now: link in bio · lidpet.store\n\n"
                   "#catlover #catsofinstagram #funnycat #catowner #catparent #funnytshirt "
                   "#giftforcatlovers #petparent #catlife #lidpet",
        "tiktok_caption": "My cat does not fetch. Does not come when called. Still perfect 🐱 Link in bio "
                          "#cattok #funnycat #catlover #lidpet",
        "pin_title": "Does Not Fetch Does Not Come When Called Tee – Funny Cat Owner Shirt",
        "pin_description": "Funny tee for cat owners whose cat has other plans. 4 colors, sizes XS–2XL. "
                           "A great gift for cat lovers. Shop at lidpet.store.",
    },
}


def main():
    src_root = Path(sys.argv[1])
    for n, cfg in POSTS.items():
        cfg = dict(cfg)
        src = src_root / cfg.pop("src")
        dst = ROOT / "posts" / n
        if (ROOT / "done" / n).exists():
            print(f"skip {n}: deja f done/")
            continue
        dst.mkdir(parents=True, exist_ok=True)
        for f in src.iterdir():
            if f.is_file() and f.suffix.lower() in (".jpg", ".jpeg", ".png"):
                shutil.copy2(f, dst / f.name)
        names = {f.name for f in dst.iterdir()}
        used = set(cfg["mockups"]) | {cfg["pin_hero"]} | {s["image"] for s in cfg["video"]["scenes"]}
        missing = used - names
        if missing:
            sys.exit(f"post {n}: ma kaynach {sorted(missing)}")
        (dst / "post.json").write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"ok post {n}: {cfg['product']}")


if __name__ == "__main__":
    main()
