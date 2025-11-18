class Armor:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount   # amount = defense bonus
        self.durability = 100

    def attach(self, user):
        """
        Equip this armor onto the player.
        Replaces current armor if one is already equipped.
        """
        if user.armor:
            print(f"Removing old armor: {user.armor.name}")

        user.armor = self
        user.defense += self.amount
        print(f"{self.name} equipped! Defense increased by {self.amount}.")

    def detach(self, user):
        """
        Remove this armor and drop its defense bonus.
        """
        print(f"{self.name} removed.")
        user.defense -= self.amount
        user.armor = None

    
        