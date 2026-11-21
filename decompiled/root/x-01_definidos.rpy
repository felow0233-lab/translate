default rudeus = Character("Rudeus", color="#ffffff")

default aisha = Character("Aisha", color="#ff4f4f")

default zenith = Character("Zenith", color="#ffc88a")

default roxy = Character("Roxy", color="#8ac1ff")

define lilia = Character("Lilia", color="#ff578a")

default paul = Character("Paul", color="#ffc88a")

default slime_girl = Character("Slime Girl", color="#80bbff")


transform my_left:
    xalign 0.2

transform my_right:
    xalign 0.8

default local_atual = "entrada_rudeus"

default energia = 3
default max_energia = 3

default player_gold = 0


define player_patreon = True

default affection_cheat_on = False
define AFFECTION_CHEAT_MAX = 500


default dog_girl_unlocked = False


default sc_player_hp = 100
default sc_player_max = 100
default sc_enemy_hp = 80
default sc_enemy_max = 80
default sc_defending = False
default sc_charging = False
default sc_just_met = False


default slime_girl_intro_seen = False
default slime_girl_affection = 0
default slime_girl_groped = False
default slime_girl_handjob_done = False
default slime_girl_blowjob_done = False
default slime_girl_sex_done = False


define sc_slime_hurt_sounds = [
    "audio/slime_girl/slime_girl_hurt_01.mp3",
    "audio/slime_girl/slime_girl_hurt_02.mp3",
    "audio/slime_girl/slime_girl_hurt_03.mp3",
    "audio/slime_girl/slime_girl_hurt_04.mp3",
    "audio/slime_girl/slime_girl_hurt_05.mp3",
    "audio/slime_girl/slime_girl_hurt_06.mp3",
]


define sc_slime_attack_sounds = [
    "audio/slime_girl/slime_girl_hya_01.mp3",
    "audio/slime_girl/slime_girl_hya_02.mp3",
    "audio/slime_girl/slime_girl_hya_03.mp3",
    "audio/slime_girl/slime_girl_hya_04.mp3",
    "audio/slime_girl/slime_girl_hya_05.mp3",
]







transform sc_idle:
    xalign 0.5
    yalign 1.0
    zoom 1.0

transform sc_hurt:
    xalign 0.5
    yalign 1.0
    zoom 1.0
    xoffset 0
    linear 0.05 xoffset 18
    linear 0.05 xoffset -18
    linear 0.05 xoffset 18
    linear 0.05 xoffset -18
    linear 0.05 xoffset 0

transform sc_attack:
    xalign 0.5
    yalign 1.0
    zoom 1.0
    xoffset 0
    linear 0.15 xoffset -100
    linear 0.15 xoffset 0

transform sc_embarrassed:
    xalign 0.5
    yalign 1.0
    zoom 1.0
    xoffset 0
    linear 0.06 xoffset -10
    linear 0.06 xoffset 10
    linear 0.06 xoffset -10
    linear 0.06 xoffset 10
    linear 0.06 xoffset 0

transform sc_charge_pose:
    xalign 0.5
    yalign 1.0
    zoom 1.0
    linear 0.15 zoom 1.08
    linear 0.15 zoom 1.0
    linear 0.15 zoom 1.08
    linear 0.15 zoom 1.0


transform sc_kneel:
    xalign 0.5
    yalign 1.0
    zoom 1.0
    rotate 0
    yoffset 0
    linear 0.3 rotate -4 yoffset 15
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
