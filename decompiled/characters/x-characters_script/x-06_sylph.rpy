
define sylph_intro = True
define sylph_on = True
define sylphie_lesson = 0

define bully1 = Character("Bully 1", color="#FF0000")
define bully2 = Character("Bully 2", color="#FF0000")
define bully3 = Character("Bully 3", color="#FF0000")

define sylphie = Character("Sylphiette", color="#aaffaa")

default sylph_afeicao = 0
default sylph_talked_today = False
default sylph_gifted_today = False
default sylph_interacted_today = False


label sylphie_intro:
    scene black with fade

    rudeus "Another sunny afternoon in the Buena village. Not bad for a little walk… maybe something interesting will show up."

    rudeus "Trained magic in the morning, helped Zenith in the garden… now it's time to relax a bit."

    narrator "Suddenly, cruel laughter and muffled screams come from a clearing near the village exit."

    rudeus "Huh? That doesn't sound like kids playing… Better check it out."

    scene bg floresta with dissolve
    narrator "In the clearing, two older boys from the village have formed a circle around a small figure. Stones fly occasionally, hitting the ground near her."
    narrator "In the center, a green-haired elf girl is curled up, hugging her knees and trembling in fear."

    show bully1 angry:
        xalign 1.0
    show bully2 angry:
        xalign 0.7
    show sylphie embarrassed:
        xalign 0.3
        xzoom -1
    with dissolve

    bully1 "Look at the weird green-haired elf again!"
    bully2 "Thought we forgot about you? This ain't a place for pointy-eared freaks!"

    sylphie "Please stop… I just came to gather some medicinal herbs…"

    narrator "The girl tries to curl up even more, hugging her knees tightly. Her light-green hair is messy, with some leaves stuck in it, and there are light scratches on her arms where the stones grazed her."

    rudeus "(These idiots… I'm so fucking tired of this kind of shit in the village.)"
    rudeus "(If I don't do something, this girl is really gonna get hurt.)"

    "You approach the clearing."

    show rudeus normal at left with moveinleft
    rudeus "Hey! You three. Cut that shit out right now."

    bully1 "Oh look, the rich Greyrat boy came to play hero."
    bully2 "Get lost, Rudeus. This doesn't concern you!"

    rudeus "(Fucking cowards… Two against one defenseless girl.)"

    menu:
        "Intimidate with magic":
            rudeus "Last chance. Get the fuck out of here before I lose my patience."
            play sound "audio/magic_charge.ogg"
            narrator "Rudeus slowly raises his hand. The air around him becomes humid, and a huge spinning sphere of water forms above the boys, swirling with pressure."

            bully2 "Holy shit… he actually knows real magic!"
            bully1 "Run, run!!"
            hide bully1 with dissolve
            hide bully2 with dissolve

            narrator "The two stumble over each other trying to escape."
            rudeus "Think you're getting away with it, huh? Tsk tsk…"
            narrator "The water sphere shoots toward the boys, who disappear screaming into the trees."
        "Solve it with fists":

            rudeus "Alright. If that's how you want it…"
            show rudeus:
                ease 0.25 xalign 0.5
            show sylphie:
                ease 0.25 xalign 0.2
            show bully2:
                ease 0.25 xalign 0.75
            show bully1:
                ease 0.25 xalign 1.05
            narrator "Rudeus moves fast. A controlled punch to the stomach of the first one — the older boy is already running before he even gets hit."

            bully2 "This guy's way too strong!"
            bully2 "Let's get the hell out!"
            hide bully1 with dissolve
            hide bully2 with dissolve

            narrator "The two stumble over each other trying to escape."
            rudeus "Think you're getting away with it, huh? Tsk tsk…"
            narrator "Rudeus slowly raises his hand. The air becomes humid again, and a huge spinning sphere of water forms in front of him."
            rudeus "Next time I see you around here, I won't be so nice."
            narrator "The water sphere shoots toward the boys, who vanish screaming among the trees."

    narrator "Silence returns to the clearing. The elf girl is still curled up, trembling slightly."
    show rudeus:
        xzoom -1
        xalign 0.8
    with dissolve

    rudeus "Hey… they're gone. You can get up. They won't be back anytime soon."

    narrator "She slowly lifts her face. Big, teary green eyes stare at Rudeus with a mix of fear and surprise."

    sylphie "Th-thank you… I… I really thought I was going to get badly hurt this time…"

    rudeus "Not while I'm around."
    rudeus "(Now that I'm seeing her up close… holy shit. She's actually pretty cute.)"
    rudeus "(Green hair, pointy ears… a real elf. And so young-looking… but legal, apparently.)"

    rudeus "My name is Rudeus Greyrat. And you?"

    sylphie "S-Sylphiette… but you can call me Sylphie."
    sylphie "You… used magic? That water ball was amazing! I could never do anything like that…"

    rudeus "Hehe, just a basic trick. You like magic?"

    sylphie "I love it! But… I'm terrible at it. Everyone says I'll never learn properly because I'm half-human."

    rudeus "(Golden opportunity. Time to show off my teacher skills.)"

    rudeus "Nonsense. It's just a matter of having the right teacher."

    rudeus "If you want, I can teach you chantless magic. I'm sure you'll be able to do it."

    sylphie "R-really?! You'd do that… for a total stranger?"

    rudeus "After saving you, you're not a stranger anymore. And I like teaching motivated people."

    sylphie "Thank you… really. You're the first person in the village who's ever stood up for me."

    narrator "She slowly stands up, brushing the dirt off her simple clothes. A few leaves still cling to her hair."

    rudeus "Do you live far? Those idiots might come back with friends."

    sylphie "I live in the forest… it's not too far, but…"

    rudeus "Then I'll walk you home. Just to be safe. Doesn't cost me anything."

    sylphie "N-no need to trouble yourself!"

    rudeus "It's no trouble. Let's go?"

    narrator "Sylphie hesitates for a second, then nods shyly."

    scene bg floresta with fade
    show rudeus normal:
        xalign 0.7
        xzoom -1
    show sylphie embarrassed:
        xalign 0.3
    with dissolve

    narrator "The two walk along the narrow forest path. The afternoon sun filters through the leaves, creating patches of light on the ground."

    rudeus "(Those little ears twitching every time she gets nervous… Oh daddy… control yourself, Rudy.)"

    sylphie "You… are really strong. And kind. Most people here avoid me because of my ears."

    rudeus "They're so cute. Who wouldn't want little ears like that?"

    sylphie "C-cute…? N-no one has ever said that before…"

    narrator "She lowers her head, ears trembling slightly from embarrassment."

    scene black with fade
    narrator "After about fifteen minutes, they arrive at a simple wooden cottage surrounded by tall trees. A small herb garden in front."

    scene bg sylph_hut with dissolve
    show rudeus normal:
        xalign 0.7
        xzoom -1
    show sylphie embarrassed:
        xalign 0.3
        xzoom -1
    with dissolve

    sylphie "We're here… this is my house."
    rudeus "It's really cozy. I like it."
    rudeus "You live alone here?"

    sylphie "No, I live with my parents and my brother."

    rudeus "Ah, nice. They must be happy to have you back."

    sylphie "Y-yeah… Thank you for walking me home, Rudeus."
    sylphie "I… I'm going to take a bath now. I'm all dirty and have dirt in my hair because of those boys…"

    rudeus "(Bath? Water running down that delicate little elf body… calm down, brain, calm down.)"

    rudeus "No problem. Rest well. I'll come by tomorrow to start the lessons, okay?"

    sylphie "Okay! I… I'll be waiting."

    hide sylphie with dissolve

    narrator "Sylphie waves shyly from the door, goes inside, and slowly closes it. Rudeus stands there for a second, staring at the house."

    rudeus "(Hehe… this is going to be way more fun than I imagined. And who knows… maybe I'll get a little piece of this cute elf…)"

    $ sylph_intro = False
    $ local_atual = "sylph_hut"
    $ sylph_on = False
    jump locais




label sylp_house_menu:

    $ local_atual = "sylph_hut"
    jump sylph_hut

label sylph_label:

    show sylphie embarrassed at right
    show rudeus normal at left
    with dissolve
    jump sylph_menu

label sylph_menu:
    menu:

        "💬 Chat" if not sylph_talked_today:
            $ chat_reward = get_chat_reward(sylph_afeicao)
            rudeus "Hey, Sylphie? How's your magic training going?"
            sylphie "I've been training a lot… I think I'm getting a little better every day."
            rudeus "That's awesome! Practice makes perfect, hehe."

            $ sylph_afeicao += chat_reward
            $ sylph_talked_today = True
            $ renpy.notify("You gained +{} affection with Sylphie!".format(chat_reward))
            jump sylph_menu

        "🎁 Give gift" if not sylph_gifted_today:
            $ available_gifts = []
            if simple_flower_count > 0:
                $ available_gifts.append(("simple_flower", "Simple Flower", simple_flower_count, 10))
            if chocolate_box_count > 0:
                $ available_gifts.append(("chocolate_box", "Box of Chocolates", chocolate_box_count, 25))
            if luxury_jewelry_count > 0:
                $ available_gifts.append(("luxury_jewelry", "Diamond Earring", luxury_jewelry_count, 50))



            $ chosen_gift = renpy.call_screen("gift_selection_screen", "sylphie", "Sylphie", available_gifts)

            if chosen_gift == "simple_flower":
                $ simple_flower_count -= 1
                rudeus "Hey, Sylphie, I brought a flower for you!"
                sylphie "Oh! A flower for me? Thank you… It smells so nice."
                $ sylph_afeicao += 10
                $ sylph_gifted_today = True
                $ renpy.notify("Sylphie loved the gift! +10 Affection")

            elif chosen_gift == "chocolate_box":
                $ chocolate_box_count -= 1
                rudeus "Sylphie, I brought some fancy chocolates for you!"
                sylphie "Wow! They look delicious! Thank you so much, Rudy!"
                $ sylph_afeicao += 25
                $ sylph_gifted_today = True
                $ renpy.notify("Sylphie loved the gift! +25 Affection")

            elif chosen_gift == "luxury_jewelry":
                $ luxury_jewelry_count -= 1
                rudeus "Sylphie… I want you to have this."
                sylphie "This is… a jewel!? It's so beautiful! Thank you, Rudy…"
                $ sylph_afeicao += 50
                $ sylph_gifted_today = True
                $ renpy.notify("Sylphie loved the gift! +50 Affection")









            jump sylph_menu

        "😏 Interact" if not sylph_interacted_today:

            menu:
                "Ask to show her breasts (30)":

                    if sylph_afeicao < 30:
                        "🔒 You need at least 30 affection to unlock this option."
                        jump sylph_menu
                    else:

                        $ interaction_reward = get_interaction_reward(sylph_afeicao)

                        rudeus "Sylphie, you were great in class today… I think I deserve a special little reward, don't I? Something to motivate the teacher."
                        sylphie "R-reward…? What do you have in mind this time…?"

                        rudeus "How about showing me those cute little elf tits? Just a peek, so I can admire my favorite student's body."

                        sylphie "M-me?! Show… my breasts?! N-no… that's way too embarrassing… My ears are already burning just thinking about it."

                        rudeus "Come on, Sylphie… It's just because you improved so much in magic. I'll keep it a secret, and who knows, maybe I'll teach you an extra trick afterward?"

                        sylphie "Hmm… extra trick?"

                        rudeus "Yeah, something only my most dedicated students learn. But for that, I need to see a bit more of you."

                        sylphie "…Arghh… Okay… just a second, and only because I want to learn more magic… But don't stare too much!"

                        rudeus "I promise."

                        scene black with fade

                        narrator "Sylphie slowly lifts her shirt, revealing small, firm breasts with pink nipples hardening in the cool air. She looks away, clearly embarrassed."

                        scene sylphie_lift_shirt_blush with fade

                        sylphie "T-there… satisfied now…?"

                        sylphie "(Why is my heart beating so fast… And why do I feel… weird…?)"

                        rudeus "Damn… perfect. So delicate and pink."

                        rudeus "They're gorgeous, Sylphie. Makes me want to grab them and nibble those little nipples."

                        sylphie "N-no nibbling, you just asked to look…"

                        rudeus "Alright… But just seeing you like this already gets me excited."

                        "She looks away, biting her lip, clearly nervous and aroused at the same time."

                        sylphie "S-shut up, you pervert… And don't tell anyone, okay?"

                        sylphie "My dad would kill me if he knew…"

                        sylphie "(My face is on fire… Why am I feeling like this…?)"

                        rudeus "I promise, your secret is safe with me."

                        sylphie "Th-thank you… I… I think…"

                        $ sylph_afeicao += interaction_reward
                        $ sylph_interacted_today = True
                        $ renpy.notify("You gained +{} affection with Sylphie!".format(interaction_reward))
                        jump passar_tempo
                "Ask to show her panties (80)":

                    if sylph_afeicao < 80:
                        "🔒 You need at least 80 affection to unlock this option."
                        jump sylph_menu
                    else:
                        if True:
                            $ interaction_reward = get_interaction_reward(sylph_afeicao)

                            rudeus "Sylphie, what a class today, huh?"
                            rudeus "You're improving so fast, I'm impressed."

                            sylphie "Th-thank you. I really tried hard this time."

                            rudeus "So… time for another special reward."

                            rudeus "I think I deserve something… a bit more exciting, don't you?"

                            sylphie "E-exciting? W-what do you want this time…?"

                            rudeus "How about showing me your panties? Just a little, so I can see how a dedicated student rewards her favorite teacher."

                            sylphie "M-my panties…? S-serious…? My face is already burning just thinking about it…"

                            rudeus "Why not? You're doing so well in magic… I promise it's just a little, and no one will know."

                            sylphie "Hmph… Okay… just a little… B-but why does this excite you so much?"

                            rudeus "You know I love those elf curves. It's like a prize for teaching you so well."

                            rudeus "Plus, seeing you all shy like this is irresistible…"

                            sylphie "…Arghh… Just because it's you… and just this once! But if I get too nervous, you stop looking."

                            rudeus "Deal."

                            scene black with fade

                            narrator "Sylphie slowly lowers her shorts, revealing simple white panties clinging lightly to her soft curves. A subtle scent of arousal hangs in the air."

                            scene sylphie_lift_skirt with fade

                            sylphie "T-there… b-but don't look too much… my ears are gonna burn!"

                            sylphie "(Why does my body react like this when he asks for these things?)"

                            rudeus "Wow… Perfection… your panties are soaked… Damn, I can see a little wetness there. You're enjoying this, aren't you?"

                            sylphie "Y-you've seen enough! Stop now… But… maybe a little."

                            rudeus "Hmm… I'm not done yet. How about we continue the reward?"

                            sylphie "What do you mean by 'continue the reward'…?"

                            menu:
                                "Don't ask for more (0)":

                                    rudeus "Nothing more today. You were already amazing."
                                    sylphie "Th-thank you… I… I think…"
                                "Lie down and spread your legs (100)":

                                    if sylph_afeicao >= 100:
                                        rudeus "So I can see better… lie down on the grass and spread your legs, okay? Like an obedient student."

                                        sylphie "L-lie down and… spread my legs?! I-I don't know if I can… My whole body is tingling."

                                        rudeus "Come on, Sylphie… Do it for your favorite teacher. I'll reward you with an extra lesson tomorrow."

                                        sylphie "Hmm…. O-okay… just because you asked… But slowly."

                                        scene sylphie_lay_down with fade

                                        narrator "Sylphie lies down on the soft grass, slowly spreading her legs."

                                        narrator "The panties stretch, revealing the damp outline of her pussy, the sweet scent of arousal stronger now."

                                        sylphie "Like this…? Rudy, I'm dying of embarrassment… But… it's a little exciting too."

                                        sylphie "No one has ever seen my panties before…"

                                        rudeus "Just like that… Look at that beautiful view. I can see everything perfectly through the panties. You're wet because of me, right?"

                                        sylphie "D-don't say that… I get embarrassed… That's enough, right?"

                                        rudeus "Almost… Just a bit more. Spread a little wider so I can see better."

                                        sylphie "Ahh… okay… just a little more and that's it…"

                                        scene sylphie_spreading_lying with fade

                                        "She spreads wider, the panties now soaked in the center, outlining the entrance of her pussy."

                                        rudeus "Woah… perfect. So tight and inviting."

                                        rudeus "Sylphie, you're amazing."

                                        sylphie "R-rudy… my face is on fire…"
                                        sylphie "And I'm feeling… something weird down there…"

                                        sylphie "(My body is so hot… am I enjoying this…?)"

                                        rudeus "Hehe, naughty girl. You can stop now, but you did great."
                                    else:

                                        rudeus "So I can see better… lie down on the grass and spread your legs, okay? Like an obedient student."
                                        sylphie "I-I can't… I'm still too nervous for that…"
                                        rudeus "(Damn, I need her more comfortable first.)"
                                        rudeus "Alright, we'll save it for next time then."
                                        sylphie "O-okay…"
                                "Get on all fours and spread your ass (120)":

                                    if sylph_afeicao >= 120:
                                        rudeus "Why don't you turn around? And to see better… spread your ass cheeks with your hands, okay?"

                                        sylphie "S-spread?! N-no… that's way too embarrassing, Rudy! My legs are shaking already."

                                        rudeus "Come on, Sylphie… Do it for your favorite teacher. It's a well-deserved reward for your magic effort."

                                        sylphie "Hmm…. O-okay… just because you asked… But don't laugh at me."

                                        sylphie "I'm so embarrassed…"

                                        rudeus "I would never laugh at you, Sylphie. Now show me that cute little ass."

                                        sylphie "Ahh… O-okay…"

                                        show vid_sylph_twerk with fade

                                        narrator "Sylphie turns around, arching her back. She spreads her cheeks with trembling hands, the panties wedged in, almost revealing her tight pink ring."

                                        sylphie "R-rudy… Like this…?"

                                        rudeus "Perfect. Arch that ass more… Spread it wide so I can see the perfect shape."

                                        sylphie "Ahh… I'm sweating… so embarrassing… and you have this weird smile…"

                                        rudeus "It's perfect… Can I give it a light slap?"

                                        sylphie "Eeek! N-no, you pervert… That's enough…"

                                        rudeus "Hehe, alright. (Better not push too hard…)"
                                    else:

                                        rudeus "Why don't you turn around? And to see better… spread your ass cheeks with your hands, okay?"
                                        sylphie "I… can't stay in that position… it's too exposed, Rudeus…"
                                        rudeus "(Need her more comfortable first.)"
                                        rudeus "Alright, we'll save it for next time then."
                                        sylphie "O-okay…"

                            $ sylph_afeicao += interaction_reward
                            $ sylph_interacted_today = True
                            $ renpy.notify("You gained +{} affection with Sylphie!".format(interaction_reward))
                            jump passar_tempo
                        else:

                            $ patreon_msg = get_patreon_message(1)
                            "[patreon_msg]"
                            jump sylph_menu
                "Ask for blowjob (140)":

                    if sylph_afeicao < 140:
                        "🔒 You need at least 140 affection to unlock this option."
                        jump sylph_menu
                    else:
                        if True:
                            $ interaction_reward = get_interaction_reward(sylph_afeicao)

                            rudeus "Sylphie… today the reward has to be bigger. I deserve something really tasty for your progress in magic."

                            sylphie "B-bigger…? What do you want now…? My stomach is already flipping from nerves."

                            rudeus "I want that cute little mouth working on my cock."

                            rudeus "Suck it, I'll guide you. It's gonna be amazing for both of us."

                            sylphie "S-suck you?! I… I've never done this… it's gonna be weird… What if I do it wrong?"

                            rudeus "Relax, I'll teach you. It'll be just between us, and I promise you'll enjoy it too."

                            sylphie "…Okay… but slowly, okay? If it's too weird, I'll stop."

                            scene black with fade

                            narrator "Sylphie kneels down, trembling hands opening his pants."
                            narrator "Rudeus holds his erect, hot, throbbing cock in front of her face."

                            sylphie "W-woah… it's so big… Ahn… I… I don't know if I can fit it…"

                            rudeus "Take it easy, Sylphie. Just the tip for now."

                            sylphie "O-okay… I'll try…"

                            show vid_sylph_blowjob_1 with fade

                            "She brings the tip to her mouth, licking slowly, her shy tongue exploring the glans."

                            sylphie "(It's so big… hot… how do I fit the whole thing? I'm shaking all over.)"

                            rudeus "Like that… open your mouth slowly… use your tongue on the tip…"

                            sylphie "Mmmph… Hmmph…"

                            "She sucks slowly, tongue swirling, saliva dripping down her chin."

                            rudeus "Yes… yes… now go a little deeper…"

                            sylphie "Ahn… O-okay… (She goes deeper, sucking up to half the shaft.)"

                            rudeus "Fuck… your mouth is perfect. Keep going, suck it nice and good…"

                            sylphie "(It's throbbing… am I doing it right? My body is getting hot too…)"

                            sylphie "Mmmph… (She sucks harder, taking it to the base.)"

                            sylphie "(Ah… the head is hitting my throat… Is he enjoying it…?)"

                            narrator "The pace increases, Sylphie sucks with more confidence, cheeks flushed. Rudeus gently holds her green hair, guiding the movements."

                            rudeus "Sylphie… I'm almost… gonna cum in your little mouth… Get ready to swallow."

                            sylphie "Mmmph… (Eyes wide, but she keeps going, feeling the cock swell.)"

                            call gozando from _call_gozando_13

                            show vid_sylph_blowjob_cum with fade

                            narrator "The cock pulses hard, shooting thick, hot semen into her mouth."

                            rudeus "Argh… FUCK… Keep going!"

                            sylphie "Urgh… *cough*…"

                            narrator "Sylphie keeps sucking with effort, eyes watering, but keeps her mouth firm until the last spurt."

                            sylphie "(W-what is this in my mouth?)"

                            sylphie "(Should I stop?)"

                            rudeus "Ahn… holy shit… that was incredible, Sylphie…"

                            sylphie "I-I… glup… swallow?"

                            "The vibration of her voice makes Rudeus shudder."

                            rudeus "(Argh… fuck… that's insanely good!)"

                            rudeus "Yes, swallow it all, you naughty little elf."

                            scene black with fade

                            "She swallows his thick cum, trying not to make a face."

                            sylphie "Glup… *cough* *cough*…"

                            sylphie "It has a strong taste… but it's not that bad…"

                            scene bg sylph_hut with fade
                            show sylphie embarrassed at right
                            show rudeus normal at left
                            with dissolve

                            sylphie "R-rudy… I… I did it… I swallowed everything…"

                            rudeus "You were perfect. Best blowjob of my life."

                            rudeus "Your mouth is addictive, Sylphie. I want more."

                            sylphie "D-don't say it like that… you dummy… but… I liked it too…"

                            sylphie "Swallowing that hot liquid was weird… it made me kinda dizzy…"

                            sylphie "I never thought I would do something like this with a man one day…"

                            rudeus "Hehe, good. We'll repeat whenever you want."

                            sylphie "O-okay…"

                            $ sylph_afeicao += interaction_reward
                            $ sylph_interacted_today = True
                            $ renpy.notify("You gained +{} affection with Sylphie!".format(interaction_reward))
                            jump passar_tempo
                        else:

                            $ patreon_msg = get_patreon_message(1)
                            "[patreon_msg]"
                            jump sylph_menu
                "Ask to lick her (220)":

                    if sylph_afeicao < 220:
                        "🔒 You need at least 220 affection to unlock this option."
                        jump sylph_menu
                    else:
                        if True:
                            $ interaction_reward = get_interaction_reward(sylph_afeicao)

                            rudeus "Sylphie… today the reward has to be mutual. I want to make you feel good too, to motivate you for the lessons."

                            sylphie "M-make me feel good…? How…? My body is already shivering just imagining."

                            rudeus "I want to eat you out. Your little pussy… or maybe your ass. I'm gonna drive you crazy."

                            sylphie "E-eat me… down there?! Rudy, that's… I've never… my legs are gonna shake!"

                            rudeus "Relax, I'll go slowly. It's gonna feel good for you."

                            sylphie "…Okay… but slowly, okay? I'm a virgin down there…"

                            menu:
                                "Eat her pussy":
                                    rudeus "Your pussy… I want to taste naughty little elf pussy."

                                    sylphie "M-my pussy…? B-but… I've never let anyone do this… I'm… scared."

                                    rudeus "Trust me, Sylphie. I'll be very careful. You'll love it, I promise."

                                    sylphie "O-okay… my pussy… but slowly, okay?"

                                    scene black with fade

                                    narrator "You kneel between her legs, kissing the inside of her thighs first, feeling the soft skin and sweet scent. Then you reach her wet pussy, pink lips swollen with arousal."

                                    show vid_sylph_oral with fade

                                    rudeus "Good girl. Spread your legs more… So wet already… tastes like naughty elf."

                                    sylphie "Ahn… Rudy… your tongue… it's hot… ahn!"

                                    sylphie "(It's… throbbing… It's weird but so good…)"

                                    narrator "You lick slowly, circling her clit, then push a little inside, feeling the hot walls contract."

                                    narrator "Sylphie moans softly, hips moving involuntarily."

                                    sylphie "D-don't stop… it feels so good… my ears… they're tingling…"

                                    sylphie "Ahn, faster!"

                                    rudeus "I'm gonna make you cum in my mouth, Sylphie."

                                    narrator "The pace quickens, Sylphie arches her back, legs trembling. Her climax arrives first…"

                                    sylphie "Rudy… I'm gonna… I'm gonna cum… Ahn! Ahh-ahhh!"

                                    call gozando from _call_gozando_14

                                    scene sylphie_spread_legs_eat_out_blush_cum with fade

                                    narrator "Sylphie cums hard, pussy pulsing, squirting honey into his mouth. Her body convulses in waves of pleasure, breathing ragged as Rudeus keeps licking."

                                    sylphie "I… I… came… so embarrassing…"

                                    sylphie "But it felt so good… your tongue… left me all weak…"

                                    sylphie "Y-you can stop now… no need to lick anymore…"

                                    rudeus "I can't resist, you're addictive, Sylphie."

                                    sylphie "Aah so embarrassing… B-but I liked it… Can we do it again someday…?"

                                    rudeus "Of course, naughty little elf."
                                "Eat her ass":

                                    rudeus "Your little ass… I want to taste naughty elf from behind."

                                    sylphie "M-my ass?! That's… so weird… I don't know if I can… But if you promise to be gentle…"

                                    rudeus "Trust me. I'll get you nice and relaxed. I want to lick that cute little ass."

                                    sylphie "…Okay… but if I say stop, you stop, okay?"

                                    rudeus "Promise."

                                    scene black with fade

                                    narrator "She gets on all fours, arching her back. Rudeus spreads her cheeks, kissing around first, feeling the goosebumps. Then he licks her tight ring slowly, wetting it with saliva, feeling it twitch."

                                    show vid_sylph_lick_anus with fade

                                    sylphie "Ahn… it's weird… but… good… ahn!"

                                    sylphie "(My ass… it's… reacting… I never thought I'd feel this…)"

                                    rudeus "Relax… your ass is trembling."

                                    rudeus "But your little hole is so tight, I love it."

                                    sylphie "R-Rudy… I'm wet in front too… so embarrassing…"

                                    narrator "You keep licking slowly, circling and pushing the tip of your tongue in, feeling her body relax little by little. Sylphie moans louder, arching more."

                                    sylphie "Ahn… I'm liking it… your licks… making me all weak… More, please!"

                                    narrator "After a while, you notice her legs starting to tremble slightly, orgasm approaching from anal stimulation alone."

                                    sylphie "I can't take it anymore… my legs are giving out… Ahn, I'm gonna…!"

                                    call gozando from _call_gozando_15
                                    scene sylph_sweat_postsex with fade

                                    narrator "Sylphie cums trembling, asshole clenching around the tongue. She falls forward, panting, ass red from arousal."

                                    rudeus "Good little elf. You took it well. Came just from ass play? What a naughty girl."

                                    sylphie "Y-yes… it was intense… like a wave of pleasure up my spine."

                                    rudeus "Hehe, your ass is addictive."

                            $ sylph_afeicao += interaction_reward
                            $ sylph_interacted_today = True
                            $ renpy.notify("You gained +{} affection with Sylphie!".format(interaction_reward))
                            jump passar_tempo
                        else:

                            $ patreon_msg = get_patreon_message(1)
                            "[patreon_msg]"
                            jump sylph_menu
                "Vaginal sex (310)":

                    if sylph_afeicao < 310:
                        "🔒 You need at least 310 affection to unlock this option."
                        jump sylph_menu
                    else:
                        if True:
                            $ interaction_reward = get_interaction_reward(sylph_afeicao)

                            rudeus "Sylphie… it's time. I want to fuck your little pussy nice and deep today. The ultimate reward for your dedication in class."

                            sylphie "F-fuck…? Inside me…? Rudy, I've never done this… Will it hurt?"

                            rudeus "Don't worry, I'll go slow at first. But you want it, right? You're already dripping just thinking about it."

                            sylphie "…I want it… but go gentle, okay? My heart is beating so fast…"

                            rudeus "I promise."

                            scene black with fade

                            narrator "You lie on your back on the grass, Sylphie climbs on top, aligning her wet little pussy with your erect cock. She lowers slowly, feeling the head spread her lips."

                            sylphie "Ahn… Rudy… it's going in… slowly… It's big… but feels good."

                            rudeus "You're so tight and warm… My cock is drooling just from touching you. Go deeper, my little elf."

                            show vid_sylph_vaginal_1 with fade

                            narrator "Rudeus holds her thighs and pushes slowly. Sylphie bites her lip, eyes closed, feeling every inch stretch her. The smell of sex fills the air."

                            sylphie "Ahn… it hurts a little… but… keep going… I can take it… Now it's filling everything."

                            rudeus "Good girl… I'm all the way in… Fuck, you're so hot and wet."

                            sylphie "R-Rudy… it's hitting so deep… ahn… slow… no, wait… harder now…"

                            narrator "The rhythm starts slow, then speeds up. Skin slapping skin, moans echoing. Sylphie squeezes her legs around him, feeling the cock pulse inside."

                            show vid_sylph_vaginal_2 with fade

                            sylphie "More… deeper… ahn! Rudy… it feels so good… my pussy… it's opening for you… I feel it stretching…"

                            rudeus "You're perfect, Sylphie… Squeezing my cock like that… I'm gonna cum so hard."

                            sylphie "Ahn… ahn… I feel everything… my ears… tingling… don't stop! I'm getting close…"

                            narrator "The pace gets intense, Sylphie arches her back, pussy contracting in waves. Her orgasm hits first…"

                            sylphie "Rudy… I'm gonna… gonna cum… Ahn! Ahh-ahhh!"

                            call gozando from _call_gozando_16

                            narrator "Sylphie cums trembling, pussy pulsing hard around the cock, squirting hot fluids down her thighs. Her body convulses, eyes rolling slightly in pleasure."

                            rudeus "Cum for me, little elf… Squeeze tighter… Arghh… I'm almost there too…"

                            rudeus "Cumming inside… take it all… Ahn!"

                            call gozando from _call_gozando_17
                            scene sylphie_vaginal_outdoors_pov_cum with fade

                            narrator "The cock pulses, filling her pussy with thick hot spurts, mixing with her juices. Sylphie moans loudly, feeling the warmth spread."

                            sylphie "M-my body is shaking so much, is this normal?"

                            rudeus "You were incredible, Sylphie. My naughty little elf is no longer a virgin."

                            sylphie "D-don't say it like that… but… it's true… I feel different… so hot inside…"

                            rudeus "Hehe, I'll keep you hot whenever you want."

                            $ sylph_afeicao += interaction_reward
                            $ sylph_interacted_today = True
                            $ renpy.notify("You gained +{} affection with Sylphie!".format(interaction_reward))
                            jump passar_tempo
                        else:

                            $ patreon_msg = get_patreon_message(1)
                            "[patreon_msg]"
                            jump sylph_menu
                "Anal sex (420)":

                    if sylph_afeicao < 420:
                        "🔒 You need at least 420 affection to unlock this option."
                        jump sylph_menu
                    else:
                        if True:
                            $ interaction_reward = get_interaction_reward(sylph_afeicao)

                            rudeus "Sylphie… today I want something even more special."

                            sylphie "Oh no… what do you want now, Rudy…? I already gave you my pussy…"

                            sylphie "What more do you want from me…?"

                            rudeus "I want to fuck your little ass nice and slow. The final reward for the magic master you've become."

                            sylphie "N-no… in my ass?! Rudy… that's… I've never… it's gonna hurt a lot, right…?"

                            rudeus "I'll prepare you properly, don't worry."

                            sylphie "Okay… I trust you… but promise to go really slow?"

                            rudeus "Promise. You're my precious little elf."

                            scene black with fade

                            narrator "Rudeus starts licking her tight ring slowly, wetting it with tongue and gentle fingers, using saliva as lube. Sylphie trembles, moaning softly, asshole relaxing bit by bit."

                            sylphie "Ahn… so weird… ahn… don't stop…"

                            rudeus "You're already relaxing… Look how it opens for me. Ready?"

                            sylphie "Y-yes… slowly… please…"

                            show vid_sylph_anal with fade

                            narrator "He pushes slowly, inch by inch, holding her waist. The tight ring stretches, gripping the cock with pressure."

                            rudeus "Deep breath… Just the tip first… Like that… Fuck, so tight."

                            sylphie "Ahn… hurts… but… keep going… ahn… it's opening… my ass… opening for your cock…"

                            narrator "The rhythm starts slow, then picks up a little. Sylphie arches more, shaking her ass, moans getting louder, sweat running down her back."

                            show vid_sylph_anal_2 with fade

                            sylphie "So deep… ahn! My ass… Rudy… ahn! I feel you all inside me."

                            rudeus "Good girl… Squeeze like that… I'm gonna fuck this virgin ass so good."

                            sylphie "Ahn… ahn… my ears… burning… I'm gonna cum… ahn!"

                            rudeus "Cum for me, little elf… Squeeze that ass tighter… Arghh… I'm almost there too…"

                            call gozando from _call_gozando_18

                            narrator "She trembles hard, cumming intensely from anal alone – asshole clenching rhythmically, a powerful anal orgasm making her whole body shake."

                            rudeus "Arghh… cumming inside your ass… take it all… Ahn!"

                            call gozando from _call_gozando_19
                            scene sylph_anal_cum with fade

                            narrator "The cock pulses, filling her ass with thick hot spurts, some leaking out the edges. Sylphie moans loudly, feeling the warmth spread."

                            sylphie "I-I… came just from this… so embarrassing… but… it was incredible… hot, like fire magic…"

                            rudeus "You took it like a champ. My naughty girl."

                            sylphie "D-don't say it like that… but… I want to do it again… when I'm more used to it."

                            rudeus "Of course, I'll get your little ass nice and trained, hehehe."

                            $ sylph_afeicao += interaction_reward
                            $ sylph_interacted_today = True
                            $ renpy.notify("You gained +{} affection with Sylphie!".format(interaction_reward))
                            jump passar_tempo
                        else:

                            $ patreon_msg = get_patreon_message(1)
                            "[patreon_msg]"
                            jump sylph_menu
                "Back":

                    jump sylph_menu
        "Back":

            jump locais
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
