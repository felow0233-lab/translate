


default contratou_roxy = False

default roxy_afeicao = 0


define roxy_gifted_today = False
define roxy_talked_today = False
define roxy_interacted_today = False


label roxy_intro:
    show rudeus normal at left, slide_fade
    show roxy normal at right, slide_fade
    roxy "Yes?"
    jump roxy_menu




label roxy_pre_menu:
    scene bg taverna with fade

    "You step into the tavern, the warm smell of ale and roasted meat hanging in the air."

    rudeus "(Hm? Who's that, sitting all alone in the back?)"

    show roxy normal at center, slide_fade
    with dissolve

    rudeus "(...Huh. Cute. Really cute, actually.)"

    rudeus "(Wonder what she's doing here all by herself.)"

    show roxy:
        ease 0.5 xalign 0.8

    show rudeus normal at my_left, slide_fade

    rudeus "Hey there. Mind if I join you for a bit?"

    roxy "Oh! Um... s-sure, go ahead..."

    rudeus "So, what's a girl like you doing all alone in a place like this?"

    roxy "I-I'm not just 'a girl'... I'm a magic tutor, actually."

    rudeus "(A magic tutor? And cute on top of that... heh, lucky me.)"

    rudeus "A magic tutor, huh? That's pretty impressive."

    roxy "I-I know I might not look the part, but I really do know my magic."

    rudeus "I don't doubt it for a second. So... how much would it cost to have you teach me?"

    roxy "I charge 25 gold coins per lesson."

    rudeus "Sounds fair. Honestly, I could really use someone like you around."

    menu:
        "Hire her as your tutor":
            rudeus "Alright, you're hired. Welcome aboard, teacher."

            roxy "R-really?! You mean it?"

            "Roxy's face lights up, a huge smile spreading across her face."

            roxy "Thank you so much! I promise I'll be a great tutor for you!"

            $ contratou_roxy = True
            $ roxy_evento = 1
            $ renpy.notify("You hired Roxy as your magic tutor!")
            jump locais


image roxy normal:
    "images/pers/roxy/roxy normal.png"
    zoom 0.5

label roxy_menu:
    menu:


        "💬Chat" if not roxy_talked_today:

            $ chat_reward = get_chat_reward(roxy_afeicao)
            rudeus "So, Roxy… how's your day going?"
            roxy "Oh… It's been good… Thank you for asking!"
            $ roxy_afeicao += chat_reward
            $ roxy_talked_today = True
            $ renpy.notify("You gained +{} affection with Roxy!".format(chat_reward))
            jump roxy_menu

        "🎁Give a gift" if not roxy_gifted_today:
            $ available_gifts = []
            if simple_flower_count > 0:
                $ available_gifts.append(("simple_flower", "Simple Flower", simple_flower_count, 10))
            if chocolate_box_count > 0:
                $ available_gifts.append(("chocolate_box", "Box of Chocolates", chocolate_box_count, 25))
            if luxury_jewelry_count > 0:
                $ available_gifts.append(("luxury_jewelry", "Diamond Earring", luxury_jewelry_count, 50))



            $ chosen_gift = renpy.call_screen("gift_selection_screen", "roxy", "roxy", available_gifts)

            if chosen_gift == "simple_flower":
                $ simple_flower_count -= 1
                rudeus "Hey Roxy, I brought you a flower!"
                roxy "Oh! A flower for me? Thank you so much."
                $ roxy_afeicao += 10
                $ roxy_gifted_today = True
                $ renpy.notify("Roxy loved the gift! +10 Affection")

            elif chosen_gift == "chocolate_box":
                $ chocolate_box_count -= 1
                rudeus "Roxy, I got you some fancy chocolates!"
                roxy "Wow! These look so delicious!"
                $ roxy_afeicao += 25
                $ roxy_gifted_today = True
                $ renpy.notify("Roxy loved the gift! +25 Affection")

            elif chosen_gift == "luxury_jewelry":
                $ luxury_jewelry_count -= 1
                rudeus "Roxy... I want you to have this."
                roxy "Is that... a jewel!? This is too much!"
                roxy "It's so beautiful... I'll treasure it forever!"
                $ roxy_afeicao += 50
                $ roxy_gifted_today = True
                $ renpy.notify("Roxy loved the gift! +50 Affection")

            elif chosen_gift == "premium_necklace":
                $ premium_necklace_count -= 1
                rudeus "Roxy... This necklace represents how much you mean to me."
                roxy "Rudeus... This is breathtaking! I've never seen anything like it!"
                roxy "Thank you so much! This means the world to me!"
                $ roxy_afeicao += 125
                $ roxy_gifted_today = True
                $ renpy.notify("Roxy ABSOLUTELY loved the gift! +125 Affection")
            else:

                pass

            jump roxy_menu


        "😏Interact" if not roxy_interacted_today:
            label roxy_interact_menu:

                menu:
                    "Ask to see her panties (30)":

                        if roxy_afeicao < 30:
                            "You need at least 30 affection to unlock this option."
                            jump roxy_interact_menu
                        else:
                            rudeus "Hey Roxy… show me your panties."
                            roxy "M-my… my panties? Rudeus, why would you ask something like that?"
                            rudeus "Come on… I bet you're wearing something super sexy underneath."
                            rudeus "I'd love to see you flashing them for me…"
                            roxy "F-fine… but only this once!"
                            show vid_roxy_showing with fade
                            rudeus "Holy shit, Roxy… those panties look incredible on you…"
                            roxy "D-did you like them?"
                            rudeus "Hell yes… and they smell amazing too…"
                            roxy "Y-you shouldn't say stuff like that, Rudeus…"
                            rudeus "Ahhh… Teach… you're so fucking hot…"
                            rudeus "I can't stop staring…"
                            roxy "Hngh… you little pervert…"
                            $ interaction_reward = get_interaction_reward(roxy_afeicao)
                            $ roxy_afeicao += interaction_reward
                            $ roxy_interacted_today = True
                            $ renpy.notify("You gained +{} affection with Roxy!".format(interaction_reward))
                            jump passar_tempo
                    "Eat her ass (80)":

                        if roxy_afeicao < 80:
                            "You need at least 80 affection to unlock this option."
                            jump roxy_interact_menu
                        else:

                            rudeus "Hey teach… turn around and bend over for me."
                            roxy "W-what do you have in mind now, Rudeus?"
                            rudeus "How about you let me lick your asshole?"
                            roxy "L-lick my asshole? Rudeus, that's so filthy…"
                            rudeus "Come on… I promise you're gonna love it."
                            roxy "N-nhgh… Fine…"
                            scene vid_roxy_anilingus with fade
                            roxy "A-ahhh… R-Rudeus…"
                            roxy "Your tongue feels so… good…"
                            rudeus "Hehe… you love it when I tongue your little asshole, don't you, teach?"
                            roxy "N-nhgh… Y-yes… you're way too good at this…"
                            rudeus "Just wait until you feel my cock in there…"
                            roxy "A-angh… you dirty boy…"
                            $ interaction_reward = get_interaction_reward(roxy_afeicao)
                            $ roxy_afeicao += interaction_reward
                            $ roxy_interacted_today = True
                            $ renpy.notify("You gained +{} affection with Roxy!".format(interaction_reward))
                            jump passar_tempo
                    "Ask for anal (180)":

                        if roxy_afeicao < 180:
                            "You need at least 180 affection to unlock this option."
                            jump roxy_interact_menu
                        else:


                            rudeus "Hey Roxy… I want to bury it balls-deep in your ass…"
                            roxy "B-balls-deep? B-but… I've never done anal before…"
                            rudeus "Don't worry, I'll be gentle… at first."
                            scene vid_roxy_anal with fade
                            roxy "Nghhh… S-slow down, you pervert…"
                            roxy "You're stretching me so much…"
                            rudeus "I-I can't help it, teach…"
                            rudeus "Your ass is insanely tight…"
                            roxy "N-nnhgnh… You really love my ass that much?"
                            rudeus "Fuck yes… I love how it keeps trying to push my cock out…"
                            roxy "N-nhgh… This feels so weird…"
                            roxy "It kinda makes me feel like I need to poop…"
                            rudeus "Just hold on a little longer, teach…"
                            rudeus "I-I'm about to blow…"
                            call gozando from _call_gozando_9
                            play sound "cum.mp3"
                            scene roxy_anal_cum with fade
                            roxy "A-angh… You… you came inside my ass…"
                            rudeus "Hnghh… Teach, you're the best…"
                            rudeus "At this rate I'll become the strongest mage in the continent…"
                            $ interaction_reward = get_interaction_reward(roxy_afeicao)
                            $ roxy_afeicao += interaction_reward
                            $ roxy_interacted_today = True
                            $ renpy.notify("You gained +{} affection with Roxy!".format(interaction_reward))
                            jump passar_tempo
                    "Go back":


                        jump roxy_menu
        "Return":

            jump locais
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
