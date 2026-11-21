

define goddess = Character("Goddess", color="#ffffaa")



label splashscreen:
    scene black
    call screen disclaimer
    return

label start:

    play music "audio/Through the Veil of Dreams.mp3" fadein 1.0 loop
    window hide

    menu:
        "Skip introduction":
            play music "Dream in a Teacup.mp3" fadein 3.0 loop
            jump locais
        "Watch introduction":
            pass

    scene black with fade
    pause 0.5
    scene white with Dissolve(1.5)

    "You open your eyes."
    "" "'Where... where am I?'"
    "An endless white stretches in every direction. No sound, no color... only silence."
    "You try to walk, but your feet don’t touch the ground — you’re floating."
    "" "'Is this... the afterlife?'"
    "" "'Damn... I knew that expired sushi would send me to my grave.'"

    "Suddenly, a gentle voice echoes within your mind, like a whisper carried by the wind."
    show goddess at center, slide_fade:
        zoom 0.85
    goddess "Rudeus Greyrat."
    goddess "That shall be your new name."

    rudeus "Hey! Who’s there?!"
    rudeus "A loli goddess?!"
    rudeus "I must be dreaming..."
    goddess "I am the one who guides lost souls."
    goddess "And you, Rudeus, are between two worlds. It was I who chose you."

    rudeus "Chose me? For what, exactly?"
    goddess "For a new life."
    goddess "A fresh start, in a completely different world."
    goddess "Where you’ll have the chance to correct the mistakes of your past."

    rudeus "So... I’m going to be reborn? Like... in an isekai?"
    goddess "If you wish to think of it that way, yes."
    goddess "But know this — destiny is shaped by will... and the courage to change."
    goddess "So, tell me. What is it that you desire most in this new life?"

    rudeus "Heh... courage, I’ve got plenty of that. And I already know what I want."
    rudeus "A harem full of beautiful girls! The perfect life!"
    goddess "Your ambitions are... peculiar. But perhaps this new world will surprise you, Rudeus Greyrat."

    "The light around you begins to grow stronger. The void dissolves into a blinding glow."
    goddess "Live your new life... and make it something truly unforgettable."

    scene black with fade
    pause 0.8
    play music "Dream in a Teacup.mp3" fadein 3.0 loop
    centered "{size=+8}Eighteen years later...{/size}"

    scene bg quarto_rudeus with fade
    show zenith normal at right with dissolve
    show rudeus normal at left with dissolve

    zenith "Rudy, my love! How does it feel to finally be an adult?"
    rudeus "Ahhh... honestly, Mom, it doesn’t feel that different."
    zenith "Haha, you’ve always been so mature for your age."
    zenith "But now that you’re eighteen... the world is full of possibilities!"
    zenith "Enjoy every moment, my dear."
    "She leans in and gives you a gentle kiss on the forehead."
    rudeus "I will, Mom."

    hide zenith with dissolve
    pause 0.3
    rudeus "Alright... now it begins."
    rudeus "Time to put my plan into action..."
    rudeus "My very own harem... Dream life, here I come!"
    scene black with fade
    "Your journey begins now."
    "Meet new people, build relationships, and explore this new world."
    "Earn their affection and, perhaps... just perhaps, your deepest desires may come true."
    jump locais
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
