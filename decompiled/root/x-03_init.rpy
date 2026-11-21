



init python:




    def get_time_of_day():
        e = store.energia
        mx = store.max_energia
        if e >= mx:
            return {"name": "Morning", "icon": "☀", "color": "#FFD700", "period": "morning"}
        elif e >= 2:
            return {"name": "Afternoon", "icon": "🌅", "color": "#FF8C00", "period": "afternoon"}
        else:
            return {"name": "Night", "icon": "🌙", "color": "#6688CC", "period": "night"}

    def is_night():
        return store.energia <= 1

    def is_daytime():
        return store.energia >= 2






    def location_thumb(base, w=384, h=216):
        e = store.energia
        mx = store.max_energia
        if e >= mx:
            suffix = ""          
        elif e >= 2:
            suffix = "_tarde"    
        else:
            suffix = "_noite"    
        return im.Scale("images/general_locations/bg {}{}.png".format(base, suffix), w, h)





    def get_chat_reward(current_affection):
        """Retorna recompensa de interação escalada baseada na afinidade atual"""
        
        if current_affection < 100:
            return 5  
        elif current_affection < 300:
            return 7  
        else:
            return 10  






    def get_interaction_reward(current_affection):
        """Retorna recompensa de interação escalada baseada na afinidade atual"""
        if current_affection < 100:
            return 5  
        elif current_affection < 300:
            return 7  
        else:
            return 10  




    def add_xp(amount):
        """Adiciona XP ao Rudeus e checa level up"""
        store.rudeus_xp += amount
        renpy.notify("Rudeus gained {} XP!".format(amount))
        check_level_up()

    def check_level_up():
        """Verifica se Rudeus subiu de level - mostra tela de recompensa"""
        while store.rudeus_xp >= store.rudeus_xp_to_next_level:
            store.rudeus_xp -= store.rudeus_xp_to_next_level
            store.rudeus_level += 1
            
            
            store.rudeus_xp_to_next_level = int(store.rudeus_xp_to_next_level * 1.25)
            
            
            store.player.base_max_hp += 25
            atk_bonus = renpy.random.randint(1, 3)
            store.player.base_min_attack += atk_bonus
            store.player.base_max_attack += atk_bonus
            store.player.hp = store.player.max_hp
            
            renpy.notify("🎉 LEVEL UP! Rudeus is now level {}! +25 HP, +{} ATK".format(store.rudeus_level, atk_bonus))

    def get_enemy_xp(enemy_type):
        """Retorna o XP que o inimigo dá baseado no tipo"""
        xp_ranges = {
        "slime": (8, 14),
        "wolf": (15, 22),
        "bandit": (18, 28),
        "orc": (25, 35),
        "boss": (50, 75)
    }
        
        
        enemy_lower = enemy_type.lower()
        for key, (min_xp, max_xp) in xp_ranges.items():
            if key in enemy_lower:
                return random.randint(min_xp, max_xp)
        
        
        return random.randint(15, 25)






    CARD_UPGRADES = {
    "Fire Strike": {
        2: {"damage_min": 8, "damage_max": 14, "effect_chance": 0.30},
        3: {"damage_min": 14, "damage_max": 22, "effect_chance": 0.50}
    },
    "Wind Slash": {
        2: {"damage_min": 16, "damage_max": 26, "effect_chance": 0},
        3: {"damage_min": 24, "damage_max": 36, "effect_chance": 0}
    },
    "Ice Shard": {
        2: {"damage_min": 9, "damage_max": 16, "effect_chance": 0.30},
        3: {"damage_min": 15, "damage_max": 24, "effect_chance": 0.50}
    },
    "Water Heal": {
        2: {"heal_min": 18, "heal_max": 26, "effect_chance": 0},
        3: {"heal_min": 26, "heal_max": 38, "effect_chance": 0}
    },
    "Earth Quake": {
        2: {"damage_min": 12, "damage_max": 18, "effect_chance": 0},
        3: {"damage_min": 18, "damage_max": 26, "effect_chance": 0}
    },
    "Fire Ball": {
        2: {"damage_min": 10, "damage_max": 16, "effect_chance": 0.30},
        3: {"damage_min": 16, "damage_max": 24, "effect_chance": 0.50}
    },
    "Dark Orb": {
        2: {"damage_min": 16, "damage_max": 24, "heal_min": 8, "heal_max": 12, "effect_chance": 0},
        3: {"damage_min": 24, "damage_max": 34, "heal_min": 12, "heal_max": 17, "effect_chance": 0}
    },
    "Quick Strike": {
        2: {"damage_min": 4, "damage_max": 8, "effect_chance": 0},
        3: {"damage_min": 7, "damage_max": 12, "effect_chance": 0}
    },
    "Shield Guard": {
        2: {"heal_min": 10, "heal_max": 15, "effect_chance": 0},
        3: {"heal_min": 15, "heal_max": 22, "effect_chance": 0}
    },
    "Weaken": {
        2: {"damage_min": 5, "damage_max": 10, "effect_chance": 1.0},
        3: {"damage_min": 8, "damage_max": 14, "effect_chance": 1.0}
    }
}






    ENEMY_CARD_POOLS = {
    "slime": ["Fire Strike", "Shield Guard", "Ice Shard"],
    "wolf": ["Wind Slash", "Weaken", "Water Heal"],
    "bandit": ["Ice Shard", "Fire Ball", "Dark Orb"],
    "ogre": ["Earth Quake", "Fire Ball", "Dark Orb", "Water Heal"]
}


    def get_card_by_name(name):
        """Returns a card template by name"""
        card_map = {
        "Fire Strike": store.fire_strike,
        "Wind Slash": store.wind_slash,
        "Ice Shard": store.ice_shard,
        "Water Heal": store.water_heal,
        "Earth Quake": store.earth_quake,
        "Fire Ball": store.fire_ball,
        "Dark Orb": store.dark_orb,
        "Shield Guard": store.shield_guard,
        "Weaken": store.weaken_spell
    }
        return card_map.get(name, None)

    def generate_combat_rewards(enemy_type, num_choices=3):
        """
    Generates reward choices on LEVEL UP (Vampire Survivors style).
    NEW CARD is prioritized (more common), UPGRADES are rarer.
    STAT BOOST (+HP) fills remaining slots.
    """
        import copy
        import random
        
        pool = ENEMY_CARD_POOLS.get(enemy_type, ["Fire Strike", "Shield Guard", "Ice Shard"])
        
        
        owned_cards = {}
        for card in store.player_permanent_deck:
            if card.name not in owned_cards:
                owned_cards[card.name] = card.level
            else:
                owned_cards[card.name] = max(owned_cards[card.name], card.level)
        
        
        new_card_rewards = []
        upgrade_rewards = []
        
        for card_name in pool:
            if card_name in owned_cards:
                current_level = owned_cards[card_name]
                if current_level < 3:
                    preview = None
                    if card_name in CARD_UPGRADES and (current_level + 1) in CARD_UPGRADES[card_name]:
                        preview = CARD_UPGRADES[card_name][current_level + 1]
                    card_ref = get_card_by_name(card_name)
                    if card_ref:
                        upgrade_rewards.append({
                        "type": "upgrade",
                        "card_name": card_name,
                        "card_ref": card_ref,
                        "current_level": current_level,
                        "preview": preview
                    })
            else:
                card_ref = get_card_by_name(card_name)
                if card_ref:
                    new_card_rewards.append({
                    "type": "new_card",
                    "card_name": card_name,
                    "card_ref": card_ref,
                    "current_level": 0,
                    "preview": None
                })
        
        
        random.shuffle(new_card_rewards)
        random.shuffle(upgrade_rewards)
        
        rewards = []
        
        
        for r in new_card_rewards:
            if len(rewards) < num_choices:
                rewards.append(r)
        
        
        max_upgrades = 1 if len(new_card_rewards) > 0 else num_choices
        upgrades_added = 0
        for r in upgrade_rewards:
            if len(rewards) < num_choices and upgrades_added < max_upgrades:
                rewards.append(r)
                upgrades_added += 1
        
        
        stat_options = [5, 10, 15, 20]
        while len(rewards) < num_choices:
            hp_bonus = random.choice(stat_options)
            rewards.append({
            "type": "stat_boost",
            "card_name": "+{} Max HP".format(hp_bonus),
            "card_ref": None,
            "current_level": 0,
            "preview": {"hp_bonus": hp_bonus}
        })
        
        
        random.shuffle(rewards)
        
        return rewards

    def apply_combat_reward(reward):
        """Applies the chosen reward from the Vampire Survivors screen"""
        import copy
        
        if reward["type"] == "new_card":
            
            card_ref = reward["card_ref"]
            if card_ref:
                new_card = copy.deepcopy(card_ref)
                store.player_permanent_deck.append(new_card)
                if new_card.name not in store.purchased_cards:
                    store.purchased_cards.append(new_card.name)
                renpy.notify("New card: {}!".format(new_card.name))
        
        elif reward["type"] == "upgrade":
            
            card_name = reward["card_name"]
            for card in store.player_permanent_deck:
                if card.name == card_name and card.level < 3:
                    upgrade_card_level(card)
        
        elif reward["type"] == "stat_boost":
            
            hp_bonus = reward["preview"].get("hp_bonus", 5)
            store.player.base_max_hp += hp_bonus
            store.player.hp = min(store.player.hp + hp_bonus, store.player.max_hp)
            renpy.notify("+{} Max HP!".format(hp_bonus))

    def get_card_type_color(card_type):
        """Returns color based on card type"""
        colors = {
        "attack": "#FF6347",
        "heal": "#32CD32",
        "block": "#4488ff",
        "lifesteal": "#9B59B6",
        "debuff": "#aa44ff",
        "buff": "#44ff44"
    }
        return colors.get(card_type, "#FFFFFF")

    def get_card_type_label(card_type):
        """Returns label text based on card type"""
        labels = {
        "attack": "ATTACK",
        "heal": "HEAL",
        "block": "BLOCK",
        "lifesteal": "LIFESTEAL",
        "debuff": "DEBUFF",
        "buff": "BUFF"
    }
        return labels.get(card_type, "CARD")

    class Item:
        def __init__(self, name, type, attack_bonus=0, hp_bonus=0, mp_bonus=0, agi_bonus=0, crit_chance_bonus=0,
    description="", debuff=None, extra_damage_vs=None, effect=None, idle_image=None, hover_image=None,
    stackable=False, sell_value=50, craft_cost=None, heal_chance=0.0, heal_amount=0, mp_chance=0.0, mp_amount=0,target_type=None):
            self.name = name
            self.type = type
            self.attack_bonus = attack_bonus
            self.hp_bonus = hp_bonus
            self.mp_bonus = mp_bonus
            self.agi_bonus = agi_bonus
            self.crit_chance_bonus = crit_chance_bonus
            self.description = description
            self.debuff = debuff or {}
            self.extra_damage_vs = extra_damage_vs or {}
            self.effect = effect
            self.idle_image = idle_image
            self.hover_image = hover_image
            self.stackable = stackable
            self.quantity = 1 if stackable else 0
            self.sell_value = sell_value
            self.craft_cost = craft_cost
            self.heal_chance = heal_chance
            self.heal_amount = heal_amount
            self.mp_chance = mp_chance
            self.mp_amount = mp_amount
            self.target_type = target_type  
        
        def __getstate__(self):
            return self.__dict__.copy()
        
        def __setstate__(self, state):
            self.__dict__.update(state)

    def hp_potion_effect(char):
        heal_amount = renpy.random.randint(12, 24)  
        
        char.hp = min(char.max_hp, char.hp + heal_amount)
        renpy.notify(f"Recovered {heal_amount} Hp!")

    def mp_potion_effect(char):
        mp_amount = renpy.random.randint(16, 20)  
        
        char.mp = min(char.max_mp, char.mp + mp_amount)
        renpy.notify(f"Recovered {mp_amount} Mp!")

    def agility_buff_effect(char):
        effect = {"type": "agi_buff", "agi_mod": 5, "duration": 5}
        char.effects.append(effect)

    def burn_debuff_effect(char):
        effect = {"type": "burn", "damage": renpy.random.randint(3, 5), "duration": 3}
        char.effects.append(effect)


    def remove_item_from_inventory(item):
        if isinstance(item, Item) and item in inventory:
            if item.stackable and item.quantity > 1:
                item.quantity -= 1
                renpy.notify(f"Usou 1x {item.name}, restam {item.quantity}")
            else:
                inventory.remove(item)
                renpy.notify(f"Usou {item.name}, removido do inventário")
            renpy.restart_interaction()

    def add_item_to_inventory(item):
        if isinstance(item, Item):
            if item.stackable:
                
                for existing_item in inventory:
                    if existing_item.name == item.name and existing_item.stackable and existing_item.quantity < 5:
                        existing_item.quantity += 1
                        
                        renpy.restart_interaction()
                        return
                
                new_item = copy.deepcopy(item)
                new_item.quantity = 1
                inventory.append(new_item)
            else:
                inventory.append(item)
            renpy.restart_interaction()

    def create_stackable_image(item, is_hover=False):
        if item.stackable:
            base_image = item.hover_image if is_hover else item.idle_image
            return LiveComposite(
            (150, 150),
            (0, 0), base_image,
            (10, 10), Text(f"{item.quantity}x", size=18, color="#ffffff", outlines=[(2, "#000000", 0, 0)])
        )
        return item.hover_image if is_hover else item.idle_image

    def sell_single_item(item):
        global golds
        if item.stackable and item.quantity > 1:
            
            sell_value = item.sell_value
            golds += sell_value
            item.quantity -= 1
            renpy.notify(f"Vendeu 1x {item.name} por {sell_value} Golds!")
        else:
            
            sell_value = item.sell_value
            golds += sell_value
            inventory.remove(item)
            renpy.notify(f"Vendeu 1x {item.name} por {sell_value} Golds!")
        renpy.restart_interaction()

    def sell_item(item):
        global golds
        if item.stackable and item.quantity > 1:
            
            sell_value = item.sell_value * item.quantity
            golds += sell_value
            inventory.remove(item)
            renpy.notify(f"Vendeu {item.quantity}x {item.name} por {sell_value} Golds!")
        else:
            
            sell_value = item.sell_value
            golds += sell_value
            inventory.remove(item)
            renpy.notify(f"Vendeu 1x {item.name} por {sell_value} Golds!")
        renpy.restart_interaction()



    class Personagem:
        def __init__(self, name, hp, max_hp, min_attack, max_attack, agi=0, mp=0, max_mp=0, crit_chance=0, passives=None, skills=None, sprite_idle="default.png", sprite_hover="default_bright.png", drop_item=None, drop_chance=0, exp_min=0, exp_max=0, gold_min=0, gold_max=0, hurt_sounds=None, death_sounds=None):
            self.name = name
            self._hp = hp
            self.base_max_hp = max_hp
            self.base_min_attack = min_attack
            self.base_max_attack = max_attack
            self.base_agi = agi
            self._mp = mp
            self.base_max_mp = max_mp
            self.base_crit_chance = crit_chance
            self.passives = passives if passives is not None else []
            self.skills = skills if skills else []
            self.sprite_idle = sprite_idle
            self.sprite_hover = sprite_hover
            self.equipment = {"weapon": None, "armor": None, "necklace": None, "boots": None, "gloves": None}
            self.type = None
            self.drop_item = drop_item
            self.drop_chance = drop_chance
            self.exp_min = exp_min
            self.exp_max = exp_max
            self.gold_min = gold_min
            self.gold_max = gold_max
            self.hurt_sounds = hurt_sounds if hurt_sounds is not None else []
            self.death_sounds = death_sounds if death_sounds is not None else []
            self.level = 1
            self.exp = 0
            self.exp_to_next_level = 30
            self.block = 0
            self.strength = 0
            self.intent = None
            self.intent_value = 0
            self.effects = []
            self.effect_damages = []
        
        def __getstate__(self):
            state = self.__dict__.copy()
            return state
        
        def __setstate__(self, state):
            self.__dict__.update(state)
            for attr, default_val in [('block', 0), ('strength', 0), ('intent', None), ('intent_value', 0), ('effects', []), ('effect_damages', [])]:
                if attr not in self.__dict__:
                    setattr(self, attr, default_val)
        
        @property
        def hp(self):
            return self._hp
        
        @hp.setter
        def hp(self, value):
            self._hp = max(0, min(value, self.max_hp))
        
        @property
        def mp(self):
            return self._mp
        
        @mp.setter
        def mp(self, value):
            self._mp = max(0, min(value, self.max_mp))
        
        @property
        def max_hp(self):
            bonus = sum(item.hp_bonus for item in self.equipment.values() if item)
            return self.base_max_hp + bonus
        
        @property
        def max_mp(self):
            bonus = sum(item.mp_bonus if hasattr(item, "mp_bonus") else 0 for item in self.equipment.values() if item)
            return self.base_max_mp + bonus
        
        @property
        def min_attack(self):
            bonus = self.equipment["weapon"].attack_bonus if self.equipment["weapon"] else 0
            return self.base_min_attack + bonus
        
        @property
        def max_attack(self):
            bonus = self.equipment["weapon"].attack_bonus if self.equipment["weapon"] else 0
            return self.base_max_attack + bonus
        
        @property
        def agi(self):
            bonus = sum(item.agi_bonus for item in self.equipment.values() if item)
            return self.base_agi + bonus
        
        @property
        def dodge_chance(self):
            return self.agi / 100.0  
        
        @property
        def crit_chance(self):
            bonus = sum(item.crit_chance_bonus if hasattr(item, "crit_chance_bonus") else 0 for item in self.equipment.values() if item)
            return self.base_crit_chance + bonus






    def has_effect(character, effect_type):
        return any(effect["type"] == effect_type for effect in character.effects)


    def get_effective_agi(character):
        return character.agi  

    def get_effective_hp(character):
        return character.hp  

    def get_effective_attack_range(character):
        min_attack = character.min_attack  
        max_attack = character.max_attack
        return min_attack, max_attack

    def get_effective_crit(character):
        return character.crit_chance  


    def calculate_attack_damage(attacker, target):
        weapon = attacker.equipment["weapon"]
        base_damage = renpy.random.randint(attacker.min_attack, attacker.max_attack)  
        extra_damage = 0
        
        if weapon and weapon.extra_damage_vs and target.type in weapon.extra_damage_vs:
            extra_damage = weapon.extra_damage_vs[target.type]
            "[attacker.name] causa [extra_damage] de dano extra contra [target.name] por ser um [target.type]!"
        
        total_damage = base_damage + extra_damage
        
        if weapon and weapon.debuff and renpy.random.random() < weapon.debuff["chance"]:
            damage = renpy.random.randint(weapon.debuff["damage"][0], weapon.debuff["damage"][1])
            target.effects.append({"type": weapon.debuff["type"], "damage": damage, "duration": weapon.debuff["duration"]})
            if weapon.debuff["type"] == "freeze":
                target.frozen = True
            "[attacker.name] aplicou [weapon.debuff['type']] em [target.name]!"
        
        return total_damage



    def update_tooltip(text):
        global tooltip
        tooltip = text
        if text:
            renpy.show_screen("tooltip")
        else:
            renpy.hide_screen("tooltip")




    def create_enemy_from_template(template, tag):
        """Cria uma cópia de um inimigo a partir de um template"""
        import copy
        enemy = Personagem(
        template.name, 
        template.max_hp, 
        template.max_hp, 
        template.min_attack, 
        template.max_attack,
        agi=template.agi,
        mp=template.mp,
        max_mp=template.max_mp,
        crit_chance=template.crit_chance,
        skills=copy.deepcopy(template.skills),
        sprite_idle=template.sprite_idle,
        sprite_hover=template.sprite_hover,
        exp_min=template.exp_min,
        exp_max=template.exp_max,
        hurt_sounds=template.hurt_sounds,
        death_sounds=template.death_sounds
    )
        enemy.tag = tag
        
        if "slime" in template.name.lower():
            enemy.type = "slime"
        elif "wolf" in template.name.lower():
            enemy.type = "wolf"
        elif "bandit" in template.name.lower():
            enemy.type = "bandit"
        elif "ogre" in template.name.lower():
            enemy.type = "ogre"
        else:
            enemy.type = "unknown"
        
        enemy.gold_min = template.gold_min if hasattr(template, 'gold_min') else 5
        enemy.gold_max = template.gold_max if hasattr(template, 'gold_max') else 10
        
        enemy.lust = 0
        return enemy

    def generate_random_wave(difficulty=1):
        """
    Gera uma wave aleatória de inimigos
    difficulty: 1-3 (fácil, médio, difícil)
    Retorna uma lista de inimigos
    """
        import copy
        enemies = []
        
        
        if difficulty == 1:
            enemy_pool = [enemy_slime_template] * 4 + [enemy_wolf_template] * 1  
            num_enemies = renpy.random.randint(2, 3)  
        elif difficulty == 2:
            enemy_pool = [enemy_slime_template] * 2 + [enemy_wolf_template] * 2 + [enemy_bandit_template] * 2 + [enemy_ogre_template] * 1  
            num_enemies = renpy.random.randint(3, 4)  
        else:  
            enemy_pool = [enemy_wolf_template] * 2 + [enemy_bandit_template] * 2 + [enemy_ogre_template] * 2  
            num_enemies = renpy.random.randint(3, 5)  
        
        
        for i in range(num_enemies):
            template = renpy.random.choice(enemy_pool)
            tag = f"enemy{i+1}"
            enemy = create_enemy_from_template(template, tag)
            enemies.append(enemy)
        
        return enemies

    def get_wave_difficulty(wave_number):
        """Retorna a dificuldade baseada no número da wave"""
        if wave_number <= 2:
            return 1  
        elif wave_number <= 4:
            return 2  
        else:
            return 3  

    def get_enemy_damage_position(target, enemies):
        """Retorna a posição de dano para um inimigo específico"""
        if target not in enemies:
            return enemy_dano_pos
        
        enemy_index = enemies.index(target)
        damage_positions = [enemy_dano_pos, enemy_dano_pos2, enemy_dano_pos3, enemy_dano_pos4, enemy_dano_pos5]
        return damage_positions[enemy_index] if enemy_index < len(damage_positions) else enemy_dano_pos




    def initialize_deck():
        """Inicializa o deck do jogador com cartas padrão"""
        global player_deck, player_permanent_deck, deck_initialized
        import copy
        
        
        if not deck_initialized or len(player_permanent_deck) == 0:
            
            del player_permanent_deck[:]
            player_permanent_deck.append(copy.deepcopy(fire_strike))
            player_permanent_deck.append(copy.deepcopy(wind_slash))
            deck_initialized = True
        
        
        player_deck = []
        for card in player_permanent_deck:
            player_deck.append(copy.deepcopy(card))
        
        
        shuffle_deck()

    def shuffle_deck():
        """Embaralha o deck do jogador (usando Fisher-Yates shuffle múltiplas vezes)"""
        global player_deck
        import random
        
        
        
        for _ in range(5):  
            renpy.random.shuffle(player_deck)
            
            random.shuffle(player_deck)

    def draw_cards(num_cards, show_animation=False):
        """
    Puxa cartas para a mão usando sistema de peso/raridade
    Cartas mais comuns (maior rarity_weight) aparecem com mais frequência
    """
        global player_hand, player_permanent_deck
        import copy
        import random
        
        cards_drawn = []
        
        if len(player_permanent_deck) == 0:
            return 0  
        
        
        while len(cards_drawn) < num_cards and len(player_hand) < max_hand_size:
            
            cards_pool = []
            weights_pool = []
            
            for card in player_permanent_deck:
                cards_pool.append(card)
                
                weight = getattr(card, 'rarity_weight', 1.0)
                weights_pool.append(weight)
            
            
            
            selected_card = random.choices(cards_pool, weights=weights_pool, k=1)[0]
            
            
            card_copy = copy.deepcopy(selected_card)
            player_hand.append(card_copy)
            cards_drawn.append(card_copy)
        
        
        if show_animation and len(cards_drawn) > 0:
            renpy.show_screen("show_card_draw", cards_to_show=cards_drawn)
            
            try:
                renpy.sound.play("audio/dodge_sound.mp3")
            except:
                pass  
            
            total_time = len(cards_drawn) * 0.15 + 0.5
            renpy.pause(total_time)  
            renpy.hide_screen("show_card_draw")
        
        return len(cards_drawn)

    def discard_card(card):
        """Descarta uma carta da mão"""
        global player_hand, player_discard
        if card in player_hand:
            player_hand.remove(card)
            player_discard.append(card)

    def reset_energy():
        """Reseta a energia do jogador no início do turno"""
        global player_energy
        player_energy = max_energy

    def can_play_card(card):
        """Verifica se o jogador pode jogar a carta"""
        return player_energy >= card.energy_cost

    def play_card(card):
        """Joga uma carta (remove da mão e descarta)"""
        global player_energy
        if can_play_card(card):
            player_energy -= card.energy_cost
            discard_card(card)
            return True
        return False




    def add_card_to_deck(card):
        """Adiciona uma carta ao deck permanente do jogador"""
        global player_permanent_deck, purchased_cards
        import copy
        player_permanent_deck.append(copy.deepcopy(card))
        
        
        if card.name not in purchased_cards:
            purchased_cards.append(card.name)
        
        renpy.notify(f"Added {card.name} to your deck!")

    def gain_exp(amount):
        """Adiciona experiência e verifica level up"""
        global player_exp, player_level, player_exp_to_next, player
        player_exp += amount
        
        leveled_up = False
        while player_exp >= player_exp_to_next:
            player_exp -= player_exp_to_next
            player_level += 1
            
            
            player.base_min_attack += 1
            player.base_max_attack += 2
            
            
            player_exp_to_next = int(player_exp_to_next * 1.25)
            
            leveled_up = True
            
            
            renpy.notify(f"LEVEL UP! Now Level {player_level}!")
        
        return leveled_up

    def upgrade_card_power():
        """Aumenta o poder base de todas as cartas"""
        global player_card_power, player_permanent_deck
        player_card_power += 1
        
        
        for card in player_permanent_deck:
            card.card_power_bonus = player_card_power
        
        renpy.notify(f"Card Power increased! All cards +{player_card_power} damage")

    def update_card_description(card):
        """Atualiza a descrição da carta baseada no seu nível e stats atuais"""
        
        base_descriptions = {
        "Fire Strike": "Fire attack dealing {damage_min}-{damage_max} damage. {effect_text}",
        "Wind Slash": "Quick wind attack dealing {damage_min}-{damage_max} damage",
        "Water Heal": "Heal {heal_min}-{heal_max} HP",
        "Ice Shard": "Ice attack dealing {damage_min}-{damage_max} damage. {effect_text}",
        "Fire Ball": "Fire ball dealing {damage_min}-{damage_max} damage to all enemies. {effect_text}",
        "Earth Quake": "Earth attack dealing {damage_min}-{damage_max} damage to all enemies",
        "Dark Orb": "Dark magic draining life. Deals {damage_min}-{damage_max} damage and heals {heal_min}-{heal_max} HP"
    }
        
        
        base_desc = base_descriptions.get(card.name, "")
        
        
        effect_text = ""
        if card.effect and card.effect_chance > 0:
            effect_chance_percent = int(card.effect_chance * 100)
            effect_name = card.effect.name.lower()
            
            
            if "stun" in effect_name or "frozen" in effect_name:
                effect_text = f"{effect_chance_percent}% chance to freeze (stun for 1 turn)"
            elif "burn" in effect_name:
                effect_text = f"{effect_chance_percent}% chance to burn ({card.effect.damage_min}-{card.effect.damage_max} dmg/turn for {card.effect.duration} turns)"
            elif "poison" in effect_name:
                effect_text = f"{effect_chance_percent}% chance to poison ({card.effect.damage_min}-{card.effect.damage_max} dmg/turn for {card.effect.duration} turns)"
            elif "bleed" in effect_name:
                effect_text = f"{effect_chance_percent}% chance to bleed ({card.effect.damage_min}-{card.effect.damage_max} dmg/turn for {card.effect.duration} turns)"
            else:
                effect_text = f"{effect_chance_percent}% chance to apply {effect_name}"
        
        
        if card.card_type == "attack" or card.card_type == "lifesteal":
            if "{heal_min}" in base_desc:
                
                card.description = base_desc.format(
                damage_min=card.damage_min,
                damage_max=card.damage_max,
                heal_min=card.heal_min if hasattr(card, 'heal_min') else 0,
                heal_max=card.heal_max if hasattr(card, 'heal_max') else 0,
                effect_text=effect_text
            )
            else:
                
                card.description = base_desc.format(
                damage_min=card.damage_min,
                damage_max=card.damage_max,
                effect_text=effect_text
            )
        elif card.card_type == "heal":
            card.description = base_desc.format(
            heal_min=card.heal_min,
            heal_max=card.heal_max
        )
        
        
        if card.level > 1:
            card.description = f"[Lv.{card.level}] {card.description}"

    def get_upgrade_preview(card):
        """Retorna um dicionário com os stats após o upgrade"""
        if card.level >= 3 or card.name not in CARD_UPGRADES:
            return None
        
        next_level = card.level + 1
        if next_level not in CARD_UPGRADES[card.name]:
            return None
        
        return CARD_UPGRADES[card.name][next_level]

    def upgrade_card_level(card):
        """Faz upgrade no nível de uma carta específica usando valores manuais"""
        if card.level >= 3:
            renpy.notify("Card is already at max level!")
            return False
        
        card.level += 1
        
        
        if card.name in CARD_UPGRADES and card.level in CARD_UPGRADES[card.name]:
            upgrades = CARD_UPGRADES[card.name][card.level]
            
            
            if "damage_min" in upgrades:
                card.damage_min = upgrades["damage_min"]
            if "damage_max" in upgrades:
                card.damage_max = upgrades["damage_max"]
            
            
            if "heal_min" in upgrades:
                card.heal_min = upgrades["heal_min"]
            if "heal_max" in upgrades:
                card.heal_max = upgrades["heal_max"]
            
            
            if "effect_chance" in upgrades:
                card.effect_chance = upgrades["effect_chance"]
        
        
        update_card_description(card)
        
        renpy.notify(f"{card.name} upgraded to Level {card.level}!")
        return True

    def upgrade_all_cards_of_type(card_name):
        """Faz upgrade em todas as cartas de um mesmo tipo no deck permanente"""
        global player_permanent_deck
        upgraded_count = 0
        
        
        first_card = None
        for card in player_permanent_deck:
            if card.name == card_name:
                first_card = card
                break
        
        if not first_card:
            return False
        
        
        old_level = first_card.level
        if first_card.card_type == "attack":
            old_damage_min = first_card.damage_min
            old_damage_max = first_card.damage_max
        elif first_card.card_type == "heal":
            old_heal_min = first_card.heal_min
            old_heal_max = first_card.heal_max
        
        
        for card in player_permanent_deck:
            if card.name == card_name:
                if upgrade_card_level(card):
                    upgraded_count += 1
        
        if upgraded_count > 0:
            
            if first_card.card_type == "attack":
                renpy.show_screen("card_upgrade_result", 
                card_name=card_name,
                card_icon=first_card.icon_idle,
                old_level=old_level,
                new_level=first_card.level,
                old_damage_min=old_damage_min,
                old_damage_max=old_damage_max,
                new_damage_min=first_card.damage_min,
                new_damage_max=first_card.damage_max,
                card_type="attack",
                upgraded_count=upgraded_count)
            elif first_card.card_type == "heal":
                renpy.show_screen("card_upgrade_result", 
                card_name=card_name,
                card_icon=first_card.icon_idle,
                old_level=old_level,
                new_level=first_card.level,
                old_heal_min=old_heal_min,
                old_heal_max=old_heal_max,
                new_heal_min=first_card.heal_min,
                new_heal_max=first_card.heal_max,
                card_type="heal",
                upgraded_count=upgraded_count)
        
        return True




    def apply_effect(target, effect):
        """Aplica um efeito em um alvo"""
        import copy
        
        if not hasattr(target, 'effects'):
            target.effects = []
        
        
        existing_effect = None
        for eff in target.effects:
            if eff.name == effect.name:
                existing_effect = eff
                break
        
        if existing_effect:
            
            if existing_effect.effect_type == "slimy":
                max_stacks = 3
                current_stacks = getattr(existing_effect, 'stacks', 1)
                if current_stacks < max_stacks:
                    existing_effect.stacks = current_stacks + 1
                existing_effect.duration = max(existing_effect.duration, effect.duration)
            else:
                
                existing_effect.duration = max(existing_effect.duration, effect.duration)
        else:
            
            new_eff = copy.deepcopy(effect)
            if new_eff.effect_type == "slimy":
                new_eff.stacks = 1
            target.effects.append(new_eff)



    def drop_loot(enemy):
        """Sistema de drop de loot baseado no tipo de inimigo"""
        if not hasattr(enemy, 'type'):
            return
        
        drop_chance = 0
        loot_item = ""
        
        
        if enemy.type == "slime":
            drop_chance = 0.30  
            loot_item = "slime_skin"
        elif enemy.type == "wolf":
            drop_chance = 0.20  
            loot_item = "wolf_pelt"
        elif enemy.type == "ogre":
            drop_chance = 0.15  
            loot_item = "orc_tusk"
        
        
        if loot_item and renpy.random.random() < drop_chance:
            
            if loot_item == "slime_skin":
                store.slime_skin += 1
                renpy.notify(f"Dropped: Slime Skin! ({store.slime_skin}/5)")
            elif loot_item == "wolf_pelt":
                store.wolf_pelt += 1
                renpy.notify(f"Dropped: Wolf Pelt! ({store.wolf_pelt})")
            elif loot_item == "orc_tusk":
                store.orc_tusk += 1
                renpy.notify(f"Dropped: Orc Tusk! ({store.orc_tusk})")

    def process_effects(target):
        """Processa todos os efeitos ativos em um alvo no início do seu turno"""
        if not hasattr(target, 'effects'):
            target.effects = []
            return
        
        effects_to_remove = []
        
        for effect in target.effects:
            
            if effect.damage_min > 0 or effect.damage_per_turn > 0:
                damage = effect.get_damage()
                target.hp -= damage
                
                
                if not hasattr(target, 'effect_damages'):
                    target.effect_damages = []
                target.effect_damages.append({"damage": damage, "effect_name": effect.name})
            
            if effect.heal_per_turn > 0:
                target.hp = min(target.hp + effect.heal_per_turn, target.max_hp)
                renpy.notify(f"{target.name} recovers {effect.heal_per_turn} HP from {effect.name}!")
            
            
            if not effect.tick():
                effects_to_remove.append(effect)
                renpy.notify(f"{effect.name} wore off from {target.name}!")
        
        
        for effect in effects_to_remove:
            target.effects.remove(effect)




    def apply_block_to_char(target, amount):
        """Adds block to a character"""
        if not hasattr(target, 'block'):
            target.block = 0
        target.block += amount

    def take_damage_with_block(target, raw_damage):
        """Applies damage considering block. Returns (hp_damage, blocked_amount)."""
        if not hasattr(target, 'block'):
            target.block = 0
        if target.block > 0:
            if raw_damage <= target.block:
                blocked = raw_damage
                target.block -= raw_damage
                return 0, blocked
            else:
                blocked = target.block
                remaining = raw_damage - target.block
                target.block = 0
                target.hp -= remaining
                return remaining, blocked
        else:
            target.hp -= raw_damage
            return raw_damage, 0




    def calculate_outgoing_damage(attacker, base_damage):
        """Calculates damage considering strength, weakness, and slimy stacks"""
        damage = base_damage + getattr(attacker, 'strength', 0)
        if hasattr(attacker, 'effects'):
            for effect in attacker.effects:
                if effect.effect_type == "weakness":
                    damage = int(damage * 0.75)
                    break
            for effect in attacker.effects:
                if effect.effect_type == "slimy":
                    stacks = getattr(effect, 'stacks', 1)
                    reduction = min(stacks * 0.25, 0.75)  
                    damage = int(damage * (1.0 - reduction))
                    break
        return max(1, damage)

    def apply_vulnerability_damage(damage, target):
        """Increases damage by 50% if target is vulnerable"""
        if hasattr(target, 'effects'):
            for effect in target.effects:
                if effect.effect_type == "vulnerable":
                    return int(damage * 1.5)
        return damage




    def generate_enemy_intent(enemy):
        """Generates enemy intent for the next turn"""
        import random
        if not hasattr(enemy, 'intent'):
            enemy.intent = None
        if not hasattr(enemy, 'intent_value'):
            enemy.intent_value = 0
        
        
        if hasattr(enemy, 'mp') and hasattr(enemy, 'max_mp') and enemy.max_mp > 0 and enemy.mp >= enemy.max_mp:
            enemy.intent = "special"
            enemy_type = getattr(enemy, 'type', 'unknown')
            if enemy_type == "wolf":
                enemy.intent_value = 0  
            else:
                enemy.intent_value = int(random.randint(enemy.min_attack, enemy.max_attack) * 1.5)
            return
        
        enemy_type = getattr(enemy, 'type', 'unknown')
        
        if enemy_type == "slime":
            
            enemy.intent = "attack"
            enemy.intent_value = random.randint(enemy.min_attack, enemy.max_attack)
        
        elif enemy_type == "wolf":
            roll = random.random()
            if roll < 0.45:
                enemy.intent = "attack"
                enemy.intent_value = random.randint(enemy.min_attack, enemy.max_attack)
            elif roll < 0.70:
                enemy.intent = "attack_heavy"
                enemy.intent_value = int(random.randint(enemy.min_attack, enemy.max_attack) * 1.5)
            else:
                enemy.intent = "debuff"
                enemy.intent_value = 0
        
        elif enemy_type == "ogre":
            roll = random.random()
            if roll < 0.40:
                enemy.intent = "attack"
                enemy.intent_value = random.randint(enemy.min_attack, enemy.max_attack)
            elif roll < 0.60:
                enemy.intent = "attack_heavy"
                enemy.intent_value = int(random.randint(enemy.min_attack, enemy.max_attack) * 1.5)
            elif roll < 0.80:
                enemy.intent = "buff"
                enemy.intent_value = 0
            else:
                enemy.intent = "defend"
                enemy.intent_value = random.randint(10, 20)
        
        elif enemy_type == "bandit":
            roll = random.random()
            if roll < 0.40:
                enemy.intent = "attack"
                enemy.intent_value = random.randint(enemy.min_attack, enemy.max_attack)
            elif roll < 0.65:
                enemy.intent = "attack_heavy"
                enemy.intent_value = int(random.randint(enemy.min_attack, enemy.max_attack) * 1.5)
            elif roll < 0.85:
                enemy.intent = "debuff"
                enemy.intent_value = 0
            else:
                enemy.intent = "buff"
                enemy.intent_value = 0
        
        else:
            enemy.intent = "attack"
            enemy.intent_value = random.randint(enemy.min_attack, enemy.max_attack)

    def generate_all_intents():
        """Generates intents for all living enemies"""
        for enemy in store.enemies:
            if enemy.hp > 0:
                generate_enemy_intent(enemy)

    def get_intent_icon(intent):
        """Returns an icon for the intent type"""
        icons = {
        "attack": "⚔",
        "attack_heavy": "💥",
        "buff": "💪",
        "debuff": "☠",
        "defend": "🛡",
        "special": "⭐"
    }
        return icons.get(intent, "❓")

    def get_intent_color(intent):
        """Returns a color for the intent type"""
        colors = {
        "attack": "#ff4444",
        "attack_heavy": "#ff0000",
        "buff": "#44ff44",
        "debuff": "#aa44ff",
        "defend": "#4488ff",
        "special": "#ff00ff"
    }
        return colors.get(intent, "#ffffff")

    def get_effect_description(effect):
        """Returns a human-readable description of what an effect does"""
        descs = {
        "burn": "Deals {}-{} fire damage per turn.".format(effect.damage_min, effect.damage_max),
        "poison": "Deals {}-{} poison damage per turn.".format(effect.damage_min, effect.damage_max),
        "bleed": "Deals {}-{} bleed damage per turn.".format(effect.damage_min, effect.damage_max),
        "stun": "Skips the next turn.",
        "debuff": "Deals {}-{} damage per turn. Slowed.".format(effect.damage_min, effect.damage_max),
        "weakness": "Reduces outgoing damage by 25%.",
        "vulnerable": "Increases incoming damage by 50%.",
        "slimy": "Slimy! -{}% damage ({} stacks).".format(min(getattr(effect, 'stacks', 1) * 25, 75), getattr(effect, 'stacks', 1)),
    }
        return descs.get(effect.effect_type, "Unknown effect.")

    def get_intent_description(enemy):
        """Returns a human-readable description of the enemy's intent"""
        intent = getattr(enemy, 'intent', 'attack')
        value = getattr(enemy, 'intent_value', 0)
        if intent == "attack":
            return "Atk {}".format(value)
        elif intent == "attack_heavy":
            return "Heavy {}".format(value)
        elif intent == "buff":
            return "Buff"
        elif intent == "debuff":
            return "Debuff"
        elif intent == "defend":
            return "Def +{}".format(value)
        elif intent == "special":
            return "Special!"
        return "?"

    def get_intent_tooltip(enemy):
        """Returns a detailed tooltip dict for an enemy's intent"""
        intent = getattr(enemy, 'intent', 'attack')
        value = getattr(enemy, 'intent_value', 0)
        if intent == "attack":
            return {"name": "Attack", "desc": "Will deal {} damage.".format(value)}
        elif intent == "attack_heavy":
            return {"name": "Heavy Attack", "desc": "Will deal {} heavy damage!".format(value)}
        elif intent == "buff":
            return {"name": "Buff", "desc": "Will buff itself (Strength or Block)."}
        elif intent == "debuff":
            return {"name": "Debuff", "desc": "Will apply a debuff (Weakness or Vulnerable)."}
        elif intent == "defend":
            return {"name": "Defend", "desc": "Will gain {} block.".format(value)}
        elif intent == "special":
            enemy_type = getattr(enemy, 'type', 'unknown')
            if enemy_type == "slime":
                return {"name": "Slimy Coat", "desc": "Will apply Slimy debuff! (-25% damage, stackable)"}
            elif enemy_type == "wolf":
                return {"name": "Enrage", "desc": "Will buff itself with +5 Strength!"}
            return {"name": "Special Attack", "desc": "Will use a powerful special attack with debuff! ({} damage)".format(value)}
        return {"name": "Unknown", "desc": "Unknown action."}
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
