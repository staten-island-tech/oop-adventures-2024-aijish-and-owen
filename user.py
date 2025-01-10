class User:
    def __init__(self, name, coins):
        self.name = name
        self.health = 100
        self.base_damage = 5
        self.coins = coins
        self.inventory = []
        self.weapon = None
        self.armor = None

    def is_alive(self):
        return self.health > 0

    def attack(self, target):
        # Calculate total damage with equipped weapon
        weapon_damage = 0
        if self.weapon:
            weapon_damage = self.weapon["damage"]
            self.weapon["durability"] -= 1  # Reduce weapon durability
            print(f"{self.weapon['name']} durability: {self.weapon['durability']}")

            if self.weapon["durability"] <= 0:
                print(f"{self.weapon['name']} has broken!")
                self.weapon = None  # Unequip the broken weapon

        total_damage = self.base_damage + weapon_damage
        print(f"{self.name} attacks {target.name} for {total_damage} damage!")
        target.take_damage(total_damage)


    def take_damage(self, amount):
        # Reduce damage based on equipped armor
        armor_protection = self.armor["protection"] if self.armor else 0
        net_damage = max(amount - armor_protection, 0)
        self.health -= net_damage
        self.health = max(self.health, 0)  # Ensure health does not drop below 0
        print(f"{self.name} takes {net_damage} damage and has {self.health} health left!")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item['name']} added to your inventory.")

    def show_inventory(self):
        print("\nInventory:")
        for item in self.inventory:
            print(f"- {item['name']}")


    def equip_weapon(self):
        weapons = [item for item in self.inventory if "damage" in item]
        if not weapons:
            print("You have no weapons in your inventory.")
            return

        print("\nAvailable Weapons:")
        for idx, weapon in enumerate(weapons, start=1):
            print(f"{idx}. {weapon['name']} (Damage: {weapon['damage']}, Durability: {weapon['durability']})")

        choice = input("Enter the number of the weapon to equip or 'b' to go back: ")
        if choice.lower() == "b":
            return

        try:
            weapon_choice = int(choice)
            if 1 <= weapon_choice <= len(weapons):
                self.weapon = weapons[weapon_choice - 1]
                print(f"You equipped {self.weapon['name']}!")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")


    def equip_armor(self):
        armors = [item for item in self.inventory if "protection" in item]
        if not armors:
            print("You have no armor in your inventory.")
            return

        print("\nAvailable Armor:")
        for idx, armor in enumerate(armors, start=1):
            print(f"{idx}. {armor['name']} (Protection: {armor['protection']})")

        choice = input("Enter the number of the armor to equip or 'b' to go back: ")
        if choice.lower() == "b":
            return

        try:
            armor_choice = int(choice)
            if 1 <= armor_choice <= len(armors):
                self.armor = armors[armor_choice - 1]
                print(f"You equipped {self.armor['name']}!")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")

