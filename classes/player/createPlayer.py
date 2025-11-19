import random
from .armor import Armor
from .specials import Special
from classes.items import StoreItems
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
        self.badBoy = False
        self.increaseDefend = 0

        
        

        if type == "warrior":
            self.health = 200
            self.damage = 10
            self.defense = 4
            self.space = 3
            self.attacks = [
                Special("Taco HITTER", "attack", True, False, 20, 10),
                Special("Counter Strike", "attack", True, False, 10, 10),
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

    def myStats(self):
        avalibleSpace = self.space - len(self.items) 
        print(f"Here is {self.name}'s silly stats\n")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}")
        if self.armor is None:
            print(f"Base Defense: ", self.defense)
            print("Armor: None")
        else:
            print(f"Base Defense: ", self.damage - self.armor.amount)
            print(f"Armor: {self.armor.name} || DEF: +{self.armor.amount} || DUR: {self.armor.durability}")
        if self.weapon is None:
            print(f"Base Damage: ", self.damage)
            print("Weapon: None")
        else:
            print(f"Base Damage: ", self.damage - self.weapon.amount)
            print(f"Weapon: {self.weapon.name} || DMG: +{self.weapon.amount}")
        print(f"Available Space {avalibleSpace}")

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

        elif choice == 2:
            counter = 0
            for i in self.attacks:
                print(counter, i.name, i.manaCost)
                counter += 1
            specialChoice = int(input("which special do you wanna useeeeeee? "))

            # FIXED: use(self, enemy) instead of mainCharacter, enemy
            dmg = self.attacks[specialChoice].use(self, enemy)
            return dmg

        elif choice == 3:
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
        elif choice == 4:
            extraDefense = random.randint(1, 8)
            print("Ahhhhhh you scared huh")
            print(f"This round: DEF +{extraDefense}")
            self.increaseDefend = extraDefense
            
            return 0
        else:
            return 0
        
    def defend(self, success, incomingDamage):

        # Safety check: no armor equipped
        if self.armor is None:
            return incomingDamage
        elif self.increaseDefend == 0:
            # Dodge chance
            if success % 2 == 0:
                if random.random() < 0.1:
                    print("GOOD DODGE")
                    return 0

                #Damage reduction
                reducedDamage = incomingDamage - self.defense
                reducedDamage = max(reducedDamage, 1)

                # Armor durability logic
                if self.armor.durability is None:
                    self.armor.durability = 100

                durabilityLoss = int((reducedDamage / 3) - 1)
                if durabilityLoss < 1:
                    durabilityLoss = 1

                self.armor.durability -= durabilityLoss

                # Prevent negative durability
                if self.armor.durability <= 0:
                    self.armor.durability = 0
                    print(f"{self.armor.name} broke!")
                    self.armor.detach(self)

                return reducedDamage

        elif self.increaseDefend > 0:
            # Dodge chance
            if success % 2 == 0:
                if random.random() < 0.1:
                    print("GOOD DODGE")
                    return 0

                #Damage reduction
                reducedDamage = incomingDamage - self.defense - self.increaseDefend
                reducedDamage = max(reducedDamage, 1)

                # Armor durability logic
                if self.armor.durability is None:
                    self.armor.durability = 100

                durabilityLoss = int((reducedDamage / 3) - 1)
                if durabilityLoss < 1:
                    durabilityLoss = 5

                self.armor.durability -= durabilityLoss

                # Prevent negative durability
                if self.armor.durability <= 0:
                    self.armor.durability = 0
                    print(f"{self.armor.name} broke!")
                    self.armor.detach(self)
                    
                self.increaseDefend = 0

                return reducedDamage
        # No dodge / odd success → full damage 
        return incomingDamage
   
    def storage(self):
        if not hasattr(self, "items"):
            self.items = []

        while True:
            print("\n===== STORAGE MENU =====")
            print("1. Check Stats")
            print("2. Remove item")
            print("3. View all items")
            print("4. Use an item")
            print("5. Attach / Detach Armor")
            print("6. Attach / Detach Weapon")
            print("7. Exit storage")

            choice = input("> ").strip()

            # 1. CHECK SPACE
            if choice == "1":
                self.myStats()

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

                        if getattr(item, "armor", False):
                            kind = "Armor"
                        elif getattr(item, "weapon", False):
                            kind = "Weapon"
                        else:
                            kind = "Item"

                        # Show durability for armor
                        if kind == "Armor":
                            durability = getattr(item, "durability", "N/A")
                            print(f"{i}: {item.name} ({kind}) - Durability: {durability}")
                        else:
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
    




