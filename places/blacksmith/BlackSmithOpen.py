from classes.items import StoreItems
from .Build import craftableItems, build

def openBlacksmith(mainCharacter):

    while True:
        print(f"\nYou have {mainCharacter.wallet} monkey money.")
        print("\n--- BLACKSMITH MENU ---")
        print("1. BUILD")
        print("2. REPAIR")
        print("3. SCAVENGE")
        print("4. Leave")

        blacksmithChoice = input("What would you like to do? >>> ").strip()
        # BUILD OPTION

        if blacksmithChoice == "1":
            
            print("\n--- CRAFTABLE ITEMS ---")
            for i, item in enumerate(craftableItems):
                mats = ", ".join([f"{k}: {v}" for k, v in item.required_items.items()])
                print(f"{i}. {item.name}  |  requires: {mats}")

            choice = input("\nWhich item would you like to craft? >>> ").strip()

            if not choice.isdigit() or int(choice) not in range(len(craftableItems)):
                print("Invalid choice!")
                continue

            chosen = craftableItems[int(choice)]
            build(mainCharacter, chosen)
            continue

        # REPAIR
        elif blacksmithChoice == "2":
            print("Repair system coming soon...")
            continue


        # SCAVENGE 

        elif blacksmithChoice == "3":
            print("You scavenge for scraps...")
            continue


        # EXIT
        elif blacksmithChoice == "4":
            print("You leave the blacksmith.")
            break

        else:
            print("Invalid option, try again!")
