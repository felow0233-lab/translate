



define black_merchant = Character("Black Merchant", color="#c7c7c7")
define s_dog = Character("[s_dog_name]", color="#c7a7a7")


default s_dog_name = "Dog Slave"
default buy_dog_slave = False


default merchant_intro = True





label black_merchant_event:
    if merchant_intro:

        scene black with fade

        rudeus "(The Citadel of Roa at night... bigger, richer, and a lot more shadows than Buena.)"

        scene bg eris_place_noite with fade

        "???" "Psst... Hey, kid... yeah, you. Come here for a sec..."

        rudeus "(Huh? What was that...)"

        rudeus "(...From the alley by the wall? Someone's hiding back there.)"

        rudeus "(Could be trouble. Better keep my guard up.)"

        show rudeus normal at left, slide_fade
        show s_merchant normal at right, slide_fade
        with dissolve

        rudeus "...Who's there? Step out where I can see you."

        black_merchant "Heh, easy now. No need for that look, kid. I'm not here to cause trouble."

        rudeus "(A shady guy in a dark coat, hiding in an alley under the citadel walls... yeah, totally not suspicious.)"

        rudeus "Right. And who exactly are you supposed to be?"

        black_merchant "Hehe... let's just say I'm a special kind of merchant. I deal in very particular goods."

        rudeus "(Special merchant. In a Roa alley. Calling people over in secret.)"
        rudeus "(...Yeah, I think I already know where this is going.)"

        rudeus "Special goods, huh? That's awfully vague."

        black_merchant "Hahaha, sharp one! Fine, I'll be blunt then... I deal in slaves, boy."

        rudeus "(Called it.)"

        rudeus "...Slaves. Just like that, out in the open? In the capital?"

        black_merchant "Relax, relax. Perfectly legal in this kingdom, as long as the coin's good."
        black_merchant "And let me tell you, I've got some real beauties in stock right now. Exotic types, well-trained, very... obedient."

        rudeus "(...Okay. I really shouldn't be interested in this.)"

        black_merchant "If you ever feel like taking a look, just come find me around the citadel. I'm always around."
        black_merchant "I promise, kid... you won't walk away disappointed."

        rudeus "(A slave merchant, casually doing business under the Citadel of Roa...)"
        rudeus "(This world really doesn't hold back, does it?)"

        rudeus "(...Still. Can't hurt to take a look sometime. Right?)"

        $ merchant_intro = False
        $ local_atual = "eris_location"
        jump locais
    else:
        if energia == 1:
            scene bg eris_place_noite
        elif energia == 2:
            scene bg eris_place_tarde
        else:
            scene bg eris_place
        with fade
        show rudeus normal at left, slide_fade
        show s_merchant normal at right, slide_fade
        jump slave_merchant_menu




label slave_merchant_menu:
    menu:
        "Buy Dog Girl (!)" if not buy_dog_slave:

            black_merchant "Heh, look who's back. Couldn't stay away, could you, kid?"

            rudeus "…Yeah, yeah. I was just in the area. No big deal."

            black_merchant "Sure, sure. 'Just in the area.' Heh, whatever helps you sleep at night, kid."
            black_merchant "Lucky for you, that little beauty I told you about is still here. Wanna see her?"

            rudeus "...Might as well, since I'm already here."

            black_merchant "Take a look for yourself, kid."
            black_merchant "Hey! Dog-eared girl, get that pretty ass over here and show this fine gentleman just how obedient you can be!"
            s_dog "Y-yes, sir…"
            show s_dog normal at center, slide_fade
            black_merchant "Feast your eyes on this little beauty… one of my most obedient pets."
            rudeus "Damn… she’s actually really cute."
            black_merchant "And the best part? She can be yours for the low price of just 200 gold coins."
            black_merchant "So, what do you say? Ready to take her home and break her in?"
            menu s_dog_buy_menu:
                "Buy the slave (200 gold)":


                    if player_gold >= 200:
                        $ player_gold -= 200
                        rudeus "Deal! I’ll take her."
                        black_merchant "Excellent choice, lad! You’re gonna love every second with her."
                        black_merchant "Here’s your new toy. Enjoy!"
                        black_merchant "And if you ever get bored of her, I’ve always got fresh stock."
                        rudeus "Uh… thanks, I guess…"
                        hide s_merchant normal with dissolve
                        rudeus "So, what’s your name, cutie?"
                        s_dog "M-my name… I don’t have one, Master…"
                        rudeus "Hmm… then I’ll give you one right now."
                        $ temp = renpy.input("What name do you want to give her?")
                        $ temp = temp.strip()

                        if temp == "":
                            $ s_dog_name = "Mel"
                        else:
                            $ s_dog_name = temp
                        rudeus "From now on, your name is [s_dog_name]."
                        s_dog "Th-thank you so much, Master…"

                        $ buy_dog_slave = True
                        $ local_atual = "entrada_rudeus"
                        $ renpy.notify("You bought a slave! She’s now waiting for you in the barn.")
                        jump locais
                    else:
                        black_merchant "Looks like your wallet’s a little light, buddy."
                        black_merchant "Come back when you’ve got the gold."
                "Pass":
                    rudeus "I’ll think about it."
                    black_merchant "No rush, kid. My girls aren’t going anywhere."
            jump locais
        "Return":













            $ local_atual = "eris_location"
            jump locais



default s_femboy = Character("[s_femboy_name]", color="#c7a7c7")


default s_femboy_name = "Femboy Slave"
default buy_femboy_slave = False


label black_merchant_event_part2:
    show rudeus normal at left, slide_fade
    show s_merchant normal at right, slide_fade

    black_merchant "Ora ora, voltou tão cedo, rapaz? Já sentiu falta do meu estoque de qualidade?"
    rudeus "Na verdade… vim ver se você tem mais alguma coisa interessante."
    black_merchant "Hoho~ Claro que tenho. Sempre guardo as peças mais… especiais pros clientes fiéis."

    black_merchant "Ei! Você aí, o de orelhinhas de gato e rabinho balançando… vem cá mostrar pro moço!"

    show s_femboy normal at center, slide_fade

    rudeus "......"
    rudeus "...pera aí."
    rudeus "Isso… é uma garota?"

    black_merchant "Hahahaha! A reação clássica! Todo mundo cai nessa na primeira vez."
    black_merchant "Esse aqui é um dos meus garotos mais refinados. Treinado pra ser doce, obediente e… bem delicado."
    black_merchant "Olha só essas perninhas, essa cintura fina, esse jeitinho de abaixar a cabeça envergonhado… perfeito, não é?"

    s_femboy "B-boa tarde… gentil senhor…"

    rudeus "...cara, eu não esperava isso."
    rudeus "Tipo… eu vim achando que ia ver outra garota fofa, não um… uh… garoto extremamente fofo."

    black_merchant "Exatamente! É aí que entra a surpresinha."
    black_merchant "Ele é versátil. Pode ser sua donzela tímida durante o dia… e à noite, bem… digamos que ele sabe usar muito bem esse corpinho delicado."
    black_merchant "Muitos dos meus clientes mais exigentes adoram essa dualidade. É um sabor diferente, entende?"

    rudeus "Você tá me vendendo um femboy com propaganda de ‘versátil’ agora?"
    rudeus "Isso é… inesperado pra caramba."

    black_merchant "E o melhor: só 250 moedas de ouro. Um pouco mais caro que a garotinha-loba, mas olha essa pele macia, esses olhinhos pidões… vale cada centavo."
    black_merchant "Então, o que me diz? Quer levar esse mimo pra casa e experimentar algo… diferente?"

    menu s_femboy_buy_menu:
        "Comprar o escravo (250 ouro)":
            if player_gold >= 250:
                $ player_gold -= 250
                rudeus "…tá bom. Tô dentro. Vai que é uma experiência nova."
                black_merchant "Excelente! Sabia que você tinha mente aberta, garoto!"
                black_merchant "Toma aqui sua nova aquisição. Cuida bem dele, hein? Ele é sensível."
                black_merchant "Qualquer problema, já sabe onde me encontrar."
                black_merchant "Mas já te aviso: se ele cagar no seu piso, não me responsabilizo, hein?"
                hide s_merchant normal with dissolve


                rudeus "C-cagar no piso? Ah, deixa pra lá…"
                s_femboy "Não se preocupe, senhor... eu não vou fazer bagunça..."
                rudeus "…e aí, você tem nome?"
                s_femboy "N-não, Mestre… meu antigo dono só me chamava de ‘gatinho’ ou ‘coisinha’…"

                rudeus "Certo… então vou te dar um nome agora."
                $ temp = renpy.input("Qual nome você quer dar pra ele?")
                $ temp = temp.strip()

                if temp == "":
                    $ s_femboy_name = "Yuri"
                else:
                    $ s_femboy_name = temp

                rudeus "A partir de agora você é [s_femboy_name]."
                s_femboy "Obrigado… Mestre... [s_femboy_name]… eu gostei bastante…"

                $ buy_femboy_slave = True
                $ renpy.notify("Você comprou outro escravo! Ele está esperando por você no celeiro.")
                jump locais
            else:
                black_merchant "Opa, parece que o bolso ainda tá vazio pra essa delícia."
                black_merchant "Volta quando tiver as 250 moedinhas, tá?"
        "Passar":

            rudeus "Acho que… por hoje não. Ainda tô processando isso."
            black_merchant "Sem problema. Ele não vai a lugar nenhum. Quando quiser provar algo mais… exótico, é só voltar."
            jump locais
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
