class UnifiedMerchant:
    def __init__(self, armor_data, item_data, weapon_data):
        self.armor_inventory = self.load_inventory(armor_data)
        self.item_inventory = self.load_inventory(item_data)
        self.weapon_inventory = self.load_inventory(weapon_data)


    def load_inventory(self, data):
        """Load inventory from data."""
        if isinstance(data, dict):
            # Flatten nested categories if the JSON is structured with categories
            inventory = []
            for category, items in data.items():
                inventory.extend(items)
            return inventory
        elif isinstance(data, list):
            return data  # Data is already a flat list
        else:
            raise ValueError("Invalid inventory data format.")


    def display_inventory(self, inventory):
        """Display items in inventory."""
        for idx, item in enumerate(inventory, start=1):
            price = item.get("price", "N/A")
            print(f"{idx}. {item['name']} (Price: {price} coins)")


    def buy_item(self, player, inventory, item_index):
        """Allow the player to buy an item."""
        # Validate the item index
        if item_index < 1 or item_index > len(inventory):
            print("Invalid selection.")
            return


        item = inventory[item_index - 1]
       
        # Check if the player can afford the item
        if player.coins >= item["price"]:
            player.coins -= item["price"]  # Deduct the cost
            player.inventory.append(item)  # Add item to inventory
            print(f"You bought {item['name']} for {item['price']} coins!")
        else:
            print(f"You don't have enough coins to buy {item['name']}.")


        # Debugging output for clarity (optional)
        print(f"Remaining coins: {player.coins}")








    def merchant(self, player):
        """Merchant interaction."""
        while True:
            print("\nWelcome to the Merchant!")
            print("1. Buy Weapons")
            print("2. Buy Armor")
            print("3. Buy Items")
            print("4. Exit")
            choice = input("What would you like to do? ")


            if choice == "1":
                print("\nAvailable Weapons:")
                self.display_inventory(self.weapon_inventory)
                item_choice = input("Enter the number of the weapon to buy or 'b' to go back: ")
                if item_choice.lower() == "b":
                    continue
                try:
                    item_index = int(item_choice)
                    self.buy_item(player, self.weapon_inventory, item_index)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
           
            elif choice == "2":
                print("\nAvailable Armor:")
                self.display_inventory(self.armor_inventory)
                item_choice = input("Enter the number of the armor to buy or 'b' to go back: ")
                if item_choice.lower() == "b":
                    continue
                try:
                    item_index = int(item_choice)
                    self.buy_item(player, self.armor_inventory, item_index)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
           
            elif choice == "3":
                print("\nAvailable Items:")
                self.display_inventory(self.item_inventory)
                item_choice = input("Enter the number of the item to buy or 'b' to go back: ")
                if item_choice.lower() == "b":
                    continue
                try:
                    item_index = int(item_choice)
                    self.buy_item(player, self.item_inventory, item_index)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
           
            elif choice == "4":
                print("Thank you for visiting the merchant!")
                break
           
            else:
                print("Invalid choice. Please try again.")




