default eris = Character("Eris", color="#ff4444")

default eris_event = 0
default eris_afeicao = 0

default eris_talked_today = False
default eris_gifted_today = False
default eris_interacted_today = False

default eris_on = True

default eris_intro = True

default eris_bj_intro = True
default eris_sex_intro = True




label eris_intro:
    show black with fade

    "Today was my first day as a tutor at the Boreas Greyrat mansion."
    "Philip — Eris' father — had hired me to teach her reading, writing, and arithmetic."
    "'She's a handful,' he warned me. 'Strong-willed. Violent. Doesn't listen to anyone.'"
    "'If you can last a week, I'll double your pay.'"

    "I expected a spoiled noble girl. Maybe some tantrums, some crying."
    "What I did NOT expect was—"

    hide black
    show eris base_clothes at center
    with fade

    "A fist flying toward my face the moment I walked through the door."

    "I barely dodged it. A girl with fiery red hair and sharp crimson eyes glared at me."
    "She was about my age — maybe a year older — with a fierce expression that screamed 'I will bite you.'"
    "Her hair was wild and untamed, like a mane of flames."

    eris "Who the hell are you?! Another tutor?! I already told father I don't NEED one!"

    show rudeus normal at left with dissolve
    show eris base_clothes:
        ease 0.5 xalign 1.0

    rudeus "I'm Rudeus Greyrat. Your new tutor. Nice to meet—"

    eris "Greyrat?! You're related to me?! That's even WORSE!"

    rudeus "Distant relatives, yes. But I'm here to teach you magic and—"

    eris "I don't WANT to learn magic! Magic is for weaklings who can't fight with their fists!"

    "She threw another punch. This time I caught her wrist."

    eris "...! Let go of me!"

    rudeus "Not until you calm down."

    eris "I AM calm! This is how I always am!"

    rudeus "...That's concerning."

    "She yanked her hand free and stepped back, breathing hard."
    "Her eyes were burning with defiance... but also curiosity."
    "She'd never met someone who could actually stop her punch."

    eris "...You're stronger than you look."

    rudeus "And you're louder than I expected."

    eris "What did you say?!"

    rudeus "I said you have great... enthusiasm. For learning."

    eris "...Hmph!"

    "She crossed her arms and looked away. Her cheeks were flushed — from anger or embarrassment, I couldn't tell."

    eris "Fine! ONE week. If you bore me, I'll kick you out myself!"

    rudeus "Deal."

    "She stomped away, her red hair swaying behind her like a flame."
    "I could hear her muttering something about 'stupid tutors' as she disappeared around the corner."

    hide eris with dissolve
    show rudeus:
        ease 0.5 xalign 0.5

    "...Philip was right. She IS a handful."
    "But there was something in those eyes. Behind all that anger..."
    "A girl who wanted to prove herself. Who was tired of people giving up on her."

    "I won't give up on her."

    $ eris_intro = False
    $ eris_afeicao += 5
    $ renpy.notify("You met Eris! +5 Affection")

    jump passar_tempo





label eris_label:

    if eris_intro:
        jump eris_intro
    else:

        show rudeus normal at left
        show eris base_clothes at right
        with dissolve

        python:
            if eris_event >= 7:
                greeting = renpy.random.choice([
        "Rudeus! ...You came. Good. I was getting bored without you.",
        "There you are! What took you so long?! ...Not that I was waiting!",
        "Hmph. You're here. ...My day just got less boring. Don't let it go to your head!"
    ])
            elif eris_event >= 4:
                greeting = renpy.random.choice([
        "Oh, it's you. ...What? I'm not happy to see you or anything!",
        "Rudeus. ...Fine, you can stay. But don't annoy me!",
        "You again? ...I suppose I don't hate your company."
    ])
            elif eris_event >= 2:
                greeting = renpy.random.choice([
        "What do you want? ...If it's a lesson, fine. But make it interesting!",
        "Rudeus. ...Did you bring anything fun? No? Then why are you here?",
        "Hmph. At least you're not as boring as the other tutors."
    ])
            elif eris_event >= 1:
                greeting = renpy.random.choice([
        "What?! You again?! ...Fine. But don't waste my time!",
        "Here to teach me more useless stuff? ...Ugh, fine.",
        "If you're going to be here, at least be entertaining!"
    ])
            else:
                greeting = renpy.random.choice([
        "What do YOU want?! Go away!",
        "Not YOU again! I told you, I don't need a tutor!",
        "Hmph! If you're here to lecture me, save your breath!",
        "You better have a good reason for bothering me!"
    ])

        eris "[greeting]"

        jump eris_menu





label eris_menu:

    menu:

        "🌟 The First Lesson" if eris_event == 0 and eris_on:
            jump eris_event_1

        "🌟 She Trusts You" if eris_event == 1 and eris_on:
            jump eris_event_2

        "🌟 Magic Awakens" if eris_event == 2 and eris_on:
            jump eris_event_3

        "🌟 What I Feel For You" if eris_event == 3 and eris_on:
            jump eris_event_4

        "🌟 The Barn" if eris_event == 4 and eris_on:
            jump eris_event_5

        "🌟 Fair is Fair" if eris_event == 5 and eris_on:
            jump eris_event_6

        "🌟 Her Room at Night" if eris_event == 6 and eris_on:
            jump eris_event_7
        "😏 Interact":






























































            menu:

                "Quickie" if eris_event >= 7:
                    if eris_sex_intro:
                        jump eris_sex_intro_label
                    else:
                        jump eris_sex_generic

                "Blowjob" if eris_event >= 7:
                    if eris_bj_intro:
                        jump eris_bj_intro_label
                    else:
                        jump eris_bj_generic
                "Teach her magic":

                    python:
                        if eris_event >= 5:
                            magic_response = renpy.random.choice([
        ("You begin today's magic lesson.",
        "...Fine. But only because YOUR magic is actually cool.",
        "Eris focuses intensely. A small flame appears in her palm.",
        "I DID IT! ...I mean, obviously I did. I'm amazing."),
        ("You demonstrate a water ball technique.",
        "That's it? Let me try! ...Why won't it work?!",
        "She slams her fist into the training dummy in frustration.",
        "...Okay FINE. Show me again. SLOWLY this time.")
    ])
                        elif eris_event >= 3:
                            magic_response = renpy.random.choice([
        ("You set up a magic practice session.",
        "Ugh, more magic? Can't we just spar instead?",
        "She reluctantly sits down and tries to focus.",
        "...It flickered! Did you see?! The fire FLICKERED!"),
        ("You try to teach her basic mana control.",
        "This is BORING! When do I get to blow things up?!",
        "She clenches her fists, and a spark appears between her fingers.",
        "...Huh. That was actually kind of cool.")
    ])
                        elif eris_event >= 2:
                            magic_response = renpy.random.choice([
        ("You explain the fundamentals of mana.",
        "Mana? What's that? Can I punch it?",
        "She tries to concentrate but keeps fidgeting.",
        "This is STUPID! I'm a WARRIOR, not a mage!"),
        ("You show her a simple fire spell.",
        "Ooh, fire! Let me try!",
        "Nothing happens. She kicks the table.",
        "UGH! This magic stuff is RIGGED!")
    ])
                        else:
                            magic_response = renpy.random.choice([
        ("You suggest starting with magic basics.",
        "Magic is for LOSERS! Real fighters use SWORDS!",
        "She crosses her arms stubbornly.",
        "...Fine. But if it's boring, I'm leaving!"),
        ("You try to explain what mana is.",
        "I don't CARE about mana! Show me something COOL or go away!",
        "She glares at you impatiently.",
        "...ONE more minute. Then I'm done.")
    ])

                    "[magic_response[0]]"
                    eris "[magic_response[1]]"
                    "[magic_response[2]]"
                    eris "[magic_response[3]]"

                    $ eris_afeicao += 5
                    $ eris_interacted_today = True
                    $ renpy.notify("+5 Affection with Eris!")
                    jump passar_tempo

                "Spar with her" if eris_event >= 1:
                    python:
                        if eris_event >= 5:
                            spar_response = renpy.random.choice([
        ("You challenge Eris to a sparring match.",
        "FINALLY! Something worth doing! Come at me, Rudeus!",
        "She fights with incredible intensity, her eyes shining.",
        "Ha! I almost got you that time! ...Best of three?!"),
        ("You take a fighting stance.",
        "That's more like it! None of that book nonsense!",
        "She launches a flurry of punches. You barely block them.",
        "You're getting better! ...Not as good as ME, obviously!")
    ])
                        elif eris_event >= 2:
                            spar_response = renpy.random.choice([
        ("You suggest some combat training.",
        "NOW you're talking! Put 'em up!",
        "She throws a wild haymaker that you dodge.",
        "Stand still so I can hit you!"),
        ("You raise your training sword.",
        "Ooh, swords! Ghislaine taught me a new move!",
        "She swings with raw power but no finesse.",
        "...Did I win? What do you mean 'not how swords work'?!")
    ])
                        else:
                            spar_response = renpy.random.choice([
        ("You ask Eris if she wants to spar.",
        "YEAH! Let's GO!",
        "She charges at you before you're even ready.",
        "Too slow! You need to be faster to fight a Boreas!"),
        ("You mention wanting to practice fighting.",
        "About TIME you said something interesting!",
        "She punches you square in the stomach before you can react.",
        "...What? You said practice! That WAS practice!")
    ])

                    "[spar_response[0]]"
                    eris "[spar_response[1]]"
                    "[spar_response[2]]"
                    eris "[spar_response[3]]"

                    $ eris_afeicao += 5
                    $ renpy.notify("+5 Affection with Eris!")
                    jump passar_tempo
                "Study together":

                    python:
                        if eris_event >= 5:
                            study_response = renpy.random.choice([
        ("You pull out a textbook for today's lesson.",
        "...Ugh, FINE. But only because it's you teaching.",
        "She actually tries to read, leaning close to you.",
        "...I got this word right, didn't I? ...Don't give me that look! I CAN learn!"),
        ("You prepare a writing exercise.",
        "My handwriting is FINE! ...Okay maybe it's not. Help me.",
        "She grips the pen like a sword hilt.",
        "...There! 'Eris Boreas Greyrat!' ...It's NOT messy! You're just picky!")
    ])
                        elif eris_event >= 2:
                            study_response = renpy.random.choice([
        ("You suggest a reading exercise.",
        "Reading again?! Can't I just learn to sign my name and call it done?!",
        "She struggles through a sentence, getting more frustrated.",
        "These words are STUPID! Who even uses 'perambulate'?!"),
        ("You try teaching basic arithmetic.",
        "If I have 5 swords and buy 3 more, I have 8 swords. SEE? I can do math!",
        "You try harder problems. She breaks the pencil in half.",
        "...Numbers are the ENEMY!")
    ])
                        else:
                            study_response = renpy.random.choice([
        ("You try to start a lesson.",
        "I TOLD you, I don't need to learn this stuff!",
        "She flips the textbook off the table.",
        "...Hmph! Fine, pick it up. But make it INTERESTING!"),
        ("You open a children's reading primer.",
        "IS THAT A KIDS' BOOK?! Do I LOOK like a kid to you?!",
        "Her face turns red from embarrassment.",
        "...J-Just read it to me first. So I know what it's SUPPOSED to sound like!")
    ])

                    "[study_response[0]]"
                    eris "[study_response[1]]"
                    "[study_response[2]]"
                    eris "[study_response[3]]"

                    $ eris_afeicao += 5
                    $ eris_interacted_today = True
                    $ renpy.notify("+5 Affection with Eris!")
                    jump passar_tempo
                "Talk":

                    if eris_talked_today:
                        eris "We already talked today! Stop bothering me! ...I mean, come back tomorrow!"
                        jump eris_menu
                    else:
                        python:
                            if eris_event >= 5:
                                talk_options = [
        ("What do you want to do when you grow up?",
        "I want to be the strongest swordswoman in the world! Stronger than Ghislaine!",
        "...And maybe... travel the world. With someone I trust.",
        "...Don't look at me like that! I didn't say it was YOU! ...But it could be."),
        ("Tell me about your family.",
        "The Boreas family is the best! We're strong, proud, and we never back down!",
        "...Father is strict but he cares. Grandfather is... weird. But strong.",
        "And now there's you. ...You're part of this family too, I guess. ...IDIOT!"),
        ("What matters most to you?",
        "Strength! Obviously! ...But also...",
        "...Having people who don't give up on me. Everyone else always leaves.",
        "...You didn't leave. That... that means something. Shut up!")
    ]
                            elif eris_event >= 3:
                                talk_options = [
        ("How's your sword training with Ghislaine?",
        "It's BRUTAL! She doesn't hold back at all!",
        "...But I'm getting stronger! I can almost keep up with her now!",
        ""),
        ("Do you like living in this mansion?",
        "It's boring! Nothing ever happens!",
        "...Well, it got less boring since you showed up. A LITTLE less boring!",
        ""),
        ("What's your favorite thing to do?",
        "Fighting! Sword practice! Punching things!",
        "...AND eating sweets. But that's a SECRET!",
        "")
    ]
                            elif eris_event >= 2:
                                talk_options = [
        ("How are you today, Eris?",
        "I'm FINE! Why does everyone keep asking me that?!",
        "...I trained all morning. Ghislaine said my stance improved.",
        ""),
        ("Have you ever been outside the mansion?",
        "Father never lets me go anywhere! It's SO unfair!",
        "...One day I'll be strong enough to go wherever I want!",
        ""),
        ("What do you think of magic?",
        "Magic is... okay I GUESS. Your fire spells are kind of cool.",
        "...Don't tell anyone I said that!",
        "")
    ]
                            elif eris_event >= 1:
                                talk_options = [
        ("How's it going?",
        "Don't ask stupid questions! How do you THINK it's going?!",
        "",
        ""),
        ("Nice weather today.",
        "Who CARES about weather?! Weather doesn't make you stronger!",
        "",
        ""),
        ("Want to talk about something?",
        "Talk about WHAT?! If you have nothing to say, then GO AWAY!",
        "...But don't actually go away. I'm bored.",
        "")
    ]
                            else:
                                talk_options = [
        ("Hey Eris, how are you?",
        "NONE of your business! Go away!",
        "",
        ""),
        ("Want to be friends?",
        "FRIENDS?! With YOU?! Ha! Don't make me laugh!",
        "",
        ""),
        ("I'm your new tutor, we should get along.",
        "I don't GET ALONG with anyone! Especially tutors! You'll quit like the rest!",
        "",
        "")
    ]

                            talk_choice = renpy.random.choice(talk_options)

                        rudeus "[talk_choice[0]]"
                        eris "[talk_choice[1]]"
                        if talk_choice[2]:
                            eris "[talk_choice[2]]"
                        if talk_choice[3]:
                            eris "[talk_choice[3]]"

                        $ eris_afeicao += 5
                        $ eris_talked_today = True
                        $ renpy.notify("You gained +5 affection with Eris!")
                        jump passar_tempo
                "Nevermind":

                    jump eris_menu
        "👋 Leave":


            python:
                if eris_event >= 5:
                    farewell = renpy.random.choice([
        "You're LEAVING?! ...I-I mean, fine! See if I care! ...Come back soon!",
        "Already?! But we barely... UGH! Fine! Go! ...But come back tomorrow!",
        "...Hmph. Finally some peace and quiet. ...It's too quiet. COME BACK!"
    ])
                elif eris_event >= 3:
                    farewell = renpy.random.choice([
        "Leaving already? ...Whatever! I have training to do anyway!",
        "Fine! Go! I don't care! ...Maybe I care a LITTLE. Shut up!",
        "Hmph! Don't think I'll miss you! ...I won't wait by the door or anything!"
    ])
                elif eris_event >= 2:
                    farewell = renpy.random.choice([
        "FINALLY! Now I can do something FUN!",
        "About time! You were starting to bore me!",
        "Go then! Who needs you! ...Not me!"
    ])
                else:
                    farewell = renpy.random.choice([
        "GOOD! Go away and don't come back!",
        "Finally! I thought you'd NEVER leave!",
        "Hmph! And STAY gone!"
    ])

            eris "[farewell]"

            hide rudeus
            hide eris
            with dissolve
            jump locais





label eris_event_1:

    scene bg eris_castle
    with fade

    "Another day at the mansion. Eris was waiting in the study room."
    "Surprisingly, she was actually sitting at the desk this time, instead of destroying furniture."

    show rudeus normal at my_left
    show eris base_clothes at my_right
    with dissolve

    rudeus "Eris? You're... already here?"

    eris "Don't act so surprised! I can be on time if I WANT to!"

    rudeus "Right. Well, let's start today's lesson. We'll—"

    eris "Magic. I want to learn MAGIC today."

    "That was new. She usually resisted magic lessons like a cat resists a bath."

    rudeus "Magic? Really? I thought magic was 'for losers.'"

    eris "I NEVER said that! ...Okay maybe I said that. But I changed my mind!"
    eris "Ghislaine told me that combining magic with swordplay makes you unstoppable."
    eris "And I want to be UNSTOPPABLE."

    rudeus "Fair enough. Let's start with the basics. Try to focus your mana in your palm."

    "She squeezed her eyes shut and clenched her fist."
    "Her whole body tensed. The veins in her arm bulged."

    eris "HRRRRRGH!"

    rudeus "Eris, you don't need to—"

    hide rudeus
    hide eris
    with dissolve
    show bg eris_castle:
        blur 5
    show eris_casting with dissolve

    "A tiny spark appeared in her palm. Then it flickered out."

    eris "...DID YOU SEE THAT?!"

    hide eris_casting with dissolve
    scene bg eris_castle with dissolve
    show rudeus normal at my_left
    show eris base_clothes at my_right
    with dissolve

    rudeus "I did! That was great for a first—"

    eris "I DID MAGIC! I ACTUALLY DID MAGIC!"

    "She jumped up from her chair and grabbed my shoulders."
    "Her face was beaming — a genuine, unguarded smile that I'd never seen before."

    eris "Did you see it?! The spark?! It was a spark, right?!"

    rudeus "It was definitely a spark. With practice, you could turn that into—"

    "She hugged me. Just for a second. Then she shoved me away."

    eris "T-That was... I was just excited! Don't think anything of it!"

    rudeus "I didn't say anything."

    eris "Your FACE said something! Stop making that face!"

    "She stomped around the room, trying to act angry, but the corners of her mouth kept twitching upward."

    eris "...Rudeus."

    rudeus "Yeah?"

    eris "Same time tomorrow. Be here."
    eris "...And bring something harder to learn. This easy stuff is beneath me!"

    hide eris with dissolve
    show rudeus:
        ease 0.5 xalign 0.5

    "She ran out of the room like she was fleeing a battlefield."
    "But I caught a glimpse of her face as she left."
    "She was smiling. A real, honest smile."

    "...Progress."

    $ eris_event = 1
    $ eris_on = False
    $ eris_afeicao += 5

    $ renpy.notify("Event complete! +5 Affection")
    jump passar_tempo





label eris_event_2:

    scene bg eris_castle
    with fade

    "I found Eris sitting alone in the garden."
    "She wasn't training. She wasn't destroying anything."
    "She was just... sitting there, staring at the sky."

    show rudeus normal at my_left
    show eris base_clothes at my_right
    with dissolve

    rudeus "Eris? Are you okay?"

    eris "...I'm FINE. Go away."

    rudeus "You don't look fine."

    eris "I SAID I'm fine! Are you deaf?!"

    "Her eyes were red. Had she been... crying?"

    rudeus "You know, it's okay to not be fine sometimes."

    eris "..."

    "She was quiet for a long moment. The wind rustled through the garden."

    eris "...The other tutors. Before you. They all quit."
    eris "Every single one. They said I was 'unteachable.' 'Impossible.' 'A lost cause.'"
    eris "Father yelled at me every time. 'Why can't you behave? Why can't you be proper?'"

    rudeus "Eris..."

    eris "I TRIED! I tried to be good! But I just... I can't sit still! I can't be quiet!"
    eris "My body wants to MOVE and FIGHT and everyone tells me that's WRONG!"

    "She punched the ground. Hard enough to crack the stone."

    eris "...So I stopped trying. If everyone thinks I'm a monster, then FINE. I'll be a monster."

    rudeus "You're not a monster, Eris."

    eris "What do YOU know?!"

    rudeus "I know that a monster wouldn't cry about being called one."

    eris "I'm NOT crying!"

    "She wiped her face aggressively."

    rudeus "Eris. The other tutors were wrong. You're not unteachable."
    rudeus "You learn differently. You need to MOVE, to DO things. There's nothing wrong with that."
    rudeus "I'll teach you in a way that works for YOU. Not the other way around."

    eris "..."
    eris "...You promise?"

    rudeus "I promise."

    eris "...If you break that promise, I'll break your legs."

    rudeus "Wouldn't expect anything less."

    "For just a moment, she leaned against my shoulder."
    "Then she shoved me away and stood up."

    eris "...We never talk about this. EVER."
    eris "And I was NOT crying!"

    hide eris with dissolve
    show rudeus:
        ease 0.5 xalign 0.5

    "She ran off toward the training grounds."
    "...But before she turned the corner, she looked back."

    eris "...Thank you. ...IDIOT!"

    "I couldn't help but smile."

    $ eris_event = 2
    $ eris_on = False
    $ eris_afeicao += 5

    $ renpy.notify("Event complete! +5 Affection")
    jump passar_tempo





label eris_event_3:

    scene bg eris_castle
    with fade

    "Weeks had passed since I started adjusting my teaching methods for Eris."
    "Instead of sitting at a desk, we practiced in the training grounds."
    "Magic through movement. Spells through sword forms. Theory through sparring."

    "And today, something incredible happened."

    show rudeus normal at my_left
    show eris base_clothes at my_right
    with dissolve

    rudeus "Alright, Eris. Remember what I taught you? Channel the mana through your arm as you strike."

    eris "I KNOW! Stop repeating yourself!"

    "She took a deep breath. Drew her wooden sword."
    "Her stance was textbook Sword God Style — Ghislaine's teaching showed."
    "But her arm was coated in a faint glow of mana — MY teaching."

    eris "HAAAA!"

    "She swung the sword in a single, explosive arc."
    "Fire erupted along the blade's path, leaving a scorching trail in the air."

    "The training dummy didn't just break. It disintegrated."

    rudeus "...!"

    eris "...Did... did that just happen?!"

    rudeus "You combined Sword God Style with fire magic. That was... incredible."

    eris "I... I did that?! I ACTUALLY DID THAT?!"

    "She looked at her hands in disbelief."
    "Then she looked at me — and for once, there was no anger, no defiance."
    "Just pure, unfiltered joy."

    eris "RUDEUS! DID YOU SEE?! I'M A GENIUS!"

    rudeus "Well, I wouldn't go THAT far—"

    eris "Shut up! I'm a GENIUS and you KNOW IT!"

    "She grabbed my hands and jumped up and down."

    eris "Teach me more! I want to learn MORE! What else can I do?!"

    rudeus "We can try wind enchantment next. It would increase your sword speed."

    eris "YES! Let's do it NOW!"

    "She was practically vibrating with excitement."
    "This was the girl everyone called 'unteachable.' The 'impossible' student."
    "She just needed someone to meet her where she was."

    eris "...Rudeus."

    rudeus "Hmm?"

    eris "You're... actually a good teacher."
    eris "DON'T let it go to your head! I'm just stating a FACT!"

    hide eris with dissolve
    show rudeus:
        ease 0.5 xalign 0.5

    "She charged off to find Ghislaine, probably to show off her new technique."
    "I could hear her yelling across the courtyard:"

    eris "GHISLAINE! WATCH THIS! WATCH WHAT I CAN DO!"

    "...I've never been more proud of a student."

    $ eris_event = 3
    $ eris_on = False
    $ eris_afeicao += 5

    $ renpy.notify("Event complete! +5 Affection")
    jump passar_tempo





label eris_event_4:

    scene bg eris_castle
    with fade

    "I was heading to the study room when I heard something unusual."
    "Eris' voice. But not yelling. Whispering."

    show rudeus normal at my_left
    with dissolve

    "I stopped by the door and listened. She was talking to Ghislaine."

    eris "...I don't know what's WRONG with me, Ghislaine!"
    eris "Every time he shows up, my chest gets tight and my face gets hot!"
    eris "Am I SICK?! Is this a CURSE?!"

    "I heard Ghislaine's deep, even reply:"

    ghislaine "...That's not a sickness, Eris."

    eris "Then what IS it?!"

    ghislaine "...You'll figure it out."

    eris "That's NOT HELPFUL!"

    "I stepped away from the door, my heart pounding."
    "Did she mean...?"

    "Later that evening, Eris found me in the garden."

    show eris base_clothes at my_right with dissolve

    eris "...Rudeus."

    rudeus "Eris? What's—"

    eris "Shut up and LISTEN!"
    eris "I... I have something to say and I'm only going to say it ONCE."

    "She was trembling. Her fists were clenched so tight her knuckles were white."
    "Her face was the same color as her hair."

    eris "I... I think I..."
    eris "I think you're... not... TERRIBLE."

    rudeus "...Not terrible?"

    eris "YES! Not terrible! You're actually... kind of..."
    eris "AAAGH! Why is this so HARD?!"

    "She grabbed her own hair in frustration."

    eris "YOU MAKE ME FEEL WEIRD, OKAY?!"
    eris "My stomach does flips and my heart won't shut up and I can't THINK straight around you!"
    eris "And it's YOUR fault for being... for being YOU!"

    rudeus "Eris..."

    eris "I'M NOT FINISHED!"
    eris "...When you leave at the end of the day, I count the hours until you come back."
    eris "And when you praise me during lessons, I feel like I could fight a dragon."
    eris "And when you smile at me..."

    "She looked away, her entire body shaking."

    eris "...When you smile at me, I forget that I'm angry at the world."

    "Silence. The garden was quiet except for the evening crickets."

    eris "...Say SOMETHING, you idiot!"

    rudeus "I like you too, Eris."

    eris "..."
    eris "...You... you do?"

    rudeus "More than you know."

    eris "...WELL THEN! ...Good! ...OBVIOUSLY you do!"

    "She turned away, but not before I saw the tears streaming down her cheeks."

    eris "I'm NOT crying! It's the WIND! There's wind in my eyes!"

    rudeus "There's no wind, Eris."

    eris "THEN I'M ALLERGIC TO YOUR STUPID FACE!"

    "She wiped her tears with her arm and turned back to me."
    "Her cheeks were red. Her eyes were shining."
    "And she was smiling — the most beautiful, genuine smile I'd ever seen."

    eris "...Same time tomorrow. And the day after. And the day after that."
    eris "You're not allowed to leave. EVER."

    "She stomped away into the mansion."
    "But halfway to the door, she ran back, punched my arm, and whispered:"

    eris "...Thank you for not giving up on me."

    "Then she was gone."

    hide eris with dissolve

    "...Eris Boreas Greyrat."
    "Violent, stubborn, loud, impossible..."
    "...And the most honest person I've ever met."

    $ eris_event = 4
    $ eris_on = False
    $ eris_afeicao += 10

    $ renpy.notify("Event complete! +10 Affection")
    jump passar_tempo





label eris_event_5:

    scene bg eris_castle
    with fade

    "Today's lesson didn't go well."
    "Eris was more restless than usual. She couldn't focus, couldn't sit still."
    "Every time I tried to explain a new spell formula, she'd fidget, grunt, and look away."

    show rudeus normal at my_left
    show eris base_clothes at my_right
    with dissolve

    rudeus "Eris, you need to concentrate. The mana flow requires—"

    eris "I KNOW! You've said that THREE times already!"

    rudeus "Because you keep losing focus. If you would just—"

    eris "Maybe if your lessons weren't so BORING, I wouldn't lose focus!"

    rudeus "Boring? I literally set a training dummy on fire for you yesterday."

    eris "That was yesterday! Today is TODAY and today SUCKS!"

    "Something was clearly bothering her. But Eris was never one to explain her feelings."
    "She expressed everything through violence."

    rudeus "Eris, what's really—"

    eris "SHUT UP! You don't understand ANYTHING!"

    "She kicked the desk, sending books flying."
    "Then she stormed out of the room, slamming the door so hard the hinges cracked."

    hide eris with dissolve
    show rudeus:
        ease 0.5 xalign 0.5

    rudeus "...There she goes again."

    "I sighed. This wasn't the first time she'd run off."
    "But something about today felt different. She wasn't just angry — she was frustrated. With herself."

    "I should find her."

    scene black with fade

    "I searched the mansion. The training grounds. The garden. The kitchen."
    "No Eris."
    "One of the servants mentioned seeing her run toward the barn at the edge of the property."

    scene bg celeiro
    with fade

    "The barn was dim, dusty, and warm. Hay bales were stacked along the walls."
    "Afternoon sunlight filtered through the wooden slats, painting golden stripes across the floor."

    "And there she was."

    show eris_lying_01 with fade

    "Eris was lying on a pile of hay in the corner."
    "Curled up on her side, her red hair fanned out beneath her like a burning halo."
    "Her breathing was slow and even. She'd fallen asleep."

    rudeus "(She must have exhausted herself running all the way here...)"

    "I approached quietly. She looked... peaceful. For once."
    "No scowl. No clenched fists. Just a girl, sleeping in the hay."
    "Her face was relaxed in a way I'd never seen while she was awake."
    "Tear tracks still glistened on her cheeks."

    rudeus "(She was crying before she fell asleep...)"

    "I knelt beside her, careful not to make a sound."
    "That's when I noticed."

    "Her skirt had ridden up as she tossed in her sleep."
    "Her legs were slightly parted, one knee bent, the other extended."
    "The fabric had bunched up high on her thighs, teasing a sliver of white underneath."

    rudeus "(...!)"

    "My brain screamed at me to look away. My body did not cooperate."

    rudeus "(She's asleep. Completely defenseless. I could see her panties if I just...)"
    rudeus "(No. NO. She's your student. She trusts you. What kind of man are you?)"

    "But the thought had already taken root."
    "She was lying there, warm and soft and vulnerable, breathing like she didn't have a care in the world."
    "Her thighs were smooth and pale, still flushed from the run, and between them — just barely hidden by the bunched skirt — a hint of white cotton."

    rudeus "(Just a peek. That's all. She'll never know.)"
    rudeus "(...God, I'm disgusting. I'm actually considering this.)"

    "My hands were trembling. My mouth was dry."
    "The rational part of my brain was screaming. The rest of me was already reaching forward."

    rudeus "(She looks so peaceful... so soft. Nothing like the violent hellcat who throws desks at me.)"
    rudeus "(What would she feel like? Her skin looks so smooth... those thighs...)"
    rudeus "(STOP. Get up. Walk away. Be a decent human being for ONCE.)"

    "I should leave. I should absolutely, unequivocally leave."

    menu:
        "Spread her legs to get a better look":
            pass

    rudeus "(...I'm going to hell for this.)"

    scene black with fade

    "My hands moved on their own."
    "Gently — so gently — I placed my fingers on her knee."
    "She didn't stir. Her breathing stayed even."

    "I eased her bent leg outward. Slowly. Millimeter by millimeter."
    "Her thigh was warm under my fingers — impossibly warm, the skin velvet soft."
    "My heart was hammering so loud I was sure it would wake her."

    rudeus "(I really am the worst kind of person...)"
    rudeus "(But I can't stop. I don't WANT to stop.)"

    "I guided her other leg apart with my other hand."
    "Her body offered no resistance — relaxed, pliant, trusting."
    "Her skirt fell away completely as her thighs spread."

    scene eris_lying_02 with fade

    "And there it was."

    "White cotton panties with a small ribbon at the front."
    "Simple. Innocent. Girlish. Completely at odds with the violent girl who wore them."
    "The fabric clung to her like a second skin, slightly damp from sweat after her run."
    "I could see EVERYTHING through the thin material — the soft mound, the gentle cleft, the way the cotton pressed into her folds and left nothing to the imagination."

    rudeus "(...She's beautiful. She's absolutely beautiful.)"
    rudeus "(This is wrong. This is SO wrong. But she's right HERE, spread open in front of me, and I—)"

    "My eyes devoured every detail. The way her inner thighs glistened softly in the filtered sunlight."
    "The way her hips were tilted ever so slightly upward, as if offering herself."
    "A tiny dark spot on the cotton where the fabric had been pressed tightest — warmth, or maybe something else."

    rudeus "(If I touched her right now... if I just ran my finger along that line...)"
    rudeus "(She'd never even know. She's deeply asleep. Just one touch. Just to feel...)"

    "I was hard. Painfully hard. The front of my pants strained."
    "The rational voice in my head had gone completely silent."
    "All I could hear was my own heartbeat and her soft, steady breathing."

    rudeus "(Just the panties. I'll just move them aside. Just to see. That's all.)"
    rudeus "(I won't do anything else. I just need to SEE.)"

    scene black with fade

    "My fingers found the edge of her panties."
    "The fabric was warm — body-warm — and I could feel the heat radiating from underneath."
    "I hooked my finger under the hem and slowly, carefully pulled it to the side."

    "The white cotton peeled away from her skin with the faintest sound."
    "And I saw everything."

    scene eris_lying_03 with fade

    "Pink. Glistening. Slightly puffy. Framed by the softest wisps of red hair."
    "She was... perfect. Untouched. Every fold and curve on display."
    "The outer lips were delicate, barely parted, and between them I could see the slick shine of her arousal."
    "Even in sleep, her body was warm and wet."

    rudeus "(Oh god. Oh god oh god oh god.)"
    rudeus "(She's... she's wet. Is she dreaming about something? About... someone?)"

    "A drop of her wetness caught the light, trailing slowly down."
    "I was shaking. Every nerve in my body was on fire."
    "The scent of her reached me — faint, warm, intoxicating."

    rudeus "(I should stop here. I've already gone too far. WAY too far.)"
    rudeus "(But she's so wet... and warm... and if I just...)"

    "My fingers moved on their own. Trembling, I placed both thumbs on either side of her slit."
    "Gently — so gently — I spread her open."

    show eris_lying_03_close with dissolve

    "The smell hit me instantly. Stronger now. Thick and sweet, the unmistakable scent of a girl's arousal filling my nostrils."
    "Her small vagina was completely exposed. Pink, glistening, the inner folds wet and slightly twitching."
    "So tiny. So delicate. Every detail laid bare under my gaze."
    "The wetness clung to her lips in thin strands, and a fresh bead of it welled up from deep inside, sliding slowly down."

    rudeus "(It's... it's right there. Open. Wet. Waiting.)"
    rudeus "(I can feel the heat radiating from it on my thumbs.)"

    "I held her open, staring, mesmerized. Her inner walls glistened, clenching faintly around nothing."
    "The scent was overwhelming this close. My head was spinning."

    "Before I could think, I'd freed myself from my pants."
    "I was throbbing. Aching. My body had completely overridden my conscience."

    scene eris_lying_04 with fade

    "I positioned myself between her spread legs."
    "Slowly — agonizingly slowly — I pressed myself against her."

    "The first contact sent a shockwave through my body."
    "The head of my cock rested against her bare slit."
    "She was scorching. Silk and fire. The wetness coated me instantly."

    rudeus "(Oh... oh fuck...)"

    scene eris_lying_05 with fade

    "I didn't push in. Not yet. I started to grind. Slowly."
    "Sliding the shaft along the length of her pussy, parting her outer lips with each stroke."
    "Up and down. Feeling every fold, every ridge of her press against me."
    "The slick heat was maddening. Her wetness made the glide frictionless."

    "She murmured something in her sleep. Her hips twitched — the tiniest, unconscious push back against me."

    rudeus "(She moved. She MOVED. Is she waking up?!)"
    rudeus "(...No. Still sleeping. Her body is just... reacting.)"
    rudeus "(God, she's so soft. So incredibly soft and warm and—)"

    "I rocked against her faster. The head of my cock caught against her entrance on each downstroke."
    "Every time it did, I felt a surge — a pull — like her body was trying to draw me in."
    "It would be so easy. Just a little pressure. Just shift my hips forward and—"

    rudeus "(Do it. Just... do it. She's right here. She wants it — her body wants it.)"
    rudeus "(NO. No no no. This is insane. She's ASLEEP. I can't—)"
    rudeus "(...But what if I just... put the tip in? Just the tip. That's all.)"

    "I angled my hips. Lined myself up with her entrance."
    "The tip pressed against her opening — hot, tight, impossibly inviting."
    "I pushed. Just slightly. Just enough to feel her start to give way—"

    scene eris_lying_06 with fade

    eris "...!!!"

    "Her eyes snapped open."

    "Time stopped."

    "Crimson eyes — hazy with sleep — locked onto mine."
    "For one horrible second, she didn't understand what was happening."
    "Then she felt it. My cock pressed against her. Her panties pulled aside. Her legs spread wide."
    "Her gaze traveled down between their bodies."

    "The realization hit her like a thunderbolt."

    eris "YOU—!!!"

    scene eris_punch with fade

    "What followed was the worst beating I'd ever received."
    "And I include the time I sparred with Ghislaine in that assessment."

    "She launched me off her with a kick that would have killed a lesser man."
    "Fists. Kicks. A hay bale thrown at my head."
    "She grabbed a pitchfork and I had to use magic to deflect it."

    eris "YOU PERVERT! YOU DISGUSTING FILTHY PERVERTED ANIMAL!"

    rudeus "Eris, I can explain—"

    eris "EXPLAIN?! EXPLAIN WHAT?! Your DICK was TOUCHING my—!!!"

    "Her face turned so red I thought she'd burst a blood vessel."

    eris "YOU SPREAD MY LEGS! You pulled my panties aside! YOU WERE GOING TO—!!!"

    rudeus "I wasn't— I mean— I—"

    eris "YOUR PANTS ARE STILL DOWN, YOU IDIOT!"

    "I looked down. She was right. I scrambled to pull them up."
    "Another punch. Stars exploded in my vision."

    rudeus "OW! Eris, please—"

    eris "DON'T 'ERIS PLEASE' ME! I was SLEEPING and you— you—"

    "Her voice cracked. For a fraction of a second, I saw something beyond the fury."
    "Confusion. Embarrassment. And something else she'd never admit."

    eris "I was WET! I could FEEL it! Was that— did YOU—?!"

    rudeus "That was— you were already—"

    eris "DON'T FINISH THAT SENTENCE OR I WILL BURY YOU IN THIS BARN!"

    "She picked up another hay bale. This one was bigger."

    rudeus "Eris, calm down—"

    eris "I WILL NOT CALM DOWN!"

    scene eris_choke with fade

    "Her hand shot out and grabbed me by the throat."
    "With strength that shouldn't be possible for a girl her size, she shoved me backward."
    "I hit the ground hard, landing on my ass in the hay."
    "She stood over me, one hand still outstretched, breathing hard, face crimson."
    "She yanked her skirt down with one hand and fixed her panties with the other, all while glaring at me with the fury of a thousand suns."

    eris "If you EVER tell ANYONE about this, I will KILL you."
    eris "Not metaphorically. I will ACTUALLY kill you. With a SWORD. And then I'll resurrect you and kill you AGAIN."

    rudeus "I won't tell anyone. I promise."

    eris "And stop LOOKING at me! You've done ENOUGH looking for a LIFETIME!"

    rudeus "I'm sorry. I really am."

    eris "SORRY?! You were between my LEGS! You were RUBBING your— against my—!!!"

    "She couldn't finish. She screamed into her hands."

    eris "AAAAAAGH!"

    scene black with fade

    "She stomped toward the barn door."

    scene bg celeiro
    show rudeus normal at right:
        xzoom -1
    show eris base_clothes at left
    with dissolve

    "But she stopped. Right at the threshold."
    "Her back was to me. Her shoulders were shaking — but not from anger."
    "She was hugging herself, fingers digging into her arms."

    eris "...I felt it."

    rudeus "...What?"

    eris "When you were... grinding against me. I was half-awake for the last part."
    eris "I could feel it. Your... thing. Against my... my..."
    eris "It was HOT. And it felt..."

    "She slammed her fist against the door frame."

    eris "It felt GOOD, okay?! Is that what you want to hear?! IT FELT GOOD!"
    eris "And I HATE you for making me feel that! And I hate my STUPID body for reacting!"
    eris "And I hate that I was WET and you could FEEL it and—"

    "She pressed her forehead against the door frame."

    eris "...My panties were white. In case you didn't get a close enough LOOK."
    eris "Which you DID. Because you MOVED them."

    "She took a shuddering breath."

    eris "...If anyone's going to do that to me... I'd rather it be you than anyone else."
    eris "But NEXT TIME..."

    "She looked over her shoulder. Her eyes were glistening, her cheeks burning."

    eris "...Next time, at least have the guts to WAKE ME UP FIRST, you coward!"

    "She ran out of the barn."

    hide eris with dissolve
    show rudeus:
        ease 0.5 xalign 0.5

    "I lay there in the hay for a solid ten minutes."
    "My ribs hurt. My pride hurt worse. And something else was still throbbing."
    "I could still feel the ghost of her warmth against me."

    rudeus "(She said 'next time.')"
    rudeus "(...There's going to be a next time?)"

    "Tomorrow is going to be VERY awkward."

    $ eris_event = 5
    $ eris_on = False
    $ eris_afeicao += 5

    $ renpy.notify("Event complete! +5 Affection")
    jump passar_tempo





label eris_event_6:

    scene bg eris_castle
    with fade

    "Days had passed since the barn incident."
    "Every lesson, every meal, every hallway crossing — the tension was suffocating."
    "Eris couldn't look at me without turning crimson. I couldn't look at her without... remembering."

    "After today's sword training, Eris cornered me in the hallway."
    "Not with a punch this time. With words."

    show eris base_clothes at right
    show rudeus normal at left
    with dissolve

    eris "Rudeus. My room. Now."

    rudeus "...Am I about to get beaten again?"

    eris "Just COME!"

    rudeus "(She said 'my room, now.' A girl just dragged me to her bedroom.)"
    rudeus "(In my past life, the closest I got to this was being called to the teacher's office.)"
    rudeus "(...This is already better.)"

    scene bg eris_room
    with fade

    "She slammed the door behind us."
    "Her room was immaculate, as always. The bed was made. The curtains drawn."
    "She stood with her arms crossed, staring at the floor."

    show eris base_clothes at my_right
    show rudeus normal at my_left
    with dissolve

    eris "..."

    rudeus "Eris? What's this about?"

    eris "Shut up. I'm... I'm working up to it."

    "She paced back and forth. Three steps left. Three steps right."
    "Finally, she stopped and pointed at me."

    eris "You saw EVERYTHING. In the barn. Every... part of me."

    rudeus "Eris, I already apologized for—"

    eris "I'M NOT DONE!"

    "She took a shaky breath."

    eris "You saw me. All of me. My... my chest. My... down there. EVERYTHING."
    eris "And I've seen NOTHING of you!"

    rudeus "...What?"

    eris "It's not FAIR! You have an unfair advantage! You know what I look like and I don't know what YOU look like!"
    eris "In the Boreas family, debts are ALWAYS repaid! This is a matter of HONOR!"

    rudeus "...Are you asking me to strip?"

    eris "I'm DEMANDING it! For FAIRNESS! It has NOTHING to do with wanting to see your— I mean— SHUT UP!"

    "She was so red she looked like she might combust."

    rudeus "(She's been thinking about this for days. That's... kind of adorable.)"
    rudeus "(A beautiful noble girl is DEMANDING to see me naked.)"
    rudeus "(And she genuinely thinks this is about 'fairness.')"
    rudeus "(God bless the Boreas family and their insane sense of honor.)"

    rudeus "Alright. Fair is fair."

    eris "...Wait, really? Just like that?"

    rudeus "You're right. It IS unfair. I'll show you mine if you want."

    eris "I— good! FINALLY you're being reasonable! Just— do it! Before I change my mind!"

    show rudeus naked with dissolve

    "I undid my belt. Her eyes tracked every movement, wide and unblinking."
    "When I pulled my pants down, she stared."

    "For a very long time."

    eris "..."
    eris "...That's... that's it?"

    rudeus "...Thanks?"

    eris "It's not a COMPLIMENT! I just expected... well, it was DARK in the barn and it FELT bigger when it was pressing against my—"

    "She slapped both hands over her mouth."

    eris "FORGET I SAID THAT!"

    rudeus "It's not fully... ready yet, Eris."

    eris "Ready? What do you mean READY? It has MODES?!"

    rudeus "It gets bigger when... stimulated."

    eris "...How much bigger?"

    rudeus "Touch it and find out."

    "The room went dead silent."
    "She stared at me. Then at it. Then back at me."

    eris "...I'm only doing this for RESEARCH. For FAIRNESS. Don't get any ideas."

    "She stepped closer. Her hand reached out, hesitated, pulled back."
    "Reached out again. Pulled back."

    eris "It's not going to... DO anything, right? It won't attack me?"

    rudeus "It's not a snake, Eris."

    eris "It LOOKS like a snake!"

    "But she touched it. Just a fingertip at first. Barely grazing the surface."

    eris "It's... warm. And it—"

    "It twitched. Hard. Jumping against her finger like a living thing."

    eris "—KYAAA!!!"

    "She snatched her hand back like she'd touched a hot stove."
    "She stumbled backward, eyes wide with genuine horror."

    eris "IT MOVED! IT ATTACKED ME!"

    rudeus "It didn't attack you, it just—"

    eris "IT TWITCHED! AGAINST MY FINGER! Like it was trying to GRAB me!"

    rudeus "That's a normal—"

    eris "NORMAL?! There is NOTHING normal about a body part that MOVES ON ITS OWN!"

    rudeus "(...She looks like she just fought a demon and lost.)"

    "She was pressed against the wall, pointing at my crotch accusingly."
    "It twitched again. She flinched."

    eris "SEE?! It did it AGAIN! It's THREATENING me!"

    rudeus "Eris, it's literally just blood fl—"

    eris "I am NOT touching that with my hands! EVER! My hands are for SWORDS, not for... for TWITCHING THINGS!"

    rudeus "(This is really happening. Eris Boreas Greyrat is having a standoff with my penis.)"
    rudeus "(I'm in a girl's bedroom with my pants down and she's treating my dick like a hostile creature.)"
    rudeus "(If someone wrote this in a book, nobody would believe it.)"

    "But she didn't tell me to leave. She didn't look away either."
    "She was staring at it with a mix of fear and stubborn determination."
    "The Boreas pride wouldn't let her back down from a challenge — even this one."

    eris "...There has to be another way. To... make it do the bigger thing. Without TOUCHING it with my hands."

    rudeus "(Is she... actually trying to find a workaround?)"

    rudeus "Well... you could use your feet."

    "I said it as a joke. Half a joke. Maybe a quarter of a joke."

    eris "...My feet?"

    rudeus "I mean— it was just a suggestion, you don't have to—"

    eris "My feet don't have FINGERS. It can't GRAB my feet. That's... that's actually SMARTER."

    rudeus "(Wait. Wait wait wait. She's actually considering it?!)"

    "She looked down at her own feet. Then at me. Then at my cock, which chose that exact moment to twitch again."
    "She flinched. Then steeled herself."

    eris "FINE! I'll use my feet! It's the same as stepping on an enemy — I'm just... stepping on it GENTLY."

    rudeus "(Eris Boreas Greyrat is about to give me a footjob.)"
    rudeus "(I lived a full life in Japan and died without ever experiencing this.)"
    rudeus "(I was reborn into a fantasy world, and THIS is the scene God chose for me.)"
    rudeus "(...Thank you. Thank you, whoever is in charge up there.)"

    scene black with fade

    "She sat on the edge of the bed. I stood in front of her."
    "She extended one leg, her bare foot hovering inches from my cock."
    "Her toes were small, pale, and surprisingly delicate for someone who kicked things for a living."

    eris "...If it twitches against my foot, I'm kicking it."

    rudeus "Please don't."


    show vid_eris_foojob_idle with fade

    "She pressed her sole against me. Gently."

    "The softness was unexpected. Warm skin, smooth arch, the slight curve of her toes pressing against the shaft."

    rudeus "...!"

    eris "HA! You flinched! Now YOU know how it feels!"

    rudeus "(Oh god. Oh god it's actually happening.)"
    rudeus "(Her foot is on my— her FOOT is on my—)"
    rudeus "(It's so soft. HOW is it this soft? She trains with swords every day!)"

    "She brought her other foot up. Both soles pressed against my cock, sandwiching it."
    "The heat of her skin against me from both sides was maddening."

    eris "...It's really getting bigger. I can FEEL it growing between my feet."
    eris "That's... actually kind of fascinating. Disgusting, but fascinating."

    rudeus "(She's holding my cock between her feet and calling it 'fascinating.')"
    rudeus "(I have officially lost my mind. This can't be real.)"

    "She started to move. Awkward at first — sliding her feet up and down in uneven strokes."
    "Her toes curled and uncurled against the shaft, searching for the right grip."

    rudeus "That's... Eris, that feels incredible."

    eris "Obviously! My footwork is LEGENDARY! Ghislaine says my kicks are the best she's ever—"
    eris "Wait. This doesn't COUNT as footwork! This is DIFFERENT!"

    rudeus "(She's comparing this to sword training. She's actually categorizing this as a combat technique.)"
    rudeus "(I love this woman.)"

    "She found a rhythm. Her soles gliding up and down, squeezing on the upstroke."
    "When her toes reached the tip, they curled over the head — soft, warm pressure that sent electricity through my spine."

    rudeus "Ngh...!"

    eris "Another noise! I'm WINNING!"

    rudeus "(She thinks this is a competition. She's trying to BEAT me with a footjob.)"
    rudeus "(And honestly? She's winning.)"

    "Her feet moved faster. More confident. The warrior in her adapting, learning the rhythm."
    "She watched my face with laser focus, adjusting her technique based on every reaction."
    "When she pressed her toes hard against the underside of the head, my knees nearly buckled."

    eris "THERE! That spot! Your face went all weird when I pressed THERE!"

    "She pressed again. And again. Merciless."

    "Pre-cum leaked from the tip, coating her toes."

    eris "It's— it's getting SLIPPERY! What IS this stuff?!"

    rudeus "It means... you're doing really well."

    eris "I KNOW I'm doing well! I don't need YOUR validation!"

    "The slickness made her strokes smoother. Her feet glided effortlessly now."
    "The wet sounds filled the room. She stared at the scene between her feet — mesmerized despite herself."

    rudeus "(Her toes are glistening. Her face is bright red. She's biting her lip.)"
    rudeus "(I'm supposed to be the pervert here but she hasn't looked away ONCE.)"

    "She squeezed tighter. Her arches hugging the shaft, toes interlocking at the top."

    eris "Your face is getting more and more pathetic. Does this really feel that good?"

    rudeus "You... have no idea."

    eris "Hmph! Then we're getting close to EVEN!"

    "She kept going. Relentless. The same intensity she brought to swordplay."
    "Her arches hugging the shaft, toes interlocking at the top on every upstroke."

    rudeus "(This is insane. This is absolutely insane.)"
    rudeus "(Eris Boreas Greyrat is milking me with her feet and she's treating it like a training exercise.)"
    rudeus "(I can't... I can't hold it much longer...)"

    "Something was building inside me. Fast. Too fast."
    "The pressure was unbearable — her soft soles, the slickness, the way her toes curled around the head each time."

    "My breathing got heavy. Ragged. My hands were shaking."

    eris "...Your face looks strange. Are you okay? You're turning red."

    "I couldn't answer. My body was acting on its own."

    "My hands shot forward and grabbed her ankle."


    show vid_eris_footjob_pov with fade

    eris "H-HEY! What are you—"

    "I gripped both her ankles — hard — and squeezed her feet tighter around me."
    "She couldn't pull away. Both soles locked against my cock, trapped in my grip."

    eris "Rudeus?! Why are you grabbing— you're squeezing too HARD—!"

    "I started thrusting. Fast. Desperate."
    "Using her soft soles, pumping between them with frantic urgency."
    "All the restraint, all the careful composure — gone."

    rudeus "(I can't stop. I can't stop. She feels too good—)"

    "She stared at me — eyes wide, mouth half-open."
    "She'd never seen this expression on my face before. Raw. Desperate. Almost feral."

    eris "Rudeus! You're— you're going too FAST! What's happening to y—"

    "Her toes curled helplessly as I slammed forward one last time."

    call gozando from _call_gozando_8
    scene eris_footjob_03 with fade

    "Everything went white."

    "I came. Hard."
    "It shot across her feet, her ankles, up her shins, thick ropes splattering across her thighs."
    "Some of it reached her skirt. Some dripped down between her toes."
    "And a stray shot arced higher — landing right across her cheek and the corner of her lips."

    "Her eyes went wide as saucers."

    eris "...!!!"

    "She stared down at herself. At her feet — covered, dripping, glistening."
    "At the mess trailing up her legs."
    "Her hand went to her face. She touched the warm streak on her cheek, looked at her fingers."
    "At me — panting, still gripping her ankle, looking like I'd just lost a fight."

    eris "...WHAT is this?! It's on my FACE?!"

    rudeus "That's... that's what happens when..."

    eris "You SPRAYED me! Like a— like a FOUNTAIN! WITHOUT WARNING!"
    eris "My FEET are RUINED! And my SKIRT! Do you know how hard it is to explain stains to the maids?!"

    "She was waving her foot in the air, disgusted. Strings of cum connecting her toes."
    "But she wasn't screaming. She wasn't hitting me."
    "She was... examining it."

    eris "...It's warm. And thick. And it keeps COMING OUT."

    "She pressed her toes together, watching the white strands stretch between them."

    eris "...Is this what was going to go INSIDE me in the barn?"

    rudeus "...Yeah. Basically."

    eris "..."

    "Something flickered in her eyes. Not disgust. Not anger."
    "Curiosity. Raw, unfiltered curiosity."

    eris "...There's SO much of it. Does it always... come out this much?"

    rudeus "Only when it... feels really good."

    eris "So I did that? My FEET made you lose control like that?"

    rudeus "...Completely."

    "A strange expression crossed her face. Something between pride and fascination."

    eris "...Hmph. Of COURSE they did. I'm a Boreas. Even my FEET are superior."

    "She stared at her sole one more time, watching a droplet slide between her toes."

    eris "...You GRABBED me. At the end. You grabbed my foot and you couldn't STOP."
    eris "Your face was... I've never seen you look like that before."
    eris "Like you were going to DIE if you didn't finish."

    rudeus "...Sorry. I lost control."

    eris "I didn't say I MINDED! I said I've never SEEN it! There's a DIFFERENCE!"

    rudeus "(She's not angry. She's... turned on by the fact that she made me lose it.)"
    rudeus "(Eris Boreas Greyrat discovered she can break me with her feet and she's PROUD of it.)"

    scene bg eris_room
    with fade
    show rudeus normal at my_left
    show eris base_clothes at my_right
    with dissolve

    "We cleaned up in awkward silence."
    "She sat on the bed, arms crossed, staring at the wall."

    eris "...We're EVEN now. The debt is REPAID. This was purely about HONOR."

    rudeus "Of course."

    eris "Stop AGREEING with everything! It's suspicious!"

    "Silence."

    eris "...Rudeus."

    rudeus "Yeah?"

    eris "Your... thing. When it was... between my feet."
    eris "I could feel EVERYTHING. Every twitch. Every pulse. Through my SOLES."
    eris "The way it got HARDER right before you..."
    eris "And when you GRABBED me and started going FAST..."

    "She shook her head violently."

    eris "NEVER MIND! Forget I said anything!"

    "She grabbed the pillow and pressed it against her face."

    eris "My body keeps BETRAYING me around you and it's YOUR FAULT!"

    "She lowered the pillow. Her eyes were fierce but vulnerable."

    eris "...I want to know what the real thing feels like. Not just... feet."

    rudeus "...Eris?"

    eris "Your thing inside me. The REAL thing. Not feet. Not... whatever."

    "She turned away, hugging herself."

    eris "NOT NOW! I'm not ready! But... eventually. When I decide."
    eris "And it'll be MY choice. On MY terms. Got it?!"

    rudeus "Got it."

    eris "Good. Now GET OUT. I need to... process."

    "I headed for the door."

    eris "RUDEUS!"

    "I turned. She was sitting on the bed, one foot raised, staring at it."
    "At her toes. At the faint sticky residue still between them."
    "She wiggled them slowly, like she was replaying the sensation."

    eris "...My feet still feel warm. Where you... where it was."
    eris "And your thing really does get much bigger."

    rudeus "...Goodnight, Eris."

    eris "IT WAS AN OBSERVATION! NOT A COMPLIMENT!"

    scene black with fade

    "I left her room with my heart pounding."
    "She wanted to know what the real thing felt like."
    "Coming from Eris, that was practically a love confession."

    rudeus "(She's going to drive me insane.)"
    rudeus "(...And I'm going to enjoy every second of it.)"

    $ eris_event = 6
    $ eris_on = False
    $ eris_afeicao += 10

    $ renpy.notify("Event complete! +10 Affection")
    jump passar_tempo





label eris_event_7:

    scene bg eris_castle:
        matrixcolor TintMatrix("#88aaff")
    with fade

    "It was late. The mansion was quiet."
    "Most of the servants had retired. Ghislaine was on night patrol."
    "I was heading back to my room after a long day of lessons."

    "That's when I noticed it."
    "Eris' bedroom door was open. Not all the way — just a crack."
    "But enough to see inside."

    show rudeus normal at center
    with dissolve

    "I should have kept walking. A normal person would have kept walking."
    "But the barn incident had done something to my brain."
    "Like a door had been opened that I couldn't close."

    "I glanced through the crack."

    "And my heart stopped."


    show vid_eris_showing_butt with fade

    "Eris was on her bed. Face-down. Or rather... face to the side."
    "Her body was angled toward the door — toward ME."
    "She was completely naked. Every inch of pale skin on display."
    "No nightgown. No sheets. Just Eris."
    "Her back was arched, her hips raised, her legs slightly parted."

    "The position was unmistakable."
    "She was presenting herself. Deliberately."

    "The only thing she still wore were her panties — white, just like in the barn — pulled to the side."
    "I could see everything. The soft curves, the glistening skin, the way her body trembled slightly."

    rudeus "(...Is she... is this on purpose?)"

    "Her eyes were closed. Her breathing was slow and measured — TOO slow. TOO measured."
    "Nobody breathes like that in their sleep. She was faking."

    "And then — the tiniest movement."
    "Her hips shifted. A slow, deliberate roll. A gentle rock backward, toward the door."
    "Toward me."

    "One eye cracked open. Just barely. Just enough to check if I was watching."
    "Our eyes met for a fraction of a second before she squeezed it shut again."

    rudeus "(She KNOWS I'm here. She WANTS me to see this.)"

    "My body moved before my brain could stop it."
    "I pushed the door open and stepped inside."

    "The moment the door creaked, her whole body tensed."
    "But she didn't move. Didn't scream. Didn't throw anything."

    "She just lay there. Trembling. Waiting."



    scene black with fade

    "I approached the bed. My footsteps were deafening in the silence."
    "She was still 'sleeping.' Still arching. Still rocking her hips in that slow, maddening rhythm."

    "I stood at the edge of the bed. Close enough to touch her."

    rudeus "...Eris."

    "No response. Just a tiny hitch in her breathing."

    rudeus "I know you're awake."

    "Silence."
    "Then — in a voice so small I barely recognized it —"

    eris "...Shut up."

    rudeus "Your eyes were open a second ago."

    eris "They were NOT! I was SLEEPING!"

    rudeus "You don't sleep with your hips in the air."

    eris "I DO! It's... it's a NOBLE sleeping position! The Boreas family has ALWAYS—"

    rudeus "Eris."

    eris "...FINE!"

    scene eris_sex_01_5 with fade

    "She turned her head to face me. Her face was burning crimson."
    "But her body didn't change position. She stayed exactly where she was."
    "Hips up. Legs apart. Everything exposed."

    "Her eyes were fierce — but not with anger."
    "With frustration. The kind that comes from wanting something and not knowing how to ask."

    eris "Since that day in the barn, I can't stop THINKING about it!"
    eris "The way you LOOKED at me! Nobody's ever looked at me like that!"
    eris "And every night I keep thinking about your stupid face staring at my—"

    "She grabbed a pillow and screamed into it."

    eris "AAAAAAGH!"

    "She emerged, red-faced, eyes blazing."

    eris "Just— just do it already! Put it in! Like you were going to do at the barn!"

    rudeus "I wasn't going to do anything at the barn! I was fixing your sk—"

    eris "LIAR! You WANTED to! I could see it! You wanted me and you were TOO CHICKEN to do anything!"
    eris "So I'm making it EASY for you because you're clearly TOO STUPID to take a hint!"

    "She gestured at her own naked body — at the panties pulled aside, at everything on display."

    eris "What do I have to do?! Send a LETTER?! Draw a MAP?!"

    "I stared at her."
    "This furious, red-faced, trembling girl who had set up an elaborate 'accidental' seduction scene"
    "and was now YELLING at me for not taking the bait fast enough."

    "This was the most Eris thing that had ever happened."

    rudeus "...Eris. I want to. Believe me, I want to."

    eris "THEN WHY ARE YOU STILL TALKING?!"

    rudeus "Because... I need a little help first."

    "I said it with the most innocent expression I could manage."
    "In truth, I was already rock-hard. But I wanted to see her react."

    eris "Help?! Help with WHAT?!"

    "I gestured downward."

    eris "..."
    eris "...You mean your...?"

    rudeus "It needs to be... ready. And it would go faster if you helped."

    eris "W-What do you mean 'helped'?! How am I supposed to—"

    menu:
        "Ask her to use her mouth":
            rudeus "With your mouth."

            "The silence that followed could have cracked stone."
            "Eris' face went through about seven colors in three seconds."

            eris "MY MOUTH?! You want ME to... with my MOUTH?! On YOUR...?!"
            eris "You are the most SHAMELESS, PERVERTED—"

            rudeus "You're the one who set this up."

            eris "...!"

            "She opened her mouth. Closed it. Opened it again."
            "For once in her life, Eris Boreas Greyrat had no comeback."

            eris "...FINE! But only because YOU need help, not because I WANT to!"
            eris "And if you tell ANYONE, I swear on the Boreas name, I will END you!"

            scene black with fade

            "She slid off the bed and knelt in front of me."
            "Her hands were shaking. Her face was on fire."
            "She stared at my crotch like it was an enemy she needed to defeat."

            eris "...How do I... do you just... ugh, this is STUPID!"

            rudeus "Just start slow. Use your lips first."

            eris "I KNOW how it works! I'm not an IDIOT! ...Ghislaine told me about... stuff."

            "She pulled down my pants with the same aggressive energy she used for everything."
            "When she saw it, she froze — but not from surprise. She'd seen it before, during the footjob."
            "But seeing it THIS close, right in front of her face... that was different."

            eris "...It looks even more intimidating from this angle."

            rudeus "You've seen it before."

            eris "SEEING it and having it IN MY FACE are TWO DIFFERENT THINGS!"
        "Skip the blowjob — go straight to the main event":

            rudeus "Never mind. I'm already ready."

            eris "...You ARE?! Then why did you say you needed help?!"

            rudeus "I wanted to see your reaction."

            eris "YOU— I'M GOING TO KILL YOU!"
            eris "After this! I'll kill you AFTER!"

            "I pulled my pants down. She stared."

            eris "...It's already... like THAT?!"

            rudeus "I told you. I was ready."

            eris "THEN STOP WASTING TIME AND—"

            jump eris_event_7_fingering

    "She took a deep breath. Steeled herself like she was about to charge into battle."
    "Then she leaned forward and pressed her lips against the tip."




    show vid_eris_blowjob_01 with fade

    "The contact was electric."
    "Her lips were soft — softer than I expected from someone who punched walls recreationally."
    "She was clumsy, unsure, but determined."

    eris "Mmph... is... is this right?"

    rudeus "Y-Yeah... just like that..."

    "She took more of me into her mouth. Her tongue pressed against the underside clumsily."
    "She gagged slightly and pulled back, eyes watering."

    scene eris_blowjob_talking with fade

    "Even as she pulled away, her hand stayed wrapped around the shaft."
    "Her fingers moved on their own — slow, absent strokes — like she didn't even realize she was doing it."

    eris "This is DISGUSTING! How does ANYONE do this voluntarily?!"

    "Her grip tightened slightly. Her thumb brushed the tip. Still stroking."
    "She hadn't noticed. Or she was pretending not to."

    rudeus "You don't have to—"

    eris "I SAID I'd do it so I'm DOING it! A Boreas NEVER backs down!"


    show vid_eris_blowjob_01 with fade

    "She went back in. This time deeper. More confident."
    "Her tongue moved with more purpose, swirling around the tip."
    "She was learning — adapting — the same way she did in combat."
    "Turning something unfamiliar into something she could dominate."

    "And despite her protests, her eyes had changed."
    "The disgust was gone. Replaced by something intense. Focused."
    "She was studying my reactions. Watching what made me twitch, what made me gasp."
    "Cataloging it. The warrior in her was turning this into a skill to master."

    "Her head bobbed faster. Her hands gripped my thighs."
    "Small sounds escaped her throat — muffled, wet, somewhere between effort and... enjoyment."

    eris "Mmm... mph..."

    "She pulled back with a wet pop, a string of saliva connecting her lips to my cock."
    "Her face was flushed, eyes half-lidded, breathing hard."
    "She looked furious. She looked beautiful."

    scene eris_blowjob_talking with fade

    eris "There! That's ENOUGH! You're ready now, RIGHT?!"

    rudeus "...Yeah. More than ready."

    label eris_event_7_fingering:

    rudeus "But now it's your turn."

    eris "My turn?! My turn for WHAT?!"

    rudeus "You need to be ready too. If I just put it in, it'll hurt."

    eris "I told you I don't feel PAIN! I'm a Bore—"

    rudeus "Eris. Trust me."

    "Something in my voice made her stop."
    "She stared at me. Then, slowly, sat back on the bed."

    eris "...Fine. What do I have to do?"

    rudeus "Nothing. Just lie back."

    scene black with fade

    "She lay down, stiff as a board, arms at her sides like a soldier awaiting inspection."
    "Her bare skin glowed in the dim light. The only thing she still wore were those white panties."

    "I hooked my fingers into the waistband."

    eris "W-Wait! What are you—!"

    "I slid them down. Slowly. Past her thighs, her knees, her ankles."
    "She was trembling. Not from cold."
    "I tossed them aside and looked at her. All of her. Completely bare."

    eris "...D-Don't just STARE!"

    "I knelt between her legs and spread them apart with both hands."

    eris "H-Hey! What are you— don't just SPREAD me open like—!"

    "I leaned in."
    "She must have expected fingers. A touch. Something."
    "She didn't expect my mouth."

    scene eris_sex_02 with fade

    "I pressed my lips against her inner thigh first. She flinched."

    eris "What are you DOING down th—"

    "I dragged my tongue along her slit. One slow, deliberate lick from bottom to top."
    "The sentence died in her throat."

    eris "—!!!"

    "The taste hit me immediately. Warm. Faintly sweet. Unmistakably her."
    "I could feel her opening up under my tongue — her folds soft, slick, twitching at every pass."

    eris "R-Rudeus...! That's your... your TONGUE! You're using your TONGUE there?!"

    "I didn't answer. I licked again. Slower this time, savoring her."
    "Her thighs trembled on either side of my head. Her hips shifted involuntarily."

    "I couldn't believe this was happening."
    "Eris Boreas Greyrat — flushed, trembling, coming undone under my tongue."

    "I found her clit. The tip of my tongue circled it once."
    "Her back arched clean off the bed."

    eris "WHAT— WHAT IS— DO THAT AGAIN!"

    "I did it again. And again. Slow circles, then fast flicks."
    "Her hands grabbed my hair and PULLED."

    eris "Ah—! Hah—! That's... why does... Rudeus...!"

    "Her taste grew stronger. Wetter. I could feel her pulsing against my lips."
    "I pressed my tongue flat against her, lapping at everything she gave me."

    "She was melting. The fierce, proud Eris — reduced to gasps and half-words."

    eris "Don't... stop... if you stop I'll KILL—! Ahhh...!"

    "I pushed my tongue inside her."
    "Her whole body seized. Her back arched so hard her shoulders lifted off the mattress."
    "Her thighs clamped around my head like a vice."

    eris "INSIDE?! You put it INSIDE?! That's— that's—!!"

    "I curled my tongue, pressed deeper."
    "Her inner walls clenched around it — hot, tight, quivering."
    "Her hips bucked against my face, grinding shamelessly."

    eris "Something's... happening... I can't... Rudeus, I CAN'T—!"

    "I moved back to her clit and sucked gently while my tongue flicked across it."
    "That was all it took."

    "Her body locked up. Every muscle rigid."
    "She arched off the bed — mouth open, eyes wide, no sound coming out."
    "Then the wave hit her and she SCREAMED."

    scene black with fade

    "Her thighs crushed my head. Her hands nearly ripped my hair out."
    "I felt her pulse against my mouth — fast, rhythmic contractions that seemed to go on forever."
    "A rush of warmth flooded over my lips and chin."

    scene eris_sex_03 with fade

    "She collapsed, gasping, trembling, her legs still twitching."

    eris "Wh... what the HELL... was that...?!"

    rudeus "That's what 'ready' feels like."

    "I wiped my mouth. Her taste lingered."

    eris "...It felt like I was going to DIE. In a GOOD way."
    eris "You did THAT... with your MOUTH?! That's even more perverted than I thought you were!"

    rudeus "Says the girl who just crushed my skull with her thighs."

    eris "SHUT UP! That was... involuntary! My body MOVED ON ITS OWN!"

    "She was still trembling. Still wet. Still clenching around nothing."
    "Her body was open. Relaxed. Ready."

    eris "...Okay. NOW put it in. Before the feeling goes away."
    eris "And I am NOT saying please!"

    scene black with fade

    "She was still limp. Still trembling. Her legs barely holding."
    "I didn't give her time to recover."

    "I slid my hands under her — one behind her back, one under her thighs — and lifted her."

    scene eris_sex_04 with fade

    eris "Wh— HEY! What are you— put me DOWN!"

    "She was light. Lighter than I expected."
    "Her body was hot against mine, slick with sweat, still shaking from the aftershocks."
    "She tried to push against my chest but her arms had no strength."

    eris "I can WALK! I don't need you to— my legs just... they won't..."

    rudeus "I know."

    "I set her down on the edge of the bed. She swayed."
    "Her eyes were glazed, unfocused. Her red hair stuck to her flushed cheeks."
    "She looked drunk. Drunk on what I'd just done to her."

    "I turned her around gently. She let me — too dazed to argue."

    "Her body was trembling. Not from fear. From anticipation."
    "Every inch of pale skin on display — flushed, glistening, completely bare."

    eris "...Just... hurry up... before my legs give out completely..."

    rudeus "Since when does a Boreas admit weakness?"

    eris "I'm not WEAK! My body is just... STUPID right now! Because of YOUR stupid mouth!"

    scene black with fade

    "I positioned myself at her entrance. She was wet — incredibly wet."
    "Her body was honest even when her mouth wasn't."
    "The heat radiating from her was almost scorching."

    rudeus "This might hurt a little at first."

    eris "I'm a Boreas! I don't feel PAIN! ...Maybe a little. Just— be... be careful."
    eris "NOT because I'm SCARED! Because I don't want you messing it up!"

    "I pressed forward. Slowly."


    show vid_eris_vaginal with fade

    "The moment I entered her, she gasped — sharp, sudden, her back arching violently."
    "Her fingers clawed at the sheets."

    eris "Ngh...! W-Wait—! It's... it's big...!"

    rudeus "Should I stop?"

    eris "I said WAIT, not STOP! There's a DIFFERENCE! ...Just... go slow. SLOWLY!"

    "I pushed deeper. Inch by inch."
    "She was incredibly tight — her body resisting and accepting at the same time."
    "Her insides squeezed around me — impossibly tight, burning hot, pulling me in like she never wanted to let go."
    "Every inch deeper pulled another sound from her throat."
    "Small, desperate sounds she didn't even try to hide."
    "She was looking at me. Not away. Not into a pillow. Directly at me."
    "Her eyes were glassy, half-lidded, cheeks flushed crimson — shy and fierce at the same time."
    "Like she wanted to see every expression on my face as I filled her."

    eris "...Mmph...! Ah...! It's... inside... it's all the way..."

    rudeus "Are you okay?"

    eris "I'm FINE! Stop asking! Just... move! Do the... the thing!"

    "'The thing.' Only Eris could describe sex like that."

    "I started moving. Slowly. Gently."
    "Her body reacted to every thrust — small jerks, muffled gasps, her hips unconsciously pushing back to meet me."

    eris "Ah...! Ngh...! That's... why does it... why does it feel...!"

    "She was trying so hard to stay angry. To maintain control."
    "But her body was telling a completely different story."
    "Her back arched deeper with every thrust. Her hips rocked back faster."
    "The wet sounds of our bodies connecting filled the room."

    rudeus "You can let go, Eris. It's just us."

    eris "I AM NOT holding baaack— AH!"

    "I thrust harder. She screamed into the pillow."

    eris "AGAIN! Do that AGAIN!"

    "I did."

    eris "AH! ...Why is this... why does it feel... so GOOD?!"
    eris "This is STUPID! Sex shouldn't feel this good! It's not FAIR!"

    "She was unraveling. The angry shell cracking apart with every thrust."
    "Her moans grew louder, less controlled."
    "She stopped trying to muffle them with the pillow."

    eris "Rudeus...! Harder...! I said HARDER, you wimp!"

    "I grabbed her hips tighter and gave her what she wanted."
    "The sound that came out of her wasn't a scream. It was a howl."

    eris "YES! Like THAT! Don't you DARE stop!"

    "Her body moved with the same ferocity she brought to everything."
    "No hesitation. No restraint. Pure, overwhelming intensity."
    "She slammed her hips back against me, meeting every thrust with equal force."
    "The bed creaked. The headboard hit the wall."

    "She was sweating now, her red hair sticking to her face and neck."
    "Her pale skin was glistening with sweat, every curve of her body on display."
    "Every muscle in her body was taut, straining, reaching for something."

    eris "Something's... something's HAPPENING! Rudeus! What's— what is—"

    rudeus "Let it happen. Don't fight it."

    eris "I'm not FIGHTING it! I don't fight things I— AH! AHHH!"

    "Her whole body locked up."
    "Her back arched so sharply I thought it might break."
    "Her inner walls clamped down on me — impossibly tight, pulsing, squeezing in waves."
    "A scream tore from her throat. Raw. Unfiltered. The most honest sound she'd ever made."

    eris "RUDEUS—!"

    "She came. Hard. Violently. The same way she did everything."
    "Her body convulsed, her hips slamming back against me over and over."
    "I couldn't hold back anymore."

    rudeus "Eris... I'm going to—"

    eris "I don't CARE! Just— don't pull out! If you pull out I'll KILL you!"

    "She reached back and grabbed my arm with a grip that could bend steel."
    "And she pulled me deeper."

    call gozando from _call_gozando_10
    scene eris_sex_06 with fade

    "I came inside her. Everything. All of it."
    "Her body seized up again — a second orgasm hitting her before the first had even finished."
    "Her scream dissolved into something broken and desperate."
    "She buried her face in the pillow, muffling sounds that would have woken the entire mansion."

    scene black with fade

    "Her arms gave out. She collapsed face-first into the pillow."
    "Her hips stayed raised for a moment longer — twitching, clenching — before they too sank down."
    "She lay there, a trembling, sweating mess, face hidden in the pillow."

    scene eris_sex_07 with fade

    "I could see my seed leaking out of her, trailing down her inner thighs."
    "My hand found her ass — squeezing gently, kneading the soft flesh."
    "I watched it drip. Thick, white trails running down her skin."
    "My thumb traced along her inner thigh, smearing through it absently."
    "Her body still shuddered with aftershocks, tiny spasms that rippled through her."

    eris "...You're... staring again... pervert..."

    "She didn't tell me to stop. Her hips even pushed back slightly into my hand."

    "She was quiet for a long time. Just breathing. Just existing."

    "Then, muffled by the pillow:"

    eris "...hah... hah... hah..."

    "A pause."

    eris "...why... why didn't we do this SOONER?!"

    "I laughed. I couldn't help it."

    eris "Don't LAUGH! I asked a legitimate QUESTION!"

    scene bg eris_room:
        matrixcolor TintMatrix("#88aaff")
    with fade
    show rudeus naked at my_left
    show eris naked at my_right
    with dissolve

    "She rolled onto her back, staring at the ceiling."
    "Her face was red. Her hair was a mess. Her body still bare, marked with sweat."
    "But her eyes... they were soft. Vulnerable."

    eris "...Rudeus."

    rudeus "Yeah?"

    eris "If you tell anyone about this night... about the sounds I made... about me asking you to..."

    rudeus "I won't tell a soul."

    eris "...Good."

    "Silence."

    eris "...I wasn't REALLY faking sleep, by the way."

    rudeus "Yes you were."

    eris "I was NOT! I was... resting my eyes! In a... strategic position!"

    rudeus "A 'strategic position.' With your panties pulled to the side."

    eris "THAT WAS THE WIND!"

    rudeus "We're indoors."

    eris "INDOOR WIND! It exists!"

    "She punched my arm. Hard. Then she curled up against me."

    eris "...Don't move. I'm... I'm sleeping here tonight."
    eris "NOT because I want to be close to you! I'm just... too tired to go to my own bed. Which is THIS bed. But STILL."

    rudeus "Whatever you say, Eris."

    eris "...Rudeus?"

    rudeus "Hmm?"

    eris "...Next time... you don't need the... the 'help' excuse. Just... come to me."
    eris "But KNOCK first! I need time to... prepare my STRATEGIC POSITION!"

    "I looked at her. This furious, impossible girl who had just given me everything."
    "I couldn't help but smile."

    rudeus "...Heh. Yeah. Goodnight, Eris."

    eris "...What's so funny?!"

    rudeus "Nothing. Just... happy."

    "She stared at me. Her mouth opened — then closed."
    "For a second, her eyes went soft. Really soft."

    eris "...Idiot. ...Goodnight."

    scene black with fade

    "She was asleep within minutes. Curled against my chest like an angry kitten."
    "Her fist was still clenched, even in sleep. Probably dreaming of punching something."

    "Eris Boreas Greyrat."
    "Violent. Stubborn. Loud. Foul-mouthed."
    "And completely, utterly mine."

    $ eris_event = 7
    $ eris_on = False
    $ eris_afeicao += 25
    $ renpy.notify("Your bond with Eris has deepened. +25 Affection")
    jump passar_tempo





label eris_bj_intro_label:

    scene bg eris_castle
    with fade

    "Ghislaine had left for her afternoon patrol. The training yard was empty."
    "Eris was leaning against the wall, arms crossed, looking bored out of her mind."

    show rudeus normal at my_left
    show eris base_clothes at my_right
    with dissolve

    "This was my chance."

    rudeus "Hey, Eris."

    eris "What?"

    rudeus "Ghislaine's gone for a while..."

    "She narrowed her eyes."

    eris "...Why are you saying it like that? Why do you have that LOOK on your face?"

    rudeus "What look?"

    eris "The look that means you're about to say something perverted!"

    rudeus "I was just thinking... about what you did for me that night. With your mouth."

    "Her face went scarlet instantly."

    eris "WH— Don't just bring that up out of NOWHERE! What if someone HEARS you?!"

    rudeus "No one's around. Ghislaine's gone. The servants are in the west wing."

    eris "So WHAT?! That doesn't mean I'm going to— you can't just ASK me to—"

    "She was already looking around, checking corners, making sure no one was watching."

    rudeus "You don't have to. I just thought—"

    eris "I KNOW what you thought! You thought 'Ghislaine's not looking, so I can get Eris to...' UGH!"

    "She grabbed my wrist."

    eris "COME ON. Before she gets back!"

    scene black with fade

    "She dragged me behind the storage building, shoving me against the wall."

    eris "If ANYONE finds out about this—"

    rudeus "I know, I know. The Boreas name. You'll end me."

    eris "Don't say it like it's a JOKE! I WILL!"

    "She glared at me. Then dropped to her knees."
    "Her hands went straight for my belt — yanking, pulling, aggressive as always."
    "She didn't fumble this time. She'd learned."

    "She pulled my pants down with one sharp tug."
    "My cock sprang free. She stared at it, frowning, like sizing up an opponent."

    eris "...Hmph. Let's get this over with."


    show vid_eris_blowjob_2 with fade

    "She didn't hesitate. Her lips wrapped around the tip and she pushed forward."
    "No more clumsy first-timer. She remembered what worked."
    "Her tongue pressed against the underside, swirling as she took me deeper."

    eris "Mmph..."

    "Her head bobbed steadily. One hand gripped the base, squeezing in rhythm."
    "She was efficient. Focused. Treating it like a combat drill."

    rudeus "E-Eris... you've gotten better at this..."



    eris "Obviously! I'm a FAST LEARNER!"

    "She went back in immediately. Deeper this time."
    "Her other hand gripped my thigh, nails digging into skin."
    "She was picking up speed — sloppy, wet sounds filling the narrow gap between buildings."



    "I felt it building. Fast."

    rudeus "Eris... I'm going to—"

    "She didn't pull back. She looked up at me — defiant, determined."
    "Like pulling away would be admitting defeat."

    scene eris_blowjob_generic_cum with fade

    "I came. In her mouth. Hard."
    "Her eyes went wide. She froze, cheeks puffing slightly."

    "She pulled back, hand over her mouth, eyes watering."

    eris "MMPH—! Wh— what IS this?! It's THICK! And SALTY! And WARM!"

    "She swallowed. Then immediately looked like she regretted it."

    scene eris_blowjob_generic_post_cum with fade

    eris "That was DISGUSTING! Why didn't you WARN me?!"

    rudeus "I literally said 'I'm going to—'"

    eris "You should have said it EARLIER! And LOUDER! And with more URGENCY!"

    "She wiped her mouth with the back of her hand, face burning red."
    "But through the disgust... there was something else."
    "A small, almost imperceptible look of satisfaction."
    "She'd finished what she started. A Boreas never backs down."

    scene black with fade

    eris "...Don't think this is going to be a regular thing!"

    rudeus "Of course not."

    eris "I MEAN IT!"

    "She punched my arm. Hard."
    "Then walked away, still wiping her mouth, muttering curses under her breath."

    $ eris_bj_intro = False
    $ eris_afeicao += 10
    $ eris_interacted_today = True
    $ renpy.notify("+10 Affection with Eris!")
    jump passar_tempo





label eris_bj_generic:

    scene bg eris_castle
    with fade

    python:
        bj_setup = renpy.random.choice([
    ("Ghislaine went to talk to Father. She'll be gone for at least an hour.",
    "So?",
    "So... we have time.",
    "Time for WHAT?! ...Oh. You mean THAT again?!"),
    ("I glanced around. The hallway was empty. Ghislaine was nowhere in sight.",
    "...Why are you looking around like a criminal?",
    "Just making sure we're alone.",
    "ALONE?! Why would we need to be— oh. OH. You're SHAMELESS!"),
    ("Eris was practicing her swings in the courtyard. Ghislaine had been called away.",
    "What do you WANT? I'm busy!",
    "Ghislaine's gone...",
    "And?! ...AND?! Don't give me that look! FINE! But we're being QUICK about it!")
])

    show rudeus normal at my_left
    show eris base_clothes at my_right
    with dissolve

    "[bj_setup[0]]"

    eris "[bj_setup[1]]"

    rudeus "[bj_setup[2]]"

    eris "[bj_setup[3]]"

    "She looked around one more time — then grabbed my wrist and pulled me somewhere private."

    scene black with fade

    "She was already on her knees before I could say anything."
    "Her hands grabbed my belt and yanked my pants down — quick, rough, impatient."

    eris "Hurry up and... stand still! Stop MOVING!"


    show vid_eris_blowjob_2 with fade

    python:
        bj_middle = renpy.random.choice([
    ("She took me in her mouth without a word. No hesitation.",
    "Her technique was improving every time. She'd figured out the rhythm — what pace drove me crazy.",
    "Her tongue swirled around the tip, then she plunged deeper, humming against me."),
    ("She spat on her palm and gripped me first, stroking a few times before wrapping her lips around the head.",
    "She was rougher today. More confident. Like she was trying to prove something.",
    "Her head bobbed fast, each push going deeper than the last."),
    ("She started slow this time. Just the tip. Her tongue tracing lazy circles.",
    "She watched my face the whole time, cataloging my reactions like she was studying a combat technique.",
    "When she found what made me shudder, she doubled down — relentless, focused.")
])

    "[bj_middle[0]]"
    "[bj_middle[1]]"
    "[bj_middle[2]]"

    "Her breathing got heavier. Muffled sounds escaped her throat."

    rudeus "I'm close..."

    python:
        bj_finish = renpy.random.choice([
    ("She pulled back just in time. The first shot hit her cheek. She flinched.",
    "...You got it on my FACE! Do you have ANY idea how hard this is to explain?!",
    "She wiped it off furiously, face burning. But she didn't seem truly angry."),
    ("She kept going. Pushed through. Swallowed everything without stopping.",
    "...There. Are you SATISFIED now?!",
    "She wiped her mouth and looked away, ears bright red."),
    ("She pulled off and finished me with her hand — fast, firm strokes.",
    "...Ugh. It's everywhere. You're CLEANING this up!",
    "She stared at the mess with equal parts disgust and fascination.")
])

    scene eris_blowjob_generic_cum with fade

    "[bj_finish[0]]"
    eris "[bj_finish[1]]"
    "[bj_finish[2]]"

    eris "...Don't get used to this."

    rudeus "Too late."

    eris "I SAID— ugh! You're impossible!"

    $ eris_afeicao += 10
    $ eris_interacted_today = True
    $ renpy.notify("+10 Affection with Eris!")
    jump passar_tempo





label eris_sex_intro_label:

    scene bg eris_castle
    with fade

    show rudeus normal at my_left
    show eris base_clothes at my_right
    with dissolve

    "I found Eris in the garden, practicing her stances."
    "Ghislaine was across the estate, training the junior guards."

    rudeus "Eris."

    eris "What? Can't you see I'm BUSY?"

    "I leaned close to her ear."

    rudeus "I want you. Right now."

    "She nearly dropped her sword."

    eris "WH— HERE?! Are you INSANE?! We're OUTSIDE!"

    rudeus "Then let's find somewhere private."

    eris "We can't just— in the middle of the DAY— what if someone SEES?!"

    "Her face was on fire. But her free hand was already gripping my sleeve."

    eris "UGH! This is YOUR fault! If we get caught, YOU'RE explaining it!"

    scene black with fade

    "She grabbed my wrist and dragged me away."
    "We ducked through a side corridor, past the unused storage rooms, around a corner."
    "She shoved me through the last door and slammed it shut behind us."

    eris "FINE! But we're being FAST! Before Ghislaine finishes with the guards!"

    "The second the door closed, she hiked her skirt up."
    "All the way up. Past her thighs. Past her hips."
    "She was wearing white panties. She hooked her thumbs into the waistband and shoved them down to her knees in one quick motion."

    eris "There! HAPPY?! Now hurry up before I change my MIND!"

    "She was already wet. I could see it glistening on her inner thighs."
    "Her body was honest. Always had been."

    "I closed the distance. My hands found her hips."
    "I turned her around and bent her forward — her palms flat against the wall, back arched."


    show vid_eris_vaginal_2 with fade

    eris "W-Wait! Not so ROUGH! ...Actually, no. Be rough. I don't CARE!"

    "I pushed inside her. One thrust."
    "Her head dropped between her arms. Her mouth fell open."

    eris "Ngh—! AH! You just— without even—!"

    rudeus "You said hurry."

    eris "I didn't mean THAT fast! ...D-Don't stop though!"

    "I set the pace. Hard. Fast. No pretense."
    "Her fingers clawed at the wooden planks. Her nails dug into the grain."
    "Every thrust pushed a sound out of her — sharp, bitten off, like she was trying to swallow them."

    eris "Hah— ah— why does it— feel different— standing up—!"

    rudeus "Better?"

    eris "SHUT UP and keep GOING!"

    "The wooden wall creaked with every push."
    "Her arms were shaking, barely holding her up."
    "Her skirt was bunched around her waist, her pale back arched, completely exposed."

    "She pressed her forehead against the wall to muffle the sounds."
    "Her breath was hot. Ragged. Interrupted by small whimpers she'd never admit to."

    eris "Mmph...! Rudeus...! Faster— I said FASTER!"

    "I gave her what she wanted."
    "Her whole body started shaking. I could feel her clenching rhythmically around me."

    eris "Something's— I'm going to— AGAIN— like that night—!"

    "She bit down on her own arm. HARD. Muffling the scream that tore through her."
    "Her body locked up — pulsing, clenching, pulling me in."

    "That was enough to take me over the edge."

    scene eris_vaginal_generic_cum with fade

    "I came inside her. Pressed deep, pinning her against the wall."
    "She shuddered — a second wave hitting her, smaller, dragged out."

    "Her arms finally gave out. She slumped forward against the wall."
    "Breathing. Trembling."

    eris "...Pull my panties back up."

    "I knelt down and slid them back up her legs. She shivered at the touch."
    "She turned around slowly, grabbing my arm for balance."

    eris "...My legs are shaking. This is YOUR fault."

    rudeus "Worth it?"

    eris "......"
    eris "...Maybe."
    eris "If you tell ANYONE—"

    rudeus "Boreas name, you'll end me. I know."

    scene black with fade

    "She punched my arm. Pulled her skirt down. Straightened her hair."
    "She cracked the door open, peeked both ways, then slipped out."
    "Walking like nothing happened — except for the subtle wobble in her step."

    $ eris_sex_intro = False
    $ eris_afeicao += 10
    $ eris_interacted_today = True
    $ renpy.notify("+10 Affection with Eris!")
    jump passar_tempo





label eris_sex_generic:

    scene bg eris_castle
    with fade

    python:
        sex_setup = renpy.random.choice([
    ("Ghislaine went to report to Father. The training field was deserted.",
    "...You have that look again. The perverted one.",
    "What look?",
    "The look that means I need to find somewhere with a WALL! Come on, before she gets back!"),
    ("I found Eris between lessons. The hallway was empty.",
    "If you're going to suggest what I THINK you're suggesting—",
    "Somewhere private?",
    "You're UNBELIEVABLE! ...Last door on the left. It's more private. NOT that I've checked or anything!"),
    ("Eris was stretching after her sword practice. I watched for a moment too long.",
    "...Are you staring at my legs?",
    "Maybe.",
    "UGH! Fine! But you OWE me dessert after this! TWO desserts!")
])

    show rudeus normal at my_left
    show eris base_clothes at my_right
    with dissolve

    "[sex_setup[0]]"

    eris "[sex_setup[1]]"

    rudeus "[sex_setup[2]]"

    eris "[sex_setup[3]]"

    "She grabbed my wrist. We disappeared around the nearest corner."

    scene black with fade

    "The second we were alone, she hiked her skirt up."
    "No hesitation. She already knew the routine."
    "Panties shoved down. Bent against the wall. Eyes daring me to keep up."

    eris "Well?! What are you waiting for, an INVITATION?!"


    show vid_eris_vaginal_2 with fade

    python:
        sex_middle = renpy.random.choice([
    ("I lifted her. She locked her legs around me immediately — practiced, natural.",
    "She gasped when I pushed in — a sharp, hungry sound she'd stopped trying to hide.",
    "The pace was hard from the start. She didn't want gentle. She wanted release."),
    ("She turned around this time. Hands flat against the wall. Looking back over her shoulder.",
    "The view nearly killed me. Her skirt around her waist, her back arched, waiting.",
    "I grabbed her hips and pushed inside. She moaned through clenched teeth."),
    ("I pressed her against the wall, face to face. She wrapped her arms around my neck.",
    "Her eyes locked onto mine as I entered her — defiant, daring, burning.",
    "She kissed me. Hard. Like she was trying to prove she could do that aggressively too.")
])

    "[sex_middle[0]]"
    "[sex_middle[1]]"
    "[sex_middle[2]]"

    "The sounds she made echoed off the walls — muffled, desperate, angry at herself for making them."

    eris "Hah— don't you DARE slow down—!"

    python:
        sex_finish = renpy.random.choice([
    ("She came first. Clenching around me, biting her lip hard enough to draw blood.",
    "I followed seconds later. Deep inside. She shuddered at the warmth.",
    "...Again? Inside? You're going to get us in TROUBLE!"),
    ("We came together. Her body arched against mine, trembling, nails raking my back.",
    "She pressed her face into my chest, hiding the sounds.",
    "...Hmph. That wasn't BAD. For a quickie. Don't look so smug!"),
    ("She pushed back against me hard — driving me over the edge.",
    "I pulled her tight against me as I finished. She gasped at the final thrust.",
    "...Idiot. My legs are going to be shaking all through dinner. Everyone will NOTICE!")
])

    scene eris_vaginal_generic_cum with fade

    "[sex_finish[0]]"
    "[sex_finish[1]]"
    eris "[sex_finish[2]]"

    "She smoothed her skirt. Fixed her hair. Took a deep breath."
    "Walked away like a proper Boreas noble."
    "Except for the flush on her cheeks, and the faint wobble in her stride."

    $ eris_afeicao += 10
    $ eris_interacted_today = True
    $ renpy.notify("+10 Affection with Eris!")
    jump passar_tempo
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
