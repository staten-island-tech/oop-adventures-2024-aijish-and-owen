import random
import json
from user import User
from monsters import GreekMonster, FinalBoss
from unifiedmerchant import UnifiedMerchant

# Load weapons
with open('weapon.json', 'r') as f:
    weapons = json.load(f)

# Load armors
with open('armor.json', 'r') as f:
    armors = json.load(f)

# Add items to player inventory
player = User("Hero", 100)
for weapon in weapons:
    player.add_item(weapon)

for armor in armors:
    player.add_item(armor)
