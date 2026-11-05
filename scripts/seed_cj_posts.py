"""One-time helper: writes posts/11..18/post.json for the 8 CJ products (Christmas items first).
Edit the JSON files directly afterwards; this script is only kept as a record."""
import json
from pathlib import Path

POSTS = Path(__file__).resolve().parent.parent / "posts"
S = "https://lidpet.store/products/"
DOG = "#doglover #dogsofinstagram #dogparent #petparent #christmasgifts #giftfordoglovers #dogchristmas #lidpet"
CAT = "#catlover #catsofinstagram #catparent #petparent #giftforcatlovers #lidpet"
PET = "#doglover #catlover #petparent #dogsofinstagram #catsofinstagram #petgifts #lidpet"
XMAS = "\n\n🎄 Order by December 10 for Christmas delivery."


def write(n, **c):
    c.setdefault("board", "Pet Christmas Gifts")
    c["video"].setdefault("fit", True)
    (POSTS / str(n) / "post.json").write_text(json.dumps(c, indent=2, ensure_ascii=False), encoding="utf-8")
    print("wrote", n)


write(11, priority=5, product="Cat Advent Calendar – 24 Days of Toys", short_name="Cat Advent Calendar", price="$29.99",
      url=S + "cat-advent-calendar-24-toys", headline=["CAT ADVENT", "CALENDAR"],
      pin_subtitle="24 surprise toys · one for every day of December",
      image_order=["04.jpg", "02.jpg", "06.jpg", "01.jpg", "07.jpg", "05.jpg", "03.jpg"],
      mockups=["01.jpg", "07.jpg", "05.jpg", "03.jpg"],
      video={"scenes": [
          {"image": "04.jpg", "top": ["POV:"], "bottom": ["your cat gets a gift", "every day of December"], "highlight": ["cat", "gift"], "seconds": 4.0},
          {"image": "02.jpg", "top": ["24 doors."], "bottom": ["24 surprise toys."], "highlight": ["24"]},
          {"image": "06.jpg", "bottom": ["Order by Nov 18", "to start Dec 1"], "highlight": ["nov", "18"]}],
          "colors_after": 1, "colors_text": "Inside the box"},
      caption="You count down to Christmas. Now your cat can too. 🎄🐱\n\n24 doors, 24 surprise toys, one for every day of December.\n\n🎁 A gift every cat person will love\n📦 Order by November 18 to have it before December 1\n\nShop now: link in bio · lidpet.store\n\n" + CAT + " #christmasgifts #adventcalendar",
      tiktok_caption="POV: your cat gets a gift every day of December 🎄🐱 Link in bio #cattok #adventcalendar #catsoftiktok #christmasgifts #lidpet",
      pin_title="Cat Advent Calendar – 24 Days of Christmas Cat Toys",
      pin_description="A Christmas countdown for your cat: 24 surprise toys, one for every day of December. A perfect gift for cat lovers. Order by November 18. Shop at lidpet.store.")

write(12, priority=4, product="Christmas Elk & Tree Knit Dog Sweater", short_name="Christmas Dog Sweater", price="$24.99",
      url=S + "christmas-dog-sweater-elk-tree", headline=["CHRISTMAS", "DOG SWEATER"],
      pin_subtitle="Cozy knit sweater for dogs · Elk or Christmas Tree",
      image_order=["01.jpg", "05.jpg", "03.jpg", "02.jpg", "04.jpg", "06.jpg"],
      mockups=["02.jpg", "04.jpg", "06.jpg", "03.jpg"],
      video={"scenes": [
          {"image": "01.jpg", "top": ["Your dog in"], "bottom": ["the family", "Christmas photo"], "highlight": ["christmas"], "seconds": 4.0},
          {"image": "05.jpg", "top": ["Soft knit."], "bottom": ["Warm walks."], "highlight": ["warm"]},
          {"image": "03.jpg", "bottom": ["Elk or Tree", "XS to XXL"], "highlight": ["xxl"]}],
          "colors_after": 1, "colors_text": "Pick your style"},
      caption="The family Christmas photo just got a new star. 🎄🐶\n\nA soft knit sweater that keeps your dog warm on winter walks and camera-ready for the holidays.\n\n🐾 Elk or Christmas Tree design\n🐾 Sizes XS–XXL" + XMAS + "\n\nShop now: link in bio · lidpet.store\n\n" + DOG + " #dogsweater",
      tiktok_caption="Your dog in the family Christmas photo 🎄🐶 Link in bio #dogtok #dogsweater #christmasdog #lidpet",
      pin_title="Christmas Dog Sweater – Elk and Christmas Tree Knit for Dogs",
      pin_description="A cozy knit Christmas sweater for dogs in Elk or Christmas Tree design, sizes XS–XXL. The holiday photo outfit your dog will actually wear. Shop at lidpet.store.")

write(13, priority=3, product="Santa Legs Hat for Dogs & Cats", short_name="Santa Hat for Pets", price="$14.99",
      url=S + "santa-hat-for-dogs-cats", headline=["SANTA HAT", "FOR DOGS & CATS"],
      pin_subtitle="The funniest Christmas hat for your pet",
      image_order=["02.jpg", "03.jpg", "06.jpg", "04.jpg", "05.jpg", "01.jpg"],
      mockups=["03.jpg", "04.jpg", "05.jpg", "06.jpg"],
      video={"scenes": [
          {"image": "02.jpg", "top": ["When Santa gets"], "bottom": ["stuck in the chimney"], "highlight": ["santa"], "seconds": 4.0},
          {"image": "03.jpg", "top": ["Santa legs hat"], "bottom": ["for dogs & cats"], "highlight": ["dogs", "cats"]},
          {"image": "06.jpg", "bottom": ["The Christmas photo", "your pet was born for"], "highlight": ["christmas"]}],
          "colors_after": 9},
      caption="When Santa gets stuck in the chimney… 🎅😂\n\nThe funniest Christmas hat for dogs and cats. Soft, comfy and made for holiday photos.\n\n🐾 Adjustable strap · fits small dogs and cats" + XMAS + "\n\nShop now: link in bio · lidpet.store\n\n" + PET + " #funnypets #christmaspets",
      tiktok_caption="When Santa gets stuck in the chimney 🎅😂 Link in bio #dogtok #cattok #funnypets #christmas #lidpet",
      pin_title="Funny Santa Legs Christmas Hat for Dogs and Cats",
      pin_description="A funny Santa legs hat for dogs and cats. Soft, adjustable and perfect for Christmas photos. Shop at lidpet.store.")

write(14, priority=2, product="Christmas Plaid Bandana, Hat & Bow Tie", short_name="Christmas Pet Plaid", price="$12.99",
      url=S + "christmas-plaid-pet-bandana-hat-bow-tie", headline=["CHRISTMAS", "PLAID FOR PETS"],
      pin_subtitle="Bandana, hat or bow tie · for dogs & cats",
      image_order=["02.jpg", "01.jpg", "08.jpg", "03.jpg", "05.jpg", "04.jpg", "06.jpg", "07.jpg"],
      mockups=["01.jpg", "03.jpg", "05.jpg", "08.jpg"],
      video={"scenes": [
          {"image": "02.jpg", "top": ["Holiday look:"], "bottom": ["unlocked."], "highlight": ["unlocked."], "seconds": 4.0},
          {"image": "01.jpg", "top": ["Red plaid"], "bottom": ["bandana"], "highlight": ["plaid"]},
          {"image": "03.jpg", "bottom": ["Bandana, hat", "or bow tie"], "highlight": ["bow", "tie"]}],
          "colors_after": 1, "colors_text": "Pick your style"},
      caption="Holiday look: unlocked. 🎄❤️\n\nClassic red plaid for dogs and cats. Choose a bandana, a Santa hat or a dapper bow tie.\n\n🐾 6 festive styles · easy to put on" + XMAS + "\n\nShop now: link in bio · lidpet.store\n\n" + PET + " #dogbandana",
      tiktok_caption="Holiday look: unlocked 🎄 Link in bio #dogtok #cattok #dogbandana #christmaspets #lidpet",
      pin_title="Christmas Plaid Pet Bandana, Hat and Bow Tie",
      pin_description="Red plaid and snowflake Christmas bandanas, hats and bow ties for dogs and cats. Under $15. Shop at lidpet.store.")

write(15, priority=1, product="Christmas Squeaky Plush Dog Toy", short_name="Christmas Plush Toy", price="$9.99",
      url=S + "christmas-squeaky-plush-dog-toy", headline=["NAUGHTY OR NICE?", "CHRISTMAS TOYS"],
      pin_subtitle="Squeaky Christmas plush toys for dogs",
      skip_images=["02.jpg"],
      image_order=["03.jpg", "05.jpg", "07.jpg", "01.jpg", "04.jpg", "06.jpg", "08.jpg"],
      mockups=["01.jpg", "04.jpg", "07.jpg", "05.jpg"],
      video={"scenes": [
          {"image": "03.jpg", "top": ["Naughty"], "bottom": ["or nice?"], "highlight": ["nice?"], "seconds": 4.0},
          {"image": "05.jpg", "top": ["Squeaky"], "bottom": ["Christmas toys"], "highlight": ["christmas"]},
          {"image": "07.jpg", "bottom": ["The stocking stuffer", "your dog will love"], "highlight": ["dog"]}],
          "colors_after": 1, "colors_text": "Pick a toy"},
      caption="Naughty or nice? Your dog gets a gift either way. 🎁🐶\n\nSoft squeaky Christmas plush toys: Santa, Naughty and Nice bones.\n\n🐾 From $9.99 · the perfect stocking stuffer" + XMAS + "\n\nShop now: link in bio · lidpet.store\n\n" + DOG + " #dogtoys",
      tiktok_caption="Naughty or nice? Your dog gets a gift either way 🎁 Link in bio #dogtok #dogtoys #christmas #lidpet",
      pin_title="Christmas Squeaky Plush Dog Toys – Naughty or Nice",
      pin_description="Squeaky Christmas plush toys for dogs: Santa, Naughty and Nice bones. The perfect stocking stuffer from $9.99. Shop at lidpet.store.")

write(16, board="Pet Parent Gifts", product="Foldable Cat Play Tunnel", short_name="Cat Play Tunnel", price="$19.99",
      url=S + "foldable-cat-play-tunnel", headline=["CAT PLAY", "TUNNEL"],
      pin_subtitle="Foldable crinkle tunnel · hours of hide-and-seek",
      skip_images=["07.jpg"],  # another brand name (Dr.DC) on the photo
      image_order=["03.jpg", "02.jpg", "06.jpg", "05.jpg", "04.jpg", "08.jpg", "11.jpg", "12.jpg", "01.jpg", "09.jpg"],
      mockups=["04.jpg", "08.jpg", "11.jpg", "12.jpg"],
      video={"scenes": [
          {"image": "03.jpg", "top": ["Zoomies:"], "bottom": ["activated."], "highlight": ["activated."], "seconds": 4.0},
          {"image": "02.jpg", "top": ["Hide."], "bottom": ["Pounce. Repeat."], "highlight": ["pounce."]},
          {"image": "06.jpg", "bottom": ["Folds flat", "when playtime is over"], "highlight": ["flat"]}],
          "colors_after": 1, "colors_text": "Pick a style"},
      caption="Zoomies: activated. 🐱💨\n\nA crinkly cat tunnel for hiding, pouncing and zooming. It folds flat when playtime is over.\n\n🐾 6 styles · hanging toy included\n\nShop now: link in bio · lidpet.store\n\n" + CAT + " #cattoys",
      tiktok_caption="Zoomies: activated 🐱💨 Link in bio #cattok #cattoys #catsoftiktok #lidpet",
      pin_title="Foldable Cat Play Tunnel with Hanging Toy",
      pin_description="A crinkly, collapsible cat tunnel with hanging toys. Hours of hide-and-seek, then it folds flat. Shop at lidpet.store.")

write(17, board="Pet Parent Gifts", product="Motion-Activated Moving Tail Cat Toy", short_name="Smart Cat Toy", price="$49.99",
      url=S + "motion-activated-moving-tail-cat-toy", headline=["SMART", "CAT TOY"],
      pin_subtitle="Moving tail that wakes up when your cat comes near",
      image_order=["05.jpg", "07.jpg", "01.jpg", "03.jpg", "04.jpg", "02.jpg", "06.jpg"],
      mockups=["02.jpg", "04.jpg", "03.jpg"],
      video={"scenes": [
          {"image": "05.jpg", "top": ["For the cat who is"], "bottom": ["bored when you leave"], "highlight": ["bored"], "seconds": 4.0},
          {"image": "07.jpg", "top": ["The tail moves"], "bottom": ["when your cat comes near"], "highlight": ["cat"]},
          {"image": "01.jpg", "bottom": ["USB rechargeable.", "No batteries."], "highlight": ["rechargeable."]}],
          "colors_after": 9},
      caption="For the cat who is bored the minute you leave. 🐱\n\nThe tail starts wiggling when your cat walks by, then changes direction to wake up the hunter inside.\n\n🐾 Motion sensor · USB rechargeable\n\nShop now: link in bio · lidpet.store\n\n" + CAT + " #indoorcats",
      tiktok_caption="For the cat who is bored when you leave 🐱 Link in bio #cattok #cattoys #indoorcats #lidpet",
      pin_title="Motion-Activated Moving Tail Smart Cat Toy",
      pin_description="A rechargeable smart cat toy with a wiggling tail that moves when your cat comes near. Keeps indoor cats busy. Shop at lidpet.store.")

write(18, board="Pet Parent Gifts", product="Peekaboo Cat Tunnel Bed", short_name="Peekaboo Cat Bed", price="$59.99",
      url=S + "peekaboo-cat-tunnel-bed", headline=["PEEKABOO", "CAT TUNNEL BED"],
      pin_subtitle="Play tunnel and cozy bed in one",
      image_order=["01.jpg", "03.jpg", "08.jpg", "02.jpg", "04.jpg", "06.jpg", "07.jpg", "05.jpg"],
      mockups=["02.jpg", "04.jpg", "06.jpg", "08.jpg"],
      video={"scenes": [
          {"image": "01.jpg", "top": ["Part tunnel."], "bottom": ["Part nap spot."], "highlight": ["nap"], "seconds": 4.0},
          {"image": "03.jpg", "top": ["Peekaboo holes"], "bottom": ["for surprise attacks"], "highlight": ["attacks"]},
          {"image": "08.jpg", "bottom": ["Play and sleep", "in one place"], "highlight": ["sleep"]}],
          "colors_after": 9},
      caption="Part tunnel, part hideout, part nap spot. 😻\n\nA soft donut tunnel bed with peekaboo holes for ambushes and a cozy center for the nap after.\n\n🐾 Fits cats up to 22 lbs · washable mat\n\nShop now: link in bio · lidpet.store\n\n" + CAT + " #catbed",
      tiktok_caption="Part tunnel. Part nap spot 😻 Link in bio #cattok #catbed #catsoftiktok #lidpet",
      pin_title="Peekaboo Cat Tunnel Bed – Plush Donut Tunnel for Cats",
      pin_description="A soft donut-shaped tunnel bed with peekaboo holes. Your cat can play, hide and nap in one spot. Shop at lidpet.store.")
