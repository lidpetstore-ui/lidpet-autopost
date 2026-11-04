"""One-time helper: writes posts/<n>/post.json for the first batch of posts.
Edit the JSON files directly afterwards; this script is only kept as a record."""
import json
from pathlib import Path

POSTS = Path(__file__).resolve().parent.parent / "posts"
STORE = "https://lidpet.store/products/"

DOG_TAGS = "#doglover #dogsofinstagram #dogparent #petparent #dogowner #funnytshirt #giftfordoglovers #lidpet"
CAT_TAGS = "#catlover #catsofinstagram #catparent #petparent #catowner #funnytshirt #giftforcatlovers #lidpet"


def post(n, **kw):
    d = POSTS / str(n)
    cfg = {
        "board": "Lidpet – Gifts for Pet Lovers",
        **kw,
    }
    (d / "post.json").write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8")
    print("wrote", d / "post.json")


post(1,
     product="Good Mood Sponsored By My Dog Tee", short_name="Good Mood Tee", price="$23.99",
     url=STORE + "unisex-t-shirt-13",
     headline=["GOOD MOOD", "SPONSORED BY MY DOG"],
     pin_subtitle="Funny dog lover tee · a gift for every dog person",
     mockups=["4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg"],
     video={"scenes": [
         {"image": "2.png", "top": ["POV:"], "bottom": ["your dog is the reason", "you're in a good mood"], "highlight": ["dog"], "seconds": 4.0},
         {"image": "3.png", "top": ["Good mood?"], "bottom": ["Sponsored by", "my dog."], "highlight": ["dog."]},
         {"image": "1.png", "bottom": ["The tee every", "dog lover needs"], "highlight": ["dog", "lover"]}],
         "colors_after": 1},
     caption="Good mood? Sponsored by my dog. 🐶☀️\n\nSome people need coffee. We just need a wag at the door.\n\n🐾 Soft cotton tee in 7 colors · XS–2XL\n🐾 A gift every dog person will actually wear\n\nShop now: link in bio · lidpet.store\n\n" + DOG_TAGS + " #goldenretriever #goodvibes",
     tiktok_caption="POV: your dog is the reason you're in a good mood 🐶 Link in bio 🛒 #dogtok #doglover #goldenretriever #funnytshirt #lidpet",
     pin_title="Good Mood Sponsored By My Dog Tee – Funny Dog Lover Shirt",
     pin_description="A funny, soft cotton tee for dog people whose best days start with a wag. 7 colors, sizes XS–2XL. A great gift for golden retriever lovers and every dog owner. Shop at lidpet.store.")

post(2,
     product="Best Cat Ever? Yeah, That Was Me Tee", short_name="Best Cat Ever Tee", price="$25.99",
     url=STORE + "best-cat-ever-yeah-that-was-me-t-shirt-funny-cat-lover-sarcastic-tee",
     headline=["BEST CAT EVER?", "YEAH, THAT WAS ME"],
     pin_subtitle="Funny cat lover tee · a gift for every cat person",
     mockups=["4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg"],
     video={"scenes": [
         {"image": "3.jpg", "top": ["POV:"], "bottom": ["your cat thinks", "this shirt is about them"], "highlight": ["cat"], "seconds": 4.0},
         {"image": "2.jpg", "top": ["Best cat ever?"], "bottom": ["Yeah.", "That was me."], "highlight": ["me."]},
         {"image": "1.jpg", "bottom": ["The tee every", "cat lover needs"], "highlight": ["cat", "lover"]}],
         "colors_after": 1},
     caption="Best cat ever? Yeah, that was me. 😼\n\nFor everyone who knows exactly who runs the house.\n\n🐾 Soft cotton tee in 6 colors · XS–2XL\n🐾 The perfect gift for any cat person\n\nShop now: link in bio · lidpet.store\n\n" + CAT_TAGS + " #sarcasticshirt #catsoftiktok",
     tiktok_caption="Best cat ever? Yeah, that was me 😼 Link in bio 🛒 #cattok #catlover #funnytshirt #catsoftiktok #lidpet",
     pin_title="Best Cat Ever Yeah That Was Me Tee – Funny Cat Lover Shirt",
     pin_description="A sarcastic, soft cotton tee for cat people. 6 colors, sizes XS–2XL. A great gift for any cat owner. Shop at lidpet.store.")

post(3,
     product="California Golden Retriever Sunglasses Tee", short_name="California Golden Tee", price="$21.99",
     url=STORE + "california-golden-retriever-sunglasses-dog-tee",
     headline=["GOOD VIBES.", "DOG STYLE."],
     pin_subtitle="Retro golden retriever tee · for every golden lover",
     mockups=["4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg"],
     video={"scenes": [
         {"image": "2.png", "top": ["Good vibes."], "bottom": ["Dog style."], "highlight": ["dog"], "seconds": 4.0},
         {"image": "1.png", "top": ["POV:"], "bottom": ["your golden has", "more style than you"], "highlight": ["golden"]},
         {"image": "3.png", "bottom": ["The tee every", "golden lover needs"], "highlight": ["golden", "lover"]}],
         "colors_after": 1},
     caption="Good vibes. Dog style. 😎🐶\n\nA retro California golden retriever, sunglasses on, ready for the weekend.\n\n🐾 Soft cotton tee in 5 colors · XS–2XL\n🐾 A gift every golden lover will love\n\nShop now: link in bio · lidpet.store\n\n" + DOG_TAGS + " #goldenretriever #goldensofinstagram #california",
     tiktok_caption="Good vibes, dog style 😎 Link in bio 🛒 #goldenretriever #dogtok #doglover #funnytshirt #lidpet",
     pin_title="California Golden Retriever Sunglasses Tee – Retro Dog Lover Shirt",
     pin_description="A retro California golden retriever tee with sunglasses and a cap. 5 colors, sizes XS–2XL. A great gift for golden retriever lovers. Shop at lidpet.store.")

post(4,
     product="My Favorite Child Has 4 Legs Hoodie", short_name="My Favorite Child Hoodie", price="$35.99",
     url=STORE + "my-favorite-child-has-4-legs-pet-parent-hoodie",
     headline=["MY FAVORITE CHILD", "HAS 4 LEGS"],
     pin_subtitle="Cozy pet parent hoodie · a gift for every pet lover",
     mockups=["5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg"],
     video={"scenes": [
         {"image": "2.png", "top": ["Asked who my", "favorite child is?"], "bottom": ["Easy.", "Four legs."], "highlight": ["four"], "seconds": 4.0},
         {"image": "1.png", "bottom": ["Cozy hoodie for", "proud pet parents"], "highlight": ["pet", "parents"]},
         {"image": "4.png", "bottom": ["Same love.", "More paws."], "highlight": ["paws."]}],
         "colors_after": 1},
     caption="My favorite child has 4 legs. 🐾\n\nNo explanation needed. Every pet parent gets it.\n\n🧡 Cozy hoodie in 5 colors · S–3XL\n🧡 The gift for the pet parent who has everything\n\nShop now: link in bio · lidpet.store\n\n#petparent #doglover #catlover #dogsofinstagram #catsofinstagram #hoodieseason #giftforpetlovers #lidpet",
     tiktok_caption="Asked who my favorite child is? Easy. Four legs 🐾 Link in bio #petparent #dogtok #cattok #hoodie #lidpet",
     pin_title="My Favorite Child Has 4 Legs Hoodie – Funny Pet Parent Sweatshirt",
     pin_description="A cozy hoodie for proud dog and cat parents. 5 colors. A perfect Christmas gift for pet lovers. Shop at lidpet.store.")

post(5,
     product="Dogs Before Dudes Tee", short_name="Dogs Before Dudes Tee", price="$23.99",
     url=STORE + "dogs-before-dudes-funny-dog-lover-tee",
     headline=["DOGS BEFORE", "DUDES"],
     pin_subtitle="Funny dog lover tee · because the dog comes first",
     mockups=["5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg"],
     video={"scenes": [
         {"image": "4.png", "top": ["My dog", "comes first."], "bottom": ["No debate."], "highlight": ["dog"], "seconds": 4.0},
         {"image": "2.png", "top": ["Dogs before"], "bottom": ["dudes."], "highlight": ["dudes."]},
         {"image": "1.png", "bottom": ["Some relationships", "just come first"], "highlight": ["first"]}],
         "colors_after": 1},
     caption="Dogs before dudes. 🐶❤️\n\nSome relationships just come first.\n\n🐾 Soft cotton tee in 5 colors · XS–2XL\n🐾 For anyone whose dog is their favorite person\n\nShop now: link in bio · lidpet.store\n\n" + DOG_TAGS,
     tiktok_caption="My dog comes first. No debate 🐶 Link in bio #dogtok #doglover #funnytshirt #lidpet",
     pin_title="Dogs Before Dudes Tee – Funny Dog Lover Shirt",
     pin_description="A funny dog lover tee for people whose dog always comes first. 5 colors, sizes XS–2XL. Shop at lidpet.store.")

post(6,
     product="Best Friends Forever Oversized Tee", short_name="Best Friends Forever Tee", price="$37.99",
     url=STORE + "best-friends-forever-oversized-tee",
     headline=["BEST FRIENDS", "FOREVER"],
     pin_subtitle="Oversized dog & cat tee · for pet best friends",
     mockups=["5.jpg", "7.jpg", "9.jpg", "4.jpg"],
     video={"scenes": [
         {"image": "1.png", "top": ["Best friends"], "bottom": ["forever."], "highlight": ["forever."], "seconds": 4.0},
         {"image": "3.jpg", "top": ["Big print"], "bottom": ["on the back"], "highlight": ["back"]},
         {"image": "2.png", "bottom": ["Oversized fit.", "Made for pet people."], "highlight": ["pet"]}],
         "colors_after": 1},
     caption="Best friends forever. 🐶🐱\n\nA dog, a cat, and a love that doesn't need words.\n\n🐾 Oversized tee with a big back print · 5 colors\n🐾 For every dog and cat best friend\n\nShop now: link in bio · lidpet.store\n\n#doglover #catlover #petparent #oversizedtee #streetwear #giftforpetlovers #lidpet",
     tiktok_caption="Best friends forever 🐶🐱 Big print on the back. Link in bio #oversizedtee #doglover #catlover #lidpet",
     pin_title="Best Friends Forever Oversized Tee – Dog and Cat Lover Shirt",
     pin_description="An oversized tee with a cute dog and cat back print. 5 colors. A sweet gift for pet lovers. Shop at lidpet.store.")

post(7,
     product="I'm Here For The Dogs Tee", short_name="Here For The Dogs Tee", price="$22.99",
     url=STORE + "im-here-for-the-dogs-tee",
     headline=["I'M HERE", "FOR THE DOGS"],
     pin_subtitle="Funny dog lover tee · for every party with a dog",
     mockups=["4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg"],
     video={"scenes": [
         {"image": "3.png", "top": ["Me at every party:"], "bottom": ["I'm here", "for the dogs."], "highlight": ["dogs."], "seconds": 4.0},
         {"image": "1.png", "bottom": ["Wear what you love"], "highlight": ["love"]},
         {"image": "2.png", "bottom": ["The tee every", "dog lover needs"], "highlight": ["dog", "lover"]}],
         "colors_after": 1},
     caption="Me at every party: I'm here for the dogs. 🐶🎉\n\nPeople are great. Dogs are better.\n\n🐾 Soft cotton tee in 9 colors · XS–2XL\n🐾 A gift for anyone who says hi to the dog first\n\nShop now: link in bio · lidpet.store\n\n" + DOG_TAGS,
     tiktok_caption="Me at every party: I'm here for the dogs 🐶 Link in bio #dogtok #doglover #funnytshirt #lidpet",
     pin_title="I'm Here For The Dogs Tee – Funny Dog Lover Shirt",
     pin_description="A funny tee for people who always say hi to the dog first. 9 colors, sizes XS–2XL. Shop at lidpet.store.")

post(8,
     product="My Dog's Emotional Support Human Tee", short_name="Emotional Support Human", price="$22.99",
     url=STORE + "emotional-support-human-tee",
     headline=["MY DOG'S EMOTIONAL", "SUPPORT HUMAN"],
     pin_subtitle="Funny dog lover tee · your dog chose you",
     # The "ChatGPT Image..." ad carries another brand name (VELORA): never post it.
     skip_images=["ChatGPT Image Aug 26, 2026, 05_23_33 PM.png"],
     mockups=["unisex-staple-t-shirt-black-heather-front-6a7aeeefd6b65.jpg",
              "unisex-staple-t-shirt-gold-front-6a7aeeefd7840.jpg",
              "unisex-staple-t-shirt-ocean-blue-front-6a7aeffb7b33b.jpg",
              "unisex-staple-t-shirt-soft-pink-front-6a7aeffb7d846.jpg",
              "unisex-staple-t-shirt-heather-columbia-blue-front-6a7aeeefd8484.jpg",
              "unisex-staple-t-shirt-white-front-6a7aeffb7cd9f.jpg"],
     video={"scenes": [
         {"image": "Emotional Support Human and Golden Retriever.png", "top": ["My dog chose me."], "bottom": ["I'm the emotional", "support human."], "highlight": ["human."], "seconds": 4.0},
         {"image": "Lidpet’s Emotional Support Collection.png", "bottom": ["Your dog's", "favorite human"], "highlight": ["favorite"]}],
         "colors_after": 0},
     caption="This is my dog's emotional support human. 🐶💛\n\nYour dog chose you. Might as well wear it.\n\n🐾 Soft cotton tee in 6 colors · XS–2XL\n🐾 A funny gift for every dog person\n\nShop now: link in bio · lidpet.store\n\n" + DOG_TAGS,
     tiktok_caption="My dog chose me. I'm the emotional support human 🐶 Link in bio #dogtok #doglover #funnytshirt #lidpet",
     pin_title="My Dog's Emotional Support Human Tee – Funny Dog Lover Shirt",
     pin_description="A funny tee for every dog person. Your dog chose you, so wear it proudly. 6 colors, sizes XS–2XL. Shop at lidpet.store.")

post(10,
     product="5 AM Walk Club Tee", short_name="5 AM Walk Club Tee", price="$25.99",
     url=STORE + "5-am-walk-club-t-shirt-hiking-dog-owner-morning-walk-tee",
     headline=["5 AM", "WALK CLUB"],
     pin_subtitle="Dog walking tee · for every early morning walker",
     mockups=["4.jpg", "5.jpg", "6.jpg", "7.jpg"],
     video={"scenes": [
         {"image": "2.png", "top": ["Alarm: 5 AM"], "bottom": ["My dog: let's go."], "highlight": ["dog:"], "seconds": 4.0},
         {"image": "1.png", "top": ["Members only:"], "bottom": ["5 AM Walk Club"], "highlight": ["club"]},
         {"image": "3.png", "bottom": ["For every early", "morning walker"], "highlight": ["morning"]}],
         "colors_after": 1},
     caption="Welcome to the 5 AM Walk Club. 🌄🐕\n\nNo alarm needed. The dog takes care of that.\n\n🐾 Soft cotton tee in 4 colors · XS–2XL\n🐾 For hikers, early risers and every dog walker\n\nShop now: link in bio · lidpet.store\n\n" + DOG_TAGS + " #dogwalk #hikingwithdogs",
     tiktok_caption="Alarm: 5 AM. My dog: let's go 🌄 Link in bio #dogtok #hikingwithdogs #doglover #lidpet",
     pin_title="5 AM Walk Club Tee – Dog Walking and Hiking Shirt",
     pin_description="A tee for early morning dog walkers and hikers. 4 colors, sizes XS–2XL. A great gift for dog owners. Shop at lidpet.store.")
