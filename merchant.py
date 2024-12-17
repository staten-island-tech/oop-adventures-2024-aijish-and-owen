import json

# Assuming you have the JSON data for armors, consumables, buffs, and items like melee, ranged, magic
armor_data = json.loads("""
{
    "Light Armor": [
        {"name": "Leather Armor", "type": "Light", "defense": 5, "element": null, "Cost": 10, "Durability": 30, "special_ability": null},
        {"name": "Studded Leather Armor", "type": "Light", "defense": 8, "element": null, "Cost": 15, "Durability": 40, "special_ability": null},
        {"name": "Elven Tunic", "type": "Light", "defense": 12, "element": "Nature", "Cost": 25, "Durability": 50, "special_ability": "Nature's Resilience (Heals 5 HP every turn in nature-rich environments)"},
        {"name": "Wind Cloak", "type": "Light", "defense": 10, "element": "Wind", "Cost": 20, "Durability": 45, "special_ability": "Wind's Embrace (Increases movement speed by 15%)"},
        {"name": "Frostweave Armor", "type": "Light", "defense": 14, "element": "Ice", "Cost": 30, "Durability": 60, "special_ability": "Chill Aura (Slows enemies within 5 meters by 20%)"}
    ],
    "Medium Armor": [
        {"name": "Chainmail Armor", "type": "Medium", "defense": 18, "element": null, "Cost": 35, "Durability": 70, "special_ability": null},
        {"name": "Barbute Helmet", "type": "Medium", "defense": 20, "element": null, "Cost": 40, "Durability": 80, "special_ability": null},
        {"name": "Dragonhide Armor", "type": "Medium", "defense": 22, "element": "Fire", "Cost": 50, "Durability": 85, "special_ability": "Flame Shield (Reduces fire damage by 40%)"},
        {"name": "Shadow Armor", "type": "Medium", "defense": 19, "element": "Shadow", "Cost": 45, "Durability": 75, "special_ability": "Shadowmeld (Grants invisibility for 5 seconds when standing still)"},
        {"name": "Dwarven Plate", "type": "Medium", "defense": 25, "element": "Earth", "Cost": 60, "Durability": 90, "special_ability": "Stoneform (Increases defense by 20% for 5 seconds after taking damage)"}
    ],
    "Heavy Armor": [
        {"name": "Plate Armor", "type": "Heavy", "defense": 35, "element": null, "Cost": 70, "Durability": 100, "special_ability": null},
        {"name": "Guardian Armor", "type": "Heavy", "defense": 40, "element": null, "Cost": 80, "Durability": 120, "special_ability": null},
        {"name": "Celestial Plate", "type": "Heavy", "defense": 50, "element": "Light", "Cost": 100, "Durability": 140, "special_ability": "Divine Shield (Reduces all damage by 30% for 3 turns after activation)"},
        {"name": "Titanium Plate", "type": "Heavy", "defense": 45, "element": "Metal", "Cost": 120, "Durability": 160, "special_ability": "Ironclad (Increases resistance to physical damage by 25%)"},
        {"name": "Obsidian Armor", "type": "Heavy", "defense": 55, "element": "Fire", "Cost": 130, "Durability": 180, "special_ability": "Molten Armor (Deals 10 Fire damage to attackers on hit)"}
    ]
}
""")

# Sample data for Consumables, Buffs, and Melee weapons, etc. (more json parsing similar to above).
consumables_data = json.loads("""
{
    "Consumables": [
        {"name": "Health Potion", "type": "Consumable", "effect": "Heals 50 HP", "Cost": 10, "Durability": 1, "special_ability": null},
        {"name": "Mana Potion", "type": "Consumable", "effect": "Restores 30 Mana", "Cost": 12, "Durability": 1, "special_ability": null},
        {"name": "Antidote", "type": "Consumable", "effect": "Cures Poison", "Cost": 15, "Durability": 1, "special_ability": null}
    ],
    "Buffs": [
        {"name": "Strength Scroll", "type": "Buff", "effect": "Increases Strength by 10 for 3 turns", "Cost": 20, "Durability": 1, "special_ability": "Strength Boost"}
    ]
}
""")

items_data = json.loads("""
{
    "Melee": [
        {"name": "Basic Sword", "type": "Melee", "damage": 5, "element": null, "Cost": 8, "Durability": 25, "mana_cost": 0, "special_ability": null},
        {"name": "Steel Sword", "type": "Melee", "damage": 12, "element": null, "Cost": 15, "Durability": 50, "mana_cost": 0, "special_ability": null}
    ]
}
""")

# List all items from all categories
def show_items():
    print("Welcome to the Merchant!")
    print("Here are the items available:")
    
    print("\nLight Armor:")
    for item in armor_data["Light Armor"]:
        print(f"{item['name']} - Cost: {item['Cost']} gold")
    
    print("\nMedium Armor:")
    for item in armor_data["Medium Armor"]:
        print(f"{item['name']} - Cost: {item['Cost']} gold")
    
    print("\nHeavy Armor:")
    for item in armor_data["Heavy Armor"]:
        print(f"{item['name']} - Cost: {item['Cost']} gold")
    
    print("\nConsumables:")
    for item in consumables_data["Consumables"]:
        print(f"{item['name']} - Cost: {item['Cost']} gold")
    
    print("\nBuffs:")
    for item in consumables_data["Buffs"]:
        print(f"{item['name']} - Cost: {item['Cost']} gold")
    
    print("\nMelee Weapons:")
    for item in items_data["Melee"]:
        print(f"{item['name']} - Cost: {item['Cost']} gold")
    
    # You can add Ranged and Magic items similarly

# Main game loop for interacting with the merchant
def merchant():
    show_items()
    
    balance = 100  # Player's initial gold balance
    print(f"\nYour current balance is: {balance} gold.")
    
    choice = int(input("\nEnter the number of the item you want to buy or 0 to exit: "))
    
    # This is just a simple example of how to handle buying and inventory. You can extend it as needed.
    if choice == 1:  # Example: buying an item
        item_cost = armor_data["Light Armor"][0]["Cost"]
        if balance >= item_cost:
            balance -= item_cost
            print(f"Purchased item: {armor_data['Light Armor'][0]['name']} for {item_cost} gold.")
        else:
            print("Not enough gold!")
    else:
        print("Thanks for visiting the merchant!")

merchant()
