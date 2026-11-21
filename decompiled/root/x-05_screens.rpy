default tooltip_text = ""

transform slime_zoom:
    zoom 0.3








transform half_zoom:
    zoom 0.55




default test_size = 150


screen button_screen():
    $ time_info = get_time_of_day()




    vbox:
        align (0.0, 0.0)
        xoffset 16
        yoffset 12
        spacing 0


        frame:
            xsize 375
            ysize 112
            padding (22, 12)

            if time_info["period"] == "morning":
                background "#1a2a1aE0"
            elif time_info["period"] == "afternoon":
                background "#2a1a0aE0"
            else:
                background "#0a0a2aE0"


            add Solid("#FFD70060") align (0.5, 0.0) xsize 375 ysize 2 yoffset -12

            add Solid("#FFD70040") align (0.5, 1.0) xsize 375 ysize 2 yoffset 12

            add Solid("#FFD70050") align (0.0, 0.5) xsize 2 ysize 112 xoffset -22

            add Solid("#FFD70050") align (1.0, 0.5) xsize 2 ysize 112 xoffset 22

            vbox:
                align (0.5, 0.5)
                spacing 10


                hbox:
                    xalign 0.5
                    spacing 16
                    text "Day [day]" size 30 color "#FFFFFF"
                    text "·" size 30 color "#ffffff40"
                    hbox:
                        spacing 6
                        text time_info["icon"] size 30
                        text time_info["name"] size 30 color time_info["color"]


                hbox:
                    xalign 0.5
                    spacing 8
                    text "💰" size 28
                    text "[player_gold] Gold" size 26 color "#FFD700"


        frame:
            xsize 375
            ysize 56
            padding (12, 8)
            background "#141428E0"


            add Solid("#FFD70030") align (0.5, 1.0) xsize 375 ysize 2 yoffset 8

            add Solid("#FFD70030") align (0.0, 0.5) xsize 2 ysize 56 xoffset -12

            add Solid("#FFD70030") align (1.0, 0.5) xsize 2 ysize 56 xoffset 12

            textbutton "⏭ Next Turn":
                align (0.5, 0.5)
                action Jump("passar_tempo")
                text_size 24
                text_color "#aaccff"
                text_hover_color "#ffffff"


        null height 10






































    vbox:
        align (1.0, 0.0)
        xoffset -16
        yoffset 12
        spacing 0


        frame:
            xsize 280
            ysize 62
            padding (12, 8)
            background "#1a1a30D0"

            add Solid("#FFD70040") align (0.5, 0.0) xsize 280 ysize 2 yoffset -8
            add Solid("#FFD70030") align (0.5, 1.0) xsize 280 ysize 2 yoffset 8
            add Solid("#FFD70040") align (0.0, 0.5) xsize 2 ysize 62 xoffset -12
            add Solid("#FFD70040") align (1.0, 0.5) xsize 2 ysize 62 xoffset 12

            textbutton "🗺️  Map":
                align (0.5, 0.5)
                action Show("fast_travel")
                text_size 26
                text_color "#88ccff"
                text_hover_color "#ffffff"


        frame:
            xsize 280
            ysize 62
            padding (12, 8)
            background "#1a1a30D0"

            add Solid("#FFD70030") align (0.5, 0.0) xsize 280 ysize 2 yoffset -8
            add Solid("#FFD70040") align (0.5, 1.0) xsize 280 ysize 2 yoffset 8
            add Solid("#ff669940") align (0.0, 0.5) xsize 2 ysize 62 xoffset -12
            add Solid("#ff669940") align (1.0, 0.5) xsize 2 ysize 62 xoffset 12

            textbutton "❤️  Affections":
                align (0.5, 0.5)
                action Show("status_personagens")
                text_size 26
                text_color "#ff99aa"
                text_hover_color "#ffffff"





    vbox:
        align (0.0, 1.0)
        xoffset 16
        yoffset -28
        spacing 0


        frame:
            xsize 280
            ysize 62
            padding (12, 8)
            background "#1a1a30D0"

            add Solid("#FFD70040") align (0.5, 0.0) xsize 280 ysize 2 yoffset -8
            add Solid("#FFD70030") align (0.5, 1.0) xsize 280 ysize 2 yoffset 8
            add Solid("#cc99ff40") align (0.0, 0.5) xsize 2 ysize 62 xoffset -12
            add Solid("#cc99ff40") align (1.0, 0.5) xsize 2 ysize 62 xoffset 12

            textbutton "🛠️  Cheats":
                align (0.5, 0.5)
                action Show("cheats_menu")
                text_size 26
                text_color "#cc99ff"
                text_hover_color "#ffffff"






label eris_castle_menu:
    if energia > 1:
        menu:
            "Call Eris":
                hide screen button_screen
                jump eris_label
            "Call Ghislaine":

                hide screen button_screen
                jump ghislaine_label
            "Back":

                $ local_atual = "eris_location"
                jump locais
    else:
        menu:
            "Back":
                $ local_atual = "eris_location"
                jump locais


screen fast_travel:
    modal True
    zorder 200
    add "#00000090"


    $ tt = GetTooltip()
    if tt:
        frame:
            background "#000000CC"
            padding (22, 10)
            xalign 0.5
            yalign 0.92
            text tt size 30 color "#FFD700" xalign 0.5

    frame:
        xalign 0.5
        yalign 0.5
        padding (50, 40)
        xsize 1400
        ysize 880
        background "#0a0a1eE0"


        add Solid("#FFD70060") align (0.5, 0.0) xsize 1400 ysize 2 yoffset -40
        add Solid("#FFD70040") align (0.5, 1.0) xsize 1400 ysize 2 yoffset 40
        add Solid("#FFD70050") align (0.0, 0.5) xsize 2 ysize 880 xoffset -50
        add Solid("#FFD70050") align (1.0, 0.5) xsize 2 ysize 880 xoffset 50

        vbox:
            spacing 20
            xalign 0.5


            hbox:
                xalign 0.5
                spacing 12
                text "🗺️" size 44
                text "Fast Travel" size 44 color "#FFD700"

            add Solid("#FFD70050") xsize 1300 ysize 2 xalign 0.5


            viewport:
                ymaximum 620
                xalign 0.5

                has vpgrid
                cols 3
                spacing 30
                xalign 0.5


                frame:
                    background "#141428E0"
                    padding (15, 15)
                    xsize 400

                    has vbox
                    spacing 8
                    xalign 0.5

                    imagebutton:
                        xalign 0.5
                        idle location_thumb("jardim_rudeus")
                        hover Transform(location_thumb("jardim_rudeus"), matrixcolor=BrightnessMatrix(0.15))

                        action [Hide("fast_travel", transition=dissolve), SetVariable("local_atual", "entrada_rudeus"), Jump("locais")]

                    text "🏠 Home" size 24 color "#CCCCCC" xalign 0.5


                frame:
                    background "#141428E0"
                    padding (15, 15)
                    xsize 400

                    has vbox
                    spacing 8
                    xalign 0.5

                    imagebutton:
                        xalign 0.5
                        idle location_thumb("vilarejo")
                        hover Transform(location_thumb("vilarejo"), matrixcolor=BrightnessMatrix(0.15))

                        action [Hide("fast_travel", transition=dissolve), SetVariable("local_atual", "vilarejo"), Jump("locais")]

                    text "🏘️ Buena Village" size 24 color "#CCCCCC" xalign 0.5


                frame:
                    background "#141428E0"
                    padding (15, 15)
                    xsize 400

                    has vbox
                    spacing 8
                    xalign 0.5

                    imagebutton:
                        xalign 0.5
                        idle location_thumb("floresta")
                        hover Transform(location_thumb("floresta"), matrixcolor=BrightnessMatrix(0.15))

                        action [Hide("fast_travel", transition=dissolve), SetVariable("local_atual", "floresta"), Jump("locais")]

                    text "🌲 Forest" size 24 color "#CCCCCC" xalign 0.5


                frame:
                    background "#141428E0"
                    padding (15, 15)
                    xsize 400

                    has vbox
                    spacing 8
                    xalign 0.5

                    imagebutton:
                        xalign 0.5
                        idle location_thumb("sylph_hut")
                        hover Transform(location_thumb("sylph_hut"), matrixcolor=BrightnessMatrix(0.15))
                        action [Hide("fast_travel", transition=dissolve), SetVariable("local_atual", "sylph_hut"), Jump("locais")]

                    text "🏡 Sylph's Hut" size 24 color "#CCCCCC" xalign 0.5


                frame:
                    background "#141428E0"
                    padding (15, 15)
                    xsize 400

                    has vbox
                    spacing 8
                    xalign 0.5

                    imagebutton:
                        xalign 0.5
                        idle location_thumb("eris_place")
                        hover Transform(location_thumb("eris_place"), matrixcolor=BrightnessMatrix(0.15))

                        action [Hide("fast_travel", transition=dissolve), SetVariable("local_atual", "eris_location"), Jump("locais")]

                    text "🏰 Citadel of Roa" size 24 color "#CCCCCC" xalign 0.5


            frame:
                xsize 280
                ysize 56
                padding (12, 8)
                xalign 0.5
                background "#141428E0"

                add Solid("#FFD70040") align (0.5, 0.0) xsize 280 ysize 2 yoffset -8
                add Solid("#FFD70040") align (0.5, 1.0) xsize 280 ysize 2 yoffset 8
                add Solid("#FFD70040") align (0.0, 0.5) xsize 2 ysize 56 xoffset -12
                add Solid("#FFD70040") align (1.0, 0.5) xsize 2 ysize 56 xoffset 12

                textbutton "✖  Close":
                    align (0.5, 0.5)
                    action Hide("fast_travel")
                    text_size 26
                    text_color "#aaccff"
                    text_hover_color "#ffffff"



init python:
    def is_video(path):
        return path.lower().endswith((".webm", ".mp4", ".ogv", ".avi"))


screen status_personagens():
    modal True
    zorder 200
    add "#00000090"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1200
        ysize 950
        padding (40, 28)
        background "#0a0a1eE0"


        add Solid("#FFD70060") align (0.5, 0.0) xsize 1200 ysize 2 yoffset -28
        add Solid("#FFD70040") align (0.5, 1.0) xsize 1200 ysize 2 yoffset 28
        add Solid("#FFD70050") align (0.0, 0.5) xsize 2 ysize 950 xoffset -40
        add Solid("#FFD70050") align (1.0, 0.5) xsize 2 ysize 950 xoffset 40

        vbox:
            spacing 14
            xalign 0.5


            hbox:
                xalign 0.5
                spacing 12
                text "❤️" size 42
                text "Character Relations" size 42 color "#FFD700"
                text "❤️" size 42


            add Solid("#FFD70050") xsize 1120 ysize 2 xalign 0.5

            null height 4


            viewport:
                xsize 1080
                ysize 650
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                has vbox
                spacing 15
                xalign 0.5


                hbox:
                    spacing 20
                    xalign 0.5

                    frame:
                        background "#2a2a4e"
                        padding (18, 15)
                        xsize 510

                        has hbox
                        spacing 15

                        frame:
                            background "#1a1a3e"
                            padding (8, 8)

                            add "icons/zenith_icon.png" xsize 112 ysize 112

                        vbox:
                            spacing 8
                            yalign 0.5

                            text "Zenith Greyrat" size 30 color "#FFD700"

                            hbox:
                                spacing 8
                                text "💗 Affection:" size 24 color "#FFFFFF"
                                text "[zenith_afeicao]" size 24 color "#FF69B4"

                    frame:
                        background "#2a2a4e"
                        padding (18, 15)
                        xsize 510

                        has hbox
                        spacing 15

                        frame:
                            background "#1a1a3e"
                            padding (8, 8)

                            add "icons/aisha_icon.png" xsize 112 ysize 112

                        vbox:
                            spacing 8
                            yalign 0.5

                            text "Aisha Greyrat" size 30 color "#FFD700"

                            hbox:
                                spacing 8
                                text "💗 Affection:" size 24 color "#FFFFFF"
                                text "[aisha_afeicao]" size 24 color "#FF69B4"


                hbox:
                    spacing 20
                    xalign 0.5

                    frame:
                        background "#2a2a4e"
                        padding (18, 15)
                        xsize 510

                        has hbox
                        spacing 15

                        frame:
                            background "#1a1a3e"
                            padding (8, 8)

                            add "icons/lilia_icon.png" xsize 112 ysize 112

                        vbox:
                            spacing 8
                            yalign 0.5

                            text "Lilia" size 30 color "#FFD700"

                            hbox:
                                spacing 8
                                text "💗 Affection:" size 24 color "#FFFFFF"
                                text "[lilia_afeicao]" size 24 color "#FF69B4"

                    frame:
                        background "#2a2a4e"
                        padding (18, 15)
                        xsize 510

                        has hbox
                        spacing 15

                        frame:
                            background "#1a1a3e"
                            padding (8, 8)

                            add "icons/roxy_icon.png" xsize 112 ysize 112

                        vbox:
                            spacing 8
                            yalign 0.5

                            text "Roxy Migurdia" size 30 color "#FFD700"

                            hbox:
                                spacing 8
                                text "💗 Affection:" size 24 color "#FFFFFF"
                                text "[roxy_afeicao]" size 24 color "#FF69B4"


                hbox:
                    spacing 20
                    xalign 0.5

                    frame:
                        background "#2a2a4e"
                        padding (18, 15)
                        xsize 510

                        has hbox
                        spacing 15

                        frame:
                            background "#1a1a3e"
                            padding (8, 8)

                            add "icons/s_dog_icon.png" xsize 112 ysize 112

                        vbox:
                            spacing 8
                            yalign 0.5

                            text "[s_dog_name]" size 30 color "#FFD700"

                            hbox:
                                spacing 8
                                text "💗 Affection:" size 24 color "#FFFFFF"
                                text "[slave_dog_affection]" size 24 color "#FF69B4"

                    frame:
                        background "#2a2a4e"
                        padding (18, 15)
                        xsize 510

                        has hbox
                        spacing 15

                        frame:
                            background "#1a1a3e"
                            padding (8, 8)

                            add "icons/sylph_icon.png" xsize 112 ysize 112

                        vbox:
                            spacing 8
                            yalign 0.5

                            text "Sylphiette" size 30 color "#FFD700"

                            hbox:
                                spacing 8
                                text "💗 Affection:" size 24 color "#FFFFFF"
                                text "[sylph_afeicao]" size 24 color "#FF69B4"


                hbox:
                    spacing 20
                    xalign 0.5

                    frame:
                        background "#2a2a4e"
                        padding (18, 15)
                        xsize 510

                        has hbox
                        spacing 15

                        frame:
                            background "#1a1a3e"
                            padding (8, 8)

                            add "icons/norn_icon.png" xsize 112 ysize 112

                        vbox:
                            spacing 8
                            yalign 0.5

                            text "Norn Greyrat" size 30 color "#FFD700"

                            hbox:
                                spacing 8
                                text "💗 Affection:" size 24 color "#FFFFFF"
                                text "[norn_afeicao]" size 24 color "#FF69B4"

                    frame:
                        background "#2a2a4e"
                        padding (18, 15)
                        xsize 510

                        has hbox
                        spacing 15

                        frame:
                            background "#1a1a3e"
                            padding (8, 8)
                            xsize 128
                            ysize 128

                            add "icons/ghislaine_icon.png" xsize 112 ysize 112

                        vbox:
                            spacing 8
                            yalign 0.5

                            text "Ghislaine Dedoldia" size 30 color "#FFD700"

                            hbox:
                                spacing 8
                                text "💗 Affection:" size 24 color "#FFFFFF"
                                text "[ghislaine_afeicao]" size 24 color "#FF69B4"


                hbox:
                    spacing 20
                    xalign 0.5

                    frame:
                        background "#2a2a4e"
                        padding (18, 15)
                        xsize 510

                        has hbox
                        spacing 15

                        frame:
                            background "#1a1a3e"
                            padding (8, 8)
                            xsize 128
                            ysize 128

                            add "icons/eris_icon.png" xsize 112 ysize 112

                        vbox:
                            spacing 8
                            yalign 0.5

                            text "Eris Boreas" size 30 color "#FFD700"

                            hbox:
                                spacing 8
                                text "💗 Affection:" size 24 color "#FFFFFF"
                                text "[eris_afeicao]" size 24 color "#FF69B4"


                    frame:
                        background "#2a2a4e"
                        padding (18, 15)
                        xsize 510

                        has hbox
                        spacing 15

                        frame:
                            background "#1a1a3e"
                            padding (8, 8)
                            xsize 128
                            ysize 128

                            add "icons/slime_girl_icon.png" xsize 112 ysize 112

                        vbox:
                            spacing 8
                            yalign 0.5

                            text "Slime Girl" size 30 color "#FFD700"

                            hbox:
                                spacing 8
                                text "💗 Affection:" size 24 color "#FFFFFF"
                                text "[slime_girl_affection]" size 24 color "#FF69B4"

            null height 6


            frame:
                xsize 280
                ysize 56
                padding (12, 8)
                xalign 0.5
                background "#141428E0"

                add Solid("#FFD70040") align (0.5, 0.0) xsize 280 ysize 2 yoffset -8
                add Solid("#FFD70040") align (0.5, 1.0) xsize 280 ysize 2 yoffset 8
                add Solid("#ff669940") align (0.0, 0.5) xsize 2 ysize 56 xoffset -12
                add Solid("#ff669940") align (1.0, 0.5) xsize 2 ysize 56 xoffset 12

                textbutton "✖  Close":
                    align (0.5, 0.5)
                    action Hide("status_personagens")
                    text_size 26
                    text_color "#ff99aa"
                    text_hover_color "#ffffff"


init python:
    def toggle_affection_cheat():
        if not player_patreon:
            renpy.notify("🔒 Exclusive to Patreon supporters.")
            return
        
        store.affection_cheat_on = not store.affection_cheat_on
        
        if store.affection_cheat_on:
            affection_vars = (
            "zenith_afeicao", "aisha_afeicao", "roxy_afeicao", "lilia_afeicao",
            "slave_dog_affection", "sylph_afeicao", "norn_afeicao",
            "ghislaine_afeicao", "eris_afeicao",
        )
            for _var in affection_vars:
                setattr(store, _var, AFFECTION_CHEAT_MAX)
            store.slime_girl_affection = 100
            renpy.notify("💗 Affection Cheat ON — all girls at max affection!")
        else:
            renpy.notify("Affection Cheat OFF.")


screen cheats_menu():
    modal True
    zorder 200
    add "#00000090"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 720
        ysize 360
        padding (40, 28)
        background "#0a0a1eE0"


        add Solid("#FFD70060") align (0.5, 0.0) xsize 720 ysize 2 yoffset -28
        add Solid("#FFD70040") align (0.5, 1.0) xsize 720 ysize 2 yoffset 28
        add Solid("#FFD70050") align (0.0, 0.5) xsize 2 ysize 360 xoffset -40
        add Solid("#FFD70050") align (1.0, 0.5) xsize 2 ysize 360 xoffset 40

        vbox:
            spacing 16
            xalign 0.5


            hbox:
                xalign 0.5
                spacing 12
                text "🛠️" size 40
                text "Cheats" size 40 color "#FFD700"

            add Solid("#FFD70050") xsize 640 ysize 2 xalign 0.5

            null height 4


            frame:
                xsize 640
                ysize 96
                padding (18, 12)
                background "#1a1a30D0"

                add Solid("#ff669940") align (0.0, 0.5) xsize 2 ysize 96 xoffset -18
                add Solid("#ff669940") align (1.0, 0.5) xsize 2 ysize 96 xoffset 18

                hbox:
                    align (0.5, 0.5)
                    spacing 24

                    vbox:
                        spacing 4
                        yalign 0.5
                        text "💗 Max Affection — All Girls" size 24 color "#ffffff"
                        if player_patreon:
                            text "Patreon perk — toggle anytime" size 18 color "#88ff88"
                        else:
                            text "🔒 Patreon supporters only" size 18 color "#ff8888"

                    textbutton ("ON" if affection_cheat_on else "OFF"):
                        xsize 110
                        ysize 48
                        yalign 0.5
                        text_align (0.5, 0.5)
                        text_size 24
                        text_color ("#00ff88" if affection_cheat_on else "#ff6666")
                        text_hover_color "#ffffff"
                        action Function(toggle_affection_cheat)

            null height 4


            frame:
                xsize 280
                ysize 56
                padding (12, 8)
                xalign 0.5
                background "#141428E0"

                add Solid("#FFD70040") align (0.5, 0.0) xsize 280 ysize 2 yoffset -8
                add Solid("#FFD70040") align (0.5, 1.0) xsize 280 ysize 2 yoffset 8
                add Solid("#cc99ff40") align (0.0, 0.5) xsize 2 ysize 56 xoffset -12
                add Solid("#cc99ff40") align (1.0, 0.5) xsize 2 ysize 56 xoffset 12

                textbutton "✖  Close":
                    align (0.5, 0.5)
                    action Hide("cheats_menu")
                    text_size 26
                    text_color "#cc99ff"
                    text_hover_color "#ffffff"




screen character_gallery(char, char_name):
    modal True
    zorder 210


    $ gallery_imgs = character_gallery_images.get(char, [])

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1400
        ysize 980
        padding (40, 28)
        background "#0a0a1eE0"


        add Solid("#FFD70060") align (0.5, 0.0) xsize 1400 ysize 2 yoffset -28
        add Solid("#FFD70040") align (0.5, 1.0) xsize 1400 ysize 2 yoffset 28
        add Solid("#FFD70050") align (0.0, 0.5) xsize 2 ysize 980 xoffset -40
        add Solid("#FFD70050") align (1.0, 0.5) xsize 2 ysize 980 xoffset 40

        vbox:
            spacing 14
            xalign 0.5


            hbox:
                xalign 0.5
                spacing 12
                text "🖼️" size 42
                text "[char_name]" size 36 color "#FFD700"
                text "— Gallery" size 36 color "#aaaacc"

            add Solid("#FFD70050") xsize 1320 ysize 2 xalign 0.5

            null height 4

            if gallery_imgs:
                viewport:
                    xsize 1320
                    ysize 680
                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    has vpgrid
                    cols 4
                    spacing 10
                    xalign 0.5

                    for img_path in gallery_imgs:
                        $ _vid = is_video(img_path)
                        if _vid:
                            button:
                                background "#0d0d1e"
                                hover_background "#ffffff00"
                                xsize 316
                                ysize 178
                                padding (0, 0)
                                action Show("fullscreen_media", media_path=img_path)
                                has frame
                                xfill True
                                yfill True
                                background "#000000CC"
                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    spacing 4
                                    text "▶" size 56 color "#ffffff" xalign 0.5
                                    text "Video" size 16 color "#aaccff" xalign 0.5
                        else:
                            imagebutton:
                                idle im.Scale(img_path, 316, 178)
                                hover Transform(im.Scale(img_path, 316, 178), matrixcolor=BrightnessMatrix(0.25))
                                action Show("fullscreen_media", media_path=img_path)
            else:
                frame:
                    xsize 1080
                    ysize 600
                    background None
                    text "No media added." size 24 color "#666688" xalign 0.5 yalign 0.5

            null height 6


            frame:
                xsize 280
                ysize 56
                padding (12, 8)
                xalign 0.5
                background "#141428E0"

                add Solid("#FFD70040") align (0.5, 0.0) xsize 280 ysize 2 yoffset -8
                add Solid("#FFD70040") align (0.5, 1.0) xsize 280 ysize 2 yoffset 8
                add Solid("#ff669940") align (0.0, 0.5) xsize 2 ysize 56 xoffset -12
                add Solid("#ff669940") align (1.0, 0.5) xsize 2 ysize 56 xoffset 12

                textbutton "◀  Return":
                    align (0.5, 0.5)
                    action Hide("character_gallery")
                    text_size 26
                    text_color "#ff99aa"
                    text_hover_color "#ffffff"


screen fullscreen_media(media_path):
    modal True
    zorder 300

    add "#000000EE"

    $ _is_vid = is_video(media_path)

    if _is_vid:
        add Movie(play=media_path, loop=True, size=(config.screen_width, config.screen_height)) xalign 0.5 yalign 0.5
    else:
        add media_path xalign 0.5 yalign 0.5

    button:
        xfill True
        yfill True
        background None
        action Hide("fullscreen_media")

    key "K_ESCAPE" action Hide("fullscreen_media")


screen disclaimer():
    tag menu
    modal True


    add "#000000"

    frame:
        background None
        xalign 0.5
        yalign 0.5
        xsize 900

        has vbox
        spacing 40
        xalign 0.5


        text "{size=60}{color=#ff0000}⚠ WARNING ⚠{/color}{/size}":
            xalign 0.5
            text_align 0.5


        text "{size=42}This game is intended for adults 18 years and older only.{/size}":
            xalign 0.5
            text_align 0.5
            color "#ffffff"

        text "{size=36}This game has NO affiliation whatsoever with the creators\nof Mushoku Tensei.{/size}":
            xalign 0.5
            text_align 0.5
            color "#cccccc"

        text "{size=36}This is a fan-made parody.{/size}":
            xalign 0.5
            text_align 0.5
            color "#cccccc"


        null height 20


        hbox:
            spacing 50
            xalign 0.5


            textbutton "Continue":
                xalign 0.5
                xsize 350
                ysize 70
                text_size 33
                text_xalign 0.5
                text_yalign 0.5
                background "#00aa00"
                hover_background "#00ff00"
                text_color "#ffffff"
                action Return()


            textbutton "Quit Game":
                xalign 0.5
                xsize 350
                ysize 70
                text_size 33
                text_xalign 0.5
                text_yalign 0.5
                background "#aa0000"
                hover_background "#ff0000"
                text_color "#ffffff"
                action Quit(confirm=False)
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
