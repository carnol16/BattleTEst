import random
from .armor import Armor

from .specials import Special
class Player:
    

    def __init__(self, type, color):
        self.type = type
        self.color = color
        self.mana = 50
        self.space = 10 #default space
        self.items = [] #empty storage
        self.wallet = 0
        #self.weapon = 
        self.armor = Armor("Naked")
        
        

        if type == "warrior":
            self.health = 200
            self.damage = 10
            self.defense = 4
            self.space = 3
            self.attacks = [
                Special("Taco HITTER", "attack", True, False, 20, 10),
                Special("Women Strike", "attack", True, False, 10, 10),
                Special("Children Tears", "heal", False, True, 100, 50)
            ]   

        elif type == "basement dweller":
            self.health = 150
            self.damage = 8
            self.defense = 10
            self.space = 8
            self.attacks = [
                Special("GOONING", "attack", True, False, 5, 10),
                Special("Discord Modding", "attack", True, False, 15, 25),
                Special("White Monster into the VEINS", "heal", False, True, 25, 10)
            ]   

        elif type == "boat man":
            self.health = 180
            self.damage = 10
            self.defense = 10
            self.space = 5
            self.attacks = [
                Special("Plunder", "attack", True, False, 25, 10),
                Special("Cannon BRRRRR", "attack", True, False, 100, 50),
                Special("Motorboating", "heal", False, True, 50, 40)
            ]
            

        elif type == "ninja":
            self.health = 80
            self.damage = 7
            self.defense = 15
            self.space = 1
            self.attacks = [
                Special("Sneaky Deeky Like", "attack", True, False, 10, 5),
                Special("Back Flip", "attack", True, False, 25, 25),
                Special("Drinking Blood of My enemies", "heal", True, True, 10, 30)
            ]  

        else:
            self.health = 10
            self.damage = 1
            self.defense = 0
            self.space = 2
            self.attacks = [
                Special("depression", "attack", True, False, -10, 10)
            ]  

        if color == "blue":
            self.health += 10

        elif color == "red":
            self.health -= 8
            self.damage += 2

    def attack(self, success, option, enemy):
        choice = int(option)
        base = self.damage

        if choice == 1:
            if success % 2 == 0:
                if random.random() < 0.2:
                    print("YOU HIT A CRIT")
                    return int(base * 1.5)
                return base
            else:
                return 0  # Attack missed

        if choice == 2:
            counter = 0
            for i in self.attacks:
                print(counter, i.name)
                counter += 1
            specialChoice = int(input("which special do you wanna useeeeeee? "))

            # FIXED: use(self, enemy) instead of mainCharacter, enemy
            dmg = self.attacks[specialChoice].use(self, enemy)
            return dmg

        if choice == 3:
            counter = 0
            itemCount = len(self.items)
            if itemCount > 0:
                for i in self.items:
                    print(counter, i.name)
                    counter += 1
                itemChoice = int(input("which item do you wanna useeeeeee? "))

                # FIXED: use(self, enemy)
                self.items[itemChoice].use(self, enemy)

                del self.items[itemChoice]
                return 0
            else:
                print("wasted a turn dumbass")
                return 0

        else:
            return 0


    def defend(self, success, incoming_damage):
        if success % 2 == 0:
            if random.random() < 0.1:
                print("GOOD DODGE")
                return 0
            reduced = incoming_damage - self.defense
            return max(reduced, 1)
        return incoming_damage

    
    def storage(self, itemDropped):
        print("Here are the items you have currently:")
        for i in self.items:
            print(i)
        if not hasattr(self, "items"):
            self.items = []

        while True:
            print("\nStorage Menu:")
            print("1. Check space")
            print("2. Remove item")
            print("3. Check for an item")
            print("4. Exit")

            choice = input("Choose an action (1-5): ").strip()

            if choice == "1":
                free_space = self.space - len(self.items)
                print(f"Available slots: {free_space}")

            elif choice == "2":
                if not self.items:
                    print("Storage is empty!")
                    continue
                item = input("Enter the item to remove: ").strip()
                if item in self.items:
                    self.items.remove(item)
                    print(f"{item} removed. Current items: {self.items}")
                else:
                    print(f"{item} not found in storage.")

            elif choice == "3":
                item = input("Enter the item to check: ").strip()
                if item in self.items:
                    print(f"{item} is in storage.")
                else:
                    print(f"{item} is NOT in storage.")

            elif choice == "4":
                print("Exiting storage.")
                break

            else:
                print("Invalid choice, try again.")
                
    def quickStorage(self, addItem):
        freeSpace = self.space - len(self.items)
        if freeSpace > 0:
            self.items.append(addItem)
        else:
            print("sorry baddie, no space")
            dropItem = input("would you like to dispose of something??? ")
            
            if dropItem == "yes":
                print("Here are the items you have currently:")
                for i in self.items:
                    print(i.name)

                item = input("Enter the item to remove: ").strip()
                if item in self.items:
                    self.items.remove(item)
                    print(f"{item} removed. Current items: {self.items}")
                else:
                    print(f"{item} not found in storage.")
                
                self.items.append(addItem)
                
            else:
                print("your loss:( ")      



