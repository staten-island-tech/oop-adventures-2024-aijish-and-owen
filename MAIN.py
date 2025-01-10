import random
import json
from user import User
from monsters import GreekMonster, FinalBoss
from unifiedmerchant import UnifiedMerchant

class Game:
    def __init__(self):
        self.player = None
        self.monsters = []
        self.final_boss = FinalBoss()
        self.unified_merchant = self.load_merchant()
        self.load_monsters()

    def load_monsters(self):
        with open("monsters.json", "r") as file:
            monster_data = json.load(file)
            for monster in monster_data:
                self.monsters.append(
                    GreekMonster(
                        monster["name"], 
                        monster["health"], 
                        monster["damage"], 
                        monster["flee_rate"]
                    )
                )


    def load_merchant(self):
        with open("armor.json", "r") as armor_file, \
             open("item.json", "r") as item_file, \
             open("weapon.json", "r") as weapon_file:
            armor_data = json.load(armor_file)
            item_data = json.load(item_file)
            weapon_data = json.load(weapon_file)
            return UnifiedMerchant(armor_data, item_data, weapon_data)

    def start(self, player_name):
        self.player = User(player_name, coins=50)  # Player starts with 50 coins
        print(f"Welcome, {self.player.name}! Your journey begins...")

    def encounter_monster(self):
        monster = random.choice(self.monsters)
        print(f"A wild {monster.name} appears!")
        while monster.is_alive() and self.player.is_alive():
            print("\nOptions: 1) Attack 2) Flee")
            choice = input("What do you want to do?")
            if choice == "1":
                self.player.attack(monster)
                if monster.is_alive():
                    monster.attack(self.player)
                    if not self.player.is_alive():
                        print("You have been killed by the monster. GAME OVER!")
                        exit()  # End the game
            elif choice == "2":
                flee_chance = random.randint(1, 100)
                if flee_chance <= monster.flee_rate:
                    print("You've successfully fled the battle!")
                    return
                else:
                    print("You failed to flee!")
                    monster.attack(self.player)
                    if not self.player.is_alive():
                        print("You have been killed while trying to flee. GAME OVER!")
                        exit()  # End the game
            else:
                print("Invalid choice.")
        if self.player.is_alive():
            loot = monster.drop_loot()
            print(f"{monster.name} dropped {loot}!")
            if loot == "Coins":
                self.player.coins += 10
                print(f"{self.player.name} now has {self.player.coins} coins.")
            else:
                self.player.add_item(loot)




    def visit_merchant(self):
        """Visit the unified merchant."""
        self.unified_merchant.merchant(self.player)

    def fight_final_boss(self):
        print("You face the final boss: Typhon!")
        while self.final_boss.is_alive() and self.player.is_alive():
            print("\nOptions: 1) Attack 2) Flee")
            choice = input("What do you want to do? ")
            if choice == "1":
                self.player.attack(self.final_boss)
                if self.final_boss.is_alive():
                    self.final_boss.attack(self.player)
                    if not self.player.is_alive():
                        print("You were defeated by Typhon. GAME OVER!")
                        exit()  # End the game
            elif choice == "2":
                flee_chance = random.randint(1, 100)
                if flee_chance <= 30:  # 30% chance to successfully flee
                    print("You successfully fled the battle!")
                    return
                else:
                    print("You failed to flee!")
                    self.final_boss.attack(self.player)
                    if not self.player.is_alive():
                        print("You were defeated while trying to flee. GAME OVER!")
                        exit()  # End the game
            else:
                print("Invalid choice.")
        if self.player.is_alive():
            print("Congratulations! You defeated Typhon and won the game!")
        else:
            print("You were defeated by Typhon. GAME OVER!")


    def inventory_management(self):
        print("\nInventory Management:")
        self.player.show_inventory()
        print("1. Equip Weapon")
        print("2. Equip Armor")
        print("3. Exit")
        choice = input("What would you like to do? ")
        if choice == "1":
            self.player.equip_weapon()
        elif choice == "2":
            self.player.equip_armor()
        elif choice == "3":
            print("Exiting inventory management.")
        else:
            print("Invalid choice.")

    def run(self):
        player_name = input("Enter your character's name: ")
        self.start(player_name)

        while self.player.is_alive():
            print("\nOptions: 1) Encounter Monster 2) Visit Merchant 3) Fight Final Boss 4) Manage Inventory 5) Quit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.encounter_monster()
            elif choice == "2":
                self.visit_merchant()
            elif choice == "3":
                self.fight_final_boss()
                break
            elif choice == "4":
                self.inventory_management()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    game = Game()
    game.run()
