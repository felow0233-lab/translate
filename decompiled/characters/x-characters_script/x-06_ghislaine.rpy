default ghislaine = Character("Ghislaine", color="#c4a882")


default ghislaine_event = 0
default ghislaine_afeicao = 0

default ghislaine_talked_today = False
default ghislaine_gifted_today = False
default ghislaine_interacted_today = False

default ghislaine_intro = True

default ghislaine_breast_done = False
default ghislaine_handjob_done = False
default ghislaine_blowjob_done = False
default ghislaine_spread_done = False

default ghislaine_sex_index = 1

default ghislaine_tailjob_intro = True

label ghislaine_intro:


    show black with fade

    "Paul told me to meet someone today. An old companion from his adventuring days."
    "He called her a 'musclehead,' but said she was the strongest swordsman he'd ever fought alongside."
    "'She'll be Eris' bodyguard, but she could teach you a thing or two about the sword,' he said."
    "'Just... don't stare too much. And don't mention math around her. Trust me.'"

    "I wasn't sure what to expect. An old adventurer? Probably some grizzled veteran with—"
    hide black
    show ghislaine base_clothes at center
    with fade

    "...That was not what I expected."

    "A tall woman with dark skin, rippling muscles, and wild silver hair stood before me."
    "Cat-like ears twitched on top of her head, and a long tail swayed lazily behind her."
    "She wore... well, 'wore' is a generous word. Her outfit left very little to the imagination."
    "An eyepatch covered her left eye, and scars decorated her body like trophies."
    "She radiated an aura that screamed 'I could kill you before you blink.'"

    "She stared at me with a blank expression. No warmth. No hostility. Just... nothing."

    show rudeus normal at left with dissolve
    show ghislaine base_clothes:
        ease 0.5 xalign 1.0


    ghislaine "...You're Paul's son?"

    rudeus "Y-yes. I'm Rudeus Greyrat. Nice to meet you."

    ghislaine "..."

    "She looked me up and down like she was appraising a cut of meat."

    ghislaine "...You don't look like him."

    rudeus "I'll take that as a compliment."

    ghislaine "...It was."

    "A pause. The wind blew through the training grounds. Her tail flicked once."

    ghislaine "I'm Ghislaine. Ghislaine Dedoldia. Just Ghislaine is fine."
    ghislaine "No need for honorifics. I don't care about that stuff."

    rudeus "Alright. Ghislaine. My father said you'd be working here as Eris' bodyguard?"

    ghislaine "...Yes. I owe a debt to the Boreas family. I'll protect Eris with my life."
    ghislaine "Paul also said... you could teach me things."

    rudeus "Teach you? Like what?"

    ghislaine "...Reading. Writing. Math."

    "She said those words like someone confessing a crime."

    ghislaine "I can't do any of those. I've been tricked by merchants more times than I can count."
    ghislaine "...Which isn't saying much, since I can't count very well either."

    rudeus "You... want me to teach you?"

    ghislaine "...Is that a problem?"

    rudeus "No! Not at all. I'd be happy to."

    "For the first time, something shifted in her expression. Not quite a smile — more like the absence of a frown."

    ghislaine "...Good."
    ghislaine "In exchange, I can teach you the Sword God Style."
    ghislaine "Your father said your swordsmanship is... lacking."

    rudeus "He said 'lacking'?"

    ghislaine "...No. He said 'pathetic.' I was being polite."

    rudeus "..."

    "Well, at least she's honest."

    ghislaine "We start tomorrow. Don't be late."
    ghislaine "I don't like waiting. And I don't repeat instructions."

    hide ghislaine with dissolve
    show rudeus:
        ease 0.5 xalign 0.5

    "She turned around and walked away without another word."
    "Her tail swayed behind her — and for a brief moment, the tip curled upward."
    "Almost like she was... pleased?"

    "...This is going to be interesting."

    $ ghislaine_intro = False
    $ ghislaine_afeicao += 5
    $ renpy.notify("You met Ghislaine! +5 Affection")

    jump passar_tempo


label ghislaine_label:

    if ghislaine_intro:
        jump ghislaine_intro

    elif ghislaine_event == 0 and ghislaine_afeicao >= 30:
        jump ghislaine_event_1
    elif ghislaine_event == 1 and ghislaine_afeicao >= 80:
        jump ghislaine_event_2
    elif ghislaine_event == 2 and ghislaine_afeicao >= 140:
        jump ghislaine_event_3
    elif ghislaine_event == 3 and ghislaine_afeicao >= 200:
        jump ghislaine_event_4
    elif ghislaine_event == 4 and ghislaine_afeicao >= 260:
        jump ghislaine_event_5
    elif ghislaine_event == 5 and ghislaine_afeicao >= 340:
        jump ghislaine_event_6
    else:

        show rudeus normal at left
        show ghislaine base_clothes at right
        with dissolve

        python:
            if ghislaine_afeicao >= 200:
                greeting = renpy.random.choice([
        "Rudeus. ...Good. You're here.",
        "You came. I was... waiting. Don't make me say it twice.",
        "Hmph. Took you long enough..."
    ])
            elif ghislaine_afeicao >= 140:
                greeting = renpy.random.choice([
        "Rudeus. ...You smell different today. Did something happen?",
        "Oh. You're here. ...That's fine. I wasn't bored or anything.",
        "You came. ...Good. I had nothing better to do anyway."
    ])
            elif ghislaine_afeicao >= 100:
                greeting = renpy.random.choice([
        "Rudeus. You're here. ...Do you need something?",
        "Hmm. It's you. ...Alright, what is it?",
        "You came to see me? ...That's unusual. Not unwelcome, though."
    ])
            elif ghislaine_afeicao >= 50:
                greeting = renpy.random.choice([
        "Rudeus. ...What?",
        "You need something? ...Is it time for a lesson?",
        "...What is it? I was in the middle of training.",
        "Hmm. State your business."
    ])
            else:
                greeting = renpy.random.choice([
        "...What do you want?",
        "I'm busy. Be quick.",
        "State your business or leave.",
        "...Did Paul send you? If not, I have nothing to say."
    ])

        ghislaine "[greeting]"

        jump ghislaine_menu


label ghislaine_menu:
    menu:
        "😈 Flirt":

            python:
                if ghislaine_afeicao >= 200:
                    flirt_option = renpy.random.choice([
        ("Ghislaine... you're the most beautiful woman I've ever met.",
        "...I know you mean that. I can hear your heartbeat.",
        "...Mine does the same thing around you. That's all I'll say."),
        ("I can't stop thinking about you, Ghislaine.",
        "...That's inefficient. You should focus on your training.",
        "...But I think about you too. So I suppose we're both inefficient."),
        ("Being near you makes me feel safe... and something else entirely.",
        "...Something else?",
        "...I think I know what you mean. My tail won't stop moving when you're around.")
    ])
                elif ghislaine_afeicao >= 150:
                    flirt_option = renpy.random.choice([
        ("You know, Ghislaine, you're incredibly attractive.",
        "...I'm aware of my appearance. But hearing you say it is... different.",
        "Don't read too much into that."),
        ("Your eyes are really captivating, you know?",
        "...Even the one under the eyepatch?",
        "Hmph. You're strange, Rudeus. ...But I don't dislike it."),
        ("I love the way you move when you swing your sword.",
        "...That's swordsmanship, not something to 'love.'",
        "...But if you want to watch me train more, I won't stop you.")
    ])
                elif ghislaine_afeicao >= 100:
                    flirt_option = renpy.random.choice([
        ("Ghislaine, has anyone ever told you how gorgeous you are?",
        "...Paul used to say things like that. It didn't mean anything then either.",
        "...Though coming from you, it's less annoying."),
        ("That outfit really suits you.",
        "It's practical for combat. ...Are you staring?",
        "Focus on your studies, not on my clothes."),
        ("Your muscles are really impressive.",
        "...Of course they are. I trained for years.",
        "...Was that supposed to be flattery? It wasn't terrible.")
    ])
                elif ghislaine_afeicao >= 50:
                    flirt_option = renpy.random.choice([
        ("You're really pretty, Ghislaine.",
        "...I don't need compliments. Do you need something?",
        ""),
        ("Your tail is really cute when it moves like that.",
        "...My tail is not 'cute.' It's a natural reflex.",
        ""),
        ("You have a really nice smile, you know.",
        "...I wasn't smiling. That was just my face.",
        ""),
        ("I bet you'd look great in a dress.",
        "...A dress? I can't fight in a dress. Ridiculous.",
        "")
    ])
                else:
                    flirt_option = renpy.random.choice([
        ("Hey Ghislaine, you look beautiful.",
        "...Flattery won't make me go easier on you in training.",
        ""),
        ("I think you're really attractive.",
        "...So? What does that have to do with anything?",
        ""),
        ("You're stunning, you know that?",
        "...Focus on your sword stance, not on my appearance.",
        "")
    ])

            rudeus "[flirt_option[0]]"
            ghislaine "[flirt_option[1]]"
            if flirt_option[2]:
                ghislaine "[flirt_option[2]]"

            $ ghislaine_afeicao += 5
            $ renpy.notify("You gained +5 affection with Ghislaine!")
            jump passar_tempo
        "😏 Interact":



























































            menu:

                "Have sex with her" if ghislaine_event >= 6:
                    jump ghislaine_sex_repeatable







                "Touch her ears" if ghislaine_event >= 3:

                    scene bg eris_castle:
                        blur 5
                    show gh_headpat with dissolve

                    python:
                        if ghislaine_afeicao >= 300:
                            ear_response = renpy.random.choice([
        ("You reach out and gently stroke Ghislaine's ears.",
        "...Mmm. You know exactly where to touch.",
        "...Don't stop. That's... an order."),
        ("You scratch behind her ears softly.",
        "...Rrr...",
        "...If you tell anyone I made that sound, I'll kill you.")
    ])
                        elif ghislaine_afeicao >= 200:
                            ear_response = renpy.random.choice([
        ("You carefully reach for her ears.",
        "...You're getting bold.",
        "...Fine. But only because your hands are warm."),
        ("You gently pet her ears.",
        "...That feels... acceptable.",
        "...A little more to the left.")
    ])
                        else:
                            ear_response = renpy.random.choice([
        ("You slowly reach toward her ears.",
        "...What are you doing? Don't just—",
        "...Hmph. Fine. Just this once."),
        ("You touch the tip of her ear.",
        "...! Don't touch without asking.",
        "...It's sensitive there. Be more careful.")
    ])

                    "[ear_response[0]]"
                    ghislaine "[ear_response[1]]"
                    ghislaine "[ear_response[2]]"

                    $ ghislaine_afeicao += 5
                    $ renpy.notify("+5 Affection with Ghislaine!")
                    jump passar_tempo

                "Touch her butt" if ghislaine_event >= 2:

                    if ghislaine_afeicao < 100:
                        ghislaine "...We're not in the right place for that."
                        ghislaine "...Don't try that outside of a private room."
                        jump ghislaine_menu

                    if ghislaine_afeicao >= 200 and ghislaine_event >= 6:
                        scene bg eris_castle:
                            blur 5
                        show gh_showing_tail_naked_grab
                        with dissolve
                    else:

                        scene bg eris_castle:
                            blur 5
                        show gh_showing_tail_panties_grab
                        with dissolve

                    python:
                        if ghislaine_afeicao >= 200:
                            butt_response = renpy.random.choice([
        ("You run your hand along her tail, then let it slide down to her backside.",
        "...You always end up there, don't you?",
        "...I stopped minding a while ago. ...Don't tell anyone that."),
        ("You squeeze her butt firmly while stroking the base of her tail.",
        "...Ngh... Rudeus...",
        "...My tail curls on its own when you do that. You know what that means."),
        ("Your hand finds its way to her rear. You give it an appreciative squeeze.",
        "...You're getting bolder every time.",
        "...I don't dislike bold. Just don't do it in front of Eris.")
    ])
                        elif ghislaine_afeicao >= 150:
                            butt_response = renpy.random.choice([
        ("You brush your fingers along her tail, then let your hand rest on her backside.",
        "...! That's not the tail, Rudeus.",
        "...But I suppose you already knew that. ...Fine. Just this once."),
        ("You stroke her tail slowly, then give her butt a gentle squeeze.",
        "...Ngh. You— that wasn't part of the 'research.'",
        "...Though the muscle density there is... worth studying, I suppose."),
        ("Your hand traces the base of her tail down to the curve of her rear.",
        "...You're doing it again. The 'research' excuse won't work twice.",
        "...It won't work... but I'm not stopping you either.")
    ])
                        else:
                            butt_response = renpy.random.choice([
        ("You reach for her tail and let your hand drift to her backside.",
        "...! We talked about this. That's—",
        "...Hmph. You have exactly three seconds. Then I'm removing your hand myself."),
        ("You place your hand on her rear, pretending to check her 'muscle structure.'",
        "...'Research' again? You really think I'm that naive?",
        "...I'm not naive. I just... don't mind it from you. Don't read into that."),
        ("You give her backside a quick squeeze.",
        "...! R-Rudeus! At least warn me first!",
        "...My tail reacted before I could stop it. That's your fault.")
    ])

                    "[butt_response[0]]"
                    ghislaine "[butt_response[1]]"
                    ghislaine "[butt_response[2]]"

                    $ ghislaine_afeicao += 5
                    $ renpy.notify("+5 Affection with Ghislaine!")
                    jump passar_tempo

                "Spar with her" if ghislaine_afeicao >= 30:
                    python:
                        if ghislaine_afeicao >= 200:
                            spar_response = renpy.random.choice([
        ("You challenge Ghislaine to a sparring match.",
        "...Alright. But I won't hold back just because I like you.",
        "She defeats you effortlessly, then extends her hand to help you up.",
        "...Your stance is improving. ...And your determination is... attractive."),
        ("You draw your training sword.",
        "...Eager today. Good. Show me what you've got.",
        "She disarms you in three moves, but smiles faintly.",
        "...Not bad. For a mage.")
    ])
                        elif ghislaine_afeicao >= 150:
                            spar_response = renpy.random.choice([
        ("You ask Ghislaine to spar.",
        "...Fine. Take your stance.",
        "She knocks your sword away instantly.",
        "...Too slow. Again."),
        ("You raise your training sword.",
        "...Your grip is wrong. Here.",
        "She adjusts your hand, her fingers lingering for a moment.",
        "...There. Now try again.")
    ])
                        elif ghislaine_afeicao >= 100:
                            spar_response = renpy.random.choice([
        ("You ask for a sparring session.",
        "...If you insist. Don't blame me if you get hurt.",
        "She trips you in one move.",
        "...Pathetic. But at least you tried."),
        ("You take a fighting stance.",
        "...That stance is full of openings.",
        "She flicks your forehead instead of striking.",
        "...That's what happens in a real fight. Fix it.")
    ])
                        else:
                            spar_response = renpy.random.choice([
        ("You ask Ghislaine to train with you.",
        "...You? Spar with me? ...Fine. Hold your sword properly first.",
        "She knocks you down before you can even react.",
        "...You have a long way to go."),
        ("You challenge her to a match.",
        "...A match? Against me? That's not a match. That's a lesson.",
        "She disarms you immediately.",
        "...Come back when you can at least hold your ground for five seconds.")
    ])

                    "[spar_response[0]]"
                    ghislaine "[spar_response[1]]"
                    "[spar_response[2]]"
                    ghislaine "[spar_response[3]]"

                    $ ghislaine_afeicao += 5
                    $ renpy.notify("+5 Affection with Ghislaine!")
                    jump passar_tempo

                "Study together" if ghislaine_afeicao >= 0:
                    python:
                        if ghislaine_afeicao >= 150:
                            study_response = renpy.random.choice([
        ("You offer to teach Ghislaine more reading and math.",
        "...Yes. I want to learn.",
        "She sits close to you, closer than necessary.",
        "...Rudeus. I can read this word now. 'Love.' ...Is that what this is?"),
        ("You pull out a textbook.",
        "...Reading again? ...Alright.",
        "She leans against your shoulder as she reads.",
        "...Your voice is calming when you explain things. Don't stop.")
    ])
                        elif ghislaine_afeicao >= 100:
                            study_response = renpy.random.choice([
        ("You offer to continue her lessons.",
        "...Good. I keep confusing these letters.",
        "She focuses intensely, her tail swishing back and forth.",
        "...I got it right? ...Hmph. Of course I did."),
        ("You set up the study materials.",
        "...Math today? ...I'd rather fight a dragon.",
        "She struggles with the numbers but refuses to give up.",
        "...Don't laugh. I'll get it eventually.")
    ])
                        elif ghislaine_afeicao >= 50:
                            study_response = renpy.random.choice([
        ("You suggest studying together.",
        "...Fine. But explain it simply. I'm not good with complicated words.",
        "She tries to read the text and gets frustrated.",
        "...These letters all look the same to me."),
        ("You bring out a reading exercise.",
        "...'The... cat... sat...' This is humiliating.",
        "She clenches her fist but keeps trying.",
        "...Don't tell Eris about this.")
    ])
                        else:
                            study_response = renpy.random.choice([
        ("You offer to teach Ghislaine.",
        "...You'd teach me? ...Paul always said I was too dumb to learn.",
        "She sits down stiffly.",
        "...Fine. Show me."),
        ("You suggest a reading lesson.",
        "...Reading? I tried once. The letters don't make sense.",
        "She looks frustrated but sits down.",
        "...Alright. But go slow.")
    ])

                    "[study_response[0]]"
                    ghislaine "[study_response[1]]"
                    "[study_response[2]]"
                    ghislaine "[study_response[3]]"

                    $ ghislaine_afeicao += 5
                    $ ghislaine_interacted_today = True
                    $ renpy.notify("+5 Affection with Ghislaine!")
                    jump passar_tempo
                "Talk":

                    if ghislaine_talked_today:
                        ghislaine "...We already talked today. I need to train."
                        jump ghislaine_menu
                    else:
                        python:
                            if ghislaine_afeicao >= 200:
                                talk_options = [
        ("Tell me about your past.",
        "...I was feral as a child. Couldn't speak, couldn't think. Just fought.",
        "Master Gal found me and gave me a sword. That's when I became... me.",
        "Rudeus... you gave me something too. You gave me words. That means more than any sword."),
        ("What do you think about us?",
        "...'Us.' That word sounds strange coming from you.",
        "I'm a warrior. You're a mage. We shouldn't work together.",
        "...But we do. And I don't want it to stop."),
        ("Do you ever think about the future?",
        "Warriors don't plan for the future. We survive the present.",
        "...But lately, I've been imagining things. Quiet mornings. Someone beside me.",
        "...Don't make me say who.")
    ]
                            elif ghislaine_afeicao >= 150:
                                talk_options = [
        ("How's your training going?",
        "...Same as always. Swing the sword. Refine the form.",
        "...It's more interesting when you watch, though. I push harder.",
        ""),
        ("Tell me about the Sword God Style.",
        "One strike. One kill. That's the core of it.",
        "Speed over everything. Hesitation is death.",
        "...You'd be terrible at it. You think too much. That's not an insult."),
        ("Do you miss your adventuring days?",
        "...Sometimes. The freedom was nice.",
        "But Paul was reckless and made bad decisions. I don't miss that part.",
        "")
    ]
                            elif ghislaine_afeicao >= 100:
                                talk_options = [
        ("What do you do for fun?",
        "...Fun? I train. That is fun.",
        "...Sometimes I nap in the sun. Cats do that. Don't judge me.",
        ""),
        ("Can you teach me more sword techniques?",
        "...Your stance is still wrong. We'd have to start from basics.",
        "But you learn fast for a mage. I'll consider it.",
        ""),
        ("What's your favorite food?",
        "Meat. Preferably raw, but cooked is acceptable.",
        "...Why are you writing that down?",
        "")
    ]
                            elif ghislaine_afeicao >= 50:
                                talk_options = [
        ("How do you like living here?",
        "...It's quiet. I'm not used to quiet.",
        "But it's not bad.",
        ""),
        ("Tell me about the Beast Race.",
        "...We're stronger, faster, and have better senses than humans.",
        "That's all you need to know.",
        ""),
        ("How was your day?",
        "...I trained. I ate. Now you're here.",
        "That's my day.",
        "")
    ]
                            else:
                                talk_options = [
        ("How are you doing, Ghislaine?",
        "...Fine. Is that all?",
        "",
        ""),
        ("Nice weather today, huh?",
        "...I don't care about weather. It doesn't affect my sword.",
        "",
        ""),
        ("Want to hang out?",
        "...'Hang out'? What does that mean? Is it a human thing?",
        "...Sounds like a waste of time.",
        "")
    ]

                            talk_choice = renpy.random.choice(talk_options)

                        rudeus "[talk_choice[0]]"
                        ghislaine "[talk_choice[1]]"
                        if talk_choice[2]:
                            ghislaine "[talk_choice[2]]"
                        if talk_choice[3]:
                            ghislaine "[talk_choice[3]]"

                        $ ghislaine_afeicao += 5
                        $ ghislaine_talked_today = True
                        $ renpy.notify("You gained +5 affection with Ghislaine!")
                        jump passar_tempo
                "Nevermind":

                    jump ghislaine_menu
        "👋 Leave":


            python:
                if ghislaine_afeicao >= 260:
                    farewell = renpy.random.choice([
        "...Already? ...Come back soon. That's not a request.",
        "Leaving? ...Fine. But I'll be waiting. ...Don't keep me waiting long.",
        "...Rudeus. ...Be safe. That's all."
    ])
                elif ghislaine_afeicao >= 140:
                    farewell = renpy.random.choice([
        "...Leaving? ...Alright. See you tomorrow.",
        "Hmm. ...Go then. I have training to do anyway.",
        "...Goodbye. ...Don't get into trouble without me."
    ])
                elif ghislaine_afeicao >= 80:
                    farewell = renpy.random.choice([
        "...Alright. Goodbye then.",
        "Leaving? ...Fine. I was about to train anyway.",
        "...See you."
    ])
                elif ghislaine_afeicao >= 30:
                    farewell = renpy.random.choice([
        "...Goodbye.",
        "Hmm. Go then.",
        "...Right. See you."
    ])
                else:
                    farewell = renpy.random.choice([
        "...Finally. Go.",
        "Good. I have things to do.",
        "...Hmph."
    ])

            ghislaine "[farewell]"

            hide rudeus
            hide ghislaine
            with dissolve
            jump locais


label ghislaine_event_1:

    scene bg ghislaine_room
    with fade

    "Ghislaine showed up at my room today for another lesson."
    "She sat down at the desk across from me — no, not across. Right next to me."
    "Close enough that I could feel the warmth radiating from her body."

    show rudeus normal at my_left
    show ghislaine base_clothes at my_right
    with dissolve

    rudeus "Alright, let's continue where we left off. Can you read this sentence for me?"

    ghislaine "...'The... sw... sword... is... migh... mighti...'"

    rudeus "Mightier."

    ghislaine "'Mightier... than... the...' ...I don't know this word."

    rudeus "That's 'pen.' 'The sword is mightier than the pen.'"

    ghislaine "...That's a stupid saying. A pen can't cut anything."

    rudeus "It's a metaphor. It means words can be more powerful than—"

    ghislaine "Words don't cut people in half. Swords do. Whoever wrote this never fought anyone."

    "I couldn't exactly argue with her logic."

    "As she leaned over the book, her tail swayed behind her in slow, rhythmic movements."
    "It brushed against my leg every few seconds."

    rudeus "Uh, Ghislaine... your tail."

    ghislaine "...What about it?"

    rudeus "It keeps touching my leg."

    ghislaine "...It does that when I'm concentrating. Ignore it."

    "Ignore it. Right. Easy to say when a muscular cat-woman's tail is rubbing against your thigh."

    "She kept reading — slowly, painfully — but she never gave up."
    "Every time she got a word right, her ears would perk up just slightly."
    "And when she got one wrong, she'd growl under her breath like she was facing an enemy."

    ghislaine "...Rudeus."

    rudeus "Yeah?"

    ghislaine "...Thank you. For teaching me."
    ghislaine "No one ever had the patience before."

    rudeus "It's nothing, really."

    ghislaine "...It's not nothing to me."

    hide ghislaine with dissolve
    show rudeus:
        ease 0.5 xalign 0.5

    "She stood up and left without another word."
    "But her tail... it was curled upward again."

    $ ghislaine_event = 1
    $ ghislaine_afeicao += 5

    $ renpy.notify("Event complete! +5 Affection")
    jump passar_tempo


label ghislaine_event_2:

    scene bg ghislaine_room
    with fade

    "Another study session. Ghislaine had been making real progress."
    "She could read simple sentences now and even do basic addition."
    "Today, though, my mind was somewhere else."

    show rudeus normal at my_left
    show ghislaine base_clothes at my_right
    with dissolve

    "Her tail. It had been on my mind since last time."
    "The way it moved, the way it reacted to her emotions before her face ever did."
    "Among Beast Race, the tail was supposed to be something... intimate."

    rudeus "Hey, Ghislaine. Can I ask you something personal?"

    ghislaine "...What?"

    rudeus "Your tail. You mentioned before that touching it is... intimate for Beast Race."
    rudeus "What exactly does that mean?"

    "She stopped writing. Her ears flattened slightly."

    ghislaine "...Why do you want to know?"

    rudeus "Curiosity, I guess. You're the first Beast Race person I've spent this much time with."

    ghislaine "..."
    ghislaine "...Among my people, the tail is connected to our emotions. We can't control it."
    ghislaine "When we're happy, it rises. When we're nervous, it stiffens. When we're..."

    "She paused."

    ghislaine "...When we're aroused, it curls."
    ghislaine "That's why touching someone's tail without permission is... forward."

    rudeus "I see. So it's like an honest part of you that you can't hide."

    ghislaine "...Exactly. That's why I don't like people touching it."

    "A beat of silence."

    rudeus "Can I see it? Up close, I mean."

    ghislaine "..."

    "She stared at me for a long moment. Her expression was unreadable as always."
    "But her tail... it was swaying faster than usual."

    ghislaine "...Just looking?"

    rudeus "Just looking."



    "She hesitated for a moment, then slowly turned around, presenting her back to me."
    "Her hands move to her waist. She slips her thumbs under the fabric and pulls it down—exposing her butt completely."

    scene bg ghislaine_room:
        blur 5
    show gh_showing_tail_panties
    with dissolve

    "Her tail extended behind her — long, silver-furred, with a golden ring near the tip."
    "It was sleek and muscular at the base, tapering to something softer at the end."
    "The way it connected to her lower back, right above her rear... the view was incredible."

    rudeus "...Wow."

    "That slipped out before I could stop it. My brain short-circuited."

    ghislaine "...What? You said you wanted to see it."

    rudeus "I did! I just— it's really beautiful. The fur, the shape..."

    ghislaine "...Hmph. Are you done staring?"

    rudeus "Can I... touch it? Just once?"

    ghislaine "..."
    ghislaine "...Fine. But be gentle. The base is sensitive."

    "I reached out and carefully ran my fingers along the middle of her tail."
    "The fur was thick and warm — softer than I expected."

    ghislaine "...Ngh."

    "Her whole body tensed. Her ears stood straight up."
    "The tail twitched in my hand, curling slightly before she forced it still."

    rudeus "Are you okay?"

    ghislaine "...I said be gentle. That was... more than I expected."

    "She exhaled slowly, composing herself. But she didn't move away."
    "My eyes drifted downward, following the line of her tail to where it met her body."
    "Her glutes were... well. She was a Sword King for a reason."
    "Every muscle was sculpted like stone, perfectly defined under her dark skin."

    "The thought just came out."

    rudeus "Ghislaine... your lower body is really well-trained."
    rudeus "These muscles... you must do thousands of squats. Can I feel them?"

    ghislaine "...What?"

    rudeus "For research! I'm studying the Beast Race body. Your muscle structure is different from humans."
    rudeus "The way your tail connects to your glutes — it must give you incredible explosive power during sword strikes."

    "I delivered that with the straightest face I could manage."
    "Ghislaine turned her head to look at me over her shoulder."
    "Her expression was suspicious... but also genuinely curious."

    ghislaine "...You can tell that just from looking?"

    rudeus "I can theorize. But to confirm, I'd need to actually feel the muscle density."

    ghislaine "..."
    ghislaine "...Fine. But only because it's for study. Be quick about it."


    "She said it so matter-of-factly. Like she was agreeing to a sparring drill."

    show gh_showing_tail_panties_grab with dissolve

    "My hand moved from her tail to the curve of her backside."

    "...Hard. Ridiculously hard."
    "Not hard like tense — hard like her entire body was a weapon."
    "I could feel the layers of muscle under her skin, impossibly firm and dense."
    "This was the body of someone who had trained every single day for decades."

    rudeus "Incredible... the muscle fibers are completely different from a human's."

    "I was saying smart things. My hand was doing less smart things."
    "I squeezed — gently at first, then with more pressure, mapping the contour of her muscles."

    ghislaine "...Ngh."

    "Her tail shot straight up. Her ears twitched."

    ghislaine "...That's... thorough."

    rudeus "The gluteus connects directly to the tail's base. That's where your striking power comes from, isn't it?"

    ghislaine "...Y-yes. The tail gives balance. The hips provide force."
    ghislaine "...Are you finished with your 'research'?"

    rudeus "Almost..."

    ghislaine "...Rudeus."

    "Her voice had a warning edge. But her tail was curling."

    rudeus "Done! Thank you for the valuable data."

    scene bg ghislaine_room
    with fade
    show rudeus normal at my_left
    show ghislaine base_clothes at my_right
    with dissolve

    "She pulled her waistband back up and turned around."
    "Her face was the same stoic mask as always."
    "But her ears were bright red at the tips. And her tail wouldn't stop swaying."

    ghislaine "...Don't tell anyone about this. Especially the 'research' part."

    rudeus "My lips are sealed."

    ghislaine "...If Paul finds out, I'll know who talked."
    ghislaine "...Lesson's over for today."

    hide ghislaine with dissolve
    show rudeus:
        ease 0.5 xalign 0.5

    "She left quickly. Almost too quickly."
    "On her way out, she bumped into the doorframe."
    "Ghislaine Dedoldia, Sword King, S-rank adventurer... walked into a doorframe."

    "'Research.' I can't believe that worked."
    "...I think I broke her a little."

    $ ghislaine_event = 2
    $ ghislaine_afeicao += 5
    $ renpy.notify("Event complete! +5 Affection")
    jump passar_tempo


label ghislaine_event_3:

    scene bg eris_castle
    with fade

    "Ghislaine had been avoiding eye contact since the tail incident."
    "Not ignoring me — she still showed up for lessons and training."
    "But something had shifted. A tension that wasn't there before."
    "Today, she suggested we spar."

    show rudeus normal at left
    show ghislaine base_clothes at right
    with dissolve

    ghislaine "...Take your stance. No magic. Sword only."

    rudeus "Got it."

    "I raised my training sword. She didn't even bother with a stance."
    "She just stood there, relaxed, watching me with that single visible eye."

    rudeus "Aren't you going to—"

    show ghislaine:
        ease 0.5 xalign 0.5

    "Before I could finish, she closed the distance in a heartbeat."
    "I blocked — barely — but the force sent me stumbling backward."

    ghislaine "Too slow. Again."

    "We exchanged blows. Or rather, she struck and I desperately tried to survive."
    "My arms were getting tired. My footwork was sloppy."
    "She saw the opening and swept my legs out from under me."

    "I hit the ground hard. Before I could get up, she was on top of me."
    "One hand pinning my sword arm, one knee on either side of my torso."

    ghislaine "...Dead."

    "Her face was inches from mine. Sweat glistened on her dark skin."
    "Her chest was heaving from the exertion — which, given her outfit, was... distracting."
    "I could feel the heat of her body pressing down on me."

    rudeus "Y-you got me."

    ghislaine "...Your footwork collapsed. You leave your left side open when you're tired."

    "She hadn't moved. She was still on top of me, analyzing my mistakes like this was a perfectly normal position."

    rudeus "Ghislaine... you can get off me now."

    ghislaine "...I'm explaining your mistakes. Listen."

    "As I tried to shift my weight to get more comfortable, my hand slipped."
    "It landed on something firm and round."
    "...Her backside."

    "We both froze."

    ghislaine "..."

    rudeus "I— that was an accident, I swear—"

    ghislaine "..."

    "She stared at me. I expected to die."

    ghislaine "...Your hand."

    rudeus "R-right! Sorry!"

    "I tried to pull it away but she caught my wrist."

    ghislaine "...I didn't say remove it. I said your hand."
    ghislaine "...Your grip is too tense. Relax your fingers."

    rudeus "...What?"

    ghislaine "...When you hold a sword. Your grip. You hold it like you're holding on for your life."
    ghislaine "That's what I was going to say."

    "She released my wrist and stood up. I scrambled to my feet."
    "My heart was pounding so hard I was sure her Beast Race ears could hear it."

    ghislaine "...Training is over for today."

    rudeus "Ghislaine, about my hand—"

    ghislaine "Nothing happened. We were sparring. You fell. I corrected your grip."
    ghislaine "...That's all."

    hide ghislaine with dissolve
    show rudeus:
        ease 0.5 xalign 0.5

    "She walked away. Her tail was stiff as a board."
    "Among Beast Race, a stiff tail means nervousness."
    "Ghislaine Dedoldia... was nervous."

    "And she didn't kill me."
    "I'm going to consider that progress."

    $ ghislaine_event = 3
    $ ghislaine_afeicao += 5
    $ renpy.notify("Event complete! +5 Affection")
    jump passar_tempo


label ghislaine_event_4:




    "Ghislaine didn't show up for our lesson today."
    "Or yesterday."
    "Or the day before."

    "Three days without a word. No training, no study sessions, nothing."
    "Her room door was shut, and the maids said she'd asked not to be disturbed."

    "I was worried. Was she sick? Injured? Had I done something wrong?"
    "The incident during sparring kept replaying in my head."

    show rudeus normal at center
    with dissolve

    "I decided to ask around."
    show rudeus:
        ease 0.5 xalign 0.2
    show fox_maid at my_right with dissolve

    "One of the older Beast Race servants, an elderly woman with fox ears, gave me a knowing look when I asked."

    "Servant" "Oh, you don't know? It's her season, dear."

    rudeus "Season...?"

    "Servant" "Mating season. It happens to Beast Race folk a few times a year."
    "Servant" "The body gets... restless. Hot. Difficult to control."
    "Servant" "Lady Ghislaine is a proud warrior. She'd never let anyone see her in that state."
    "Servant" "So she locks herself away until it passes. Very disciplined of her."

    rudeus "How long does it last?"

    "Servant" "A week, sometimes more. Depends on the person."
    "Servant" "Best to leave her be, young master. Unless you want to lose an arm."

    hide fox_maid with dissolve

    "She chuckled and went back to her work."

    scene bg gh_hallway with fade
    show rudeus normal at center, slide_fade

    "I stood in the hallway outside Ghislaine's room."
    "The door was heavy oak. Sealed shut."
    "I could hear... nothing. The room was silent."

    "No — wait. If I listened carefully..."
    "...Breathing. Heavy, strained breathing."
    "And the occasional sound of claws scraping against wood."

    rudeus "..."

    "I should leave her alone. She chose to handle this herself."
    "She's a Sword King. She doesn't need my help."
    "She specifically asked not to be disturbed."

    scene black with fade

    "...I left a tray of food outside her door with a note."
    "A simple note, with simple words I knew she could read."

    "'I'm here if you need anything. — Rudeus'"

    "The next morning, the tray was empty."
    "The note was gone."

    "In its place was a single word scratched into the wood of the tray with a claw:"
    "'...Thanks.'"

    $ ghislaine_event = 4
    $ ghislaine_afeicao += 5
    $ renpy.notify("Event complete! +5 Affection")
    jump passar_tempo


label ghislaine_event_5:

    scene bg gh_hallway
    with fade

    "It happened again. Ghislaine vanished."
    "This time, I knew what it was. Mating season."
    "But something felt different. It had been four days, and the food trays were coming back barely touched."

    "I was worried. Last time she ate everything. This time..."

    "I stood outside her door again."

    show rudeus normal at center
    with dissolve

    rudeus "Ghislaine? Are you alright? You're not eating."

    "No answer."

    rudeus "Ghislaine?"

    "...A sound. Low, muffled. Like someone biting down on fabric."
    "Then a gasp. Strained. Almost pained."

    "My body moved before my brain could stop it."
    "I opened the door."

    scene bg ghislaine_room
    with fade

    "The room was dark. The curtains were drawn. The air was thick and hot."
    "And there was Ghislaine."

    scene bg ghislaine_room:
        blur 5
    show gh_masturbating with dissolve

    "She was on her bed. Her usual outfit was in disarray."
    "Her body was flushed, covered in a thin sheen of sweat."
    "Her tail was curled tightly — the sign she'd told me about."
    "One hand grasps her breast. The other moves rhythmically inside her pussy."

    "She noticed me."

    "Time stopped."

    hide gh_masturbating with dissolve

    show ghislaine base_scarf at my_right
    show rudeus normal at my_left
    with dissolve

    ghislaine "...!"
    ghislaine "R-Rudeus—! Get out!"

    rudeus "I-I'm sorry! I heard noises and I thought you were hurt—"

    ghislaine "I said GET OUT!"

    "Her voice cracked. Not with anger — with shame."
    "Ghislaine Dedoldia, the woman who faced armies without flinching, looked mortified."
    "Her ears were flat against her head. Her tail wrapped around her body like a shield."

    rudeus "I'm leaving! I'm sorry!"

    hide rudeus with dissolve
    show ghislaine:
        ease 0.5 xalign 0.5

    "I shut the door and pressed my back against it."
    "My heart was hammering."

    "...From the other side, I heard something I'd never heard from Ghislaine before."
    "A quiet, broken whisper."

    ghislaine "...Don't... think less of me."

    rudeus "I don't. I would never."

    ghislaine "..."
    ghislaine "...Leave the food. And go."

    rudeus "...Okay."

    scene black with fade

    "I left the tray and walked away."
    "My hands were shaking."
    "Not from fear."

    "Two days later, the season ended."
    "Ghislaine showed up for training like nothing happened."
    "She didn't mention it. I didn't mention it."
    "But she stood a little closer to me than before."

    "And when our hands brushed while passing the textbook..."
    "She didn't pull away."

    $ ghislaine_event = 5
    $ ghislaine_afeicao += 5
    $ renpy.notify("Event complete! +5 Affection")
    jump passar_tempo






















































































































































































































































































































































































































































































































































































































































































































































































































label ghislaine_event_6:

    scene bg gh_hallway
    with fade

    "The third time came."
    "Now I recognized the signs—the restlessness, the way her pupils dilate, her tail stiffening, and that strong, intense scent of heat that emanates from her."
    "It was impossible to miss: sweet, wet, and animalistic, the scent of her dripping folds filling the air even before she got close."
    "The day before she'd retreat to her room, she always trained harder. Like she was trying to exhaust herself."
    "It never worked."

    "This time, when she retreated, I left the tray as usual."
    "But I also left a note."

    "'You don't have to go through this alone.'"

    "One day passed."
    "Two days."

    "On the third night, a knock on my door woke me."

    show rudeus normal at center
    with dissolve

    "I opened it."
    show rudeus:
        ease 0.5 xalign 0.2
    with None
    show ghislaine base_clothes at my_right
    with dissolve

    "Ghislaine stood there."
    "She was wearing a loose robe — the first time I'd ever seen her in something that covered so much."
    "Her breathing was ragged. Her ears trembled. Her eye was glassy."
    "Her tail swayed behind her in tight, agitated circles."

    "She looked at me. No mask. No stoicism. Just raw, unfiltered need."

    ghislaine "...Rudeus."

    rudeus "Ghislaine? What—"

    ghislaine "...I read your note."
    ghislaine "...I read it twelve times. It took me that long because my hands wouldn't stop shaking."

    rudeus "..."

    ghislaine "...I'm not good with words. You know that."
    ghislaine "So I'll say it simply."

    show ghislaine:
        ease 1.0 xalign 0.65

    "She stepped closer. Close enough that I could feel the heat radiating from her skin."

    ghislaine "...I need you."
    ghislaine "...Not as a teacher. Not as a friend."
    ghislaine "...As a man."

    rudeus "Ghislaine..."

    ghislaine "...I tried to handle it alone. Every time, it gets worse."
    ghislaine "Last time, you saw me. Since then, I can't stop thinking about..."
    ghislaine "...About you seeing me like that."

    "Her hand found mine. Her grip was trembling — this woman who could shatter stone with her fists."

    ghislaine "...If you don't want this, say so now. I'll leave and we'll never speak of it."
    ghislaine "...But if you do..."

    "She didn't finish the sentence."
    "She didn't need to."

    rudeus "...Come in."

    "Her eye widened."

    ghislaine "...You're sure?"

    rudeus "I'm sure. I've been sure for a while."

    "Something broke behind her expression."
    "Not sadness — relief. Like a dam she'd been holding for months finally gave way."

    ghislaine "...Thank you."
    ghislaine "...Be warned. During the season, I'm... not gentle."

    rudeus "I can handle it."

    ghislaine "...We'll see."

    scene black with fade
    scene bg ghislaine_room
    with fade
    show rudeus normal at my_left
    show ghislaine base_clothes:
        xalign 0.65
    with dissolve

    "She stepped inside. The door closed behind her."
    "Her tail wrapped around my waist — instinctive, possessive."

    ghislaine "...Rudeus. One more thing."

    rudeus "What?"

    ghislaine "...If I scratch you... I'm sorry in advance."

    "She wasn't sorry at all. I could tell from the tail."

    "The room was dark, lit only by the faint moonlight bleeding through the curtains."
    "Ghislaine stood before me, her chest rising and falling with labored breaths."
    "The loose robe she wore clung to her sweat-dampened skin."

    "Her eye found mine. No mask. No composure. Just her."

    show ghislaine base with dissolve

    "Without a word, she untied the sash of the robe."
    "It slid off her shoulders and pooled at her feet."
    "Underneath, she wore nothing."

    "I'd seen her body before — the muscles, the scars, the dark skin."
    "But never like this. Never so bare. Never so vulnerable."
    "Her tail hung low, trembling, curling and uncurling in restless spirals."
    "Her ears were pressed flat — not from anger, but surrender."

    scene black with fade

    "She walked to the bed."
    "I expected her to sit. To hesitate. To show even a shred of the composure she wore like armor."
    "She didn't."

    "She lay on her back, spread her legs wide, and opened herself to me with her own fingers."

    scene bg ghislaine_room:
        blur 5
    show gh_spreading
    with dissolve

    "No shame. No hesitation. Just raw, animal need."
    "Her folds glistened — swollen, dripping, twitching with every ragged breath she took."
    "Her thighs trembled as she held herself open, the muscles in her abdomen flexing with the effort."
    "Her tail thrashed against the sheets, completely beyond her control."

    "She looked up at me with her single visible eye — half-lidded, glassy, burning with something feral."
    "The Sword King was gone. What stared back at me was a beast in heat, offering herself completely."

    ghislaine "...Look at me, Rudeus. All of me."
    ghislaine "...This is what you do to me. Every... single... time."
    ghislaine "...So don't make me wait. I can't... hold back much longer."

    "My throat went dry. My body moved on its own."
    "This was Ghislaine Dedoldia. The woman who could kill a man before he blinked."
    "And she was lying on my bed, legs spread, fingers parting her wet flesh, begging me with her eye."
    "The most powerful woman I'd ever known — reduced to this. Because of me."

    scene black with fade

    "I climbed onto the bed behind her."
    "I leaned down and kissed her — hard, deep."

    "She froze."
    "For a heartbeat, she didn't respond — as if she didn't know what to do."
    "Then something clicked, and she kissed me back."
    "Hard. Hungry. Clumsy."

    "She kissed like she fought — all instinct, no technique, overwhelming force."
    "Her hand grabbed the back of my head and pulled me deeper."
    "A low growl vibrated in her throat, something primal and involuntary."

    "When we broke apart, a thin thread of saliva connected our lips."
    "Her eye was hazy. Unfocused. Her composure was gone."

    ghislaine "...More. I need... more."

    "She didn't wait for me to respond."
    "With one fluid motion, she turned over and positioned herself on all fours."
    "Her back arched, her hips raised high, her tail lifting and curling in that tight spiral she'd told me about."
    "She looked back at me over her shoulder."

    ghislaine "...From behind. It's... easier for me like this."
    ghislaine "...And grab my hips. Don't be gentle."

    "I placed my hands on her hips."
    "Her skin was burning hot, slick with sweat."
    "The muscles beneath my fingers were steel wrapped in silk."
    "I gripped harder, and she made a sound — something between a purr and a growl."

    show vid_gh_sex_1 with fade
    play sound "LEWD/GH_MOAN_10.wav" loop fadein 1.0

    "When I entered her, the sound she made wasn't a moan."
    "It was a gasp — sharp, broken, like she'd been holding her breath for days."

    ghislaine "...Ngh—!"

    "She was tight. Incredibly tight."
    "But she was so wet that I slid inside in one smooth stroke — all the way to the hilt."
    "The heat hit me first. Searing, pulsing, alive — like her body was trying to melt me from the inside."
    "Her walls clenched around me, slick and swollen, squeezing in rhythmic waves I could feel down to my spine."
    "Every inch of her was drenched. Hot. Desperate."
    "The sensation was overwhelming — tight enough to make my vision blur, wet enough to make every movement effortless."
    "I could feel her pulse through her walls, fast and frantic, hammering against me like a second heartbeat."

    "Her body gripped me like it was afraid I'd disappear."
    "Her back arched deeper, muscles rippling beneath her dark skin."
    "A broken moan tore from her throat — raw, involuntary, the sound of someone who'd been starving."

    "I couldn't believe it. This woman — this warrior — was shaking beneath me."
    "Her claws dug into the sheets, tearing the fabric."
    "Her tail tightened around my forearm like a vice, pulling me closer, deeper."

    rudeus "Ghislaine... are you okay?"

    ghislaine "...Don't stop. Whatever you do... don't... stop."

    "I moved. Slowly at first."
    "Every thrust drew a sound from her — low, guttural, barely controlled."
    "She bit her lip hard enough to draw blood, trying to keep quiet."

    rudeus "You don't have to hold back. It's just us."

    ghislaine "...If I stop holding back... I'll break you."

    rudeus "Try me."

    "Something shifted in her eye. A flash of something wild."

    ghislaine "...You asked for it."

    "This time, she didn't hold back."
    "Her voice came out raw and unfiltered — moans she'd been suppressing for years."
    "The proud, stoic warrior was gone."
    "In her place was a woman consumed by need, trembling under my hands."

    "My hands explored her back — the ridges of scars, the valleys of muscle."
    "I squeezed her backside and she jerked forward with a sharp gasp."

    ghislaine "...There... yes... harder..."

    "I couldn't believe this was real."
    "Ghislaine Dedoldia, moaning my name, pressing back against me."
    "Every sound she made was honest. Unfiltered."
    "Just like her tail. She couldn't hide what she felt, and right now, she felt everything."

    "She buried her face in the pillow, her moans muffled but still loud enough to make my pulse race."
    "Her hips pushed back to meet every thrust, matching my rhythm with a warrior's precision."

    "Her breathing grew faster. Her grip on the sheets tightened."
    "Her tail thrashed wildly, completely out of control."

    ghislaine "...Rudeus... I'm... close..."

    rudeus "Me too."

    "She turned her head to look at me over her shoulder."
    "Her eye was wet. Not from sadness — from something rawer, something she'd never let anyone see."

    ghislaine "...Inside. Don't pull out."
    ghislaine "...It's the season. My body needs... I need..."
    ghislaine "...Please."

    "That word. 'Please.'"
    "I'd never heard Ghislaine say 'please' before. Not once. Not ever."
    "That single word undid me more than anything else."

    "I gripped her hips tighter. She pushed back harder."
    "Her whole body tensed — every muscle, every scar, every inch of her — and she came apart."

    ghislaine "...Ah— Rudeus—!"

    call gozando from _call_gozando_31
    scene bg ghislaine_room:
        blur 5
    show gh_sex_cum
    with fade

    play sound "cum.mp3"

    "Her back arched violently. Her claws shredded the sheets beneath her."
    "Her tail coiled around my arm as her body shuddered, clenching around me in waves."
    "I followed her over the edge, and for a moment, the world went white."

    scene black with fade

    "Her arms gave out first."
    "She collapsed onto the bed, face-down, hips still raised, trembling."
    "Slowly, her legs slid apart and she sank fully into the mattress."

    "I pulled out gently. She whimpered — a sound I never thought I'd hear from a Sword King."

    "She rolled onto her back, boneless, chest heaving."
    "Her legs fell open — not deliberately, not like before."
    "She didn't have the strength to close them."

    scene bg ghislaine_room:
        blur 5
    show gh_spreading_cum
    with dissolve

    "My seed spilled out of her slowly — a thick, white trail leaking from her swollen folds, pooling on the sheets beneath her."
    "Her inner thighs glistened, slick with the mix of both of us."
    "She was still twitching. Small, involuntary spasms that rippled through her abdomen every few seconds."
    "Her tail lay limp on the bed, the tip flicking weakly — the only part of her still moving on its own."

    "Her face was... something I'd never seen."
    "Her eye was half-rolled back, unfocused, staring at the ceiling without seeing it."
    "Her mouth hung open, each breath coming out as a shallow, broken pant."
    "A thin line of drool trailed from the corner of her lips."
    "The stoic mask, the warrior's composure — all of it was gone. Completely, utterly gone."

    "She looked... shattered. In the best possible way."

    "Her body shuddered again — an aftershock — and a soft, whimpering moan escaped her throat."
    "Her fingers clawed weakly at the sheets, grasping at nothing."

    ghislaine "...hah... hah..."

    "She tried to say something. Her lips moved, but no words came out."
    "Just breath. Just heat."

    "Another tremor ran through her. Her hips bucked once, involuntarily, and more of my warmth leaked out of her."
    "Her tail curled — just barely — then went limp again."

    ghislaine "...full..."
    ghislaine "...so... full..."

    "That was all she managed. Two words. Whispered like a prayer."
    "The Sword King, reduced to trembling flesh, overflowing with me, unable to form a sentence."

    "I watched her for a long moment. The rise and fall of her chest. The way her muscles kept twitching."
    "Slowly — very slowly — her eye drifted back into focus."
    "She blinked once. Twice. Like she was remembering where she was. Who she was."
    "Her gaze found me, and for a fleeting second, something raw and vulnerable flickered across her face."

    ghislaine "...Don't... look at me like that."

    rudeus "Like what?"

    ghislaine "...Like you're proud of yourself."

    rudeus "...I am."

    ghislaine "..."

    scene black with fade

    "She didn't argue. She couldn't. Her body was still betraying her — another small spasm, another quiet gasp."

    "She lay there, open, dripping, trembling — and made no move to cover herself."






    scene bg ghislaine_room
    with fade
    show rudeus naked at my_left
    show ghislaine base:
        xalign 0.65
    with dissolve

    "We lay there in silence."
    "Her head rested on my chest. Her tail lay draped across my legs, completely limp."
    "Her ears twitched occasionally, the only sign she was still awake."

    "The feral energy was gone. In its place was something I'd never seen from Ghislaine."
    "Calm. Real, genuine calm."

    "I ran my fingers through her silver hair. She made a low rumbling sound."

    rudeus "...Was that a purr?"

    ghislaine "...No."

    rudeus "That was definitely a purr."

    ghislaine "...Sword Kings don't purr."

    rudeus "This one does."

    ghislaine "...Shut up."

    "A pause. Her claws traced idle patterns on my chest."

    ghislaine "...Rudeus."

    rudeus "Yeah?"

    ghislaine "...I scratched your back."

    rudeus "I noticed."

    ghislaine "...Sorry."

    rudeus "You warned me. I said I could handle it."

    ghislaine "...You handled it well. For a mage."

    "Was that... a compliment? A joke? Both?"

    "Another silence. Longer this time."

    ghislaine "...I've never done this before."

    rudeus "Wait... never? But Paul—"

    ghislaine "Paul was during mating season too. But that was... different."
    ghislaine "That was just bodies. Instinct. He didn't..."

    "She paused, searching for a word she might not know."

    ghislaine "...He didn't stay after."

    "The weight of that sentence hit me harder than any of her sword strikes."

    rudeus "I'm not going anywhere."

    ghislaine "..."
    ghislaine "...I know. That's why I came to you and not..."
    ghislaine "...You taught me to read. You taught me to count. You left me food when I was weak."
    ghislaine "...No one has ever done those things for me."

    rudeus "Ghislaine..."

    ghislaine "...I'm not good with words. You know that."
    ghislaine "But I think what I feel is what that word means. The one I learned last week."

    rudeus "Which word?"

    ghislaine "...'Love.' That one."

    "She said it like she was reading it from a textbook."
    "Flat. Uncertain. Like she wasn't sure she was pronouncing it correctly."
    "And somehow, that made it the most genuine confession I'd ever heard."

    rudeus "...I love you too, Ghislaine."

    ghislaine "..."
    ghislaine "...Good. Then stay."

    "Her tail curled around my leg."
    "Her ear twitched against my chest."
    "And the rumbling started again."

    rudeus "You're purring again."

    ghislaine "...I will end you."

    "She didn't move an inch."

    scene black with fade

    "We fell asleep like that."
    "The Sword King and the mage."
    "Her claws on my chest. My hand in her hair."

    "For the first time in her life, Ghislaine didn't face the season alone."
    "And for the first time in mine, I understood what it meant to be truly needed."

    $ ghislaine_event = 6
    $ ghislaine_afeicao += 25
    $ renpy.notify("Your bond with Ghislaine has deepened. +25 Affection")

    jump passar_tempo






label ghislaine_sex_repeatable:

    if ghislaine_sex_index == 1:
        $ ghislaine_sex_scene = "night_visit"
    elif ghislaine_sex_index == 2:
        $ ghislaine_sex_scene = "after_training"
    else:
        $ ghislaine_sex_scene = "study_break"

    $ ghislaine_sex_index = (ghislaine_sex_index % 3) + 1




    if ghislaine_sex_scene == "night_visit":

        scene black with fade

        "Late at night, a familiar knock on my door."
        "I didn't even need to ask who it was."

        scene bg ghislaine_room with fade

        show rudeus normal at my_left
        show ghislaine base_clothes at my_right
        with dissolve

        "Ghislaine stood in the doorway, wearing that loose robe again."
        "Her tail swayed in slow, deliberate circles."
        "I knew what that meant by now."

        ghislaine "...Are you busy?"

        rudeus "For you? Never."

        ghislaine "...Good."

        "She stepped inside and closed the door behind her."

        show ghislaine base with dissolve

        "The robe hit the floor before I could say another word."

        ghislaine "...I wasn't going to come tonight. I told myself I didn't need to."
        ghislaine "...I lasted two hours."

        rudeus "A new record."

        ghislaine "...Shut up and take your clothes off."

        scene black with fade

        "She didn't wait."
        "She turned around and climbed onto the bed on all fours."
        "Her back arched, her hips raised, her tail lifting high."
        "She looked at me over her shoulder with that burning, impatient eye."

        ghislaine "...Hurry up. I need you now."

        "I didn't need to be told twice."

        show vid_gh_sex_1 with fade
        play sound "LEWD/GH_MOAN_10.wav" loop fadein 1.0

        "I gripped her hips and entered her from behind."
        "She was already dripping — her body had been ready long before she knocked on my door."

        ghislaine "...Ngh— yes..."

        "She set the pace by pushing back against me — controlled at first, then faster."
        "Every roll of her hips drew a low rumble from her chest."
        "But as the minutes passed, the control slipped."
        "Her breathing grew ragged. Her claws dug into the mattress."
        "Her tail coiled around my arm so tight it almost hurt."

        ghislaine "...Harder... Rudeus..."

        "Her moans echoed in the dark room."
        "Raw, desperate, unashamed."
        "She pressed her face into the pillow, muffling herself — then gave up and let the sounds out."

        ghislaine "...Close... I'm close..."

        "Her body tensed. Her walls clenched around me in pulsing waves."
        "She came with a shuddering gasp, her whole body trembling."
        "I followed moments later, gripping her hips tight as I finished inside her."

        stop sound fadeout 1.0

        scene bg ghislaine_room with fade
        show rudeus naked at my_left
        show ghislaine base at my_right
        with dissolve

        "She collapsed forward onto the bed, boneless."
        "I lay beside her. She rolled over and rested her head on my chest."
        "A low rumbling sound started in her throat."

        rudeus "You're purring."

        ghislaine "...I'll kill you tomorrow. Too tired now."

        "Her tail went limp across my legs."
        "Within a minute, she was asleep."

        "The Sword King uses me as a mattress. I don't mind."




    elif ghislaine_sex_scene == "after_training":

        scene bg eris_castle
        with fade

        "We had just finished sparring."
        "I was drenched in sweat. Ghislaine looked like she'd barely moved."
        "But there was something in her eye — a restlessness that had nothing to do with swordplay."

        show rudeus normal at my_left
        show ghislaine base_clothes at my_right
        with dissolve

        ghislaine "...You're getting better."

        rudeus "Thanks. I almost lasted ten seconds this time."

        ghislaine "...Twelve. I counted."

        "A pause. She looked around the training grounds. Empty. Everyone had gone inside."

        ghislaine "...Come with me. Now."

        rudeus "To...?"

        ghislaine "...My room. Don't ask questions."

        scene bg ghislaine_room
        with fade
        show rudeus normal at my_left
        show ghislaine base_clothes at my_right
        with dissolve

        "She pulled me into her room and shut the door."
        "Before I could speak, she was on me — her mouth against my neck, her hands pulling at my clothes."

        ghislaine "...Training makes me restless. You know that."

        rudeus "I'm starting to figure that out, yeah."

        ghislaine "...Less talking."

        scene black with fade

        "She stripped in seconds — efficient, no ceremony."
        "Then she climbed onto the bed and positioned herself on all fours, looking back at me."

        ghislaine "...What are you waiting for? Get over here."

        "Still damp from sparring, her dark skin glistened."
        "The muscles in her back and thighs flexed as she arched herself, presenting."
        "Her tail lifted high, curling in that tight spiral that meant she was beyond ready."

        show vid_gh_sex_1 with fade
        play sound "LEWD/GH_MOAN_10.wav" loop fadein 1.0

        "I entered her hard. No buildup. She didn't want it."
        "She wanted force, and she told me so."

        ghislaine "...Harder. I'm not fragile."

        "I knew that. But hearing her say it still sent a jolt through me."

        "She was louder than usual — the training had stripped away whatever restraint she normally held."
        "Her moans were sharp, rough, punctuated by growls."
        "Her claws tore into the sheets with every thrust."
        "Her tail wrapped around my thigh, pulling me deeper."

        ghislaine "...Yes— right there— don't stop—"

        "When she came, she bit down on her own forearm to muffle the sound."
        "Her body clamped down on me, and I couldn't hold back either."
        "I buried myself deep and let go."

        stop sound fadeout 1.0

        scene bg ghislaine_room
        with fade
        show rudeus naked at my_left
        show ghislaine base at my_right
        with dissolve

        "Afterward, she lay face-down on the bed, catching her breath."
        "Then she pushed herself up like nothing happened."

        ghislaine "...We need to wash these sheets before anyone sees."

        rudeus "You literally shredded them."

        ghislaine "...Your fault."

        rudeus "How is that my fault?"

        ghislaine "...You exist. That's how."

        "She kissed me once — short, firm — and started getting dressed."




    elif ghislaine_sex_scene == "study_break":

        scene bg ghislaine_room
        with fade

        "We were in the middle of a reading lesson."
        "Ghislaine had been doing well — she'd made it through an entire paragraph without stopping."
        "But she'd been distracted for the last ten minutes."
        "Her tail kept brushing against my arm. Her eye kept drifting from the book to me."

        show rudeus normal at my_left
        show ghislaine base_clothes at my_right
        with dissolve

        rudeus "Ghislaine, you've read the same line three times."

        ghislaine "...The words are blurry."

        rudeus "The words are fine. You're not looking at them."

        ghislaine "..."

        "She closed the book."

        ghislaine "...I can't concentrate."

        rudeus "Should we take a break?"

        ghislaine "...Yes. A specific kind of break."

        show rudeus:
            ease 0.5 xalign 0.35

        "She grabbed my shirt and pulled me toward her."
        "The book fell to the floor."

        rudeus "The textbook—"

        ghislaine "...I'll buy you a new one."

        scene black with fade

        "She stood up and undressed — calmly, deliberately."
        "Then she climbed onto the bed and lowered herself onto all fours."
        "But slowly. Gently. Different from the other times."
        "She rested on her elbows, her back in a soft arch, her tail swaying lazily."
        "She looked back at me. Not with urgency — with warmth."

        ghislaine "...Come here. Slowly this time."
        ghislaine "...I want to feel all of it."

        show vid_gh_sex_1 with fade
        play sound "LEWD/GH_MOAN_10.wav" loop fadein 1.0

        "I undressed and moved behind her."
        "This time, I entered her slowly. Inch by inch."
        "She let out a long, trembling exhale."

        ghislaine "...Mmm..."

        "We moved slowly this time. No urgency, no frenzy."
        "Just the two of us, tangled together in the afternoon light."
        "Her sounds were quieter here — soft gasps, whispered fragments of my name."

        ghislaine "...Ru...deus..."

        "My hands ran along her back, tracing the scars, the muscles, the curve of her spine."
        "She shivered under my touch."

        ghislaine "...This is better than reading."

        rudeus "Don't tell your teacher that."

        ghislaine "...My teacher is busy right now."

        "We took our time. Long, deep strokes that made her voice hitch with every one."
        "When we finished, it was quiet. Gentle. She trembled once, then went still."

        stop sound fadeout 1.0

        scene bg ghislaine_room with fade
        show rudeus normal at my_left
        show ghislaine base_clothes at my_right
        with dissolve

        "She picked the book up off the floor and sat back down at the desk."

        ghislaine "...Page forty-three. Where were we?"

        rudeus "You can't be serious."

        ghislaine "...I came here to learn. We just... took a detour."

        "She went back to reading."
        "Her tail was still twitching."
        "She didn't acknowledge it."

    $ ghislaine_afeicao += 10
    $ ghislaine_interacted_today = True
    $ renpy.notify("+10 Affection with Ghislaine!")
    jump passar_tempo





label ghislaine_tailjob_intro_label:

    scene black
    with fade

    "I found Ghislaine in the study."
    "She was leaning over the desk, a book spread open in front of her."
    "Her brow was furrowed in concentration — the same intense focus she brought to swordplay."

    scene ghislaine_leaning_table
    with fade

    "She was mouthing the words silently. Her finger traced each line, one letter at a time."
    "It was oddly endearing."

    "But that wasn't what caught my attention."

    "Her tail."

    "It swayed lazily behind her — slow, rhythmic arcs back and forth."
    "Thick and powerful at the base, tapering to a soft point."
    "It moved with a life of its own, completely independent of Ghislaine's focus."

    "And right below it... her ass."
    "The way she leaned over the desk pushed it out naturally."
    "Her clothing stretched tight across her hips and thighs."

    "I stared. I knew I was staring. I couldn't stop."

    rudeus "(That tail... what would it feel like? It's muscular, obviously. Dexterous.)"
    rudeus "(The way it moves... wrapping, curling, gripping...)"
    rudeus "(Could a tail like that... wrap around...?)"

    "An idea formed in my head. A terrible, wonderful, perverted idea."

    "I walked up behind her. She didn't flinch — she'd heard me coming."

    ghislaine "...Rudeus. I'm studying."

    rudeus "I know. You're doing great. I just... had a question."

    ghislaine "...About what?"

    rudeus "Your tail."

    "Her tail stopped mid-swing."

    ghislaine "...My tail?"

    rudeus "It's... really flexible, right? Strong? You can control it precisely?"

    ghislaine "...Yes. It's a part of my body. Like an arm."

    rudeus "Can you... grip things with it?"

    "She turned her head slightly. One golden eye fixed on me."

    ghislaine "...Why are you asking?"

    rudeus "Scientific curiosity."

    ghislaine "...That's the same thing you said before touching my ears."

    rudeus "And you let me."

    "She stared at me for a long moment."
    "Her tail resumed its slow swaying. She knew what I was asking."

    ghislaine "...You want me to use my tail on you."

    "It wasn't a question."

    rudeus "I mean... if you wouldn't mind..."

    ghislaine "...You're strange, Rudeus. Most men want hands. Or mouths."

    rudeus "You're not most women."

    "Something flickered in her eyes. Not quite a smile. Warmer than that."

    ghislaine "...Fine. Drop your pants."

    "So direct. So Ghislaine."

    "I did as she said. No hesitation."
    "She glanced down once. Then back at her book."

    scene black with fade

    ghislaine "...I'll keep studying. Don't distract me."

    "She shifted her stance, leaning further onto the desk."
    "Her tail uncurled from behind her and reached back toward me."

    scene ghislaine_leaning_table_02 with fade

    "The first touch was electric."
    "Her tail was warm — warmer than I expected. The fur was short and dense, almost velvety."
    "It coiled around me once. Experimentally. Gauging the size."

    rudeus "Ngh—!"

    ghislaine "...Too tight?"

    rudeus "N-No. It's... perfect."

    "She started moving. Slow, deliberate strokes."
    "The tail squeezed and released in rhythm — a pulsing grip that was different from anything I'd ever felt."
    "Not like a hand. Not like feet. Something uniquely... beast-race."

    "Her tail was strong. Muscular beneath the soft fur."
    "Every stroke sent a shudder through me."

    rudeus "G-Ghislaine... this is incredible..."

    ghislaine "...Mm."

    "She didn't look up from her book. Her finger was still tracing the words."
    "But her ears had rotated toward me. Listening. Cataloging my reactions."

    "The tail picked up speed. The coil tightened."
    "The fur was getting slick — my pre-cum mixing with the warmth, making every slide smoother."

    rudeus "Hah... the way it squeezes... and then releases... how are you doing that...?"

    ghislaine "...Muscle control. Years of training."

    "She turned a page."

    "I couldn't believe this was happening."
    "Ghislaine Dedoldia — Sword King, legendary warrior — was casually giving me a tailjob while studying basic literacy."
    "And she was treating it like it was nothing. Just another task to complete."

    "But her tail said otherwise."
    "The tip was curling around the head on each upstroke — deliberate, precise."
    "She was paying attention. More than she let on."

    rudeus "I'm... getting close..."

    ghislaine "...Understood."

    "The tail didn't slow down. If anything, the grip tightened."
    "She squeezed me with practiced precision — rhythmic contractions that pulled me toward the edge."

    "I came."
    "Hard. The first shot hit her lower back. The second landed across her ass."
    "Thick ropes of it, dripping down the curve of her hips."

    "Her tail unwound slowly. Still warm. Glistening."

    "Ghislaine looked over her shoulder at the mess I'd made."
    "She studied it the same way she'd study a new sword technique — clinical, curious."

    ghislaine "...You made a mess."

    rudeus "S-Sorry... I can clean—"

    ghislaine "...Leave it. It's warm."

    "She turned back to her book."
    "Just like that. As if nothing had happened."
    "Her tail returned to its lazy swaying — now with a slight shine to it."

    ghislaine "...Rudeus."

    rudeus "Yeah?"

    ghislaine "...Turn to page fifteen. I'm stuck on this word."

    "I stared at her. Half-naked from the waist down, cum on her ass, asking me about reading."
    "This woman was unreal."

    rudeus "...It says 'gratitude.'"

    ghislaine "...'Gratitude.' Hmm. I like that word."

    $ ghislaine_tailjob_intro = False
    $ ghislaine_afeicao += 10
    $ ghislaine_interacted_today = True
    $ renpy.notify("+10 Affection with Ghislaine!")
    jump passar_tempo





label ghislaine_tailjob_generic:

    scene bg eris_castle
    with fade

    python:
        tj_setup = renpy.random.choice([
    ("Ghislaine was at the desk again. Studying. Her tail swayed behind her.",
    "...You're looking at my tail again.",
    "Can you blame me?",
    "...No. Close the door."),
    ("I found Ghislaine practicing sword forms. Alone. Her tail kept perfect balance behind her.",
    "...You came to train, or to stare?",
    "Both.",
    "...Hmph. Training first. Then... we'll see."),
    ("Ghislaine was eating at the table. Her tail hung lazily off the side of the chair.",
    "...You're not even trying to be subtle anymore.",
    "Does subtle work on you?",
    "...No. Direct is better. Lock the door.")
])

    show ghislaine base_clothes at my_center
    with dissolve

    "[tj_setup[0]]"

    ghislaine "[tj_setup[1]]"

    rudeus "[tj_setup[2]]"

    ghislaine "[tj_setup[3]]"

    scene black with fade

    "I dropped my pants. She didn't even blink."
    "Her tail was already moving — reaching back, finding me with practiced ease."

    "The coil wrapped around me. Warm. Firm. Familiar now."

    python:
        tj_middle = renpy.random.choice([
    ("She was faster today. Confident. Her tail knew exactly what to do.",
    "The strokes were long and tight — base to tip, squeezing at the head before sliding back down.",
    "She kept her eyes forward, ears angled back, listening to every sound I made."),
    ("Her tail twisted as it stroked — a spiraling motion that made my legs weak.",
    "The fur was slick within seconds. Every pass smoother than the last.",
    "She hummed quietly. Almost... satisfied."),
    ("She started slow. Torturously slow. Long, deliberate pulls.",
    "Every time I got close, she eased off. She could feel me twitching.",
    "...Not yet. She said it once, flat and calm, like giving a military order.")
])

    "[tj_middle[0]]"
    "[tj_middle[1]]"
    "[tj_middle[2]]"

    rudeus "Ghislaine... I'm close..."

    python:
        tj_finish = renpy.random.choice([
    ("She tightened her grip and stroked faster. Three more pumps.",
    "I came across her lower back. She didn't flinch.",
    "...Hmph. You lasted longer this time."),
    ("Her tail squeezed hard — one final, firm pull that drained everything from me.",
    "The mess coated her ass and thighs. She glanced down at it.",
    "...Warm. ...Get a cloth."),
    ("She angled her tail so I finished right on the curve of her ass.",
    "It dripped down slowly. She watched it with detached curiosity.",
    "...You always make a mess. ...I don't mind.")
])

    "[tj_finish[0]]"
    "[tj_finish[1]]"
    ghislaine "[tj_finish[2]]"

    "Her tail unwound. Resumed its lazy swaying."
    "She went back to whatever she was doing before — as if nothing had happened."
    "As if a man hadn't just finished all over her."

    "That was Ghislaine. Unshakeable."

    $ ghislaine_afeicao += 10
    $ ghislaine_interacted_today = True
    $ renpy.notify("+10 Affection with Ghislaine!")
    jump passar_tempo
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
