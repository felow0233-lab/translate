



define vendedor = Character("Cute Vendedora", color="#ffff00")


default simple_flower_count = 0
default chocolate_box_count = 0
default luxury_jewelry_count = 0
default premium_necklace_count = 0


default bouquet_count = 0
default hair_ribbon_count = 0
default grimoire_count = 0
default food_count = 0



label buy_event:
    if energia == 1:
        scene bg vilage_shop_interior_noite
    elif energia == 2:
        scene bg vilage_shop_interior_tarde
    else:
        scene bg vilage_shop_interior
    with fade

    menu vendedor_menu:
        "Buy Gifts 🎁":

            call screen gift_shop_screen
            jump vendedor_menu
        "Return":

            jump locais










































            jump vendedor_menu




screen gift_shop_screen():
    modal True
    add "#000000CC"


    default item_emojis = {
        "Simple Flower": "🌸",
        "Box of Chocolates": "🍫",
        "Diamond Earring": "💎",
        "Premium Necklace": "👑",
    }

    default items = [
        {"name": "Simple Flower", "var": "simple_flower_count", "price": 25, "desc": "A beautiful flower. Simple but charming gift.", "affection": 10},
        {"name": "Box of Chocolates", "var": "chocolate_box_count", "price": 80, "desc": "Delicious premium chocolates. A special gift!", "affection": 25},
        {"name": "Diamond Earring", "var": "luxury_jewelry_count", "price": 140, "desc": "Rare and valuable jewel. The perfect gift!", "affection": 50},
        
    ]

    frame:
        xalign 0.5
        yalign 0.5
        padding (50, 40)
        xsize 1200
        background "#101225"

        has vbox
        spacing 20
        xalign 0.5

        text "Gift Shop":
            size 48
            color "#FFEE88"
            xalign 0.5

        text "Universal gifts for all the girls!":
            size 24
            color "#BBD4FF"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 10
            text "Your Gold:" size 28 color "#FFFFFF"
            text "[player_gold]":
                size 28
                color "#FFD700"

            text "💰" size 28 color "#FFD700"

        frame:
            background "#5AC8FA40"
            xalign 0.5
            xsize 1100
            ysize 3

        viewport:
            ymaximum 520
            xalign 0.5
            draggable True
            scrollbars "vertical"

            has vbox
            spacing 18
            xalign 0.5
            for it in items:
                frame:
                    background "#1B2147"
                    padding (18, 18)
                    xsize 1080
                    yminimum 160

                    has hbox
                    spacing 20

                    frame:
                        background "#0F1333"
                        padding (6, 6)
                        xsize 120
                        ysize 120

                        has vbox
                        xalign 0.5
                        yalign 0.5
                        text item_emojis.get(it["name"], "🎁"):
                            size 68
                            color "#FFEE88"
                            xalign 0.5
                            yalign 0.5

                    vbox:
                        spacing 6
                        xfill True

                        text it["name"]:
                            size 32
                            color "#FFEE88"

                        text it["desc"]:
                            size 18
                            color "#D7E0FF"
                            text_align 0.0

                        frame:
                            background "#FF69B420"
                            padding (8, 6)
                            xsize 200
                            text "💗 +[it['affection']] Affection":
                                size 20
                                color "#FF69B4"
                                xalign 0.5


                        $ owned = getattr(renpy.store, it["var"], 0)
                        text "You have: [owned]":
                            size 18
                            color "#9FD6FF"

                        hbox:
                            spacing 12
                            xfill True

                            text "Price: [it['price']] 💰":
                                size 22
                                color "#FFFFFF"
                                xalign 0.0

                            null width 1

                            textbutton "Buy":
                                xalign 1.0
                                background "#2C365F"
                                hover_background "#FFB84D"
                                text_color "#FFFFFF"
                                xsize 250
                                ysize 90
                                text_size 40
                                padding (10, 10)
                                text_xalign 0.5
                                text_yalign 0.5
                                action If(
                                                player_gold >= it["price"],
                                                true=[
                                                    SetVariable("player_gold", player_gold - it["price"]),
                                                    SetVariable(it["var"], getattr(renpy.store, it["var"], 0) + 1),
                                                    Function(renpy.notify, "Bought {}!".format(it["name"]))
                                                ],
                                                false=[
                                                    Function(renpy.notify, "Not enough gold!")
                                                ]
                                            )

        textbutton "Close":
            action Return()
            xalign 0.5
            text_size 38
            padding (100, 20)
            background "#2C365F"
            hover_background "#FFD700"
            text_color "#FFFFFF"



screen gift_selection_screen(character_id, character_name, available_gifts):
    modal True
    add "#000000DD"

    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        xsize 900
        background "#101225"

        has vbox
        spacing 20
        xalign 0.5

        text "Give Gift to [character_name]":
            size 40
            color "#FFEE88"
            xalign 0.5

        text "Choose a gift to give:":
            size 24
            color "#BBD4FF"
            xalign 0.5

        frame:
            background "#5AC8FA40"
            xalign 0.5
            xsize 820
            ysize 3

        null height 10


        vbox:
            spacing 15
            xalign 0.5


            for gift_id, gift_name, qty, affection_value in available_gifts:
                $ emoji = "🌸" if gift_id == "simple_flower" else ("🍫" if gift_id == "chocolate_box" else ("💎" if gift_id == "luxury_jewelry" else "👑"))

                frame:
                    background "#1B2147"
                    padding (20, 15)
                    xsize 820

                    has hbox
                    spacing 20


                    frame:
                        background "#0F1333"
                        padding (15, 15)
                        xsize 80
                        ysize 80
                        text emoji:
                            size 48
                            xalign 0.5
                            yalign 0.5


                    vbox:
                        spacing 5
                        yalign 0.5
                        xsize 450

                        text "[gift_name]":
                            size 26
                            color "#FFFFFF"

                        text "Affection: +[affection_value] (Owned: [qty])":
                            size 20
                            color "#90EE90"


                    textbutton "Give":
                        xalign 1.0
                        yalign 0.5
                        background "#2C5F2D"
                        hover_background "#90EE90"
                        text_color "#FFFFFF"
                        text_size 28
                        padding (30, 15)
                        action Return(gift_id)

        null height 10

        frame:
            background "#5AC8FA40"
            xalign 0.5
            xsize 820
            ysize 3

        null height 10


        textbutton "Back":
            xalign 0.5
            background "#2C365F"
            hover_background "#5A6FA8"
            text_color "#FFFFFF"
            text_size 38
            padding (100, 25)
            action Return(None)
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
