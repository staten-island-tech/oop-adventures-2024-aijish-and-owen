class GreekMonster:
    def __init__(self, name, health, damage, flee_rate):
        self.name = name
        self.health = health
        self.damage = damage
        self.flee_rate = flee_rate  # Flee success rate in percentage

    def is_alive(self):
        return self.health > 0

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.damage} damage!")
        target.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} has {self.health} health left!")

    def drop_loot(self):
        return "Coins"


class FinalBoss(GreekMonster):
    def __init__(self):
        super().__init__("Typhon", 500, 50, 5)
