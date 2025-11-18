import random

from classes.storeItems import StoreItems
from classes.player.createPlayer import Player
from classes.player.armor import Armor
from classes.player.specials import Special

def storeOpen(mainCharacter):
    
    itemChoices = [
        StoreItems("Daddy's Belt", 100, True, False, True, False, False, 100, 10, 60),
        StoreItems("Cased Hardened AK-47", 423, True, False, True, False, False, 35, 15, 15),
        StoreItems("Gamer Girl Bath Water", 30, False, True, False, True, False, 45, 75, 0),
        StoreItems("Sam Keh's Secret Love For Brian", 1, True, False, False, True, False, 1000, 5, 1),
        StoreItems("Top Ramen", 1, False, True, False, True, False, 5, 100, 0),
        StoreItems("Pink Suit", 70, False, False, False, False, True, 5, 45, 0),
        StoreItems("CS Crate", )
        
    ]

    availableItems = []

    while len(availableItems) < 2:
        chosenItem = random.choices(
            itemChoices,
            weights=[item.rarity for item in itemChoices],
            k=1
        )[0]
        availableItems.append(chosenItem)
        print(chosenItem.name, chosenItem.price)

    # --- STORE MENU LOOP ---
    while True:
        print("\nStore Menu:")
        print("1. Purchase")
        print("2. Sell")
        print("3. Leave")

        try:
            choice = int(input("Choose an action (1-3): ").strip())
        except ValueError:
            print("YOU GONNA BREAK IT")
            continue

        if choice == 1:
            freeSpace = mainCharacter.space - len(mainCharacter.items)
            if freeSpace > 0:
                pickedItem = int(input("item 1 or 2? ").strip())
                if pickedItem in [1, 2]:
                    chosen = availableItems[pickedItem - 1]

                    if mainCharacter.wallet >= chosen.price:
                        mainCharacter.wallet -= chosen.price
                        print(f"You bought {chosen.name} for {chosen.price} coins!")
                        
                        if chosen.armor:
                            print(f"{chosen.name} is armor!")

                            equip = input("Equip it now? (yes/no): ").lower()

                            if equip == "yes":
                                from classes.player.armor import Armor
                                newArmor = Armor(chosen.name, chosen.amount)

                                # Remove old armor if exists
                                if mainCharacter.armor:
                                    try:
                                        mainCharacter.armor.detach(mainCharacter)
                                    except:
                                        pass

                                newArmor.attach(mainCharacter)
                                continue  # Skip storing the item


                        if chosen.specials == False:
                            mainCharacter.items.append(StoreItems(
                                chosen.name, chosen.price, False, True,
                                chosen.damage, chosen.heal, chosen.armor,
                                chosen.amount, chosen.rarity, chosen.manaCost
                            ))
                        else:
                            mainCharacter.attacks.append(Special(
                                chosen.name,
                                0,
                                chosen.damage,
                                chosen.heal,
                                chosen.amount,
                                chosen.manaCost
                            ))

                    else:
                        print("Not enough coins!")
                else:
                    print("Invalid choice")

            else:
                print("sorry baddie, no space")
                dropItem = input("would you like to dispose of something??? ")
                if dropItem == "yes":
                    print("Here are the items you have currently:")
                    counter = 0
                    for i in mainCharacter.items:
                        print(counter, i.name)
                        counter += 1

                    removeIndex = int(input("Which number to remove? "))
                    if 0 <= removeIndex < len(mainCharacter.items):
                        removed = mainCharacter.items.pop(removeIndex)
                        print(f"Removed {removed.name}.")
                    else:
                        print("Invalid index.")

        elif choice == 2:
            print("sorry we can't buy your trash right now")

        elif choice == 3:
            print("Thanks for stopping by!!!")
            return  # <-- THIS FIXES EVERYTHING

        else:
            print("Invalid choice")                    
            