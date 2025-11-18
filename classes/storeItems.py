from classes.player.armor import Armor

class StoreItems:
    
    def __init__(self, name, price, specials, items, damage, heal, armor, amount, rarity, manaCost, weapon = False, cosmetic = False):
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
        self.weapon = weapon
        self.cosmetic = cosmetic

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
            
    def toArmor(self):
        return Armor(self.name, self.amount)