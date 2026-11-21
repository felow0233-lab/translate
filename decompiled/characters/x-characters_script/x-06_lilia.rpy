
default lilia = Character("Lilia", color="#ff99cc")

default lilia_afeicao = 0
default lilia_talked_today = False
default lilia_gifted_today = False
default lilia_interacted_today = False

label lilia_intro:
    show rudeus normal at left, slide_fade
    show lilia normal at right, slide_fade
    with dissolve

    lilia "Young Master?"

    jump lilia_menu


default tem_chave = False

label lilia_menu:
    menu:

        "💬Chat" if not lilia_talked_today:
            $ chat_reward = get_chat_reward(lilia_afeicao)
            rudeus "So, lilia!? How's your day going?"
            lilia "Same as always, cleaning..."
            lilia "But... Thanks for asking, young master."
            $ lilia_afeicao += chat_reward
            $ lilia_talked_today = True
            $ renpy.notify("You gained +{} affection with Lilia!".format(chat_reward))
            jump lilia_menu

        "🎁Give Gift" if not lilia_gifted_today:

            $ available_gifts = []
            if simple_flower_count > 0:
                $ available_gifts.append(("simple_flower", "Simple Flower", simple_flower_count, 10))
            if chocolate_box_count > 0:
                $ available_gifts.append(("chocolate_box", "Box of Chocolates", chocolate_box_count, 25))
            if luxury_jewelry_count > 0:
                $ available_gifts.append(("luxury_jewelry", "Diamond Earring", luxury_jewelry_count, 50))



            $ chosen_gift = renpy.call_screen("gift_selection_screen", "lilia", "Lilia", available_gifts)

            if chosen_gift == "simple_flower":
                $ simple_flower_count -= 1
                rudeus "Hey Lilia, I brought you a flower!"
                lilia "Oh! A flower for me? Thanks..."
                $ lilia_afeicao += 10
                $ lilia_gifted_today = True
                $ renpy.notify("Lilia loved the gift! +10 Affection")
            elif chosen_gift == "chocolate_box":
                $ chocolate_box_count -= 1
                rudeus "Lilia, I got you some fancy chocolates!"
                lilia "Wow! These look so delicious!"
                $ lilia_afeicao += 25
                $ lilia_gifted_today = True
                $ renpy.notify("Lilia loved the gift! +25 Affection")

            elif chosen_gift == "luxury_jewelry":
                $ luxury_jewelry_count -= 1
                rudeus "Lilia... I want you to have this."
                lilia "Is that... a jewel!? This is too much!"
                $ lilia_afeicao += 50
                $ lilia_gifted_today = True
                $ renpy.notify("Lilia loved the gift! +50 Affection")

            elif chosen_gift == "premium_necklace":
                $ premium_necklace_count -= 1
                rudeus "Lilia... This premium necklace is a symbol of my appreciation for you."
                lilia "Young master... This is exquisite! I'm truly honored!"
                lilia "I will cherish this always. Thank you so much!"
                $ lilia_afeicao += 125
                $ lilia_gifted_today = True
                $ renpy.notify("Lilia ABSOLUTELY loved the gift! +125 Affection")
            else:

                pass

            jump lilia_menu

        "😏Interact" if not lilia_interacted_today:
            menu:
                "Ask to show panties (30)":

                    if lilia_afeicao < 30:
                        "🔒 You need at least 30 affection to unlock this option."
                        jump lilia_menu
                    else:

                        $ interaction_reward = get_interaction_reward(lilia_afeicao)
                        rudeus "Hey Lilia, could you show me your panties?"
                        lilia "W-what? S-show you my panties?"
                        lilia "No way I'm doing that..."
                        rudeus "Come on, I know you've been fooling around with Paul again."
                        rudeus "And if I remember correctly, mom forbade you from doing that, didn't she?"
                        lilia "W-what? H-how do you know that?"
                        rudeus "I know everything, Lilia. Now show me, or else..."
                        lilia "Arghh... Okay."
                        lilia "B-but just this once..."
                        scene lilia_show_panties with fade
                        lilia "Satisfied?"
                        rudeus "Damn... You're so hot."
                        rudeus "Now I know why Paul keeps hitting on you."
                        lilia "Y-you brat..."
                        lilia "Now keep your mouth shut, okay?"
                        rudeus "Of course, your secret is safe with me."
                        $ lilia_afeicao += interaction_reward
                        $ lilia_interacted_today = True
                        $ renpy.notify("You gained +{} affection with Lilia!".format(interaction_reward))
                        jump passar_tempo
                "Ask to suck breast (80)":


                    if lilia_afeicao < 80:
                        "🔒 You need at least 80 affection to unlock this option."
                        jump lilia_menu
                    else:


                        $ interaction_reward = get_interaction_reward(lilia_afeicao)
                        rudeus "Hey Lilia, can I suck your breasts?"
                        lilia "S-suck my breasts? W-what kind of question is that?"
                        rudeus "Come on, Lilia. I know you'll enjoy it."
                        lilia "A-ahh... A-alright..."
                        scene lilia_sucking_breast with fade
                        rudeus "Hummm... Your breasts are delicious."
                        lilia "Mmmph... You better not tell your mother about this..."
                        rudeus "Of course not, I would never tell."
                        rudeus "Especially because I want more..."
                        lilia "Arghh... Y-you pervert..."
                        $ lilia_afeicao += interaction_reward
                        $ lilia_interacted_today = True
                        $ renpy.notify("You gained +{} affection with Lilia!".format(interaction_reward))
                        jump passar_tempo
                "Ask for a 69 (180)":

                    if lilia_afeicao < 180:
                        "🔒 You need at least 180 affection to unlock this option."
                        jump lilia_menu
                    else:


                        $ interaction_reward = get_interaction_reward(lilia_afeicao)
                        rudeus "Lilia... How about we do a 69?"
                        lilia "A-a 69? A-are you serious?"
                        rudeus "Of course, I saw you doing it with Paul last night."
                        lilia "H-hey... Were you spying?"
                        rudeus "Maybe... But now I want to try it too."
                        lilia "Hmpf... A-alright..."
                        show vid_lilia_blowjob with fade
                        rudeus "Ah-ahhh... Wow, Lilia, you're great at this..."
                        lilia "Pfft... It's nothing special..."
                        lilia "B-but... You're actually not so bad yourself..."
                        rudeus "Ngh... Your mouth is so warm and wet..."
                        rudeus "A-at this rate I won't last much longer..."
                        lilia "J-just finish already..."
                        call gozando from _call_gozando_11
                        scene lilia_blowjob_cum with fade
                        rudeus "Argh... That was amazing..."
                        rudeus "You came too, didn't you?"
                        lilia "I-I... yes..."
                        lilia "But only because your tongue was in the right place..."
                        rudeus "Haha, I knew you were enjoying it..."
                        $ lilia_afeicao += interaction_reward
                        $ lilia_interacted_today = True
                        $ renpy.notify("You gained +{} affection with Lilia!".format(interaction_reward))
                        jump passar_tempo
                "Ask for vaginal sex (350)":

                    if lilia_afeicao < 350:
                        "🔒 You need at least 350 affection to unlock this option."
                        jump lilia_menu
                    else:

                        $ interaction_reward = get_interaction_reward(lilia_afeicao)
                        rudeus "Lilia, can I... fuck your pussy?"
                        lilia "O-oh my god... Y-you're so direct..."
                        rudeus "Come on, Lilia... I know you want it as much as I do."
                        lilia "..."
                        lilia "A-alright... But... Just so you keep quiet..."
                        show vid_lilia_vaginal with fade
                        lilia "A-ahh... Y-young master..."
                        lilia "That's so good..."
                        rudeus "Wow... Lilia... Your pussy is so wet..."
                        rudeus "You're really horny, aren't you?"
                        lilia "Y-yes..."
                        lilia "B-but... I shouldn't be doing this with you..."
                        lilia "You're too young for these things..."
                        rudeus "Shhh... Just enjoy it..."
                        rudeus "I'm about to cum!"
                        call gozando from _call_gozando_12
                        show lilia_vaginal_2_cum with fade
                        lilia "Oh no... You came inside my pussy!?"
                        rudeus "Ngh... Fuck... I couldn't hold back..."
                        rudeus "You're so tight..."
                        $ lilia_afeicao += interaction_reward
                        $ lilia_interacted_today = True
                        $ renpy.notify("You gained +{} affection with Lilia!".format(interaction_reward))
                        jump passar_tempo
                "Go back":



                    jump lilia_menu
        "Return":

            jump locais
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
