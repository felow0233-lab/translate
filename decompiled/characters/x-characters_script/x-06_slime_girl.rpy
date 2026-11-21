


image slime_girl angry:
    "images/pers/slime_girl/slime_girl angry.png"
    zoom 0.5

image slime_girl auch:
    "images/pers/slime_girl/slime_girl auch.png"
    zoom 0.5

image slime_girl attack:
    "images/pers/slime_girl/slime_girl attack.png"
    zoom 0.5

image slime_girl surprised:
    "images/pers/slime_girl/slime_girl surprised.png"
    zoom 0.5

image slime_girl shy:
    "images/pers/slime_girl/slime_girl shy.png"
    zoom 0.5

image slime_girl lewd:
    "images/pers/slime_girl/slime_girl lewd.png"
    zoom 0.5


label slime_girl_intro_combat:

    rudeus "(Just a bit deeper into the forest... there should be some herbs worth gathering around here.)"

    show slime_girl angry at center, slide_fade

    slime_girl "...!"
    slime_girl "Stop right there! Who said you could come waltzing into our territory?!"

    rudeus "Whoa— a slime that talks?"
    rudeus "(...Holy crap, that outfit's barely holding together. Not that I'm complaining.)"
    rudeus "Look, I don't want any trouble. I'm just passing through."

    slime_girl "'Just passing through,' he says... That's exactly what they ALL say!"
    slime_girl "And then it's stomping, and burning, and dragging my sisters off in sacks!"

    rudeus "I haven't done any of that—"

    slime_girl "I don't care! You're a human, and humans mean trouble. That's just how it is!"
    slime_girl "(...He doesn't look like the others, though. Not that it matters!)"

    slime_girl "S-so here's the deal: if you want to walk through MY forest, you'll have to get through ME first!"

    rudeus "(She's... oddly fired up about this.)"
    rudeus "Fine. If that's how it has to be."

    slime_girl "Hmph! Don't think I'll go easy on you just because you've got a cute face or something!"
    slime_girl "Wha— I-I mean! Just because you ASKED nicely! That's what I meant!"

    return


label slime_girl_encounter_start:
    $ sc_just_met = not slime_girl_intro_seen
    if not slime_girl_intro_seen:
        call slime_girl_intro_combat from _call_slime_girl_intro_combat
        $ slime_girl_intro_seen = True
    jump slime_combat_simple
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
