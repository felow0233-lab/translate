

transform slide_fade:
    alpha 0.0
    xoffset -50
    linear 0.25 alpha 1.0 xoffset 0


default day = 1

label gozando:
    show white with dissolve
    hide white with dissolve
    show white with dissolve
    hide white with dissolve
    show white with dissolve
    hide white with dissolve
    return


default debug_energy = True



label locais:
    while True:
        if local_atual == "entrada_rudeus":
            call entrada_rudeus from _call_entrada_rudeus

        elif local_atual == "vilarejo":
            call vilarejo from _call_vilarejo

        elif local_atual == "floresta":
            call floresta from _call_floresta

        elif local_atual == "taverna":
            call taverna from _call_taverna

        elif local_atual == "shop":
            call shop from _call_shop

        elif local_atual == "blacksmith":
            call blacksmith from _call_blacksmith

        elif local_atual == "casa_rudeus":
            call casa_rudeus from _call_casa_rudeus

        elif local_atual == "sylph_hut":
            call sylph_hut from _call_sylph_hut

        elif local_atual == "eris_location":
            call eris_location from _call_eris_location

        elif local_atual == "eris_castle":
            call eris_castle from _call_eris_castle
        else:


            "Local não encontrado."
            $ local_atual = "entrada_rudeus"
            jump locais

label passar_tempo:
    window hide
    hide screen button_screen
    if energia > 1:
        $ energia -= 1
    else:
        scene black with fade
        "You feel tired and decide to rest for the day."

        $ local_atual = "entrada_rudeus"
        $ energia = max_energia

        $ aisha_talked_today = False
        $ aisha_gifted_today = False
        $ aisha_interacted_today = False

        $ zenith_talked_today = False
        $ zenith_gifted_today = False
        $ zenith_interacted_today = False
        $ zenith_on = True


        $ roxy_talked_today = False
        $ roxy_gifted_today = False
        $ roxy_interacted_today = False


        $ slave_dog_talked_today = False
        $ slave_dog_gifted_today = False
        $ slave_dog_interacted_today = False

        $ lilia_talked_today = False
        $ lilia_gifted_today = False
        $ lilia_interacted_today = False

        $ sylph_talked_today = False
        $ sylph_gifted_today = False
        $ sylph_interacted_today = False


        $ mila_talked_today = False
        $ mila_gifted_today = False
        $ mila_interacted_today = False

        $ norn_talked_today = False
        $ norn_gifted_today = False
        $ norn_interacted_today = False

        $ ghislaine_talked_today = False
        $ ghislaine_gifted_today = False
        $ ghislaine_interacted_today = False

        $ eris_talked_today = False
        $ eris_gifted_today = False
        $ eris_interacted_today = False
        $ eris_on = True

        $ slime_girl_interacted_today = False

        $ day += 1

        $ femboy_on = True
        $ sylph_on = True
        $ freya_on = True


    jump locais





label entrada_rudeus:

    if energia == 1:
        scene bg jardim_rudeus_noite
    elif energia == 2:
        scene bg jardim_rudeus_tarde
    else:
        scene bg jardim_rudeus
    with fade

    show screen button_screen


    if energia > 1:
        menu house_menu:
            "💗 Call Girl":
                jump house_call_menu
            "🌾 Go to the Barn":

                jump celeiro_menu
    else:
        menu:
            "🌾 Go to the Barn":
                jump celeiro_menu

label house_call_menu:
    menu:
        "Call Aisha":
            hide screen button_screen
            jump aisha_intro
        "Call Zenith":

            hide screen button_screen
            jump zenith_label

        "Call Roxy" if contratou_roxy:
            hide screen button_screen
            jump roxy_intro
        "Call Lilia":

            hide screen button_screen
            jump lilia_intro
        "Call Norn":

            hide screen button_screen
            jump norn_intro
        "Return":

            jump house_menu

label celeiro:
    jump celeiro_menu

label celeiro_menu:
    if energia == 1:
        scene bg celeiro_noite
    elif energia == 2:
        scene bg celeiro_tarde
    else:
        scene bg celeiro
    with fade
    menu:
        "Call [s_dog_name]" if buy_dog_slave and energia != 1:
            hide screen button_screen
            jump slave_dog_label
        "Return":

            jump locais

label vilarejo:
    if energia == 1:
        scene bg vilarejo_noite
    elif energia == 2:
        scene bg vilarejo_tarde
    else:
        scene bg vilarejo
    with fade

    show screen button_screen
    menu:
        "🛒 Village Shop":
            hide screen button_screen
            jump buy_event
        "🔨 Blacksmith's Forge":

            hide screen button_screen
            $ local_atual = "blacksmith"
            jump locais
        "🍺 Tavern":


            $ local_atual = "taverna"
            jump locais

label floresta:
    if energia == 1:
        scene bg floresta_noite
    elif energia == 2:
        scene bg floresta_tarde
    else:
        scene bg floresta
    with fade

    if energia > 1:
        show screen button_screen
        menu:
            "⚔️ Hunt the Slime Girl":
                hide screen button_screen
                jump slime_girl_encounter_start
    else:

        call screen button_screen

label taverna:
    if energia == 1:
        scene bg taverna:
            matrixcolor TintMatrix("#88aaff")
    else:
        scene bg taverna
    with fade

    show screen button_screen
    menu:
        "💜 Approach the mysterious girl (!)" if not contratou_roxy:
            hide screen button_screen
            jump roxy_pre_menu
        "Return":

            $ local_atual = "vilarejo"
            jump locais



label blacksmith:
    if energia == 1:
        scene bg blacksmith_noite
    elif energia == 2:
        scene bg blacksmith_tarde
    else:
        scene bg blacksmith
    with fade

    show screen button_screen
    jump smith_forge_menu

label door_house_menu:

    $ local_atual = "entrada_rudeus"
    jump locais


label sylph_hut:
    if energia == 1:
        scene bg sylph_hut_noite
    elif energia == 2:
        scene bg sylph_hut_tarde
    else:
        scene bg sylph_hut
    with fade

    if energia > 1:
        show screen button_screen

        menu:
            "Call Sylphie":
                if sylph_intro:
                    hide screen button_screen
                    jump sylphie_intro
                else:
                    hide screen button_screen
                    jump sylph_label
    else:

        call screen button_screen

label eris_location:
    if energia == 1:
        scene bg eris_place_noite
    elif energia == 2:
        scene bg eris_place_tarde
    else:
        scene bg eris_place
    with fade

    show screen button_screen
    menu:
        "🏰 Enter the Castle":
            $ local_atual = "eris_castle"
            jump locais

        "🕵️ Black Merchant" if energia == 1:
            hide screen button_screen
            jump black_merchant_event


label eris_castle:

    if energia == 1:
        scene bg eris_castle_noite
    elif energia == 2:
        scene bg eris_castle_tarde
    else:
        scene bg eris_castle
    with fade

    show screen button_screen
    jump eris_castle_menu
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
