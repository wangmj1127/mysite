import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django

django.setup()
from apps.notes.models import Note, NoteComment, WishList
from apps.accounts.models import UserAccount


def populate():
    user_accounts = [
        {"name": "Test1", "email": "Test1@test.com", "password": "test", "img": "upload/mugshots/test1.jpeg"},
        {"name": "Test2", "email": "Test2@test.com", "password": "test", "img": "upload/mugshots/test2.jpeg"},
        {"name": "Test3", "email": "Test3@test.com", "password": "test", "img": "upload/mugshots/test3.jpeg"},
        {"name": "Test4", "email": "Test4@test.com", "password": "test", "img": "upload/mugshots/test4.png"},
        {"name": "Test5", "email": "Test5@test.com", "password": "test", "img": "upload/mugshots/test5.jpg"},
    ]
    for user in user_accounts:
        add_user(user["name"], user["email"], user["password"], user["img"])

    notes = [
        {"content": "The formula glides on smoothly even when I have rather chapped lips. It doesn't accentuate my "
                    "cracked lips and does not look cakey at all. Berry shade that looks very unique, not too purple "
                    "or pink. A nice alternate to a nude color lipstick without looking too bright- if that is what "
                    "you're going for.",
         "cover": "image/2019/03/p1.jpg",
         "user": "1"},
        {"content": "What it is: A three-piece set featuring radiance-boosting favorites, presented in a giftable "
                    "box.\nWho it's for: All skin types.\nSet includes:\n- Soy Face Cleanser (1.7 oz.): an "
                    "extra-gentle, multitasking gel formula that instantly whisks away everyday impurities and "
                    "makeup—even mascara—without stripping the skin of essential moisture. Wet the skin then massage "
                    "over the face and eyes. Rinse.\n- Lotus Youth Preserve Rescue Mask (3.3 oz.): a five-minute "
                    "facial-in-a-jar that leaves skin incredibly soft and restores its natural radiance. Apply a "
                    "generous layer to skin after cleansing using circular motions. Let sit for 5 minutes. Add warm "
                    "water and massage into skin then rinse.\n- Lotus Youth Preserve Face Cream (0.5 oz.): a "
                    "lightweight daily moisturizer that minimizes visible signs of aging. Apply to clean, dry skin.",
         "cover": "image/2019/03/p2.png",
         "user": "1"},
        {"content": "What it is: A fast-acting, anti-aging serum that reveals smoother, more radiant skin in as "
                    "little as seven days.\nWho it's for: Ideal for all skin types and tones.\nWhat it does: No "
                    "regimen is complete without Advanced Génifique, the first step to every beauty routine. This "
                    "powerful anti-aging serum works to improve skin's key signs of youth: radiance, elasticity, "
                    "firmness, skin tone, and smoothness. This patented formula, which contains bifidus extract, "
                    "helps strenghten and protect skin's moisture barrier. The bottle features an exclusive "
                    "self-loading dropper for the perfect dosage of serum with every application. Over 14 years of "
                    "research and 197 formulation trials were spent developing Advanced Génifique Serum.\n\nI was "
                    "really sucked into buying this because of what it said it did, so I bought the small bottle to "
                    "try it out. Once I finished it, I liked it so much I went directly to purchasing the biggest "
                    "bottle. I just received my 4th bottle, because it really has made a difference. Around the time "
                    "I purchased the second bottle, I stopped using it for about 2 weeks, and noticed my skin not "
                    "looking that great, so I tried thinking the reasons for it, when I realized I hadn't been using "
                    "this stuff, then two days after I started using it again my skin went back to normal. I've made "
                    "sure to use it daily ever since, and my skin has never looked better.",
         "cover": "image/2019/03/p3.png",
         "user": "2"},
        {"content": "SK-II Facial Treatment Essence helps improve the appearance of the five dimensions of beautiful, "
                    "crystal clear skin—reducing spots and the appearance of wrinkles, improving skin texture and "
                    "firmness and elevating radiance. It contains 90% pure Pitera™ in every bottle. Pitera is a clear "
                    "liquid rich in vitamins, amino acids and minerals that work together to allow the skin’s natural "
                    "surface-rejuvenation process to function at its prime. This unique ingredient was discovered "
                    "more than 35 years ago and remains essentially unchanged until today. The Facial Treatment "
                    "Essence is one of the brand’s signature products and is one of the most coveted beauty products "
                    "around the world. Essences impart nutrients, vitamins, antioxidants and minerals into your skin "
                    "to help skin better absorb your serum and moisturizer. Your skin’s moisture is left replenished "
                    "to help prevent dryness, its texture is smoothed for soft, even skin and its renewal cycle is "
                    "moderated.\n\nHow to use: Sprinkle a teaspoon into your hands then press the essence gently and "
                    "evenly onto your face and neck. Your skin will absorb the essence quickly and naturally. Layer "
                    "with your serum, moisturizer and sunscreen, in that order.\n\nI have seen ads in magazines for "
                    "SK-II essence for as long as I can remember and never gave it a second thought. I turned 31 and "
                    "decided I needed to take better care of my skin if I want to continue having a fresh face. I bit "
                    "the bullet and bought my first bottle of the essence and it blew my mind. While I have always "
                    "had pretty decent skin, it totally transformed my face and made my skin tone more even. I "
                    "received so many compliments on how clear my face looks. I have been using it for almost a year "
                    "and am starting my 3rd bottle. I can't live without it and it's worth every penny.",
         "cover": "image/2019/03/p4.png",
         "user": "4"},
        {"content": "What it is: A facial cream that hydrates and smoothes skin while providing 24-hour "
                    "moisturization.\n\nWho it's for: All skin types.\n\nWhat it does: It immediately leaves skin 2–3 "
                    "times more hydrated, even in skin's driest areas. Formulated with glacial glycoprotein, "
                    "which is derived from sea glaciers, and olive-derived squalane, this beloved moisturizer helps "
                    "strengthen skin's barrier and leaves it feeling comfortable and well balanced. With an "
                    "ultra-light texture, it absorbs easily for softer, smoother, healthier-looking skin. Gentle and "
                    "effective, this bestseller is now ultra-clean and ultra-tested.\n\nHow to use: Apply to clean "
                    "facial skin day or night as needed to combat moisture depletion.\n\nI really like this cream. I "
                    "live in bone dry Colorado and this has helped a lot. I do however naturally have really dry and "
                    "sensitive skin, this cream doesn’t irritate it at all. But I do have to use it with a few other "
                    "facial oils, but if you don’t have crazy dry skin and for some reason chose to move to a crazy "
                    "dry climate, you should be fine with just this.",
         "cover": "image/2019/03/p5.png",
         "user": "3"},
        {"content": "- Full-size Revitalizing Brightening Soft Cream (1 oz.): a cream made with an exclusive blend of "
                    "grand rose extracts that visibly revitalizes skin with moisture, firmness and plumpness while "
                    "transforming from a thick, hydrating cream to a thin serum-like lotion.\n- Revitalizing "
                    "Oleo-Serum (0.16 oz.): a serum made with an exclusive blend of grand rose extracts that targets "
                    "signs of aging as it provides long-lasting hydration and leaves skin feeling nurtured and its "
                    "moisture barrier protected.\n- Revitalizing Eye Cream (0.17 oz.): an eye cream made with an "
                    "exclusive blend of grand rose extracts that targets the delicate skin around the eyes and "
                    "reveals eye contours that look rested and rejuvenated for brighter, younger-looking skin.\n- "
                    "Nourishing Lip Balm Honey-in-Rose (0.17 oz.): a lip balm that wraps lips in a luxurious, "
                    "rich salve and helps reduce the appearance of fline lines and wrinkles while moisturizing for "
                    "smoother, plumper lips.\n\nI just received this new trial set, and I am really amazed by the "
                    "quality of the product. I started out using Lancome skincare Bienfait in my teens and twenties, "
                    "transitioned to Renergie in my thirties and forties, and after that I started using the Absolue "
                    "line. I tried other high priced brands like La Mer and La Prairie, but always ended up coming "
                    "back to Lancome. The cream in this set is only a 1 ounce size, and the eye cream and lip balm "
                    "are small samples you might get in a GWP. I really like the idea of purchasing the cream in the "
                    "larger size and then buying a refill. The eye cream is super, non-irritating and moisturizing.",
         "cover": "image/2019/03/p6.png",
         "user": "1"},
        {"content": "What it is: A silky-soft moisturizing formula that gently tones and immediately rehydrates the "
                    "complexion.\nWhat it does: It instantly soothes skin with honey and almond seed extract for a "
                    "perfectly clean, soft and comforted complexion.\n\nThis is the only toner I will use. I have "
                    "tried all kinds of toner on my sensitive skin and this is the only one that does not burn my "
                    "skin. It is really comforting and it works well with all the other Lancôme products I am using. "
                    "It is the must-have item for me. I will only buy this from now. [This review was collected as "
                    "part of a promotion.]",
         "cover": "image/2019/03/p7.png",
         "user": "2"},
        {"content": "A whole new take on ‘nudes’, Huda Beauty’s The New Nude Eyeshadow Palette is a total "
                    "heartbreaker. A treasure chest of blush, mauve, taupe and beige neutrals, mingled with "
                    "show-stopping copper, golden and pink glitter jewels, it features everything you need to master "
                    "beguiling eye effects in one slimline (clutch bag-compatible) case. The array of 18 shadows "
                    "includes ten highly pigmented mattes, formulated with aloe vera and coconut oil for butter-like "
                    "application; four reflective shades, featuring shimmering pearl flecks for a gorgeous "
                    "duo-chromatic finish; two glitter formulas, infused with innovative silicones for advanced "
                    "adherence, pigment dispersion and luminosity; one pressed pearl, combined with acacia, "
                    "jojoba and sunflower wax for a high-shimmer finish that layers effortlessly on top of mattes, "
                    "adding dreamy depth and dimension; and even a concealer base, for flawless application and to "
                    "boost any eyeshadow layered on top of it. You're guaranteed to fall head-over-heels for "
                    "just-blushed cream ‘Bare’, peachy ‘Play’, mink ‘Lace’ and burgundy ‘Love Bite’, not to mention "
                    "ruby shimmer ‘Excite’, copper ‘Infatuated’ and duo-chrome silver-pink ‘Daydream’. Each of the "
                    "stunning shades looks stunning on its own, or blended for a strikingly beguiling make up look. ",
         "cover": "image/2019/03/p8.jpg",
         "user": "4"},
        {"content": "Whether you're a die-hard eye make up aficionado, or only just beginning to experiment with eye "
                    "enhancement, Charlotte Tilbury's Luxury Palette - Pillow Talk is the ultimate must-have "
                    "indulgence, especially if you're already a fan of the brand's cult favourite lipstick in the "
                    "ultra-flattering nude shade, 'Pillow Talk'. A dream come true for fans of the heavenly hue, "
                    "this palette stars four beautifully buttery, complementary shades of eyeshadow, designed to be "
                    "used individually or together to create an array of arresting effects. From daytime "
                    "understatement to a an eye-catching heatwave look, the only limit is your own imagination. The "
                    "shades in each palette are categorised as 'prime', 'enhance', 'smoke' and 'pop', and should be "
                    "applied in that order to take you seamlessly from 'desk to dusk to disco!'.\n\nI love the "
                    "colours of this palette and I think that it is a very good option for the range. I suppose that "
                    "the pigmentation will be worth but it's more than good. The glittery shades are better applied "
                    "with your finger however, It's very beautiful!",
         "cover": "image/2019/03/p9.jpg",
         "user": "3"},
        {"content": "Love your Huda palette but can’t fit it in your make up bag? Or just desperate to sample the "
                    "shadows that have sent the beauty world into a spin? The answer is Huda Beauty’s Topaz "
                    "Obsessions Palette, a slimline edit of the most sought-after, bronze-hued shadows and all you "
                    "need to achieve an array of mesmer-eyes-ing vibrant eye looks. The ultimate capsule make up "
                    "wardrobe, this unites nine ultra-versatile, buttery smooth shadows – four vibrant duo-chrome "
                    "shimmers and five creamy mattes. We’re completely besotted with the range of hues and textures "
                    "and you're guaranteed to fall head-over-heels too – especially with the beautifully versatile "
                    "range of gold, burnished bronze, bold brick and rich amber. Perfectly on-trend, "
                    "this gemstone-inspired edit is sure to become a precious product in your arsenal.\n\nIf you like "
                    "warm-toned eyeshadow looks, this palette is fab! The mattes are intense yet blendable and the "
                    "metallics have a foil-like sheen. It’s such a pretty palette with shades you don’t tend to see "
                    "inside warm palettes.",
         "cover": "image/2019/03/p10.jpg",
         "user": "1"},
        {"content": "Bring the warm tan of the islands to your face with Hoola. This matte bronzing powder from "
                    "Benefit brightens up even the palest of complexions for an all year round gorgeously glowing "
                    "tan. Simply sweep across your skin like a warm summer breeze…\nIt’s as easy as that to achieve a "
                    "natural looking kiss from the sun. Dusting the soft bronzing powder of Hoola by Benefit over "
                    "your cheeks, chin and forehead gives you a healthy complexion to revel in.\n\nDirections of "
                    "use:\nFor lighter skin tones, use the slant powder brush to contour your cheekbones, "
                    "jaw line and down the centre of your nose.\nFor darker skin tones, use the slant powder brush to "
                    "apply all over for a medium to deep tan look.\n\n",
         "cover": "image/2019/03/p11.jpg",
         "user": "4"},
        {"content": "Infuse your complexion with a healthy glow using the Burberry Check Fashion Palette, a sleek, "
                    "silver-tone compact that houses complementary shades of blusher and bronzer in the brand’s "
                    "signature check print. The ultra-fine powder dusts effortlessly onto the face, imparting "
                    "buildable and blendable colour that lasts for hours of comfortable wear. Expect naturally "
                    "radiant results.\n\n",
         "cover": "image/2019/03/p12.jpg",
         "user": "3"},
        {"content": "Condition lips, address dryness, banish chapping and shield against harmful environmental "
                    "elements with Hourglass’ Nº 28 Lip Treatment Oil, an ultra-luxe treatment for luscious lips. The "
                    "‘28’ of the title refers to the 28 beneficial ingredients used in the formula: there are 14 "
                    "essential oils (including rose, lavender and lemon oils), 10 lipid-rich plant oils (hazelnut, "
                    "sweet almond and jojoba oils) and four nourishing vitamins (A, B5, C and E), all of which "
                    "replenish moisture and soften your lips. Alongside this conditioning blend, three advanced, "
                    "potent actives (Saliporine-8, Volulip and Viamerine) work to minimise the appearance of wrinkles "
                    "and boost volume. Topping things off perfectly, the 24ct gold-plated, antibacterial tip "
                    "dispenses product perfectly, creates a soothing effect and adds a welcome touch of opulence to "
                    "any make up collection.",
         "cover": "image/2019/03/p13.jpg",
         "user": "2"},
        {"content": "The benefit Cheekleaders Mini Pink Squad Palette is a limited edition blush, brighten and "
                    "highlighter palette to pep up your complexion. The mini palette includes an iconic blusher, "
                    "face powder and the brand's new super-silky highlighter powder. Housed in super-cute palette "
                    "with integrated mirror.\n\nThe Palette Contains:\nGALifornia Powder Blush (2.5g)\nA golden pink "
                    "blusher that delivers a sunkissed effect, inspired by the warmth of Californian sunshine. "
                    "Complementing all skin tones, the soft blush blends effortlessly onto skin, adding a luminous "
                    "glow to cheeks. Infused with signature scent of Pink Grapefruit and Vanilla.\n\nTickle Box o' "
                    "Highlighter in 'Golden Pink' (2.5g)\nA super-silky powder highlighter that delivers golden pink "
                    "luminosity with high-impact payoff.\n\nDandelion Brightening Face Powder (3.5g)\nA sheer, "
                    "soft pink face powder with hint of shimmer. A multi-tasker, the powder is perfect as a blush or "
                    "an all-over finishing powder. Its brightening properties help add radiance to apples and "
                    "brightness to your complexion when lightly dusted over entire face. Buildable colour.",
         "cover": "image/2019/03/p14.jpg",
         "user": "1"},
        {"content": "Achieve beautifully rich, saturated colour and a new level of lip-wear luxury with Hourglass’ "
                    "sleek, chic Confession Ultra Slim High Intensity Refillable Lipstick. Encased in a gorgeous "
                    "golden applicator, this refillable lipstick can be used with the full collection of {Confession "
                    "Ultra Slim Lipstick Refill}, leaving you with endless options to suit changing seasons and "
                    "aesthetics. Creamy and comfortable, the saturated, long-wearing formula veils lips with a "
                    "vibrant satin finish (it was awarded Harper’s Bazaar’s coveted ‘Most Pigmented Lipstick Award’ "
                    "in 2017), in a curated collection of nude, mauve, pink and berry shades. From neutral pink-beige "
                    "‘I Wish’ to bright, vivid red ‘I Crave’ via coral pink ‘You Can Find Me’ and deep plum ‘I Hide "
                    "My’, there’s something to suit everyone. Totally vegan, there’s no reason not to love this "
                    "luscious lip formula.\n\nThe packaging is beautiful and the lipstick is lovely, smooth and "
                    "pigmented. I also love the idea that this lipstick is refillable BUT...I was quite shocked at "
                    "how little product you get for the enormous price, it’s only 0.9 grams where an average lipstick "
                    "is 3 grams. I suppose I’ll only use it on special occasions.",
         "cover": "image/2019/03/p15.jpg",
         "user": "5"},
        {"content": "Sometimes, the cold light of day can be a little harsh on skin, so recreate the most flattering "
                    "light (wherever you stray) with this ethereal illumination powder from Hourglass. An innovation "
                    "in illumination, this universally flattering finishing powder takes inspiration from the most "
                    "forgiving light sources – from morning light to candlelight, via sunset and moon light – so "
                    "you’ll feel like you have a personal lighting technician at your disposal. Thanks to "
                    "ground-breaking ‘Photoluminescent Technology’, the Ambient Lighting Palette captures, "
                    "diffuses and softens surrounding light, filtering out harsh beams to blur the visibility of "
                    "imperfections, pores and wrinkles, leaving skin looking softer, more youthful and beautifully "
                    "lit-from-within. This sublime trio unites three sumptuous shades, which can be applied "
                    "individually or layered to imbue skin with a multidimensional glow: there’s natural peach beige "
                    "‘Dim Light’, which contains the perfect balance of warm and cool tones; opalescent pearl "
                    "‘Incandescent Strobe Light’, which brightens skin with a ‘celestial’ glow and, "
                    "last but certainly not least, sun-kissed golden beige ‘Radiant Light’. \n\nI absolutely love "
                    "this product. One of my top 10 beauty favourites! I use dim light to set my foundation, "
                    "radiant light as a soft bronzer and incandescent light as a more natural highlighter. It may not "
                    "seem that special at first but under certain lights it gives the most beautiful glowing effect. "
                    "It was definitely a good investment and I intend to purchase more shades very soon!",
         "cover": "image/2019/03/p16.jpg",
         "user": "4"},
        {"content": "Ask any beauty buff to name their favourite blushers and, chances are, NARS will be top of the "
                    "list. An authority in blush, NARS has created many of the industry’s most iconic shades, "
                    "delivering them in silky matte and shimmering textures that are quickly addictive. Whichever "
                    "shade you choose, this micronised powder grants natural, healthy-looking colour that will "
                    "immediately enliven your complexion; even if you’re working with the highest intensity hues, "
                    "a light application delivers a believable, uplifting flush. Our expert curators have selected "
                    "the most flattering, covetable shades to house in the online Hall of Fame in which you currently "
                    "find yourself: of course, there’s ‘Orgasm’, the über-iconic, universally flattering shade of "
                    "peachy pink with golden shimmer, as well as ‘Super Orgasm’ if you want to ramp up the glitter "
                    "factor. There’s also matte rose pink ‘Amour’, soft pink with golden sheen ‘Deep Throat’, "
                    "matte tangerine ‘Gina’ and many more. \n\nI bought this product for one of my daughter's "
                    "Christmas presents. It has rightly become an iconic blush because it is a beautiful, "
                    "lightly sparkling shade that suits most skin tones. She was genuinely thrilled with it and wears "
                    "it all the time! She'll need another for her birthday in March and both my eldest granddaughters "
                    "also want one... They do like the humour of asking their Nan for this particular shade haha!",
         "cover": "image/2019/03/p17.jpg",
         "user": "4"},
        {"content": "What it is: An iconic, award-winning mascara that delivers lavishly long and perfectly defined "
                    "lashes with ultimate separation.\n\nWhat it does: Carefully selected polymers coat from root to "
                    "tip to help lengthen and outline each lash for unmatched definition. This best-selling mascara's "
                    "unique brush applicator has specially grooved bristles that hold the perfect amount of product "
                    "for gradual, even application every time.\n\nHow to use: Place the wand at the root of the "
                    "lashes and wiggle back and forth to give depth to the base and pull through. Layer the mascara "
                    "on the outer corner lashes to lift and extend the eye. Apply to lower lashes with the tip of the "
                    "wand and blend down. Always begin with the bottom lashes first. Use the tip of the mascara brush "
                    "while looking up into a mirror for immaculate, smudge-proof application. Then comb the lashes "
                    "with the brush in smooth, vertical strokes while looking down into your mirror.\n\nI have tried "
                    "many brands of mascara over the years, this is by far my favorite. You can build volume, "
                    "never clumps, and is perfect for day into evening. Very easy to apply.",
         "cover": "image/2019/03/p18.png",
         "user": "3"},
        {"content": "For eyes with serious sparkle, this blindingly stunning shadow pigment combines pearlescent and "
                    "glitter particles to guarantee an instant head-turning look. The water-infused texture is super "
                    "easy to apply, thanks to the applicator wand and dries to a shimmering finish that never dulls. "
                    "Yet it also cares for the skin with conditioning glycerin, while triethanolamine forms a "
                    "protective barrier between the skin and the glittery pigment, so it always feels comfortable to "
                    "wear. Choose from an array of gemstone hues, from the twinkling ebony 'Molten Midnight'; "
                    "show-stopping 'Gold Goddess' and beautiful bronze 'Smouldering Satin', to the shimmering silver "
                    "'Diamond Dust' and exquisite 'Rose Gold Retro'.\n\n I bought Gold Goddess - it is so pretty. "
                    "It’s chunkier than I imagined, but still an amazing product. No mess, no fuss, no need for "
                    "glitter glue. Just apply and go! I think this is one of the easiest eye-glitter products to use. "
                    "The colours are so beautiful. I’m going to buy Ballet Baby and Into the Blue next. All the "
                    "colours look so gorgeous! These are perfect for the party season!",
         "cover": "image/2019/03/p19.jpg",
         "user": "2"},
        {"content": "What it is: Viktor & Rolf’s acclaimed first feminine fragrance, Flowerbomb is a floral explosion "
                    "that makes everything more positive.\n\nFragrance story: Flowerbomb is an explosion of the most "
                    "luxurious and alluring flowers, with the power to transform the negative into positive. "
                    "Thousands of flowers give rise to an ultrafeminine, sensual and addictive fragrance. A bouquet "
                    "of cattleya orchids, sambac jasmine, freesia and rose petals is enriched by the addictive "
                    "patchouli and vanilla. With just one touch, the power is unleashed, whisking you into a secret "
                    "garden where your dreams become the new reality. This fragrance comes in a pink diamond "
                    "grenade-shaped bottle.\n\nStyle: Feminine, fresh, floral.\n\nSmells beautiful. Simple and "
                    "elegant, I always feel fresh and lovely when I spritz on a couple sprays.- Wheater I'm going to "
                    "run errands, to school, or even to the gym- I love how it blends with my farimones and I just "
                    "feel so soft and clean. Love the glass flower bottle, too!",
         "cover": "image/2019/03/p20.png",
         "user": "1"},
        {"content": "Discover Black Opium Eau de Parfum, the new feminine fragrance by Yves Saint Laurent. With a "
                    "glam-rock aesthetic, this addictive gourmand floral entices with notes of black coffee for a "
                    "shot of adrenaline, white florals to instantly seduce and vanilla for sweetness and sensuality. "
                    "Audacious, addictive, electrifying.\n\nNotes:\n- Top: mandarin, pink pepper, pear.\n- Middle: "
                    "jasmine, orange blossom, solar floral accord.\n- Base: cedarwood, patchouli, vanilla, "
                    "coffee.\n\nI really hate their original Opium scent, it was just way too spicy and strong for "
                    "me. This scent is just heavenly though! It's the perfect mix of spice and sweet to really "
                    "balance each other out and has really become my favorite fragrance now.",
         "cover": "image/2019/03/p21.png",
         "user": "3"},
        {"content": "Finish your makeup with the Rimmel Stay Matte Pressed Powder, a mattifying setting powder that "
                    "locks makeup in place while minimising shine.\n\nUsing natural minerals to control shine for up "
                    "to six hours, the oil-absorbing finishing powder has a smooth, non-powdery texture that blends "
                    "seamlessly onto skin to set base makeup (without affecting colour) and minimise the appearance "
                    "of pores. Promoting a flawless, shine-free complexion, it applies without cakiness and is "
                    "virtually undetectable for a natural, true matte finish.\n\nI've been using this for years.It's "
                    "good for dry/combination skin but I'm not sure if it'd work for oily skin.I have combination/dry "
                    "skin and after a few hours I see some shine around my nose.Extra note:it has fine sparkles in it "
                    "which are visible if you're under the sun.",
         "cover": "image/2019/03/p22.jpg",
         "user": "2"},

    ]
    for note in notes:
        add_note(note["content"], note["cover"], note["user"])

    comments = [
        {"note_id": 2, "user": "2",
         "comment": "Gift for my mom. These products are always fresh smelling. Go on very smooth. Great moisture. "
                    "This mask is cool and soothing, the smell is terrific, like cucumber! "
         },
        {"note_id": 2, "user": "3",
         "comment": "OH I LIKE IT!"
         },
        {"note_id": 2, "user": "4",
         "comment": "I like it too~\nI wish I can take it home!\n^.^"
         },
        {"note_id": 18, "user": "5",
         "comment": "I Like it!"
         },
        {"note_id": 15, "user": "1",
         "comment": "I LIKE IT!"
         },
        {"note_id": 10, "user": "1",
         "comment": "I LIKE IT!"
         },

    ]

    for note in notes:
        for comment in comments:
            add_comment(comment["note_id"], comment["user"], comment["comment"])


def add_user(name, email, password, img):
    u = UserAccount.objects.get_or_create(username=name, email=email, password=password, mugshot=img)[0]
    u.save()
    return u


def add_note(content, cover, user):
    n = Note.objects.get_or_create(content=content, cover=cover, user_id=user)[0]
    n.save()
    return n


def add_comment(note, user, comment):
    c = NoteComment.objects.get_or_create(note_id=note, user_id=user, comment=comment)[0]
    c.save()
    return c


if __name__ == '__main__':
    print("Start population script")
    populate()
