import random

class Enemy:

    def __init__(self, kind):
        self.kind = kind

        if kind == "goblin":
            self.health = 80
            self.damage = 10
            self.defense = 6
            self.flying = False
            self.drop = ("gold", 
                         StoreItems("big stick", 10, False, False, True, False, False, 10, 100, 0), 
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
            self.defense = 10
            self.flying = True
            self.drop = (StoreItems("shell", 31, False, False, False, False, True, 20, 100, 0), 
                         StoreItems("scales", 5, False, True, False, False, False, 0, 100, 0),
                         StoreItems("top hat", 100, False, False, False, False, True, 5, 100, 0)) #shell == +20 defense... 3 scales to make armor ... top hat = +3 defense and never a badBoy

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


class Player:
    

    def __init__(self, type, color):
        self.type = type
        self.color = color
        self.mana = 50
        self.space = 10 #default space
        self.items = [] #empty storage
        self.wallet = 0

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
            #self.special = ["GOONING"]

        elif type == "boat man":
            self.health = 180
            self.damage = 10
            self.defense = 10
            self.space = 5
            #self.special = ["Plunder"]

        elif type == "ninja":
            self.health = 80
            self.damage = 7
            self.defense = 15
            self.space = 1
            #self.special = ["Backflip"]

        else:
            self.health = 10
            self.damage = 1
            self.defense = 0
            self.space = 2
            #self.special = ["depression"]

        if color == "blue":
            self.health += 10

        elif color == "red":
            self.health -= 8
            self.damage += 2

    def attack(self, success, option):
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
            for i in mainCharacter.attacks:
                print(counter, i.name)
                counter += 1
            specialChoice = int(input("which special do you wanna useeeeeee? "))
            
            dmg = mainCharacter.attacks[specialChoice].use(mainCharacter, enemy)
            return dmg  # now dmg will be an int
        
        if choice == 3:
            counter = 0
            itemCount = len(self.items)
            if itemCount > 0:
                for i in mainCharacter.items:
                    print(counter, i.name)
                    counter += 1
                itemChoice = int(input("which item do you wanna useeeeeee? "))
                
                mainCharacter.items[itemChoice].use(mainCharacter, enemy)
                del mainCharacter.items[itemChoice]
                return 0
            else:
                print("wasted a turn dumbass")
                return 0 
                         
                
        else:
            # Handle other options here or return 0 if not implemented
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
            print("2. Add item")
            print("3. Remove item")
            print("4. Check for an item")
            print("5. Exit")

            choice = input("Choose an action (1-5): ").strip()

            if choice == "1":
                free_space = self.space - len(self.items)
                print(f"Available slots: {free_space}")

            elif choice == "2":
                if len(self.items) >= self.space:
                    print("No space to add more items!")
                    continue
                item = itemDropped
                self.items.append(item)
                print(f"{item} added. Current items: {self.items}")

            elif choice == "3":
                if not self.items:
                    print("Storage is empty!")
                    continue
                item = input("Enter the item to remove: ").strip()
                if item in self.items:
                    self.items.remove(item)
                    print(f"{item} removed. Current items: {self.items}")
                else:
                    print(f"{item} not found in storage.")

            elif choice == "4":
                item = input("Enter the item to check: ").strip()
                if item in self.items:
                    print(f"{item} is in storage.")
                else:
                    print(f"{item} is NOT in storage.")

            elif choice == "5":
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
                    print(i)

                item = input("Enter the item to remove: ").strip()
                if item in self.items:
                    self.items.remove(item)
                    print(f"{item} removed. Current items: {self.items}")
                else:
                    print(f"{item} not found in storage.")
                
                self.items.append(addItem)
                
            else:
                print("your loss:( ")      


class Special:
    def __init__(self, name, type, damage, heal, amount, manaCost):
        self.name = name
        self.type = type
        self.damage = damage
        self.heal = heal
        self.amount = amount
        self.manaCost = manaCost

    def use(self, user, target):
        """
        Returns the numeric effect of the special (damage or heal).
        """
        
        if user.mana > self.manaCost:
            if self.damage:
                target.health -= self.amount
                user.mana -= self.manaCost
                print("New mana total: ", user.mana)
                return self.amount  # return damage done
            elif self.heal:
                user.health += self.amount
                user.mana -= self.manaCost
                print("New mana total: ",  user.mana)
                print("new health total: ", user.health)
                return 0
            else:

                return 0
        else:
            print("sorry for party rocking :(")
            return 0

class StoreItems:
    
    def __init__(self, name, price, specials, items, damage, heal, armor, amount, rarity, manaCost):
        self.name = name
        self.price = price
        self.specials = specials
        self.items = items
        self.damage = damage
        self.heal = heal
        self.armor = armor
        self.amount = amount
        self.rarity = rarity
        self.manaCost = manaCost

    def use(self, user, target):
        """
        Returns the numeric effect of the special (damage or heal).
        """
        
        if user.mana >= self.manaCost:
            if self.damage:
                target.health -= self.amount
                user.mana -= self.manaCost
                print("New mana total: ", user.mana)
                return self.amount  # return damage done
            elif self.heal:
                user.health += self.amount
                user.mana -= self.manaCost
                print("New mana total: ",  user.mana)
                print("new health total: ", user.health)
                return 0
            else:
                return 0
        else:
            print("sorry for party rocking :(")
        
        
               
    
#types == range, melee
#color == RGB [R,G,B]

''' 
class Weapon:
    
    def __init__(self, type, color, damage):
        self.type = type
        self.color = color
        self.damage = damage
    
        if type == "melee":
''' 

# === GAME START ===

name = "george"
playerType = "warrior"
color = "red"

badBoy = False

mainCharacter = Player(playerType, color)

enemy_types = ("goblin", "snake", "turtle", "log")
num_enemies = random.randint(1, 5)

print("You will fight", num_enemies, "enemies.")

fight_num = 0

def storeOpen():
    itemChoices = [StoreItems("Daddy's Belt", 100, True, False, True, False, False, 100, 10, 60), #Special
                   StoreItems("Cased Hardened AK-47", 423, True, False, True, False, False, 35, 15, 15), #Special
                   StoreItems("Gamer Girl Bath Water", 30, False, True, False, True, False, 45, 75, 0), #Healing Item
                   StoreItems("Sam Keh's Secret Love For Brian", 1, True, False, False, True, False, 1000, 1, 1),  #Specials
                   StoreItems("Top Ramen", 1, False, True, False, True, False, 5, 100, 0), #Healing Item
                   StoreItems("Pink Suit", 70, False, False, False, False, True, 5, 45, 0) #armor
                   ]
    avaiableItems = []
    while len(avaiableItems) < 2:
        chosenItem = random.choices(
            itemChoices,
            weights=[item.rarity for item in itemChoices],
            k=1
        )[0]  # random.choices returns a list, take the first element
        avaiableItems.append(chosenItem)
        print(chosenItem.name, chosenItem.price)
        
    while True:
        print("\n Store Menu:")
        print("1. Purchase")
        print("2. Sell")
        print("3. Leave")
        while True:
            try:
                choice = int(input("Choose an action (1-3): ").strip())
            except ValueError:
                print("YOU GONNA BREAK IT")
        
            if choice == 1:
                pickedItem = int(input("item 1 or 2? ").strip())
                if pickedItem in [1, 2]:
                    chosen = avaiableItems[pickedItem - 1]  # grab the StoreItems object
                    if mainCharacter.wallet >= chosen.price:
                        mainCharacter.wallet -= chosen.price
                        print(f"You bought {chosen.name} for {chosen.price} coins!")
                        # optionally add to inventory
                        if chosen.specials == False:
                            mainCharacter.items.append(StoreItems(chosen.name, chosen.price, False, True, chosen.damage, chosen.heal,chosen.armor, chosen.amount, chosen.rarity, chosen.manaCost))
                        else:
                            mainCharacter.attacks.append(Special(chosen.name, 0, chosen.damage, chosen.heal, chosen.amount, chosen.manaCost))
                    else:
                        print("Not enough coins!")
                else:
                    print("Invalid choice")
            if choice == 2:
                print("sorry we can't buy your trash right now")
            if choice == 3:
                print("Thanks for stopping by!!!")
                avaiableItems = []
                break
        break
            
                    
            
        
        
    
    
#storeOpen()
         

while mainCharacter.health > 0:
    
    enemy_name = random.choice(enemy_types)
    enemy = Enemy(enemy_name)

    print("\nEnemy #" + str(fight_num+1) + ": " + enemy_name)

    turn = 1

    while enemy.health > 0 and mainCharacter.health > 0:

        if turn % 2 == 0:
            # Enemy attacks
            success = random.randint(0, 100)
            dmg = enemy.attack(success)

            reduce = mainCharacter.defend(success, dmg)
            mainCharacter.health -= reduce

            print(f"Enemy hits you for {reduce}! Your HP = {mainCharacter.health}")

        else:
            # Player attacks
            success = random.randint(0, 10)
            print("\n Battle Menu:")
            print("1. Base Attack")
            print("2. Special Attack")
            print("3. Use Item")
            print("4. Defend")

            choice = int(input("Choose an action (1-4): ").strip())


            
            dmg = mainCharacter.attack(success, choice)

            reduce = enemy.defend(success, dmg)
            enemy.health -= reduce

            print(f"You hit {enemy_name} for {reduce}! Enemy HP = {enemy.health}")

        turn += 1

        if mainCharacter.health <= 0:
            print("GAME OVER!")
            exit()
    print("Congrats!!! You defeated the", enemy_name)
    
    
    if badBoy == False:
        mainCharacter.wallet += random.randint(0, 15)
        itemDropped = enemy.getDrop()
        
        if itemDropped == "gold":
            mainCharacter.wallet += random.randint(5, 30)
            
        else:
            print("YAYYYYYYY, they dropped " + itemDropped.name)
        
            addStorage = input("would you like to put this in your inventory: ")
            
            if addStorage.lower() == "yes":
                mainCharacter.quickStorage(itemDropped)
                
            elif addStorage.lower() == "no":
                print("okayyyyyy")
                
            else:
                print("retarded ass bitch can't say yes or no...")
                print("You can't get a item drop, gold, or baddies next fight")
                badBoy = True
    else:
        print("WOMP WOMP!\nShouldn't have been a bad boy" + name)
    
    mainCharacter.health += 10
    fight_num += 1
    
    print("You currently have", mainCharacter.wallet, "monkey money")
    storeStop = input("do you wanna stop at Big Top? ")
    
    if badBoy == False:
        if storeStop == "yes":
            storeOpen()
        elif storeStop == "no":
            print("what you a poor clanker")
        else:
            print("retarded ass bitch can't say yes or no...")
            print("You can't get a item drop, gold, or baddies next fight")
            badBoy = True
    else:
        print("hope you learned your lesson silly goose")
        badBoy = False
        

    
        
        
        
        


print("\nYOU WIN THE GAME!")

