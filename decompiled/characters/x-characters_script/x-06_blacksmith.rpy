
define gunnar = Character("Gunnar", color="#ff9a3c")
define freya = Character("Freya",  color="#ff8fb0")

default smith_event = 0
default freya_on = True

default smith_hj_unlocked = False
default smith_oral_unlocked = False
default smith_vaginal_unlocked = False
default smith_anal_unlocked = False


label smith_forge_menu:
    menu:
        "📜 Meet the Blacksmith (!)" if smith_event == 0 and freya_on:
            hide screen button_screen
            jump smith_ev_1

        "📜 Talk (!)" if smith_event == 1 and freya_on:
            hide screen button_screen
            jump smith_ev_2

        "📜 Good With Her Hands (!)" if smith_event == 2 and freya_on:
            hide screen button_screen
            jump smith_ev_3

        "📜 A Walk in the Woods (!)" if smith_event == 3 and freya_on:
            hide screen button_screen
            jump smith_ev_4

        "📜 Her First Touch (!)" if smith_event == 4 and freya_on:
            hide screen button_screen
            jump smith_ev_5

        "📜 The Oblivious Dad (!)" if smith_event == 5 and freya_on:
            hide screen button_screen
            jump smith_ev_6

        "📜 Something New (!)" if smith_event == 6 and freya_on:
            hide screen button_screen
            jump smith_ev_7

        "📜 The Blacksmith's Blessing (!)" if smith_event == 7 and freya_on:
            hide screen button_screen
            jump smith_ev_8

        "📜 All the Way (!)" if smith_event == 8 and freya_on:
            hide screen button_screen
            jump smith_ev_9

        "📜 Never Satisfied (!)" if smith_event == 9 and freya_on:
            hide screen button_screen
            jump smith_ev_10

        "📜 The Last First Time (!)" if smith_event == 10 and freya_on:
            hide screen button_screen
            jump smith_ev_11

        "💗 Spend Time with Freya" if smith_event >= 11 and freya_on:
            hide screen button_screen
            jump smith_interact
        "Return":

            $ local_atual = "vilarejo"
            jump locais

image gunnar:
    "images/pers/gunnar.png"
    zoom 0.54

image freya:
    "images/pers/freya.png"
    zoom 0.5
    yalign 1.0



label smith_ev_1:


    narrator "At the edge of the village, the sound of metal striking metal cuts through the air."

    show rudeus normal at left with dissolve
    rudeus "(Gunnar's forge… I walk past here every week and never go in. Time to take a look.)"

    show gunnar at center with dissolve

    narrator "Behind a wall of heat and orange sparks stands a MOUNTAIN of a man."

    narrator "Arms like tree trunks, a beard singed at the edges, and a hammer in his fist the size of your head."

    show rudeus smirk at left

    rudeus "(Holy shit. This guy could bench-press a horse.)"

    narrator "The giant looks up, wipes his brow, and squints at you."

    gunnar "…Wait. Those eyes. That messy hair. That cocky little grin…"
    gunnar "You're PAUL'S boy! Rudeus, right?!"

    show rudeus surpreso at left
    rudeus "Uh— yeah. How the hell do you know that?"

    gunnar "GWAHAHAHA!"
    narrator "The laugh hits you like a punch. Two crows explode out of a nearby tree."

    gunnar "How do I know?! Boy, your old man NEVER shut up about you!"
    gunnar "'My Rudy this, my genius Rudy that' — swimming in beer at the tavern, crying with pride!"
    gunnar "Name's Gunnar. Best smith in three villages. Me and Paul go WAY back."

    show rudeus normal at left
    rudeus "(Great. Even here I can't escape that man's bragging.)"
    rudeus "Nice to meet you, Gunnar."

    gunnar "Any son of Paul is family to me! Tell you what—"
    narrator "He drops the hammer with a heavy CLANG and claps a hand on your shoulder that nearly folds you in half."

    gunnar "You're gonna LOVE my daughter."

    show rudeus surpreso at left
    rudeus "(…His what now?)"

    gunnar "FREYAAAAAA!!! GET OUT HERE! RIGHT NOW! THERE'S SOMEONE YOU NEED TO MEET!!!"

    narrator "He bellows toward the little house behind the forge loud enough to wake the dead. Somewhere a dog starts barking."

    show gunnar:
        ease 1.0 xalign 1.0
    show freya at center with dissolve
    narrator "The door creaks. A girl peeks out."
    narrator "Soft flushed cheeks, and two cute braids a little messy — a stray strand stuck to her face."
    freya "D-Dad… you don't have to scream like that… the whole village can hear you…"

    show rudeus extase at left
    rudeus "(…Oh. Oh no. She's adorable.)"
    rudeus "(And that smith's apron… damn. If steel melts in the forge, imagine what I'm melting right now.)"

    gunnar "Freya! This here is Rudeus, Paul's boy."
    gunnar "Smart, strong, magic prodigy, the whole package. You two are gonna be GREAT friends. I've decided."

    narrator "Freya's eyes flick up to you, then dart away instantly, her face going scarlet."

    freya "H-hi… I'm Freya… s-sorry about him, he's… loud."

    rudeus "Hi, Freya. Trust me — after Paul, loud is nothing new to me."

    narrator "That gets the tiniest smile out of her before she hides it behind her hand."

    gunnar "GWAHAHA! See?! Already getting along!"
    gunnar "Rudeus, come by whenever you like, y'hear? My door's always open for Paul's boy."
    narrator "Gunnar leans in, trying to lower his voice — which, for him, still sounds like a secret announced at the market."
    gunnar "…And Freya barely goes out. Girl needs a friend her own age. Do an old man a favor, eh?"

    show rudeus smirk_2 at left
    rudeus "(A friend. Right. I'll be the best friend she's ever had.)"
    rudeus "Leave it to me, Gunnar."

    narrator "Gunnar smacks your back hard enough to knock the air out of you. Freya just shakes her head, dying of embarrassment."

    $ freya_on = False
    $ smith_event = 1
    jump passar_tempo





label smith_ev_2:
    show rudeus normal at left with dissolve
    show gunnar at right with dissolve

    gunnar "AH! Paul's boy! Back already? GWAHAHA! Freya, look who it is!"
    show freya at center with dissolve
    narrator "Freya freezes mid-step with a bucket of water, going pink the second she sees you."

    freya "D-Dad, he probably has better things to do than—"
    gunnar "Nonsense! Come, come. Freya, don't just stand there like a fence post. Talk to the boy!"

    narrator "He shoves her forward with one huge finger. She stumbles a step closer to you, staring at her own boots."

    freya "H-hello again… Rudeus…"

    rudeus "Hey again, Freya. Good to see you."

    gunnar "She's a good girl, my Freya."
    gunnar "Strong back, wide hips — built for the forge, GWAHAHA! Swings a hammer better than most men I know!"

    show rudeus sem_graca at left
    freya "DAD!"
    narrator "Freya lets out a muffled little squeak and buries her face in her hands."

    rudeus "(He said 'wide hips' about his own daughter to a boy's face. This man is a national treasure.)"

    gunnar "What? I'm complimenting her!"
    gunnar "Rudeus, tell her — good hips, yes or no?"
    show rudeus smirk at left
    rudeus "(Do NOT answer that the way you want to, Rudy. Don't.)"
    rudeus "…She'll make an excellent blacksmith, sir."

    gunnar "HA! Diplomatic! Just like his father! I like this boy!"
    narrator "Gunnar stomps off to tend the fire, still chuckling to himself, utterly pleased."
    hide gunnar with dissolve

    narrator "Freya slowly lowers her hands. Her face is redder than forge coals."
    narrator "But then — just for a second — she peeks at you through her lashes with a look that is NOT nearly as innocent as her stammer."

    freya "…He's always like that. Please don't believe a word he says about me."
    freya "…Not that he even knows the half of it."

    show rudeus surpreso at left
    rudeus "(…Wait. What was THAT? Did shy little Freya just—)"
    rudeus "The half of what?"

    freya "N-NOTHING! Nothing! I— I have to fetch more water!"
    narrator "She bolts, ears burning, tripping over absolutely nothing on the way."
    hide freya with dissolve

    show rudeus smirk_2 at left
    rudeus "(Hmm… this girl is hiding something. And I want to find out what.)"

    $ freya_on = False
    $ smith_event = 2
    jump passar_tempo





label smith_ev_3:
    show rudeus normal at left with dissolve
    show freya at center with dissolve

    narrator "You find Freya alone at the anvil this time."
    narrator "Sweat beads on her collarbone, a smear of soot on one cheek. She's actually working — and she's good."

    rudeus "You really do this all day? Looks brutal."

    freya "I-it's not so bad once you get the rhythm."
    freya "You have to be… firm. And steady. And keep going even when your arm's begging you to stop."

    narrator "She demonstrates, hammering in slow, controlled strokes. There's a confidence in her hands the rest of her doesn't have yet."

    show rudeus smirk at left
    rudeus "Steady hands, huh."

    freya "Mhm. Dad says I've got the best grip he's ever trained."
    freya "I'm really good with my hands. I can work something soft into exactly the shape I want — and I never let go until it's finished."

    narrator "There's a beat of silence. Then Freya's own words seem to catch up with her. Her eyes go huge."

    freya "I— I MEANT METAL! Shaping METAL! Oh gods—"

    show rudeus extase at left
    rudeus "(There it is again. She doesn't even realize she's doing it. Or… does she?)"

    rudeus "Relax, Freya. I know exactly what you meant."
    rudeus "You're good with your hands. Noted."

    narrator "She hides behind the raised hammer, peeking over it, cheeks on fire — but not looking away this time."

    freya "…You're kind of a pervert, aren't you, Rudeus?"
    rudeus "Only when it's worth it."

    narrator "She bites her lip to fight a grin and goes back to hammering, sneaking glances at you the whole time."

    $ freya_on = False
    $ smith_event = 3
    jump passar_tempo





label smith_ev_4:
    show rudeus normal at left with dissolve
    show gunnar at right with dissolve

    gunnar "RUDEUS! My boy! Come, come, sit! Have a drink with an old man!"
    narrator "Gunnar drops onto a stump that groans under him and shoves a mug into your hand before you can refuse."

    gunnar "You know, it does my heart good seeing you and Freya thick as thieves. Girl's been happier this week than all year!"

    show rudeus normal at left
    rudeus "She's great company."

    gunnar "GREAT company! HA! And healthy, too!"
    gunnar "Look at her — good stock, that one. Strong. Hard-working. Wide in all the right places for—"
    show freya at center with dissolve
    narrator "From across the yard: 'DAAAAD.'"
    gunnar "—for CARRYING FIREWOOD! GWAHAHAHA!"

    show rudeus sem_graca at left
    rudeus "(He was NOT going to say firewood.)"

    gunnar "Speaking of which — do me a favor, eh?"
    gunnar "Girl's cooped up in this forge breathing coal smoke all day."
    gunnar "Take her out to the forest. Fresh air. Good hardwood grows past the creek — perfect for charcoal. Kills two birds!"

    show rudeus smirk_2 at left
    rudeus "(Send your beautiful daughter alone into the woods with me. To… gather wood. Sure, Gunnar. Anything for a friend.)"
    rudeus "I'd be happy to walk her out there. For the charcoal, of course."

    gunnar "GOOD LAD! See, THIS is why I trust Paul's boy. A gentleman!"
    narrator "He smacks your back. Beer sloshes everywhere."
    narrator "Across the yard, Freya freezes mid-step — panic and something warmer tangled together on her face."

    freya "D-Dad… alone… with him? In the forest? Just the two of us?"
    gunnar "Of course! It's Paul's boy! If I can't trust this lad, I can't trust anyone! GWAHAHA!"

    show rudeus smirk_2 at left
    rudeus "(The father himself handing over his daughter. Gunnar, you are a saint. Or a dangerously innocent man.)"

    scene black with fade
    narrator "You sling an axe over one shoulder, Freya grabs an empty basket, and the two of you head off down the path behind the forge."
    narrator "Gunnar's booming laugh and the ring of the anvil fade away behind you."

    scene bg floresta with fade
    show rudeus normal at my_left
    show freya at my_right
    with dissolve

    narrator "Soon it's just birdsong and golden light through the leaves. Freya walks beside you with the basket — but, unlike usual, she barely says a word."
    narrator "Her shoulder brushes yours every so often. She doesn't pull away. She also doesn't look at you."

    show rudeus normal at my_left
    rudeus "Freya… you okay? You're awfully quiet."

    narrator "She slows, hugs the basket to her chest, and chews her lip."

    freya "…You know, I've never done this before."
    rudeus "Gathered charcoal wood?"
    freya "No. I mean— I've never come out into the forest. Alone. With a boy."

    show rudeus smirk at my_left
    narrator "She says it fast, like she'd been holding it in the whole walk. Her cheeks are pink, but this time she looks right at you."

    freya "Nobody knows where we are. Nobody could hear us, even if… even if we did something."
    freya "…Is it bad that that's kind of… exciting?"

    show rudeus extase at my_left
    rudeus "(She's not as shy as she pretends… this is dangerous. In the best way possible.)"
    rudeus "Not bad at all. I think it's exciting too."

    narrator "Freya lets out a shaky little breath, thrilled and terrified in equal measure, and steps closer until the basket is the only thing between you."

    freya "Good. Because I keep having these… thoughts. About you. And they are NOT the kind a good girl's supposed to have."
    freya "…Then I remember I've never even touched anyone. And I get all shy again. Ugh, I'm a mess."

    rudeus "(Dirty thoughts… about me… and she's never touched anyone.)"
    rudeus "(My brain is already making a checklist of what to teach first.)"
    rudeus "(Calm down, Rudy. It's still just talk. For now.)"

    rudeus "You're not a mess. You're honest. I like honest."
    rudeus "And if you've got thoughts you want to get off your chest… I'm a very good listener."

    narrator "She giggles — a real, unguarded, slightly wicked little giggle — and for a second the shy mask is completely gone."

    freya "Maybe next time I'll tell you ALL of them."
    freya "…if you're nice to me."

    $ freya_on = False
    $ smith_event = 4
    jump passar_tempo





label smith_ev_5:
    show rudeus normal at left with dissolve
    show freya at center with dissolve

    narrator "You find Freya alone at the forge again — apron dirty, hammer idle, like she was waiting for you."
    rudeus "Freya. Want to grab more wood down by the creek?"
    freya "I-I… yes. Of course. Let me get the basket."

    scene black with fade
    narrator "You follow the trail behind the forge. The basket swings in her hand the whole way."
    narrator "The silence between you isn't like before — it's thick, warm, full of things neither of you has said out loud yet."

    scene bg floresta with fade
    show rudeus normal at my_left
    show freya at my_right
    with dissolve

    narrator "At the creek, far from her father and the forge, her nerves give way to a spark in her eyes."
    narrator "She sits on a mossy log and pats the free space beside her, inviting you. You sit close."

    show rudeus smirk at my_left
    rudeus "So… you promised to tell me those thoughts of yours."

    narrator "Freya squeaks and covers her face, but she's grinning behind her fingers."

    freya "I-I… I can't. It all gets stuck in my throat. It's too embarrassing…"
    rudeus "That's okay. Then I'll ask… and you just answer. Deal?"

    narrator "She nods, still hidden behind her hands."

    rudeus "Alright. First question…"
    rudeus "Have you ever kissed anyone?"

    freya "N-no. Never. Not once."
    rudeus "Ever wanted to?"
    freya "…All the time. Lately."
    freya "Every time I close my eyes… it's the same person."

    show rudeus smirk at my_left
    rudeus "And when you're alone at night… do you think about him?"

    freya "…Y-yes. Always."

    rudeus "Do you touch yourself thinking about him?"

    narrator "Freya makes a strangled little noise, crimson to the tips of her ears. She peeks at you between her fingers."

    freya "…Y-yes. A lot. I get all worked up and I don't even really know what I'm supposed to DO about it and it drives me crazy."

    show rudeus extase at my_left
    rudeus "(Honest. Hungry. Still so new to all of this…)"
    rudeus "You want someone to teach you?"

    freya "…Yes."
    freya "But I've never touched a man. Not like that. Never felt one. Held one. Anything."

    show rudeus smirk_2 at my_left
    rudeus "(She's trembling… and she still won't look away.)"
    rudeus "Then we start slow."
    rudeus "If you want… you can touch me. With your hands. Just that, for now. I'll guide you."

    narrator "Her eyes drop to your belt for a second — then snap back up, burning red."

    freya "W-with my… hands? On you?"
    rudeus "Only if you want to."
    freya "…I want to. Please."

    rudeus "You're sure? Because once you really touch me… I'm not going to want to stop easily."
    freya "I'm sure. Let me… feel you."

    narrator "Her calloused hands reach out, trembling — nervous and steady at the same time."

    scene black with fade

    narrator "You lie back on the moss. Freya hesitates a second — then climbs on top of you, thighs on either side of your waist, sitting in your lap."
    narrator "Her trembling hands open your belt. Breathing fast, half-nervous, half-frantic."
    narrator "Your cock springs free between your bodies and she freezes, eyes enormous."
    freya "O-oh. Oh gods. It's… so much bigger up close. And it's so HOT. And it's throbbing…"

    rudeus "Go on. You said you're good with your hands. Prove it."

    show vid_freya_handjob with fade

    narrator "She wraps that firm, practiced grip around the base and just holds it a second, feeling it pulse against her palm."
    narrator "Then she strokes — slow at first, watching your face like the hammer, reading every twitch."

    freya "Like this? I— oh… it throbbed. I felt it pulse. I did that?"

    rudeus "You did that. Tighter. Use both hands. No shyness now."

    narrator "Both hands. Long, greedy pulls, thumb dragging over the head, the same steady forge-rhythm she uses on soft iron."
    narrator "Sitting on top of you, her thighs squeeze you with every motion; her breath is shaky."
    narrator "She's soaked just from holding you — you can feel her hot, wet pussy rubbing against your thigh with every stroke."

    freya "It's so slick now… it's leaking all over my fingers… does that mean you like it?"

    rudeus "I love it. Fuck, Freya — your hands feel incredible. Faster."

    freya "Ahn— you're getting even harder, I can feel it."
    freya "…This hot, throbbing in my hand… I could do this all day."

    narrator "Wet sounds fill the clearing."
    narrator "Her strokes turn frantic. Her hips grind on your lap without even realizing, rubbing against you while her hands work."
    narrator "Eyes glassy, locked on the head of your cock every time it peeks through her fists."

    rudeus "I'm close— keep going— don't you dare stop—"
    rudeus "Freya— I'm gonna cum—"
    freya "Do it— do it— I want to see it— cum for me, please—!"

    call gozando from _call_gozando_32
    scene freya_handjob_cum with fade
    play sound "audio/cum.mp3"
    narrator "You erupt. Thick ropes paint her hands and wrists."
    narrator "Freya gasps like she just won something, pumping you through every pulse, milking every drop, staring at the mess she made like it's the hottest thing in the world."

    freya "I— I did that. Look. All over my hands… gods, that's so much…"

    scene bg floresta with fade
    show rudeus normal at my_left
    show freya at my_right
    with dissolve

    rudeus "That was… incredible."
    freya "Really?! …I mean— of course it was. I told you I'm good with my hands."
    narrator "She looks at the cum on her fingers, squeezes her thighs a little, and lets out a shaky little laugh — still breathless, still riding the high."
    freya "…We're… going to do this again, right? One of these days."
    rudeus "Whenever you want, Freya."
    narrator "She gives you a look that promises this was only the beginning — and for a second, the shy girl from the forge is completely gone."

    $ freya_on = False
    $ smith_hj_unlocked = True
    $ smith_event = 5
    jump passar_tempo





label smith_ev_6:
    show rudeus normal at left with dissolve
    show gunnar at right with dissolve

    gunnar "RUDEUS."
    narrator "You freeze in the middle of the village — chest cold, mind racing. He knows. He KNOWS. It's over. Your life is over—"

    gunnar "…There he is!"
    narrator "Gunnar smacks your back hard enough to nearly knock you down, and his laugh explodes a second later."
    gunnar "GWAHAHA! The best thing to happen to this family in years!"
    narrator "He seizes your hand and pumps it so hard your teeth click — while you try to remember how to breathe."

    gunnar "Freya came back from the woods GLOWING the other day!"
    gunnar "Cheeks all rosy, big smile, humming to herself! Whatever you two are getting up to out there, keep it up!"

    show rudeus sem_graca at left
    rudeus "(If you only knew EXACTLY what we got up to out there, Gunnar.)"
    rudeus "…We're just, uh. Working out. In the forest."

    gunnar "Working out! HA! Good for her!"
    gunnar "You know she sleeps like a baby now?"
    gunnar "Used to toss and turn all night — now she's out cold, satisfied, smiling in her sleep. A tired girl is a happy girl!"

    show freya at center with dissolve
    narrator "Behind him, Freya appears, her face going from normal to crimson in half a second."
    freya "DAD. Please. STOP. TALKING."

    rudeus "(He said 'satisfied.' He has no idea why.)"

    gunnar "What'd I say?! Bah, girls! Rudeus, you tell her — is there anything wrong with a healthy young woman getting her exercise, eh?"

    show rudeus smirk at left
    rudeus "Nothing at all, sir. I'm very committed to her… fitness."

    gunnar "GWAHAHAHA! 'Fitness!' See, Freya? Your friend GETS it!"
    hide gunnar with dissolve
    narrator "He wanders off delighted, still laughing to himself. Freya marches up to you, red as a forge coal."
    narrator "Then she jabs a finger into your chest — but she's fighting a grin the whole time."

    freya "You're ENJOYING this. You're LOVING watching me die, aren't you?"
    rudeus "I have never had more fun in my life."

    freya "…Meet me at the creek tomorrow."
    narrator "She leans in, mouth right by your ear, voice low enough that only you can hear."
    freya "I want to try something new. With my mouth this time."

    show rudeus extase at left
    rudeus "(With her… mouth. Her mouth? Okay… Breathe, Rudy. Don't cum just from imagining it.)"

    narrator "She spins on her heel and flounces off, leaving you standing there while her oblivious father whistles a work tune twenty feet away."
    hide freya with dissolve

    $ freya_on = False
    $ smith_event = 6
    jump passar_tempo





label smith_ev_7:

    scene bg floresta with fade
    show rudeus normal at my_left
    show freya at my_right
    with dissolve

    narrator "You reach the creek… and Freya is already there. Sitting on the log, restless legs, a look that swallows you before you even open your mouth."

    freya "You're late. I've been sitting here for TEN MINUTES thinking about what I want to do to you."
    rudeus "Ten minutes, huh… and you still waited. Cute."
    rudeus "Then stop killing me with curiosity and show me."

    scene black with fade

    narrator "She doesn't hesitate like last time. More confident now — she opens your pants."
    narrator "Then she wraps that firm grip around you, gives one slow stroke, and looks up with her lips already parted."
    freya "I thought about this every single night. What it'd feel like in my mouth. If it'd fit. If I'd be any good at it."

    rudeus "Then show me. Slow. Use your mouth — the way you've been imagining."

    narrator "She gets on all fours in front of you. You slide a hand into her hair and hold the back of her neck gently, guiding without forcing."
    narrator "She kisses the tip first — almost shy — then her tongue drags a hot, wet line up the underside and she takes the head into her mouth with a muffled little moan that vibrates straight through you."

    show vid_freya_blowjob with fade
    freya "Mmmph…"

    rudeus "That's it… good girl. Just like that."
    narrator "She moans around your cock, the muffled sound shivering through your skin."
    rudeus "Can you take it deeper?"
    freya "Mmm… mhm—"
    narrator "She agrees with a moan, without pulling off, and starts sinking lower."

    narrator "Inch by inch she swallows, drool on her chin, eyes locked on yours, reading every reaction."
    narrator "Her tongue moves underneath, licking, pressing. You feel her throat open hot and wet as your cock sinks deeper — squeezing around you, taking it."
    narrator "When you groan, she sucks harder — cheeks hollowing — and bobs faster, greedy for more of that sound."

    rudeus "There— fuck, just like that."

    narrator "She pulls off just enough to speak, a string of spit linking her lip to the tip of your cock, panting."
    freya "Am I doing it right?"
    rudeus "You're perfect—"
    narrator "You don't wait for her to finish catching her breath."
    narrator "Your hand on her nape pulls her head back onto your cock, sinking again into her hot, wet mouth."
    freya "Mmmph—!"

    narrator "On all fours, she moans and gives in. Your hand sets the rhythm; her mouth opens greedily for every thrust."
    narrator "Her tongue swirls over the head every time you pull back — and when you push in again, you feel her throat yield, hot, slick, closing around you."

    freya "(So thick on my tongue… I can feel him throbbing so hard.)"
    rudeus "God— Freya— I'm close—"
    freya "Mmm! Mmmhmm!"

    call gozando from _call_gozando_33
    scene freya_blowjob_cum with fade
    play sound "audio/cum.mp3"
    narrator "You cum down her throat. She takes all of it — eyes fluttering, throat working, swallowing every pulse — with your cock still deep in her mouth."
    narrator "When she finally pulls off, a string of spit and cum hangs from her lip. Breathless. Messy. Proud."

    freya "I… swallowed. All of it. G-gods… the taste is…"
    freya "…I didn't hate it. Not at all."

    scene bg floresta with fade
    show rudeus normal at my_left
    show freya at my_right
    with dissolve

    rudeus "That was… incredible, Freya. Seriously."
    freya "…I want more. I want everything. I want you to actually— you know. All the way."
    narrator "She wipes her mouth with the back of her hand, grinning, completely shameless now."
    freya "Next time… I don't just want my mouth. I want you. Inside."
    rudeus "(Fuck. This girl is going to kill me — and I'll thank her for it.)"

    $ freya_on = False
    $ smith_oral_unlocked = True
    $ smith_event = 7
    jump passar_tempo





label smith_ev_8:
    show rudeus normal at left with dissolve
    show gunnar at right with dissolve

    gunnar "RUDEUS! Come here, come here, I made you something!"
    narrator "Gunnar presses a beautiful hand-forged dagger into your palm — clearly hours of work, his best craftsmanship."

    gunnar "For you! A gift! Because let's be honest, boy…"
    narrator "He drapes a massive arm around your shoulders and lowers his voice to what he THINKS is a whisper, but is still loud enough to hear across the square."

    gunnar "…I've seen the way my Freya lights up around you. And I've seen the way you look at her. This old man isn't blind."

    show rudeus surpreso at left
    rudeus "(Oh no. Shit. Did he figure it out?)"

    gunnar "And I want you to know — you have my blessing."

    rudeus "Your… blessing?"

    gunnar "To COURT her, boy! Properly! GWAHAHA!"
    gunnar "You think I'd trust just anyone with my little girl? But Paul's son? A gentleman like you? I couldn't dream up a better match if I tried!"

    show rudeus sem_graca at left
    rudeus "(He wants me to court her. Properly. After everything we've already done in those woods…)"

    gunnar "Treat her right, eh? Be patient with her. She's… delicate. Innocent. Hasn't got a wicked bone in her body, my Freya."

    show freya at center with dissolve
    narrator "Behind the forge, you can just see Freya — who most certainly DOES have wicked bones, all of them — pretending to sweep while listening to every word, biting her lip to keep from laughing."

    rudeus "I promise I'll be exactly as gentle as she wants me to be, sir."

    gunnar "GOOD MAN!"
    narrator "He smacks your back hard enough to knock the air from your lungs."
    gunnar "Ah, grandkids! Strong grandkids! I can already see them running around the forge! GWAHAHAHA!"

    hide gunnar with dissolve
    narrator "He wanders off to daydream. Freya sidles up beside you, sweeping absolutely nothing — and failing to hide her smile."

    freya "…Delicate. Innocent. Not a wicked bone in her body."
    freya "My dad knows me so well, right?"
    rudeus "If he knew half of what we do in the forest, he'd drop dead on the spot."
    freya "That's why he's not going to know."

    freya "Meet me at the creek tomorrow."
    freya "I think it's time you found out just how wrong he is… for real."

    show rudeus extase at left
    rudeus "(You're dangerous, Freya. And I don't plan on walking away.)"

    $ freya_on = False
    $ smith_event = 8
    jump passar_tempo





label smith_ev_9:

    show rudeus normal at left with dissolve
    show freya at center with dissolve

    narrator "You barely reach the forge before Freya grabs your hand — no explanation, no looking back."
    freya "Come. Now. Before my dad shows up."

    scene black with fade
    narrator "She drags you down the path behind the forge — and the whole way she keeps giving you sidelong, filthy little looks, like she's already imagining what comes next."

    scene bg floresta with fade
    show rudeus normal at my_left
    show freya at my_right
    with dissolve

    freya "Today's the day, Rudeus. I want you to be my first. All the way."
    show rudeus smirk_2 at my_left
    rudeus "All the way… I've been waiting for you to ask for that."
    rudeus "You're sure you want to do this with me?"
    rudeus "There's no undoing this one, you know."

    freya "I've NEVER been more sure. Please. I NEED it. I need to know what it feels like to have you inside me."

    scene black with fade
    narrator "Her hands tremble a little on the ties of her dress — and even so she pulls, lets it fall, then the rest."
    narrator "Naked in front of you, cheeks burning, not backing down."
    freya "…Don't just stand there staring. Take me."

    narrator "She lies on her side in the grass. One leg lifts; you hold her thigh open, fitting in from behind and the side — chest against her back."
    narrator "The head of your cock slides against her slick little entrance. She guides it with her hand. You push in, inch by careful inch."
    rudeus "Fuck, Freya…"
    narrator "Impossibly tight. She gasps, clutching your arm as her body stretches around you."

    show vid_freya_vaginal with fade

    freya "Ahn— AHN— it's— you're splitting me open— don't stop— I can feel every bit of it going in—!"
    freya "It's so hard ohh… okay. Okay. Slow. Go slow. But don't you dare stop."

    rudeus "Fuck, Freya… you're so tight I can barely move."

    freya "You're INSIDE me. All of you. Oh gods— don't stop. Please, DON'T STOP—"

    narrator "You go slow at first."
    narrator "Your hand grips her thigh, keeping her leg open; her hips start pushing back against yours, chasing every thrust."
    narrator "Every time you bottom out she makes a broken little sound that goes straight to your gut."

    freya "So full— so deep— I can feel you throbbing inside my little pussy, Rudeus."

    narrator "The sound of skin slapping against skin echoes through the trees."
    narrator "All the shyness is gone now."
    narrator "You grip her hip hard and press her back into you with every thrust — deeper, deeper — and she just moans, begging for more."

    freya "Right there, RIGHT THERE— don't stop— I'm gonna— I'm gonna cum—!"
    rudeus "Cum on my cock. Let go. I've got you—"

    call gozando from _call_gozando_34

    narrator "She shatters — whole body seizing, pussy clenching in hot wet waves, crying out into the empty forest."
    narrator "Her grip milks you without mercy, dragging you straight to the edge — you can barely hold on."

    rudeus "I'm gonna—"
    freya "INSIDE. Inside me, all of it, I want to feel it, please—!"

    call gozando from _call_gozando_35
    scene freya_vaginal_cum with fade
    play sound "audio/cum.mp3"
    narrator "You bury yourself to the hilt and empty into her."
    narrator "Freya moans loud as the heat floods her, body trembling against yours, her pussy squeezing every last jet like she never wants to let a drop escape."

    scene black with fade
    narrator "You stay like that for a while — breathless, stuck together — until the world starts making sense again."
    narrator "Then, slowly, the clothes come back on: her dress, your belt, still-trembling fingers tying knots and buttons in the middle of the forest."

    scene bg floresta with fade
    show rudeus normal at my_left
    show freya at my_right
    with dissolve

    freya "…I'm shaking. My legs won't stop shaking. That was— why did we WAIT so long?"

    rudeus "You were worth the wait. My gorgeous, filthy little blacksmith."
    freya "Your blacksmith… I like that. Say it again later. Just… for me."

    $ freya_on = False
    $ smith_vaginal_unlocked = True
    $ smith_event = 9
    jump passar_tempo





label smith_ev_10:
    show rudeus normal at left with dissolve
    show gunnar at right with dissolve

    gunnar "RUDEUS! Come look at this! Freya forged this blade yesterday — best work she's EVER done! Girl's on FIRE lately!"
    narrator "He holds up a genuinely gorgeous sword, beaming with fatherly pride."

    gunnar "I don't know WHAT'S gotten into her, but ever since you two started spending time together, her craft's improved tenfold! She's focused! Energetic! Passionate!"

    show rudeus smirk at left
    rudeus "(Passionate… Yeah. Yesterday I was inside her. So.)"
    rudeus "She's very… inspired lately, sir."

    gunnar "INSPIRED! That's the word! Whatever you're doing for her, Rudeus, don't you ever stop! GWAHAHA!"

    show freya at center with dissolve
    narrator "Freya appears at your side and wraps around your arm, all sweet smiles for her father — clinging to you like it's the most innocent thing in the world."

    freya "Thanks, Dad. Rudeus is a very… motivating influence."
    gunnar "HA! Hear that? Go on, you two — go live a little! Don't let an old man keep you!"

    hide gunnar with dissolve
    narrator "He turns back to his anvil, whistling. The instant his back is turned, Freya's sweet smile curls into something a lot dirtier."

    freya "Okay. So. I've been thinking."
    freya "There's one thing we haven't done yet."
    rudeus "(…Oh. That tone. I know that tone.)"
    narrator "She steps close, mouth right at your ear, voice low and hot."
    freya "…I want to try it in my ass, Rudeus."
    freya "I touched myself last night… thinking about you. And I got curious about feeling your cock in my little hole."
    freya "I trust you. I want it to be with you."

    show rudeus extase at left
    rudeus "(She… touched herself… thinking about that. About her ASS. Fuck. This girl is a walking hazard.)"

    freya "Meet me in the forest tomorrow. At the creek. Don't be late."

    $ freya_on = False
    $ smith_event = 10
    jump passar_tempo





label smith_ev_11:

    scene bg floresta with fade
    show rudeus normal at my_left
    show freya at my_right
    with dissolve

    narrator "You reach the creek… and Freya is already waiting. That filthy look again — lip between her teeth, like she planned every second of this afternoon."
    rudeus "You're early."
    freya "I barely slept. I thought about this all night."
    freya "I may have… practiced. A little. By myself. Thinking about you."
    rudeus "Then let's go. Show me what you want."

    scene black with fade
    narrator "She gets on all fours in the grass, arching her back, offering herself with zero shyness left — ass up, thighs open, looking at you over her shoulder."
    narrator "You take your time opening her tight little hole with your fingers, wetting her, sinking in slowly — until she's moaning and pushing back against your hand."

    freya "Ahn— that feels so strange— strange but GOOD— more— I'm ready, I swear I'm ready, put it in—"

    narrator "You line the head of your cock against her tight ring and, inch by inch, sink into her hot little ass."
    narrator "Unbelievably tight — a ring that crushes the head of your cock — and she lets out a long, shuddering moan as she takes you all the way in."

    show vid_freya_anal with fade

    freya "OH— oh gods— it's so full— it's so much— keep going, keep GOING— I can take it— I want ALL of it—"
    rudeus "That's it— fuck, Freya… you feel unreal—"

    narrator "The inside of her ass squeezes around you — hot, tight velvet, pulling with every inch."
    narrator "You push slow at first, feeling her ring open and close around your cock, slick and insane."
    narrator "Once she adjusts, her whole demeanor changes."
    narrator "On all fours, she slams herself back onto you — ass smacking against your hips with every thrust, wet and greedy, begging for deeper."

    freya "I can feel every inch— every time you push in I see stars—"
    freya "Harder— don't hold back— I want to feel this cock in my ass for DAYS— every time I sit at the forge— AHN—!"
    rudeus "You dirty little thing— you take it so well— I'm not gonna last—"

    freya "Me neither— I'm gonna cum just from this— don't stop, don't STOP—!"

    call gozando from _call_gozando_36
    narrator "She cums. Whole body clamping down, thighs shaking, one hand rubbing her pussy hard — and her ass locks around your cock, milking you straight over the edge."

    rudeus "I'm cumming—"
    freya "INSIDE— fill me up— I want everything— AHN—!"

    call gozando from _call_gozando_37
    scene freya_anal_cum with fade
    play sound "audio/cum.mp3"
    narrator "You bury yourself deep and cum in her ass — pulse after pulse, filling that hot grip until it spills."
    narrator "Freya collapses forward into the grass, boneless and blissed-out, moaning softly as she feels the heat fill her up."

    scene bg floresta with fade
    show rudeus normal at my_left
    show freya at my_right
    with dissolve

    freya "…I can't feel my legs. I can't feel ANYTHING. That was perfect. YOU'RE perfect."
    rudeus "You gave me every single first you had, Freya. Handjob, mouth, pussy, ass — all mine."
    freya "All yours. I'm all yours. And I'm not even close to done with you."

    narrator "She rolls over in the grass, glowing, grinning up at you — the shy girl and the shameless menace of the woods, both at once."

    freya "So. Same time tomorrow? And the day after? And the day after that?"
    rudeus "Every day. Forever. …And your dad still thinks I'm the most gentlemanly boy in the village."
    freya "GWAHAHA!"
    rudeus "…Did you just do his laugh?"
    freya "Maybe."

    $ freya_on = False
    $ smith_anal_unlocked = True
    $ smith_event = 11
    jump passar_tempo





label smith_interact:

    show rudeus normal:
        xalign 0.2
    show freya:
        xalign 0.8
    with dissolve



    menu:
        "🤚 Handjob" if smith_hj_unlocked:
            jump smith_replay_hj
        "👄 Oral" if smith_oral_unlocked:
            jump smith_replay_oral
        "🍑 Vaginal" if smith_vaginal_unlocked:
            jump smith_replay_vaginal
        "🔥 Anal" if smith_anal_unlocked:
            jump smith_replay_anal
        "Return":

            hide rudeus
            hide freya
            with dissolve
            jump smith_forge_menu

label smith_replay_hj:
    scene black with fade
    narrator "You slip off into the forest. Within minutes she's in your lap, firm hands wrapped around your cock."
    show vid_freya_handjob with fade
    freya "I already know how you like it… so don't you dare hold back."
    rudeus "Faster— just like that—"
    freya "Ahn— it's throbbing in my hands— cum for me—"
    call gozando from _call_gozando_38
    scene freya_handjob_cum with fade
    play sound "audio/cum.mp3"
    narrator "You explode over her hands. Freya laughs softly, breathless, satisfied."
    $ freya_on = False
    jump passar_tempo


label smith_replay_oral:
    scene black with fade
    narrator "At the creek, she drops to all fours without hesitation. Your hand in her hair sets the rhythm."
    show vid_freya_blowjob with fade
    freya "Mmmph…"
    rudeus "Good girl— deeper—"
    freya "Mmm! Mmmhmm!"
    call gozando from _call_gozando_39
    scene freya_blowjob_cum with fade
    play sound "audio/cum.mp3"
    narrator "You cum down her throat. She swallows, wipes her lip, and grins with zero shame."
    $ freya_on = False
    jump passar_tempo


label smith_replay_vaginal:
    scene black with fade
    narrator "She lies on her side in the grass, leg open. You push in at once — she's already soaked."
    show vid_freya_vaginal with fade
    freya "Ahn— INSIDE— don't stop—"
    rudeus "Fuck, Freya— so tight—"
    freya "Cum in me— please—"
    call gozando from _call_gozando_40
    scene freya_vaginal_cum with fade
    play sound "audio/cum.mp3"
    narrator "You empty into her. Freya trembles against your arm, laughing out of breath."
    $ freya_on = False
    jump passar_tempo


label smith_replay_anal:
    scene black with fade
    narrator "On all fours again. You sink into her ass slowly — she pushes back, begging for more."
    show vid_freya_anal with fade
    freya "OH— so full— harder—"
    rudeus "You dirty little thing— I'm gonna—"
    freya "INSIDE— fill me—"
    call gozando from _call_gozando_41
    scene freya_anal_cum with fade
    play sound "audio/cum.mp3"
    narrator "You cum deep in her ass. Freya collapses into the moss, boneless and smiling."
    $ freya_on = False
    jump passar_tempo
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
