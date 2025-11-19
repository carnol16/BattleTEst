import random
from .armor import Armor
from .specials import Special
class Player:
    

    def __init__(self, type, color, name):
        self.type = type
        self.color = color
        self.name = name
        self.mana = 50
        self.space = 10 #default space
        self.items = [] #empty storage
        self.wallet = 0
        self.weapon = None
        self.armor = None

        
        

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
                print(counter, i.name, i.manaCost)
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

    
    def storage(self):
        if not hasattr(self, "items"):
            self.items = []

        while True:
            print("\n===== STORAGE MENU =====")
            print("1. Check space")
            print("2. Remove item")
            print("3. View all items")
            print("4. Use an item")
            print("5. Attach / Detach Armor")
            print("6. Attach / Detach Weapon")
            print("7. Exit storage")

            choice = input("> ").strip()

            # 1. CHECK SPACE
            if choice == "1":
                free = self.space - len(self.items)
                print(f"Inventory space: {len(self.items)}/{self.space} (Free: {free})")


            # 2. REMOVE ITEM
            elif choice == "2":
                if not self.items:
                    print("Storage is empty!")
                    continue
                
                print("\nItems:")
                for i, item in enumerate(self.items):
                    print(f"{i}: {item.name}")

                try:
                    idx = int(input("Enter index to remove: "))
                    removed = self.items.pop(idx)
                    print(f"Removed {removed.name}")
                except:
                    print("Invalid index")


            # 3. VIEW ALL ITEMS
            elif choice == "3":
                if not self.items:
                    print("Storage empty!")
                else:
                    print("\nYour Items:")
                    for i, item in enumerate(self.items):
                        kind = "Armor" if getattr(item, "armor", False) else "Weapon" if getattr(item, "weapon", False) else "Item"
                        print(f"{i}: {item.name} ({kind})")


            # 4. USE ITEM (consumables)
            elif choice == "4":
                if not self.items:
                    print("No items to use!")
                    continue

                print("\nWhich item do you want to use?")
                for i, item in enumerate(self.items):
                    print(f"{i}: {item.name}")

                try:
                    idx = int(input("Choose index: "))
                    item = self.items[idx]

                    if item.damage or item.heal:
                        item.use(self, self)  # You may need target = enemy in battle
                        print(f"Used {item.name}")
                        self.items.pop(idx)
                    else:
                        print("This isn't a usable item!")
                except:
                    print("Invalid selection.")

            # 5. ATTACH/DETACH ARMOR
            elif choice == "5":
                print("\n===== ARMOR MENU =====")

                # If player wearing armor
                if self.armor:
                    print(f"Currently equipped armor: {self.armor.name} (+{self.armor.amount} DEF)")
                    det = input("Detach current armor? (yes/no): ").lower()
                    if det == "yes":
                        old = self.armor
                        self.defense -= old.amount
                        self.armor = None
                        self.quickStorage(old)
                        print(f"Detached {old.name} and stored it.")
                    continue

                # If not wearing armor → pick one from storage
                print("\nSelect armor to attach:")
                armor_items = [(i, item) for i, item in enumerate(self.items) if getattr(item, "armor", False)]

                if not armor_items:
                    print("You have no armor in storage.")
                    continue

                for i, item in armor_items:
                    print(f"{i}: {item.name} (+{item.amount} DEF)")

                try:
                    idx = int(input("Choose armor index: "))
                    newArmor = self.items.pop(idx)

                    self.armor = newArmor
                    self.defense += newArmor.amount
                    print(f"Equipped {newArmor.name}!")
                except:
                    print("Invalid selection.")

            # 6. ATTACH/DETACH WEAPON
            elif choice == "6":
                print("\n===== WEAPON MENU =====")

                if self.weapon:
                    print(f"Equipped weapon: {self.weapon.name} (+{self.weapon.amount} DMG)")
                    det = input("Detach current weapon? (yes/no): ").lower()
                    if det == "yes":
                        old = self.weapon
                        self.damage -= old.amount
                        self.weapon = None
                        self.quickStorage(old)
                        print(f"Detached {old.name} and stored it.")
                    continue

                print("\nChoose weapon to attach:")
                weapon_items = [(i, item) for i, item in enumerate(self.items) if getattr(item, "weapon", False)]

                if not weapon_items:
                    print("You have no weapons in storage.")
                    continue

                for i, item in weapon_items:
                    print(f"{i}: {item.name} (+{item.amount} DMG)")

                try:
                    idx = int(input("Choose weapon index: "))
                    newWeapon = self.items.pop(idx)

                    self.weapon = newWeapon
                    self.damage += newWeapon.amount
                    print(f"Equipped {newWeapon.name}!")
                except:
                    print("Invalid selection.")

            # 7. EXIT
            elif choice == "7":
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



