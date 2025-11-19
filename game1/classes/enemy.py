import random
from .items import StoreItems
class Enemy:

    def __init__(self, kind):
        self.kind = kind

        if kind == "goblin":
            self.health = 80
            self.damage = 10
            self.defense = 6
            self.flying = False
            self.drop = ("gold", 
                         StoreItems("big stick", 10, False, False, False, False, False, 10, 100, 0, True), 
                         StoreItems("cape", 25, False, False, False, False, True, 10, 100, 0))  # gold = moneys (1 - 10 per drop)... big stick = +10 dmg ... cape = +10 defense

        elif kind == "snake":
            self.health = 15
            self.damage = 20
            self.defense = 1
            self.flying = False
            self.drop = (StoreItems("venom", 40, False, True, True, False, False, 20, 100, 0),
                         StoreItems("scales", 5, False, True, False, False, False, 0, 100, 0), 
                         StoreItems("snake eyes", 60, False, True, False, True, False, 25, 100, 0)) #venom == one time 20 dmg... 3 scales to make armor ... snake eyes = +25 health one time

        elif kind == "turtle":
            self.health = 100
            self.damage = 30
            self.defense = 2
            self.flying = True
            self.drop = (StoreItems("shell", 31, False, False, False, False, True, 20, 100, 0), 
                         StoreItems("scales", 5, False, True, False, False, False, 0, 100, 0),
                         StoreItems("top hat", 100, False, False, False, False, True, 5, 100, 0)) #shell == +20 defense... 3 scales to make armor ... top hat = +3 defense and never a badBoy
        elif kind == "Razer DAWG":
            self.health = 75
            self.damage = 30
            self.defense = 6
            self.flying = False
            self.drop = ("gold",)
        else:
            self.health = 50
            self.damage = 5
            self.defense = 3
            self.flying = random.choice([True, False])
            self.drop = (StoreItems("logs", 1, False, True, False, False, False, 1, 100, 0), )

    def attack(self, success):
        
        if success % 2 == 0:
            base = self.damage

            if random.random() < 0.2:
                return int(base * 1.5)

            return base

        return 0

    def defend(self, success, incoming_damage):
        if success % 2 == 0:
            if random.random() < 0.1:
                return 0
            reduced = incoming_damage - self.defense
            return max(reduced, 1)

        return incoming_damage
    
    def getDrop(self):
        return random.choice(self.drop)
