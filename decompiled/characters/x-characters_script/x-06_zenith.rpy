


define zenith = Character("Zenith", color="#ffa500")

default zenith_afeicao = 0
default zenith_talked_today = False
default zenith_gifted_today = False
default zenith_interacted_today = False




label zenith_label:
    show rudeus normal at left, slide_fade
    show zenith normal at right, slide_fade
    zenith "Rudy!"
    jump zenith_menu


label zenith_menu:
    menu:

        "💬Chat" if not zenith_talked_today:
            $ chat_reward = get_chat_reward(zenith_afeicao)
            rudeus "Hey Mom, how are you today?"
            zenith "Hi sweetie! I'm doing well, thanks for asking."
            $ zenith_afeicao += chat_reward
            $ zenith_talked_today = True
            $ renpy.notify("You gained +{} affection with Zenith!".format(chat_reward))
            jump zenith_menu

        "🎁Give a gift" if not zenith_gifted_today:
            $ available_gifts = []
            if simple_flower_count > 0:
                $ available_gifts.append(("simple_flower", "Simple Flower", simple_flower_count, 10))
            if chocolate_box_count > 0:
                $ available_gifts.append(("chocolate_box", "Box of Chocolates", chocolate_box_count, 25))
            if luxury_jewelry_count > 0:
                $ available_gifts.append(("luxury_jewelry", "Diamond Earring", luxury_jewelry_count, 50))



            $ chosen_gift = renpy.call_screen("gift_selection_screen", "zenith", "Zenith", available_gifts)

            if chosen_gift == "simple_flower":
                $ simple_flower_count -= 1
                rudeus "Mom, I brought you a flower."
                zenith "Oh honey! How thoughtful of you! I love it!"
                $ zenith_afeicao += 10
                $ zenith_gifted_today = True
                $ renpy.notify("Zenith loved the gift! +10 Affection")

            elif chosen_gift == "chocolate_box":
                $ chocolate_box_count -= 1
                rudeus "Mom, I got you some chocolates!"
                zenith "Chocolates! My favorite! You're such a sweet boy!"
                $ zenith_afeicao += 25
                $ zenith_gifted_today = True
                $ renpy.notify("Zenith loved the gift! +25 Affection")

            elif chosen_gift == "luxury_jewelry":
                $ luxury_jewelry_count -= 1
                rudeus "Mom... I want you to have this."
                zenith "A jewel!? Rudeus, this is so expensive!"
                zenith "You shouldn't have... but it's beautiful! Thank you, my dear!"
                $ zenith_afeicao += 50
                $ zenith_gifted_today = True
                $ renpy.notify("Zenith loved the gift! +50 Affection")

            elif chosen_gift == "premium_necklace":
                $ premium_necklace_count -= 1
                rudeus "Mom... This necklace is for the most important woman in my life."
                zenith "Oh Rudeus! This is... this is absolutely stunning!"
                zenith "I don't know what to say... You're such a wonderful son!"
                $ zenith_afeicao += 125
                $ zenith_gifted_today = True
                $ renpy.notify("Zenith ABSOLUTELY loved the gift! +125 Affection")
            else:

                pass

            jump zenith_menu

        "😏Interact" if not zenith_interacted_today:
            menu:
                "Ask to suck her breast (30)":

                    if zenith_afeicao < 30:
                        "🔒 You need at least 30 affection to unlock this option."
                        jump zenith_menu
                    else:
                        rudeus "Hey Mom… I was thinking. Could I suck on your breast?"
                        rudeus "You know, just to relive the old days…"
                        zenith "Oh… Rudy… I don’t have milk anymore, sweetie…"
                        rudeus "Please, Mom… Just a little…"
                        rudeus "I promise I won’t tell anyone."
                        zenith "Hmm… Alright… Just a little."
                        show vid_zenith_breastfeeding with fade
                        zenith "Ahh… This brings back so many memories…"
                        zenith "Remember when you used to cum in my panties?"
                        zenith "I had to wash them so many times because of you..."
                        rudeus "Hmph... Good times, huh Mom."
                        zenith "You were such a naughty boy..."
                        rudeus "Nghh… Mom, I’m gonna cum…"
                        call gozando from _call_gozando_2
                        scene zenith_breastfeeding_cum with fade
                        play sound "audio/cum.mp3"
                        zenith "Feeling better, sweetie?"
                        rudeus "Yeah, Mom… Way better."
                        rudeus "Thanks for taking care of me."
                        $ interaction_reward = get_interaction_reward(zenith_afeicao)
                        $ zenith_afeicao += interaction_reward
                        $ zenith_interacted_today = True
                        $ renpy.notify("You gained +{} affection with Zenith!".format(interaction_reward))
                        jump passar_tempo
                "Ask for a blowjob (80)":

                    if zenith_afeicao < 80:
                        "🔒 You need at least 80 affection to unlock this option."
                        jump zenith_menu
                    else:
                        $ interaction_reward = get_interaction_reward(zenith_afeicao)
                        rudeus "Hey Mom… I was thinking. Could you give me a blowjob?"
                        zenith "Oh… A-a blowjob? That’s so… unexpected, honey…"
                        rudeus "Please, Mom… I really need it…"
                        zenith "Oh my goddess… Alright, sweetie. I’ll try."
                        show vid_zenith_blowjob with fade
                        zenith "Ahh… You’ve grown so much, sweetie…"
                        rudeus "That feels great, Mom."
                        rudeus "Please don’t stop."
                        zenith "Y-you're such a grown man now..."
                        rudeus "Nghh… Mom, Your mouth feels amazing…"
                        rudeus "I’m gonna cum…"
                        call gozando from _call_gozando_3
                        scene zenith_blowjob_cum with fade
                        play sound "audio/cum.mp3"
                        zenith "Oh… you came so much, honey!"
                        rudeus "Ahhh, Mom. You're incredible."
                        $ zenith_afeicao += interaction_reward
                        $ zenith_interacted_today = True
                        $ renpy.notify("You gained +{} affection with Zenith!".format(interaction_reward))
                        jump passar_tempo
                "Ask for vaginal sex (180)":


                    if zenith_afeicao < 180:
                        "🔒 You need at least 180 affection to unlock this option."
                        jump zenith_menu
                    else:
                        $ interaction_reward = get_interaction_reward(zenith_afeicao)
                        rudeus "Mom, I want to make love to you."
                        zenith "Oh… Rudy… I’m not sure that’s a good idea…"
                        zenith "You should be chasing girls your own age, sweetie…"
                        rudeus "But I want you to be my woman, nothing else matters."
                        zenith "Hmm… Alright, honey. I’ll be your woman."
                        show vid_zenith_vaginal with fade
                        zenith "Ahhh… My little Rudy…"
                        zenith "This feels so good… Having you inside me again…"
                        rudeus "Hmphh… You’re the best mom, your pussy is incredible."
                        zenith "I love you so much, sweetie…"
                        rudeus "I... nhhh... I love you too, Mom."
                        call gozando from _call_gozando_4
                        scene zenith_vaginal_cum with fade
                        play sound "audio/cum.mp3"
                        zenith "H-honey… you came inside me!?"
                        rudeus "I couldn't hold back, Mom. You're so hot."
                        zenith "I-it's okay… You can cum inside me whenever you want."
                        zenith "Mommy will aways take care of you."
                        $ zenith_afeicao += interaction_reward
                        $ zenith_interacted_today = True
                        $ renpy.notify("You gained +{} affection with Zenith!".format(interaction_reward))
                        jump passar_tempo
                "Go back":


                    jump zenith_menu
        "Return":

            jump locais
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
