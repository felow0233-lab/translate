





screen sc_combat_hud():


    vbox:
        xalign 0.5
        yalign 0.02
        spacing 4

        text "Slime Girl" xalign 0.5 color "#80bbff" size 24 outlines [(2, "#000000cc", 0, 0)]


        frame:
            xsize 320
            ysize 22
            padding (3, 3)
            background "#1a1a2aee"
            $ e_fill = max(0, int(314 * sc_enemy_hp / sc_enemy_max))
            add Solid("#333333") xsize 314 ysize 16
            if e_fill > 0:
                add Solid("#4499ff") xsize e_fill ysize 16

        text "[sc_enemy_hp]/[sc_enemy_max]" xalign 0.5 color "#aaccff" size 18 outlines [(1, "#000000", 0, 0)]


    vbox:
        xalign 0.02
        yalign 0.02
        spacing 4

        text "Rudeus" color "#ffffff" size 22 outlines [(2, "#000000cc", 0, 0)]

        frame:
            xsize 280
            ysize 22
            padding (3, 3)
            background "#1a1a2aee"
            $ p_fill = max(0, int(274 * sc_player_hp / sc_player_max))
            add Solid("#333333") xsize 274 ysize 16
            if p_fill > 0:
                add Solid("#44cc44") xsize p_fill ysize 16

        text "[sc_player_hp]/[sc_player_max] HP" color "#aaffaa" size 18 outlines [(1, "#000000", 0, 0)]



screen sc_affection_hud():

    vbox:
        xalign 0.5
        yalign 0.02
        spacing 4

        text "💗 Lewdness" xalign 0.5 color "#ff69b4" size 24 outlines [(2, "#000000cc", 0, 0)]

        frame:
            xsize 320
            ysize 22
            padding (3, 3)
            background "#1a0a1aee"
            $ a_fill = max(0, min(314, int(314 * slime_girl_affection / 100)))
            add Solid("#553344") xsize 314 ysize 16
            if a_fill > 0:
                add Solid("#ff69b4") xsize a_fill ysize 16

        if slime_girl_affection >= 100:
            text "💖 MAXED OUT 💖" xalign 0.5 color "#ff2299" size 18 outlines [(1, "#000000", 0, 0)]
        else:
            text "[slime_girl_affection]/100" xalign 0.5 color "#ffb6d9" size 18 outlines [(1, "#000000", 0, 0)]






label slime_combat_simple:
    $ sc_player_hp  = 100
    $ sc_player_max = 100
    $ sc_enemy_hp   = 80
    $ sc_enemy_max  = 80
    $ sc_defending  = False
    $ sc_charging   = False


    show slime_girl angry at sc_idle with dissolve
    show screen sc_combat_hud

    if sc_just_met:
        slime_girl "Hmph! Let's see what you've got, human!"
    else:
        slime_girl "Hmph! Back again, human? This time I won't go easy on you!"

label sc_turn:
    menu:
        "⚔ Attack":
            show slime_girl auch at sc_hurt
            $ renpy.sound.play(renpy.random.choice(sc_slime_hurt_sounds))
            pause 0.3
            show slime_girl angry at sc_hurt
            pause 0.3
            show slime_girl angry at sc_idle

            if sc_charging:
                $ sc_dmg = max(1, renpy.random.randint(12, 22) // 4)
                $ sc_enemy_hp = max(0, sc_enemy_hp - sc_dmg)
                "Her skin looks hardened, almost crystallized, while she channels her power! Your attack barely scratches her for {color=#ffdd55}[sc_dmg]{/color} damage!"
            else:
                $ sc_dmg = renpy.random.randint(12, 22)
                $ sc_enemy_hp = max(0, sc_enemy_hp - sc_dmg)
                "You hit the slime for {color=#ffdd55}[sc_dmg]{/color} damage!"

            if sc_enemy_hp <= 0:
                jump sc_victory
            jump sc_enemy_turn
        "🛡 Defend":

            $ sc_defending = True
            "You brace yourself, ready to block the next hit."
            jump sc_enemy_turn
        "🏃 Flee":

            hide slime_girl with dissolve
            hide screen sc_combat_hud
            slime_girl "W-wait, you're running?! Coward!"
            "You escape from the battle."
            $ local_atual = "floresta"
            jump locais

label sc_enemy_turn:

    if sc_charging:
        $ sc_charging = False
        $ sc_raw = renpy.random.randint(22, 32)
        show slime_girl attack at sc_attack
        $ renpy.sound.play(renpy.random.choice(sc_slime_attack_sounds))
        pause 0.4
        show slime_girl angry at sc_idle

        if sc_defending:
            $ sc_taken = max(1, sc_raw // 2)
            slime_girl "HIYAAAH! Slime Crush— eh?! You blocked it?!"
            "You brace yourself just in time, soaking up most of the blow! Only {color=#ff6666}[sc_taken]{/color} damage gets through."
            $ sc_defending = False
        else:
            $ sc_taken = sc_raw
            slime_girl "HIYAAAH! Take THIS— Slime Crush!!"
            "The slime slams into you with overwhelming force for {color=#ff4444}[sc_taken]{/color} damage!"

        $ sc_player_hp = max(0, sc_player_hp - sc_taken)

        if sc_player_hp <= 0:
            jump sc_defeat

        jump sc_turn


    if renpy.random.random() < 0.25:
        $ sc_charging = True
        $ sc_defending = False
        show slime_girl angry at sc_charge_pose
        $ renpy.sound.play("audio/slime_girl/slime_bubble.mp3")
        pause 0.6
        show slime_girl angry at sc_idle
        slime_girl "Hmph! I'm done holding back— watch THIS!"
        "The Slime Girl's body starts glowing ominously... she's preparing a powerful strike!"
        jump sc_turn


    $ sc_raw = renpy.random.randint(8, 16)
    show slime_girl attack at sc_attack
    $ renpy.sound.play(renpy.random.choice(sc_slime_attack_sounds))
    pause 0.35
    show slime_girl angry at sc_idle

    if sc_defending:
        $ sc_taken = max(1, sc_raw // 2)
        slime_girl "Hiya! ...Oh, you blocked it."
        "The slime hits you for {color=#ff6666}[sc_taken]{/color} damage! (Defended)"
        $ sc_defending = False
    else:
        $ sc_taken = sc_raw
        slime_girl "Hiya!"
        "The slime hits you for {color=#ff6666}[sc_taken]{/color} damage!"

    $ sc_player_hp = max(0, sc_player_hp - sc_taken)

    if sc_player_hp <= 0:
        jump sc_defeat

    jump sc_turn

label sc_defeat:
    hide slime_girl with dissolve
    hide screen sc_combat_hud
    slime_girl "Hmph! That's what you get for trespassing in MY forest!"
    "You were defeated... Better luck next time."
    $ local_atual = "floresta"
    jump locais









label sc_victory:
    hide screen sc_combat_hud



    slime_girl "...! N-no way... I actually lost?!"
    "The Slime Girl drops to her knees, body trembling, completely out of strength."


    slime_girl "Hmph... y-you're a lot stronger than you look, I'll give you that..."
    slime_girl "F-fine! You win! Just... don't do anything weird, okay?!"
    jump sc_surrender_menu


label sc_surrender_menu:
    show screen sc_affection_hud
    menu:
        "💬 Interact":
            menu:
                "Grab her breast (20)":
                    if slime_girl_affection >= 20:
                        hide screen sc_affection_hud
                        rudeus "Hey... I went easy on you earlier. Don't you think you owe me a little reward?"
                        slime_girl "H-Hah?! What the hell are you thinking, you pervert?!"
                        rudeus "Just let me touch your breasts for a bit."
                        slime_girl "Eww! I'd never let a human touch me like that!!"
                        rudeus "I could have killed you back there, you know."
                        slime_girl "..."
                        "She crosses her arms and pouts, clearly annoyed."
                        slime_girl "Okay... Only because you spared me... But just this once, got it?!"

                        hide slime_girl angry with dissolve

                        "You step closer and reach for the bandages wrapped around her chest, slowly pulling them loose."
                        rudeus "(Finally... can't wait to get my hands on those.)"

                        scene bg floresta:
                            blur 5
                        show slime_breast_grab
                        with dissolve

                        slime_girl "Mmh...! They're sensitive, idiot... be gentle!"
                        rudeus "They're so soft... really nice."
                        slime_girl "D-don't say that out loud, you creep!"
                        "She squirms a little, but doesn't push your hands away."

                        play sound "audio/affection_gain.mp3" volume 0.7
                        $ sc_affection_gain = renpy.random.randint(5, 9)
                        $ slime_girl_affection += sc_affection_gain
                        $ slime_girl_groped = True
                        "💗 Slime Girl's affection +[sc_affection_gain]!"
                        jump sc_surrender_end
                    else:
                        slime_girl "Hey! Don't you dare touch me like that, pervert!"
                        "{color=#ff6666}Requires 20 Affection{/color}"
                        jump sc_surrender_menu
                "Ask for a handjob (50)":

                    if slime_girl_affection >= 50:
                        hide screen sc_affection_hud
                        rudeus "C'mon, I spared your life. The least you can do is use those hands of yours on me."
                        slime_girl "Eh?! You want me to... with my hand?! No way! I'd never do that for a disgusting human!"
                        rudeus "After I let you live? That's cold."
                        slime_girl "Ugh... you're impossible!"
                        "She looks away, her face turning bright blue from embarrassment."
                        slime_girl "Hmph... Just this once! And don't you dare get used to it!"

                        hide slime_girl angry with dissolve
                        scene bg floresta:
                            blur 5
                        show slime_handjob
                        with dissolve

                        "Her cool, gooey fingers wrap around you, stroking with awkward, uneven movements."

                        slime_girl "T-This is so embarrassing... I can't believe I'm doing this for a human..."

                        "She doesn't stop, picking up a faster rhythm, cheeks puffed out in a pout."

                        slime_girl "Hmph...! D-don't stare so much, pervert!"

                        rudeus "You're doing good... keep going just like that."

                        "Her strokes grow more confident, the slick coolness making every motion feel intense."

                        slime_girl "Ugh... it's twitching so much... This is weird..."



                        rudeus "Yeah... just like that."

                        rudeus "I'm gonna cum—"

                        slime_girl "W-wait, you're seriously—?!"

                        call gozando from _call_gozando_20

                        scene bg floresta:
                            blur 5
                        play sound "audio/cum.mp3"
                        show slime_handjob_cum
                        with dissolve


                        slime_girl "Ugh, gross, gross, GROSS! It's all over my face!"

                        "She stares at her own hand, nose wrinkled, but she doesn't wipe it off right away."

                        rudeus "Heh... not bad. You've got some skilled slime hands."

                        slime_girl "H-Hmph... whatever. Don't act like that means anything."

                        play sound "audio/affection_gain.mp3" volume 0.7

                        $ sc_affection_gain = renpy.random.randint(8, 14)
                        $ slime_girl_affection += sc_affection_gain
                        $ slime_girl_handjob_done = True
                        "💗 Slime Girl's affection +[sc_affection_gain]!"
                        jump sc_surrender_end
                    else:
                        slime_girl "No way! I don't trust you enough for that yet!"
                        "{color=#ff6666}Requires 50 Affection{/color}"
                        jump sc_surrender_menu
                "Ask for a blowjob (75)":

                    if slime_girl_affection >= 75:
                        hide screen sc_affection_hud
                        rudeus "Now... I want you to use that cute mouth of yours on my dick."
                        slime_girl "What?! You want me to put that in my mouth?!"
                        slime_girl "Gross! I'd never do something like that for a human!"
                        rudeus "Come on... I could’ve been a lot worse to you."
                        slime_girl "..."
                        "Her face turns completely blue with embarrassment."
                        slime_girl "Hmph... OKAY... Just this once! If you tell anyone, I'll kill you!"

                        hide slime_girl angry with dissolve

                        "She leans in hesitantly and takes you into her mouth, clumsy and unsure where to even start."







                        play sound "audio/slime_girl/slime_girl_blowjob.mp3" loop volume 1.3
                        show vid_slime_girl_blowjob
                        with fade

                        slime_girl "Mmh... mmph..."
                        slime_girl "(D-don't look at me like that, you idiot...)"
                        "Her mouth is wet and warm, sliding slowly around you as she starts to find a rhythm."
                        rudeus "(...She's actually pretty good at this.)"
                        rudeus "(If she keeps this up, I'm not gonna last much longer.)"

                        call gozando from _call_gozando_21

                        scene bg floresta:
                            blur 5
                        play sound "audio/cum.mp3"
                        show slime_blowjob_cum
                        with dissolve

                        "You jolt, spilling hot right into her mouth before she can pull away."

                        slime_girl "(I-I can't believe he just came in my mouth...)"

                        "You pull back slowly. She's left kneeling there, a dazed, disgusted look on her face."

                        scene bg floresta with fade
                        show slime_girl angry at center, slide_fade

                        slime_girl "Ewww... gross, I can't believe this..."

                        rudeus "Heh, you look kinda cute all messed up like that."

                        "Her face flushes a deep blue, completely flustered."

                        slime_girl "Sh-shut up! I'm leaving, don't follow me!"
                        hide slime_girl with dissolve
                        "She wipes her mouth and turns away, hopping off into the bushes before you can even respond."

                        play sound "audio/affection_gain.mp3" volume 0.7
                        $ sc_affection_gain = renpy.random.randint(12, 18)
                        $ slime_girl_affection += sc_affection_gain
                        $ slime_girl_blowjob_done = True
                        "💗 Slime Girl's affection +[sc_affection_gain]!"
                        jump sc_surrender_end
                    else:
                        slime_girl "That's way too embarrassing! Forget it!"
                        "{color=#ff6666}Requires 75 Affection{/color}"
                        jump sc_surrender_menu
                "Have sex with her (100)":

                    if slime_girl_affection >= 100:
                        hide screen sc_affection_hud
                        rudeus "I beat you and still spared you... I think you know what I want as thanks."
                        rudeus "It’s time to let me slip inside that little pussy, don’t you think?"
                        slime_girl "Eh?! You want... that?! No way! I'd never have sex with a human!"
                        rudeus "After everything, you're still gonna say no?"
                        slime_girl "Ughhh... you're the worst..."
                        "She covers her face with both hands, extremely embarrassed."
                        slime_girl "Okay... Just this once! And you better do it properly, idiot!"

                        hide slime_girl with dissolve


                        "She pulls you down onto the forest floor, wrapping her slimy arms around you."
                        rudeus "Woah... you seem pretty fired up for someone who 'never does this with humans.'"
                        slime_girl "Shut up and just fu— hurry up already!!"

                        "You push aside the few pieces of clothing she still has on and enter her in a single, slow motion."







                        play sound "audio/slime_girl/slime_girl_sex_01.mp3" loop
                        show vid_slime_girl_vaginal
                        with fade

                        slime_girl "Ahh... It feels so big... ahn...!"
                        rudeus "Damn... Your slime pussy is so tight..."
                        slime_girl "S-shut up and keep going...!"
                        "You stretch her open with every thrust, her slimy body molding and stretching around you each time you push deeper."
                        rudeus "Ah... Fuck..."
                        rudeus "I'm gonna cum—"

                        slime_girl "Yes, yes... F-fill me up!"

                        call gozando from _call_gozando_22
                        scene bg floresta:
                            blur 5
                        play sound "audio/cum.mp3"
                        show slime_sex_cum
                        with dissolve


                        "You fill her tight little pussy with cum, and she shudders, trembling underneath you."
                        slime_girl "Ahhn...!"
                        "You pull out slowly, watching a trickle of cum leak out from between her legs."

                        scene bg floresta:
                            blur 5
                        show slime_spreading
                        with fade

                        "She stays there, sprawled out, still trying to look annoyed despite everything."

                        rudeus "Wow... what a view."

                        "Her face flushes, legs still spread wide on the ground."

                        slime_girl "Sh-shut up! Don't just stare like that, you pervert!"

                        slime_girl "I-I'm staying like this so it drains out, okay?! I'm not getting knocked up by some human!"

                        rudeus "Guess all that 'I'd never do this with a human' talk didn't last very long, huh?"

                        slime_girl "...Don't think this means anything, okay?"
                        slime_girl "You're still my enemy. This doesn't change a thing."
                        rudeus "Sure, sure~"

                        play sound "audio/affection_gain.mp3" volume 0.7
                        $ sc_affection_gain = renpy.random.randint(15, 25)
                        $ slime_girl_affection += sc_affection_gain
                        $ slime_girl_sex_done = True
                        "💗 Slime Girl's affection +[sc_affection_gain]!"
                        jump sc_surrender_end
                    else:
                        slime_girl "No way! That's going way too far!"
                        "{color=#ff6666}Requires 100 Affection{/color}"
                        jump sc_surrender_menu
                "Never mind":

                    jump sc_surrender_menu
        "💰 Take her money 💗":

            $ sc_gold = renpy.random.randint(45, 65)
            $ player_gold += sc_gold

            slime_girl "H-hey! That's not fair, you can't just—!"
            "You snatch the small pouch of gold tied to her side and pocket it without a word."
            slime_girl "...Hmph. Guess I should be glad you didn't just finish me off instead."
            "You took {color=#FFD700}[sc_gold] Gold{/color} from her."


            play sound "audio/affection_gain.mp3" volume 0.7
            $ sc_affection_gain = renpy.random.randint(3, 5)
            $ slime_girl_affection += sc_affection_gain
            "💗 Slime Girl's affection +[sc_affection_gain]!"
            jump sc_surrender_end
        "🕊 Let her go 💗💗💗":


            slime_girl "...You're... letting me go? Just like that?"
            rudeus "Yeah. No hard feelings."
            slime_girl "...Hmph. You're a strange one. Here, take this much, at least."
            "She presses a small handful of coins into your hand before slipping off into the trees."



            $ sc_gold = renpy.random.randint(20, 30)
            $ player_gold += sc_gold
            "You gained {color=#FFD700}[sc_gold] Gold{/color}."

            play sound "audio/affection_gain.mp3" volume 0.7
            $ sc_affection_gain = renpy.random.randint(8, 15)
            $ slime_girl_affection += sc_affection_gain



            "💗 Slime Girl's affection +[sc_affection_gain]!"
            jump sc_surrender_end

label sc_surrender_end:
    hide screen sc_affection_hud

    $ local_atual = "floresta"
    jump passar_tempo
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
