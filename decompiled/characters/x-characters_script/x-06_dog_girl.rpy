

default slave_dog_affection = 0

default slave_dog_gifted_today = False
default slave_dog_talked_today = False
default slave_dog_interacted_today = False

default s_dog_route = 0

label slave_dog_label:
    show rudeus normal at left, slide_fade
    show s_dog normal at right, slide_fade
    jump slave_dog_menu


label slave_dog_menu:
    menu:
        "💬Chat" if not slave_dog_talked_today:
            rudeus "Hey [s_dog_name]... How are you feeling today?"
            s_dog "H-hi, Master! I’m doing fine… thank you for asking."
            $ renpy.notify(f"You gained +5 affection with {s_dog_name}!")
            $ slave_dog_affection += 5
            $ slave_dog_talked_today = True
            jump slave_dog_menu

        "🎁Give a gift" if not slave_dog_gifted_today:

            $ available_gifts = []
            if simple_flower_count > 0:
                $ available_gifts.append(("simple_flower", "Simple Flower", simple_flower_count, 10))
            if chocolate_box_count > 0:
                $ available_gifts.append(("chocolate_box", "Box of Chocolates", chocolate_box_count, 25))
            if luxury_jewelry_count > 0:
                $ available_gifts.append(("luxury_jewelry", "Diamond Earring", luxury_jewelry_count, 50))




            $ chosen_gift = renpy.call_screen("gift_selection_screen", "dog_girl", s_dog_name, available_gifts)

            if chosen_gift == "simple_flower":
                $ simple_flower_count -= 1
                rudeus "Here, I got you a flower."
                s_dog "A flower... for me? Master is so kind!"
                $ slave_dog_affection += 10
                $ slave_dog_gifted_today = True
                $ renpy.notify(f"{s_dog_name} loved the gift! +10 Affection")

            elif chosen_gift == "chocolate_box":
                $ chocolate_box_count -= 1
                rudeus "[s_dog_name], I brought you chocolates."
                s_dog "Chocolates! These smell amazing! Thank you, Master!"
                $ slave_dog_affection += 25
                $ slave_dog_gifted_today = True
                $ renpy.notify(f"{s_dog_name} loved the gift! +25 Affection")

            elif chosen_gift == "luxury_jewelry":
                $ luxury_jewelry_count -= 1
                rudeus "This is for you, [s_dog_name]."
                s_dog "A jewel!? Master... this is too precious for a slave like me!"
                s_dog "I'll treasure it forever! Thank you so much, Master!"
                $ slave_dog_affection += 50
                $ slave_dog_gifted_today = True
                $ renpy.notify(f"{s_dog_name} loved the gift! +50 Affection")

            elif chosen_gift == "premium_necklace":
                $ premium_necklace_count -= 1
                rudeus "[s_dog_name]... You deserve something truly special."
                s_dog "M-Master!? This necklace is... it's like something from a dream!"
                s_dog "I... I don't deserve this, but... thank you! I love you, Master!"
                $ slave_dog_affection += 125
                $ slave_dog_gifted_today = True
                $ renpy.notify(f"{s_dog_name} ABSOLUTELY loved the gift! +125 Affection")
            else:


                pass

            jump slave_dog_menu

        "😏Interact" if not slave_dog_interacted_today:
            menu:
                "Pet her (30)":

                    if slave_dog_affection < 30:
                        "🔒 You need at least 30 affection to unlock this option."
                        jump slave_dog_menu
                    else:
                        rudeus "Hey [s_dog_name]... Lie down on the floor. I wanna pet you real nice."
                        s_dog "P-pet me? Y-yes please, Master..."

                        show vid_dog_caressing with fade
                        s_dog "A-ahhnn… M-Master…"
                        s_dog "That feels… so good…"
                        rudeus "[s_dog_name], you're so soft…"
                        s_dog "T-thank you, Master..."
                        rudeus "And I'm going crazy over your scent…"
                        s_dog "S-scent? W-what scent, Master?"
                        rudeus "The smell of your little pussy… it's dripping with such a delicious aroma…"
                        s_dog "N-nghh… Master… that's so embarrassing…"
                        rudeus "Don't worry, [s_dog_name]… I love it."
                        $ interaction_reward = get_interaction_reward(slave_dog_affection)
                        $ slave_dog_affection += interaction_reward
                        $ slave_dog_interacted_today = True
                        $ renpy.notify(f"You gained +{interaction_reward} affection with {s_dog_name}!")
                        jump passar_tempo
                "Ask for a titjob (80)":

                    if slave_dog_affection < 80:
                        "🔒 You need at least 80 affection to unlock this option."
                        jump slave_dog_menu
                    else:

                        $ interaction_reward = get_interaction_reward(slave_dog_affection)
                        rudeus "Hey [s_dog_name]... Let me see if those tits of yours are big enough to give me a proper titjob."
                        s_dog "O-of course, Master… I'll do my very best…"
                        show vid_dog_paizuri with fade
                        s_dog "N-nhghh… M-Master…"
                        rudeus "Keep your mouth open, [s_dog_name]…"
                        rudeus "I want you to taste every drop of my cum…"
                        s_dog "A-ahhhh… Y-yes, Master…"
                        rudeus "That’s it… good girl…"
                        call gozando from _call_gozando_5
                        play sound "cum.mp3"
                        scene dog_paizuri_cum with fade
                        s_dog "M-M-Master… you came in my mouth…"
                        rudeus "Good girl… Now don't waste a single drop."
                        s_dog "Y-yes, Master…"
                        $ slave_dog_affection += interaction_reward
                        $ slave_dog_interacted_today = True
                        $ renpy.notify(f"You gained +{interaction_reward} affection with {s_dog_name}!")
                        jump passar_tempo
                "Ask for anal sex (180)":

                    if slave_dog_affection < 180:
                        "🔒 You need at least 180 affection to unlock this option."
                        jump slave_dog_menu
                    else:


                        $ interaction_reward = get_interaction_reward(slave_dog_affection)
                        rudeus "Hey [s_dog_name]... I wanna find out just how tight that little asshole of yours really is."
                        s_dog "M-my ass, Master? B-but I’m scared it’s gonna hurt…"
                        rudeus "Don’t worry, I’ll go nice and slow…"
                        show vid_dog_anal at stretch_bottom_right with fade
                        s_dog "A-ahhh… Master… my ass…"
                        rudeus "You like it, [s_dog_name]?"
                        s_dog "N-nghh… Y-yes, Master… it hurts a little, b-but it feels so… good…"
                        rudeus "Hehe, knew you’d love it…"
                        rudeus "Want me to speed up a bit?"
                        s_dog "Y-yes, Master… please…"
                        show vid_dog_anal_fast at stretch_bottom_right with fade
                        s_dog "N-nhgh… Master… you’re going so deep…"
                        rudeus "Haha, you love it when I fuck you hard, don’t you?"
                        s_dog "Y-yes, Master… I love it when you fuck me like this…"
                        s_dog "I-I’m feeling something weird, Master…"
                        s_dog "P-please, Master… faster…"
                        show vid_dog_anal_faster at stretch_bottom_right with fade
                        rudeus "N-nghh… You’re so fucking tight, [s_dog_name]…"
                        s_dog "A-ahhh… My ass, Master…"
                        s_dog "I-I think I’m gonna cum…"
                        call gozando from _call_gozando_6
                        play sound "cum.mp3"
                        scene dog_anal_cum with fade
                        s_dog "M-M-Master… I made you cum…"
                        s_dog "I’m so happy…"
                        rudeus "Yeah, you're such a good girl…"
                        s_dog "Th-thank you, Master…"
                        s_dog "M-my legs are shaking so much…"
                        $ slave_dog_affection += interaction_reward
                        $ slave_dog_interacted_today = True
                        $ renpy.notify(f"You gained +{interaction_reward} affection with {s_dog_name}!")
                        jump passar_tempo
                "Go back":

                    jump slave_dog_menu
        "Return":

            jump locais
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
