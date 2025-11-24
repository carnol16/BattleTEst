from classes.items import StoreItems
from .Build import craftableItems, build
from PIL import Image
import time
import vlc



image_path = r"images\blacksmith.jpg" 

img = Image.open(image_path)

music = r"audio\blacksmith.mp3"

musicPlayer = vlc.MediaPlayer(music)

# Enable looping
musicPlayer.set_media(vlc.Media(music))
musicPlayer.get_media().add_option("input-repeat=-1")  # -1 = infinite loop

def openBlacksmith(mainCharacter):
    musicPlayer.play()
    
    try:
        img.show()
    except FileNotFoundError:
        print("Error: Image file not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")
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
            if not mainCharacter.armor:
                print("You have no armor equipped.")
                continue

            arm = mainCharacter.armor
            print(f"\nArmor: {arm.name}")
            print(f"Durability: {arm.durability}")

            if arm.durability == 100:
                print("Your armor does not need repairs.")
                continue

            cost = arm.repairCost()
            print(f"Repair cost: {cost} coins")

            confirm = input("Repair armor? (yes/no): ").lower()
            if confirm != "yes":
                continue

            if mainCharacter.wallet < cost:
                print("Not enough coins!")
                continue

            mainCharacter.wallet -= cost
            arm.repair()

            print(f"{arm.name} has been fully repaired!")
            continue


        # SCAVENGE 

        elif blacksmithChoice == "3":
            print("You scavenge for scraps...")
            continue


        # EXIT
        elif blacksmithChoice == "4":
            print("You leave the blacksmith.")
            musicPlayer.stop()
            break

        else:
            print("Invalid option, try again!")
