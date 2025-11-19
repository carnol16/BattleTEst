from classes.items import StoreItems, CraftItems
from classes.player.createPlayer import Player


craftableItems = [
    CraftItems("Reptillian Origami Sweater", 100, False, True, False, False, True, 25, 10, 0, {"scales": 3}),
    CraftItems("Wooden Gun", 40, False, False, True, False, False, 9, 70, 0, {"logs": 4 })
    
    
]


def build(player, chosenItem):
    needed = chosenItem.required_items

    # Count materials in player's inventory
    inv_count = {}
    for item in player.items:
        inv_count[item.name] = inv_count.get(item.name, 0) + 1

    # Check if player has required materials
    for material, amt in needed.items():
        if inv_count.get(material, 0) < amt:
            print(f"Missing {material}: need {amt}, have {inv_count.get(material, 0)}")
            return None

    # Remove required materials
    for material, amt in needed.items():
        removed = 0
        for item in list(player.items):
            if item.name == material and removed < amt:
                player.items.remove(item)
                removed += 1

    # Add crafted item
    player.quickStorage(chosenItem)
    print(f"✅ Successfully crafted {chosenItem.name}!")
    return chosenItem

