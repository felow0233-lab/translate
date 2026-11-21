



default aisha_afeicao = 0
default aisha_talked_today = False
default aisha_gifted_today = False
default aisha_interacted_today = False



label aisha_intro:
    show rudeus normal at left, slide_fade
    show aisha feliz at right, slide_fade:
        zoom 0.5
    with dissolve
    aisha "Hey, big bro!"
    jump aisha_menu


label aisha_menu:
    menu:

        "💬Chat" if not aisha_talked_today:
            $ chat_reward = get_chat_reward(aisha_afeicao)
            rudeus "So, Aisha!? How's your day going?"
            aisha "Oh… It's fine… Thanks for asking!"

            $ aisha_afeicao += chat_reward
            $ aisha_talked_today = True
            $ renpy.notify("You gained +{} affection with Aisha!".format(chat_reward))
            jump aisha_menu

        "🎁Give Gift" if not aisha_gifted_today:

            $ available_gifts = []
            if simple_flower_count > 0:
                $ available_gifts.append(("simple_flower", "Simple Flower", simple_flower_count, 10))
            if chocolate_box_count > 0:
                $ available_gifts.append(("chocolate_box", "Box of Chocolates", chocolate_box_count, 25))
            if luxury_jewelry_count > 0:
                $ available_gifts.append(("luxury_jewelry", "Diamond Earring", luxury_jewelry_count, 50))



            $ chosen_gift = renpy.call_screen("gift_selection_screen", "aisha", "Aisha", available_gifts)

            if chosen_gift == "simple_flower":
                $ simple_flower_count -= 1
                rudeus "Hey Aisha, I brought you a flower!"
                aisha "Oh! A flower for me? Thank you so much, Big Bro!"
                $ aisha_afeicao += 10
                $ aisha_gifted_today = True
                $ renpy.notify("Aisha loved the gift! +10 Affection")

            elif chosen_gift == "chocolate_box":
                $ chocolate_box_count -= 1
                rudeus "Aisha, I got you some fancy chocolates!"
                aisha "Wow! These look so delicious! You're the best Big Bro ever!"
                $ aisha_afeicao += 25
                $ aisha_gifted_today = True
                $ renpy.notify("Aisha loved the gift! +25 Affection")

            elif chosen_gift == "luxury_jewelry":
                $ luxury_jewelry_count -= 1
                rudeus "Aisha... I want you to have this."
                aisha "Is that... a jewel!? Big Bro, this is too much!"
                aisha "It's so beautiful... I'll treasure it forever!"
                $ aisha_afeicao += 50
                $ aisha_gifted_today = True
                $ renpy.notify("Aisha loved the gift! +50 Affection")

            elif chosen_gift == "premium_necklace":
                $ premium_necklace_count -= 1
                rudeus "Aisha... This is something really special for you."
                aisha "W-what!? Big Bro, this necklace is... incredible!"
                aisha "I can't believe you got this for me! I love you so much!"
                $ aisha_afeicao += 125
                $ aisha_gifted_today = True
                $ renpy.notify("Aisha ABSOLUTELY loved the gift! +125 Affection")
            else:

                pass

            jump aisha_menu

        "😏Interact" if not aisha_interacted_today:
            menu:
                "Ask to grab her breast (30)":
                    if aisha_afeicao < 30:
                        "🔒 You need at least 30 affection to unlock this option."
                        jump aisha_menu
                    else:

                        rudeus "Hey Aisha, can I squeeze your boobs?"
                        aisha "B-big Bro... Why do you want to do that...?"
                        rudeus "I heard it helps make them bigger!"
                        aisha "Really? Ahh... Alright then..."
                        show vid_aisha_breast_grabbing with fade
                        aisha "This… this feels kinda weird, Big Bro…"
                        rudeus "But you like it, don’t you?"
                        aisha "A little, I guess…"
                        rudeus "Hehe, you’re the best, Aisha."
                        rudeus "Let's keep doing this until they're like Zenith's!"
                        aisha "O-okay..."
                        $ interaction_reward = get_interaction_reward(aisha_afeicao)
                        $ aisha_afeicao += interaction_reward
                        $ aisha_interacted_today = True
                        $ renpy.notify("You gained +{} affection with Aisha!".format(interaction_reward))
                        jump passar_tempo
                "Ask for a blowjob (80)":

                    if aisha_afeicao < 80:
                        "🔒 You need at least 80 affection to unlock this option."
                        jump aisha_menu
                    else:

                        $ interaction_reward = get_interaction_reward(aisha_afeicao)
                        rudeus "Arghh… Aisha, a snake bit my dick! Can you help me?"
                        aisha "A-a snake? Oh my god…"
                        aisha "What should I do, Big Bro!?"
                        rudeus "Just… use your mouth to suck out the venom."
                        aisha "Eek! M-my mouth?"
                        rudeus "Hurry, Aisha, please!"
                        aisha "Okay… I-I’ll try…"
                        show vid_aisha_blowjob with fade
                        aisha "Hmph… L-like this, Big Bro?"
                        rudeus "Ahhh… Yes, Aisha, that’s perfect!"
                        rudeus "Keep sucking, please."
                        rudeus "I can feel… the venom coming out!"
                        call gozando from _call_gozando
                        scene aisha_blowjob_cum with fade
                        play sound "audio/cum.mp3"
                        aisha "U-uhh… You... you came in my mouth!"
                        rudeus "Haha, thanks Aisha. You saved me!"
                        aisha "Y-you… you pervert…"
                        $ aisha_afeicao += interaction_reward
                        $ aisha_interacted_today = True
                        $ renpy.notify("You gained +{} affection with Aisha!".format(interaction_reward))
                        jump passar_tempo
                "Ask for vaginal sex (180)":

                    if aisha_afeicao < 180:
                        "🔒 You need at least 180 affection to unlock this option."
                        jump aisha_menu
                    else:

                        $ interaction_reward = get_interaction_reward(aisha_afeicao)
                        rudeus "Aisha! I think my dick's about to explode! Help me, please!"
                        aisha "O-oh no, Big Bro! Is this serious?"
                        rudeus "Yeah, I really need help…"
                        aisha "What do you want me to do?"
                        rudeus "Maybe I could... Stick it in your vagina?"
                        aisha "W-what!? M-my vagina!?"
                        rudeus "Please, Aisha! It’s urgent!"
                        aisha "Hmmm... O-okay..."
                        scene vid_aisha_vaginal_1 with fade
                        aisha "N-ghg..... Slow down, big bro..."
                        aisha "You're stretching me out!"
                        rudeus "It's just... Your pussy is so tight!"
                        aisha "I-is that good?"
                        rudeus "Yes, fucking good!"
                        rudeus "You're the best, Aisha!"
                        rudeus "N-ngh.... I-I'm gonna cum..."
                        call gozando from _call_gozando_1
                        scene aisha_vaginal_cum with fade
                        aisha "A-ahhh.... Big Bro...."
                        aisha "You came inside me!"
                        rudeus "Arghhh.... Fuck... That was amazing, Aisha!"
                        $ aisha_afeicao += interaction_reward
                        $ aisha_interacted_today = True
                        $ renpy.notify("You gained +{} affection with Aisha!".format(interaction_reward))
                        jump passar_tempo
                "Ask for anal sex (350)":

                    if aisha_afeicao < 350:
                        "🔒 You need at least 350 affection to unlock this option."
                        jump aisha_menu
                    else:

                        $ interaction_reward = get_interaction_reward(aisha_afeicao)
                        rudeus "Aisha! I really need your help again!"
                        aisha "Oh no... What is it this time, Big Bro!?"
                        rudeus "It's my dick again... I need... to put it in your ass this time!"
                        aisha "M-my ass!?"
                        rudeus "Please, I’m desperate!"
                        rudeus "You're the only one who can help me!"
                        aisha "O-ok, let’s go..!"
                        show vid_aisha_anal with fade
                        aisha "Ouch... That's weird, Big Bro..."
                        rudeus "Just hang in there, Aisha!"
                        rudeus "I’m almost there…"
                        aisha "Hmph… Okay…"
                        aisha "I can take a bit more... I think..."
                        rudeus "You’re the best, little sister."
                        rudeus "Your ass is the best!"
                        aisha "T-thank you..."
                        call gozando from _call_gozando_7
                        scene aisha_anal_cum with fade
                        play sound "audio/cum.mp3"
                        aisha "A-ah... You came inside my ass, Big Bro!"
                        rudeus "Ahhhh, that feels so good..."
                        rudeus "Always helping me out in tough times, huh?"
                        aisha "S-sisters are for that, I guess..."
                        $ aisha_afeicao += interaction_reward
                        $ aisha_interacted_today = True
                        $ renpy.notify("You gained +{} affection with Aisha!".format(interaction_reward))
                        jump passar_tempo
                "Go back":


                    jump aisha_menu
        "Return":

            jump locais
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
