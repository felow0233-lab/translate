
default norn = Character("Norn", color="#fffab0")


default norn_event = 0
default norn_afeicao = 0
default norn_talked_today = False
default norn_gifted_today = False
default norn_interacted_today = False

default norn_intro = True

default norn_breast_done = False
default norn_handjob_done = False
default norn_blowjob_done = False
default norn_spread_done = False



label norn_intro:
    if norn_intro:
        jump norn_intro_2
    else:

        show rudeus normal at left
        show norn normal at right:
            zoom 0.5
        with dissolve

        python:
            if norn_afeicao >= 200:
                greeting = renpy.random.choice([
        "Rudeus! Finally! I was... waiting for you to come by.",
        "Big brother! I'm glad you showed up... I wanted to see you.",
        "Oh, you came! I... I missed you... N-not that I was counting the minutes or anything!"
    ])
            elif norn_afeicao >= 120:
                greeting = renpy.random.choice([
        "Oh... you again. N-not that I'm happy to see you or anything...",
        "Rudeus... you showed up. I... was thinking about you earlier. J-just thinking!",
        "Hmpf... Took you long enough. I... thought you weren't coming today."
    ])
            elif norn_afeicao >= 80:
                greeting = renpy.random.choice([
        "Nii-chan! It's so good to see you! I-I mean... what do you want?",
        "Oh... it's you. N-not that I noticed you were gone or anything, okay?",
        "Rudeus-nii... you came. That's... nice, I guess."
    ])
            elif norn_afeicao >= 50:
                greeting = renpy.random.choice([
        "Hmph, you again. What do you want this time?",
        "Oh... it's you. Need something?",
        "Why are you here? I hope it's not to bother me again."
    ])
            elif norn_afeicao >= 20:
                greeting = renpy.random.choice([
        "Hmph, you're here again. What do you want?",
        "Ugh... what do you want now?",
        "Don't you have anything better to do? Why are you here?"
    ])
            else:
                greeting = renpy.random.choice([
        "Ugh, what do you want? Can't you see I'm busy?",
        "Go away. I'm busy.",
        "Seriously? You again? Leave me alone.",
        "I don't have time for you right now. Get out."
    ])

        norn "[greeting]"

        jump norn_menu


label norn_menu:
    menu:
        "😈 Flirt":

            python:
                if norn_afeicao >= 200:
                    flirt_option = renpy.random.choice([
        ("Norn, you know you're the prettiest girl I've ever seen?",
        "R-Rudeus... you can't just say things like that out of nowhere!",
        "But... thank you. You're also... pretty handsome, you know?"),
        ("You know, I can't stop thinking about you.",
        "I-I think about you too... all the time...",
        "That's... that's weird, right? But I like it..."),
        ("Every time I see you, my heart races.",
        "S-stop it! Mine does the same when you show up...",
        "That's... that means... anyway.")
    ])
                elif norn_afeicao >= 120:
                    flirt_option = renpy.random.choice([
        ("Norn, you get prettier every day.",
        "Hmpf... You really think so?",
        "W-well... you're not that ugly either..."),
        ("Your smile is beautiful, you know?",
        "I-I wasn't smiling! You're seeing things!",
        "But... if I were... would you like it?"),
        ("I love it when you blush like that.",
        "I-I'm not blushing! It's just... the heat!",
        "And you're annoying... but in a good way.")
    ])
                elif norn_afeicao >= 80:
                    flirt_option = renpy.random.choice([
        ("Hey Norn, you get prettier with each passing day.",
        "Hmpf... Fine, fine. Thanks, I guess.",
        "You... aren't so bad to look at either, sometimes."),
        ("That hairstyle really suits you.",
        "Really? I... tried something different today.",
        "Glad you noticed... idiot."),
        ("You have the most beautiful eyes I've ever seen.",
        "D-don't stare at me like that!",
        "But... thanks. Yours are pretty too.")
    ])
                elif norn_afeicao >= 50:
                    flirt_option = renpy.random.choice([
        ("Hey Norn, did you do something different with your hair?",
        "Hmpf... What are you talking about? My hair is normal, you idiot!",
        ""),
        ("That dress looks great on you.",
        "A-are you trying to get something? Why are you complimenting me?",
        "..."),
        ("You look pretty today.",
        "'Today'? So the other days I'm not?",
        "Hmpf!")
    ])
                elif norn_afeicao >= 20:
                    flirt_option = renpy.random.choice([
        ("Hey Norn, did you do something different with your hair?",
        "Hmpf... What are you talking about? My hair is normal, you idiot!",
        ""),
        ("You look pretty today.",
        "Stop trying to flatter me. It won't work.",
        ""),
        ("I like it when you smile.",
        "I wasn't smiling! And stop looking at me!",
        "")
    ])
                else:
                    flirt_option = renpy.random.choice([
        ("Hey Norn, you look really pretty today.",
        "W-what? Stop complimenting me, it's weird!",
        ""),
        ("Your hair looks nice.",
        "Buzz off! What do you want?",
        ""),
        ("You look gorgeous.",
        "Shut up! I don't want to hear that from you!",
        "")
    ])

            rudeus "[flirt_option[0]]"
            norn "[flirt_option[1]]"
            if flirt_option[2]:
                norn "[flirt_option[2]]"




            $ norn_afeicao += 5
            $ renpy.notify("You gained +5 affection with Norn!")
            jump passar_tempo
        "🎁Give Gift":


            if norn_gifted_today:
                "You've already given Norn a gift today. Try again tomorrow."
                jump norn_menu
            else:
                $ available_gifts = []
                if simple_flower_count > 0:
                    $ available_gifts.append(("simple_flower", "Simple Flower", simple_flower_count, 10))
                if chocolate_box_count > 0:
                    $ available_gifts.append(("chocolate_box", "Box of Chocolates", chocolate_box_count, 25))
                if luxury_jewelry_count > 0:
                    $ available_gifts.append(("luxury_jewelry", "Diamond Earring", luxury_jewelry_count, 50))
                $ chosen_gift = renpy.call_screen("gift_selection_screen", "norn", "Norn", available_gifts)

                if chosen_gift == "simple_flower":
                    $ simple_flower_count -= 1
                    rudeus "Norn, I picked this flower just for you!"
                    norn "A flower? That's kinda sweet, bro. Thanks!"
                    $ norn_afeicao += 10
                    $ norn_gifted_today = True
                    $ renpy.notify("Norn liked the gift! +10 Affection")
                elif chosen_gift == "chocolate_box":
                    $ chocolate_box_count -= 1
                    rudeus "Got you some chocolates, sis!"
                    norn "Chocolates? Yum! You're the best sometimes."
                    $ norn_afeicao += 25
                    $ norn_gifted_today = True
                    $ renpy.notify("Norn liked the gift! +25 Affection")

                elif chosen_gift == "luxury_jewelry":
                    $ luxury_jewelry_count -= 1
                    rudeus "Here, Norn—this earring is for you."
                    norn "Whoa, jewelry? This is fancy! Are you trying to butter me up?"
                    $ norn_afeicao += 50
                    $ norn_gifted_today = True
                    $ renpy.notify("Norn liked the gift! +50 Affection")

                elif chosen_gift == "premium_necklace":
                    $ premium_necklace_count -= 1
                    rudeus "Norn, this necklace is a token of how much I care."
                    norn "A premium necklace? Wow, brother... this is amazing!"
                    norn "I'll wear it every day. Thanks a ton!"
                    $ norn_afeicao += 125
                    $ norn_gifted_today = True
                    $ renpy.notify("Norn ABSOLUTELY loved the gift! +125 Affection")
                else:

                    pass

                jump norn_menu
        "😏 Interact":


            menu:
                "Breast (30)":

                    if norn_afeicao < 30:
                        "🔒 You need at least 30 affection to unlock this option."
                        jump norn_menu
                    else:

                        if not norn_breast_done:
                            rudeus "Hey Norn... can I take a quick look at your breasts?"
                            norn "What?! No way, you pervert!"
                            rudeus "(Time to use Aisha as bait...)"
                            rudeus "Well... Aisha lets me see and even squeeze hers when I ask."
                            rudeus "She said it's normal between siblings who care about each other..."
                            norn "She... Aisha did that for you?! Seriously?"
                            rudeus "Yeah... You know... she's kind of... affectionate with me."
                            rudeus "And I think she likes me, so she lets me do stuff like that..."
                            norn "Hmmm... fine, but only because I don't want to fall behind her."
                            rudeus "(Nice... I knew if I used Aisha as bait, she'd give in. Now I just need to stay calm and not look desperate.)"
                            norn "But... Just... just a little peek, okay?"

                            show norn_breast_show_2 with fade

                            norn "Here... take a look..."
                            norn "Way better than Aisha's, right?"
                            rudeus "Wow... they're beautiful, Norn."
                            rudeus "You're right... They're much prettier than hers..."
                            norn "Really? You think so?"
                            rudeus "Absolutely."

                            menu:
                                "Ask to squeeze":
                                    rudeus "Can I... touch them a little?"
                                    norn "T-touch them? Why would you want to do that?"
                                    rudeus "Just to make sure they're better than Aisha's, you know?"
                                    norn "Hmpf... Fine, but make it quick, you idiot!"
                                    show vid_norn_pov_grab_breast with fade
                                    rudeus "Wow... They're so soft and warm..."
                                    norn "N-ngh... d-don't squeeze so hard..."
                                    norn "They're sensitive, you moron..."
                                    rudeus "You're amazing, Norn."
                                    norn "And you're disgusting... but... thanks, I guess..."
                                    norn "That's enough!"
                                "Leave":

                                    pass

                            $ norn_breast_done = True
                        else:

                            rudeus "Norn... can I see your breasts again?"
                            norn "Hmpf... Fine."
                            show norn_breast_show_2 with fade
                            rudeus "Beautiful as always..."
                            show vid_norn_pov_grab_breast with fade
                            norn "N-ngh... that's enough!"

                        $ interaction_reward = get_interaction_reward(norn_afeicao)
                        $ norn_afeicao += interaction_reward

                        $ renpy.notify("You gained +{} affection with Norn!".format(interaction_reward))
                        jump passar_tempo
                "Handjob (80)":

                    if norn_afeicao < 80:
                        "🔒 You need at least 80 affection to unlock this option."
                        jump norn_menu
                    else:





                        if not norn_handjob_done:
                            rudeus "Norn... how about helping me relieve some stress with your hand today?"
                            norn "Are you crazy? I'm not doing that!"
                            rudeus "You know... Aisha already did it for me a few times... said it felt really good."
                            norn "I don't believe you..."
                            rudeus "I'm serious, you can ask her if you want..."
                            norn "Hmpf.. Fine... But just this once. And don't tell anyone!"

                            menu:
                                "Handjob normal":

                                    show vid_norn_handjob with fade

                                    rudeus "Just like that... yeah, Norn... that feels amazing..."
                                    norn "You're such a shameless pervert..."
                                    norn "You don't even have the decency to be embarrassed asking your own sister for this..."
                                    norn "(I can't believe the first dick I'm touching is Rudeus-nii's... How embarrassing...)"
                                    norn "(But... it's actually kind of fun... It's so hard and warm..."
                                    norn "(Damn... I don't want to admit it, but this feels really nice...)"
                                    menu:
                                        "Cum":
                                            pass
                                    rudeus "Argh... Norn... I'm gonna cum... faster!"
                                    norn "Hmpf... Fine..."
                                    call gozando from _call_gozando_23
                                    play sound "cum.mp3"
                                    scene norn_handjob_cum with fade

                                    norn "Argh! Nii-chan... Who said you could cum on me?"
                                    rudeus "Sorry... I couldn't hold it."
                                    norn "Tsk... You're pathetic..."
                                "Handjob + Breast play":

                                    show vid_norn_breast_handjob with fade
                                    rudeus "Just like that... yeah, Norn... that feels amazing..."
                                    norn "You're such a shameless pervert..."
                                    norn "(I can't believe the first dick I'm touching is Rudeus-nii's... How embarrassing...)"
                                    norn "(But... it's actually kind of fun... It's so hard and warm... And at least he's moaning my name and not Aisha's."
                                    norn "(Damn... I don't want to admit it, but this feels really nice...)"
                                    menu:
                                        "Cum":
                                            pass
                                    rudeus "Argh... Norn... I'm gonna cum... faster!"
                                    norn "Hmpf... Fine..."
                                    call gozando from _call_gozando_24
                                    play sound "cum.mp3"
                                    scene norn_breast_handjob_cum with fade
                                    norn "Argh! Nii-chan... Who said you could cum on me?"
                                    rudeus "Sorry... I couldn't hold it. You're too good at this."
                                    norn "Tsk... You're pathetic..."

                            $ norn_handjob_done = True
                        else:

                            menu:
                                "Handjob normal":
                                    rudeus "Norn... your hand again?"
                                    norn "...Fine, come on."
                                    show vid_norn_handjob with fade
                                    menu:
                                        "Cum":
                                            pass
                                    rudeus "Argh... Norn... I'm cumming!"
                                    call gozando from _call_gozando_25
                                    play sound "cum.mp3"
                                    scene norn_handjob_cum with fade

                                    norn "Hmpf... done. Happy?"
                                "Handjob + Breast play":

                                    rudeus "Norn... your hand again? And this time with those cute tits too?"
                                    norn "...Fine, come on."
                                    show vid_norn_breast_handjob with fade
                                    menu:
                                        "Cum":
                                            pass
                                    rudeus "Argh... Norn... I'm cumming!"
                                    call gozando from _call_gozando_26
                                    play sound "cum.mp3"
                                    scene norn_breast_handjob_cum with fade

                                    norn "Hmpf... done. Happy?"
                                "Go back":

                                    jump norn_menu

                        $ interaction_reward = get_interaction_reward(norn_afeicao)
                        $ norn_afeicao += interaction_reward

                        $ renpy.notify("You gained +{} affection with Norn!".format(interaction_reward))
                        jump passar_tempo
                "Blowjob (180)":

                    if norn_afeicao < 180:
                        "🔒 You need at least 180 affection to unlock this option."
                        jump norn_menu
                    else:





                        if not norn_blowjob_done:
                            rudeus "Norn... have you ever thought about trying it with your mouth?"
                            norn "NO! No way! That's disgusting!"
                            norn "I'm not putting my mouth on your dick, Nii-chan!"
                            rudeus "Aisha already did it for me. You gonna fall behind?"
                            norn "WHAT? I can't believe she already did that! UGH!"
                            rudeus "She said it's weird at first... but then she likes it."
                            norn "She... really said that?"
                            rudeus "Yeah."
                            norn "...fine. But if I hate it, you stop right away, got it?"

                            show vid_norn_blowjob with fade
                            norn "Mmmph..."
                            norn "(It looks like... A big worm... And it's warm...)"
                            rudeus "Ahhh Norn... your mouth is so warm... feels amazing..."
                            norn "(Hmpf... I can't believe I'm doing this for him...)"
                            norn "(The texture of the tip is kind of weird... But... it's actually not that bad...)"
                            norn "(And why does his dick have to be so hard and big? God...)"
                            norn "(Maybe... if I just suck a little more...)"
                            show vid_norn_blowjob_2 with fade
                            rudeus "Woah... Norn... You're incredible..."
                            norn "(Argh... Shut up Nii-chan...)"
                            norn "(But... if I stop now, he'll think I don't like doing this... And I don't want Aisha to be better than me.)"
                            norn "(I'll do better than her... I'll make him like me more than Aisha...)"
                            menu:
                                "Cum":
                                    pass
                            rudeus "Arghhh... Norn... I'm gonna cum..."
                            norn "Mphh!"
                            call gozando from _call_gozando_27
                            play sound "cum.mp3"
                            scene norn_blowjob_cum with fade

                            norn "(Mmph?! HE CAME IN MY MOUTH!?)"
                            norn "(Why... Why did I let him do that?)"

                            scene norn_blowjob_post_cum with fade

                            norn "HMPF!"
                            norn "(I can't believe I let Nii-chan cum in my mouth...)"
                            norn "(It's so... so hot and thick...)"
                            norn "(It's not bad... I kind of liked it... But I can't let him know that...)"
                            norn "W-who said you could cum in my mouth?"

                            rudeus "I'm sorry... I couldn't resist, you're so good at this."
                            norn "Urgh... You pervert..."

                            $ norn_blowjob_done = True
                        else:

                            rudeus "Norn... use that pretty mouth again?"
                            norn "...Hmpf. Come here."
                            show vid_norn_blowjob with fade
                            norn "(Here we go again...)"
                            show vid_norn_blowjob_2 with fade
                            menu:
                                "Cum":
                                    pass
                            rudeus "Argh... I'm cumming!"
                            call gozando from _call_gozando_28
                            play sound "cum.mp3"
                            scene norn_blowjob_cum with fade
                            rudeus "Arghhh... Norn..."
                            scene norn_blowjob_post_cum with fade
                            norn "Hmpf... in my mouth again, Nii-chan?"

                        $ interaction_reward = get_interaction_reward(norn_afeicao)
                        $ norn_afeicao += interaction_reward

                        $ renpy.notify("You gained +{} affection with Norn!".format(interaction_reward))
                        jump passar_tempo
                "Spread / Anal play (350)":

                    if norn_afeicao < 350:
                        "🔒 You need at least 350 affection to unlock this option."
                        jump norn_menu
                    else:






                        $ interaction_reward = get_interaction_reward(norn_afeicao)
                        if not norn_spread_done:
                            rudeus "Norn... turn around for me for a sec?"
                            rudeus "I wanna get a better look at that cute little butt of yours today."
                            norn "This again? Don't you ever get tired of this?"
                            rudeus "It's just that Aisha lets me play with her butt a lot... she says she even gets wet when I go slow."
                            norn "Wet?! She... she really says stuff like that to you?"
                            rudeus "Yeah... She's pretty open about these things. Unlike you, who blushes just from me asking."
                            norn "H-hey! I'm open too... I just don't go around saying gross stuff all the time!"
                            rudeus "Then prove it. Let me see just a little."
                            norn "Hmpf... fine. Just don't ask me to take off my panties."

                            scene norn_lifting_pov with fade

                            rudeus "Wow... even through the panties I can see how round and perky it is."
                            rudeus "What a delicious view, Norn."
                            norn "Stop saying stuff like that... you're making my face burn..."

                            menu:
                                "Ask her to sit on your lap":
                                    rudeus "Come here... sit on my lap. That way you don't have to stand."
                                    norn "Sit on your lap?! That's going too far..."
                                    rudeus "Aisha sits on my lap every time I ask to play with her butt. She says it's more comfortable."
                                    norn "...Aisha again. Fine, but only because I don't want to look like a coward compared to her."

                                    show norn_sitting_lap_panties with fade

                                    norn "There... happy now?"
                                    rudeus "Woah... Norn... You're so hot..."
                                    rudeus "Your butt is so soft and round... And the best part is I know there's a wet little pussy pressing against my dick."
                                    norn "Ahh... Shut up, you pervert..."
                                    norn "(Hmpf... But it's true... Nii-chan is so hard... And because of me, not because of Aisha.)"
                                    norn "(Take that! I can make Nii-chan horny too!)"

                                    menu:
                                        "Ask her to spread":
                                            pass

                                    rudeus "Norn... can you spread your butt a little more with your hands?"
                                    rudeus "Like... pull your cheeks apart so I can see better."

                                    norn "Urgh... You really have no limits..."

                                    show norn_spreading_behind with fade

                                    norn "Like this...?"
                                    rudeus "Perfect... look how the panties sink into the middle... I can see the exact shape of your pink little hole."
                                    norn "You say the most horrible things... You really find this hot?"
                                    rudeus "Yeah... I think it's incredibly hot... And you're so beautiful I can't stop saying these things..."
                                    norn "Hmpf... You're a shameless pervert..."

                                    menu:
                                        "Ask her to remove panties":
                                            rudeus "Norn... now take off your panties for me? I want to see for real."
                                            norn "Take them off?! No way! I said with panties on!"
                                            rudeus "But Aisha takes hers off every time... she says she feels more when I touch her skin directly."
                                            norn "Urgh... fine... you're so persistent, you pervert!"
                                            norn "But don't stare too much..."

                                            scene norn_spreading_behind_naked with fade

                                            rudeus "Damn... without panties it's a thousand times better."
                                            rudeus "Your little hole is so pink and tight... And your pussy... so perfect and wet."
                                            norn "Shut up... don't compliment those things..."
                                            rudeus "I can't stop. You're way too beautiful."
                                            menu:
                                                "Grab her butt":
                                                    scene norn_spreading_side_2 with fade
                                                    norn "HEY!"
                                                    norn "(Nii-chan grabbed my butt without warning... The nerve...)"
                                                    norn "(But... it actually feels kind of nice... He's so strong...)"
                                                    rudeus "Sorry, Norn... I couldn't resist, your butt is so soft..."

                                            menu:
                                                "Ask her to lie down naked":
                                                    rudeus "Now lie face down for me, naked? I want to see everything properly."
                                                    norn "Naked and face down?! This is getting way too ridiculous..."
                                                    rudeus "Aisha does it like that every time... says it feels better for her."
                                                    norn "Urgh... FINE!"

                                                    scene norn_pov_spreading with fade
                                                    rudeus "WOAH! Norn... You're so hot..."
                                                    rudeus "Look how your little hole is so round and tight... And your pussy... so wet and perfect..."
                                                    norn "I already told you to stop complimenting!"
                                                    rudeus "I can't help it... Look how it twitches... it's like it's inviting me."
                                                    norn "You're disgusting..."

                                                    menu:
                                                        "Massage her hole":
                                                            rudeus "Let me massage it with my finger now... nice and slow."
                                                            scene norn_anal_finger_tease with fade
                                                            norn "Argh... this is kind of weird..."
                                                            rudeus "Relax... see how it loosens up when I do this..."
                                                            norn "N-ngh... O-okay... But don't go too deep, okay?"

                                                            menu:
                                                                "Ask to put the tip in":
                                                                    rudeus "Norn... I'm throbbing here... can I put just the tip in? Just to feel the warmth... I promise I won't push it all in."
                                                                    norn "Anal?! No! Absolutely not!"
                                                                    rudeus "Just the tip... Aisha lets me do it when I ask... she says feeling my dick inside her feels amazing."
                                                                    norn "...she really let you? Seriously?"
                                                                    rudeus "Yeah... She even let me cum inside her once."
                                                                    norn "Argh, Aisha, you... Fine. Just the tip. If it hurts, you pull out right away!"

                                                                    show vid_norn_anal with fade

                                                                    norn "Ahh...! Slow down... it's stretching too much..."
                                                                    rudeus "Shhh... just the tip... look how it swallows it slowly..."
                                                                    norn "Nghh... your dick is so thick..."
                                                                    rudeus "You're enjoying it, aren't you? Want a little more?"
                                                                    norn "Don't say that... I... I don't know..."
                                                                    norn "(Damn... Why did I let him put it in my ass?)"
                                                                    norn "(It's stretching me wide... And he keeps saying I like it... How embarrassing...)"
                                                                    norn "(But... It's not as bad as I thought... Nii-chan is so gentle with me...)"
                                                                    norn "(And he's actually putting his dick inside me... Urgh... This is so wrong... But so good...)"
                                                                    norn "(I just can't let him know I'm enjoying it...)"

                                                                    norn "J-just don't get used to it, okay?"

                                                                    menu:
                                                                        "Cum":
                                                                            rudeus "Argh... Norn... I'm going to cum inside your little ass!"
                                                                            call gozando from _call_gozando_29
                                                                            play sound "cum.mp3"
                                                                            scene norn_pov_anal_cum with fade
                                                                            norn "Ahh...! It's so hot... you came inside my ass?!"
                                                                            norn "I didn't give you permission to do that... You pervert..."
                                                                            rudeus "That was incredible... Best anal I've ever had..."
                                                                            rudeus "You're so tight, Norn..."
                                                                            norn "You're... impossible... now I'm all sticky because of you..."
                                                                            rudeus "Wanna take a bath together then?"
                                                                            norn "Not a chance, you pervert."
                                                                            $ norn_spread_done = True
                                                                            $ norn_afeicao += interaction_reward

                                                                            $ renpy.notify("You gained +{} affection with Norn!".format(interaction_reward))
                                                                            jump passar_tempo
                                                "Finish":

                                                    rudeus "Alright... I've seen enough with you naked. You can get up."
                                                    norn "Thank God... I'm never doing this again..."
                                                    $ norn_spread_done = True
                                                    $ norn_afeicao += interaction_reward

                                                    $ renpy.notify("You gained +{} affection with Norn!".format(interaction_reward))
                                                    jump passar_tempo
                                        "Finish":

                                            rudeus "That's enough... you can get up. I've seen plenty for now."
                                            norn "Thank God..."
                                            $ norn_spread_done = True
                                            $ norn_afeicao += interaction_reward

                                            $ renpy.notify("You gained +{} affection with Norn!".format(interaction_reward))
                                            jump passar_tempo
                                "Finish":

                                    rudeus "It's beautiful even like this... you can stop. Thanks, Norn."
                                    norn "Finally..."
                                    $ norn_spread_done = True
                                    $ norn_afeicao += interaction_reward

                                    $ renpy.notify("You gained +{} affection with Norn!".format(interaction_reward))
                                    jump passar_tempo
                        else:

                            rudeus "Norn... turn around for me?"
                            norn "...Fine. Hurry up."
                            scene norn_pov_spreading with fade
                            norn "Good enough?"
                            show vid_norn_anal with fade
                            norn "Ngh... slow down..."
                            menu:
                                "Cum":
                                    pass
                            rudeus "Argh... I'm cumming!"
                            call gozando from _call_gozando_30
                            play sound "cum.mp3"
                            scene norn_pov_anal_cum with fade
                            norn "Hmpf... in my ass again..."
                            $ norn_afeicao += interaction_reward

                            $ renpy.notify("You gained +{} affection with Norn!".format(interaction_reward))
                            jump passar_tempo
                "Go back":

                    jump norn_menu
        "Return":

            jump locais


label norn_intro_2:


    show aisha feliz at my_left:
        xzoom -1
        zoom 0.5
        yalign 1.0
    show norn normal at my_right:
        zoom 0.5
        yalign 1.0
    with dissolve

    aisha "But Norn-nee, you always do this! I just wanted to use the comb first!"
    norn "Because you take everything that's mine without asking, Aisha! This is MINE!"
    aisha "But it's just a comb... and I'm younger, you should spoil me more!"
    norn "Spoil you? You're already way too spoiled! You always get what you want with that little angel face!"




    rudeus "Hey, hey... what's going on here? Fighting again?"

    norn "Rudeus-nii! Look what Aisha did!"
    aisha "Norn-nee is being a pain!"







    norn "She took my comb without asking! And I was using it to fix my hair!"
    norn "Tell her to apologize, Rudeus-nii!"



    rudeus "(Wow... Norn looks really hot when she's angry.)"
    rudeus "(The red cheeks, the hair swaying, her chest heaving up and down from rage... she looks stunning like this.)"
    rudeus "(I never thought of her this way, but now...)"
    rudeus "(Damn, that angry little face is such a turn-on. Imagine her making that face while I...)"
    rudeus "(No, calm down, Rudeus. She's your sister. But still...)"
    rudeus "(Aisha is the cute one... always smiling, always willing... but Norn... she's got that fire.)"
    rudeus "(I bet if I could make her give in, it would be explosive.)"
    rudeus "(But it's gonna be tough, she's never looked at me that way...)"




    rudeus "(Wait... What if I used Aisha as bait?)"
    rudeus "(She hates falling behind her. That would be perfect!)"

    norn "Nii-chan! What are you staring at?"
    rudeus "Nothing, nothing! Just thinking you're growing up fast, Norn. You're becoming a beautiful young woman."
    norn "W-what?! Don't just say stuff like that out of nowhere, you idiot!"
    aisha "Onii-chan complimenting Norn-nee? That's rare~"

    rudeus "Calm down, girls. Let's settle this like adults."
    norn "Adults? You're the worst example, Rudeus-nii!"
    aisha "Hehe, but Onii-chan always works things out nicely~"

    rudeus "Alright, alright. Norn, let me see that comb... maybe I can convince Aisha to apologize."
    norn "Hmpf... fine."



    rudeus "(Wow... Up close like this... her uniform is even tighter around her chest.)"
    rudeus "(When did they get so big? I hadn't noticed before, but now that I'm looking... damn, she's got quite the bust, huh?)"
    rudeus "(And that short skirt... if she bends over...)"
    rudeus "(Focus, Rudeus. First, earn her trust. Then... the rest.)"



    rudeus "Well... if you two stop fighting, maybe I'll buy a little present for both of you in town today. What do you think?"
    norn "A present? What kind of present?"
    aisha "I want one! I want one!"

    rudeus "(Hehe... let the game begin.)"

    $ norn_intro = False

    jump locais
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
