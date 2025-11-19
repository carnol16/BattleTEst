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
            return 0
        
    
    