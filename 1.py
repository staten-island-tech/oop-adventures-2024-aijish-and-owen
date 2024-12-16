import random

# Define the classes for different types of items (Consumables, Buffs, Artifacts, etc.)
class Item:
    def __init__(self, name, item_type, cost, durability, special_ability=None):
        self.name = name
        self.item_type = item_type
        self.cost = cost
        self.durability = durability
        self.special_ability = special_ability
    
    def use(self, character, target=None):
        if self.item_type == "Consumable":
            self._use_consumable(character)
        elif self.item_type == "Buff":
            self._use_buff(character)
        elif self.item_type == "Artifact":
            self._use_artifact(character)
        elif self.item_type == "Magic":
            self._use_magic(character, target)
        
    def _use_consumable(self, character):
        print(f"{character.name} used {self.name}.")
        if "Health Potion" in self.name:
            character.heal(50)
        elif "Mana Potion" in self.name:
            character.restore_mana(30)
        elif "Antidote" in self.name:
            character.cure_poison()
        self.durability -= 1
        if self.durability <= 0:
            print(f"{self.name} has no uses left.")

    def _use_buff(self, character):
        print(f"{character.name} used {self.name}.")
        if "Strength Scroll" in self.name:
            character.increase_strength(10)
        elif "Agility Scroll" in self.name:
            character.increase_agility(10)
        elif "Defense Elixir" in self.name:
            character.increase_defense(15)
        elif "Luck Charm" in self.name:
            character.increase_luck(20)
        elif "Speed Potion" in self.name:
            character.increase_speed(30)
        self.durability -= 1
        if self.durability <= 0:
            print(f"{self.name} has no uses left.")

    def _use_artifact(self, character):
        print(f"{character.name} activated {self.name}.")
        if "Ring of Vitality" in self.name:
            character.increase_hp(50)
        elif "Amulet of Wisdom" in self.name:
            character.increase_mana(30)
        elif "Cloak of Invisibility" in self.name:
            character.activate_invisibility()
        elif "Crystal of the Elements" in self.name:
            character.activate_elemental_resistance()
        elif "Book of Shadows" in self.name:
            character.increase_spell_power(15)
        self.durability -= 1
        if self.durability <= 0:
            print(f"{self.name} has no uses left.")
        
    def _use_magic(self, character, target):
        print(f"{character.name} used {self.name}.")
        if "Fire Staff" in self.name:
            character.cast_fireball(target)
        elif "Ice Wand" in self.name:
            character.cast_freeze(target)
        elif "Lightning Rod" in self.name:
            character.cast_lightning(target)
        elif "Death Scythe" in self.name:
            character.cast_soul_drain(target)
        elif "Wind Blade" in self.name:
            character.cast_wind_blade(target)
        elif "Earth Hammer" in self.name:
            character.cast_earthquake(target)
        elif "Light Bracer" in self.name:
            character.cast_radiance(target)
        elif "Shadow Dagger" in self.name:
            character.cast_shadow_strike(target)
        elif "Frostbow" in self.name:
            character.cast_chill(target)
        self.durability -= 1
        if self.durability <= 0:
            print(f"{self.name} has no uses left.")


# Define the character class
class Character:
    def __init__(self, name, hp, mana, strength, agility, defense, luck, speed):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.defense = defense
        self.luck = luck
        self.speed = speed
        self.poisoned = False
        self.invisibility = False
        self.spell_power = 1.0
    
    def heal(self, amount):
        self.hp += amount
        print(f"{self.name} heals for {amount} HP. Total HP: {self.hp}")
    
    def restore_mana(self, amount):
        self.mana += amount
        print(f"{self.name} restores {amount} Mana. Total Mana: {self.mana}")
    
    def cure_poison(self):
        self.poisoned = False
        print(f"{self.name} is no longer poisoned.")
    
    def increase_strength(self, amount):
        self.strength += amount
        print(f"{self.name}'s Strength increased by {amount}. Total Strength: {self.strength}")
    
    def increase_agility(self, amount):
        self.agility += amount
        print(f"{self.name}'s Agility increased by {amount}. Total Agility: {self.agility}")
    
    def increase_defense(self, amount):
        self.defense += amount
        print(f"{self.name}'s Defense increased by {amount}. Total Defense: {self.defense}")
    
    def increase_luck(self, amount):
        self.luck += amount
        print(f"{self.name}'s Luck increased by {amount}. Total Luck: {self.luck}")
    
    def increase_speed(self, amount):
        self.speed += amount
        print(f"{self.name}'s Speed increased by {amount}. Total Speed: {self.speed}")
    
    def increase_hp(self, amount):
        self.hp += amount
        print(f"{self.name}'s HP increased by {amount}. Total HP: {self.hp}")
    
    def increase_mana(self, amount):
        self.mana += amount
        print(f"{self.name}'s Mana increased by {amount}. Total Mana: {self.mana}")
    
    def activate_invisibility(self):
        self.invisibility = True
        print(f"{self.name} becomes invisible for 5 seconds.")
    
    def activate_elemental_resistance(self):
        print(f"{self.name} gains resistance to all elemental damage.")
    
    def increase_spell_power(self, amount):
        self.spell_power += amount / 100
        print(f"{self.name}'s Spell Power increased by {amount}%. Total Spell Power: {self.spell_power}")
    
    def take_damage(self, amount, damage_type):
        self.hp -= amount
        print(f"{self.name} takes {amount} {damage_type} damage. Remaining HP: {self.hp}")
    
    def is_alive(self):
        return self.hp > 0
    
    def attack(self, target):
        damage = self.strength * random.uniform(0.8, 1.2)  # Random variation in damage
        target.take_damage(damage, "Physical")
        print(f"{self.name} attacks {target.name}, dealing {damage:.2f} Physical damage.")


# Define the Monster class
class Monster:
    def __init__(self, name, hp, attack, defense, special_ability=None):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_ability = special_ability

    def take_damage(self, amount, damage_type):
        self.hp -= amount
        print(f"{self.name} takes {amount} {damage_type} damage. Remaining HP: {self.hp}")
    
    def attack(self, target):
        damage = self.attack * random.uniform(0.8, 1.2)  # Random variation in attack damage
        target.take_damage(damage, "Physical")
        print(f"{self.name} attacks {target.name}, dealing {damage:.2f} Physical damage.")
    
    def is_alive(self):
        return self.hp > 0


# Function to handle user input and gameplay
def combat_sequence(hero, monster, items):
    while hero.is_alive() and monster.is_alive():
        print(f"\n{hero.name}'s HP: {hero.hp} | {monster.name}'s HP: {monster.hp}")
        print("What would you like to do?")
        print("1: Attack")
        print("2: Use Item")
        print("3: Run")
        
        action = input("Choose an action (1/2/3): ").strip()

        if action == '1':  # Attack
            hero.attack(monster)
            if monster.is_alive():
                monster.attack(hero)
        elif action == '2':  # Use Item
            print("Select an item to use:")
            for idx, item in enumerate(items, 1):
                print(f"{idx}: {item.name} (Durability: {item.durability})")
            item_choice = int(input("Choose an item (1-{}): ".format(len(items)))) - 1
            if 0 <= item_choice < len(items):
                items[item_choice].use(hero, monster)
                if monster.is_alive():
                    monster.attack(hero)
            else:
                print("Invalid item choice.")
        elif action == '3':  # Run
            if random.random() < 0.5:  # 50% chance to escape
                print(f"{hero.name} successfully ran away!")
                break
            else:
                print(f"{hero.name} failed to escape and is still in combat.")
                monster.attack(hero)
        else:
            print("Invalid action, please choose 1, 2, or 3.")

    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{hero.name} has been defeated...")


# Example Setup
hero = Character("Hero", 100, 50, 20, 10, 10, 5, 10)
monster = Monster("Goblin", 80, 15, 5)
items = [
    Item("Health Potion", "Consumable", 10, 3),
    Item("Strength Scroll", "Buff", 5, 2),
    Item("Fire Staff", "Magic", 20, 1)
]

combat_sequence(hero, monster, items)
