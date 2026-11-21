






init python:
    enemy_pos_data = [
    (0.62, 0.05, 0.92),  
    (0.85, 0.3, 0.7),    
    (0.75, 0.5, 0.7),    
    (0.90, 0.5, 0.7),    
    (0.95, 0.3, 0.7),    
]
    player_pos_data = (0.08, 0.55, 0.7)
    ally_pos_data = (0.35, 0.55, 0.65)




transform player_text_pos:
    xalign 0.08
    yalign 0.7

transform ally_text_pos:
    xalign 0.25
    yalign 0.7

transform enemy_text_pos:
    xalign 0.7
    yalign 0.5

transform player_pos:
    xalign 0.08
    yalign 0.55
    zoom 0.7

transform ally_1_pos:
    xalign 0.35
    yalign 0.55
    zoom 0.65

transform ally_2_pos:
    xalign 0.32
    yalign 0.55
    zoom 0.65

transform enemy_pos:
    xalign 0.85
    yalign 0.3
    zoom 0.7

transform enemy_pos_2:
    xalign 0.85
    yalign 0.3
    zoom 0.7

transform enemy_pos_3:
    xalign 0.75
    yalign 0.5
    zoom 0.7

transform enemy_pos_4:
    xalign 0.90
    yalign 0.5
    zoom 0.7

transform enemy_pos_5:
    xalign 0.95
    yalign 0.3
    zoom 0.7


transform enemy_dano_pos:
    xalign 0.62
    yalign 0.45

transform enemy_dano_pos2:
    xalign 0.85
    yalign 0.5

transform enemy_dano_pos3:
    xalign 0.75
    yalign 0.5

transform enemy_dano_pos4:
    xalign 0.90
    yalign 0.5

transform enemy_dano_pos5:
    xalign 0.95
    yalign 0.3







transform damage_text:
    on show:
        alpha 1.0
        linear 1.0 yoffset -50 alpha 0.0
    on hide:
        alpha 0.0

transform heal_text:
    alpha 1.0
    linear 1.0 yoffset -50
    alpha 0.0

transform attack_move:
    xoffset 0
    linear 0.2 xoffset 50
    linear 0.2 xoffset 0

transform enemy_attack_move:
    xoffset 0
    linear 0.2 xoffset -50
    linear 0.2 xoffset 0

transform hit_effect:
    xoffset 0
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 0

transform dodge_effect:
    xoffset 0
    linear 0.05 xoffset 20
    linear 0.05 xoffset -20
    linear 0.05 xoffset 20
    linear 0.05 xoffset -20
    linear 0.05 xoffset 0



transform pos_enemy(idx):
    xalign enemy_pos_data[idx][0] yalign enemy_pos_data[idx][1] zoom enemy_pos_data[idx][2]

transform shake_enemy(idx):
    xalign enemy_pos_data[idx][0] yalign enemy_pos_data[idx][1] zoom enemy_pos_data[idx][2]
    xoffset 0
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 0

transform dodge_enemy(idx):
    xalign enemy_pos_data[idx][0] yalign enemy_pos_data[idx][1] zoom enemy_pos_data[idx][2]
    xoffset 0
    linear 0.05 xoffset 20
    linear 0.05 xoffset -20
    linear 0.05 xoffset 20
    linear 0.05 xoffset -20
    linear 0.05 xoffset 0

transform lunge_enemy(idx):
    xalign enemy_pos_data[idx][0] yalign enemy_pos_data[idx][1] zoom enemy_pos_data[idx][2]
    xoffset 0
    linear 0.2 xoffset -50
    linear 0.2 xoffset 0


transform shake_player:
    xalign player_pos_data[0] yalign player_pos_data[1] zoom player_pos_data[2]
    xoffset 0
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 0

transform shake_ally:
    xalign ally_pos_data[0] yalign ally_pos_data[1] zoom ally_pos_data[2]
    xoffset 0
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 0

transform lunge_ally:
    xalign ally_pos_data[0] yalign ally_pos_data[1] zoom ally_pos_data[2]
    xoffset 0
    linear 0.2 xoffset 50
    linear 0.2 xoffset 0


transform intent_pulse:
    alpha 0.85
    easein 1.0 alpha 1.0
    easeout 1.0 alpha 0.85
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
