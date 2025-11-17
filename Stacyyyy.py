import random
from casino import BlackJack 
from classes.storeItems import StoreItems
from classes.enemy import Enemy
from classes.player.createPlayer import Player
from classes.player.specials import Special 
        

def storeOpen():
    itemChoices = [
        StoreItems("Daddy's Belt", 100, True, False, True, False, False, 100, 10, 60),
        StoreItems("Cased Hardened AK-47", 423, True, False, True, False, False, 35, 15, 15),
        StoreItems("Gamer Girl Bath Water", 30, False, True, False, True, False, 45, 75, 0),
        StoreItems("Sam Keh's Secret Love For Brian", 1, True, False, False, True, False, 1000, 100, 1),
        StoreItems("Top Ramen", 1, False, True, False, True, False, 5, 100, 0),
        StoreItems("Pink Suit", 70, False, False, False, False, True, 5, 45, 0)
        
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
            
print(r"""
:%    @*++++++++@  .@                                                                
                                      @: @        @   @=:-*%*:         :*#=* %                                                              
                                    @ %=+% =   @ @==#+:                    .=  @                                                            
                                 @  %-:  -@  @ +-:                           -% @   @    #                                                  
                               @ +-:.    : @ @@*:                   ..--:.    - :%  %::-::#  %                                              
                             *  -       .*      :          .-++-.  .+ *  +.    =  : +     .=+# @                                            
                           =  +:        : # + #-:   -=: -*##    -  : #  @ +    .  # =         +                                             
                          @ +.         :# % #:..=+-+  .=+   =@ :*..:@    @ -    # % :         ::                                            
                        * :.          :* * #=--*  #@     @+ :  @ **        @ -. %  =           + #                                          
                       *.=.          .* @  *.  =      = @   @   @  :        @ +.@  =           :-@ *                                        
                      @ =           .+ #   ..*@@     @@    @     +            @ @  =             :                                          
                     * *:          :+ -  @=-+     @@@           @@@@@@#         %  *              .=                                        
                    + *:           + %=   -#    @  @          @ @     .+-@@@ @ # * =                + @                                     
                     *.            +   %@ *    @   +          @   #    @   = @ # =-:                 - @                                    
                   @ :             .=+-+ =@    @@  @          @  @@ =. *   * + @: :                   : :                                   
                    -                 - . *    @  @@          @   @    +   @%@ @ @=                    .-                                   
                  @*. ..-..           * @ %    @  @           @#  @ =@ @       @  -                      * @                                
                 @ +-=  :             @ %  @    #     :         @@    %    @      ..                     .=                                 
                @ @=  .= =.           @ @    @%       @                  @       %- =.                     = @                              
              @@@*-  #  :.            + =  @@  @ %@   @        @@   @  @@        @ + *:                     = @                             
                   +  =:              --@ %  @@  *   @         #  @@  @@        @   % +.                    :+ @                            
                ++  +:                  +                                      @     @ =                      = %                           
             :# #==-                 :=@ %        @@@@@@@@@@@-                @       @ +.                .:+:=:+                           
          +#  #-:                  ::@ =-+*       @          +=             @          @ -                . - .:-* @                        
       @@ @=+=                   .:@ @     @         @@@@@@@#            #@             %=.               .+ -- =*@ #                       
    @# #=-:                     .: @        @+                         @@                 *.               .:   =+ @* @                     
  @ *=-:                       - @            @:                   @@-                   +  .                 = -                           
 - +.                        :+ @               %@             .@@.   @                   - +                 .-  @                         
 %-.                        .* #                @  @@#      @@*      @                        .                 :-# @                       
 .                         .+ ..                @      @@@-          @                      @ =                   .:# +                     
                          .+ @             @@  @:                    @                       @ :                    .-  @-                  
                       :-=# @          @@.       @                    @                        #.                      .*  @                
                  -*#=-% %*          @            @                 @= #@=                    @ *:                      :==%  @@            
         .=##+--  #  :%         -@@*  @            @            =@#        @@                  @ =                         :=+:+    ---=%.  
       -=#    ::-            @@        @@           @       @@#            @  @@                @ -.                           :+#+-:...:-  
     :*  +                 @%            @          @    @@             @@       @=              # =                                     :- 
   :- -:                 -@                @         -%@             -@:            @             % +:                                      
 -% =                   @                  *-         :            @@                 @*           @  -.                                    
  @                   @                      @       #           @                      @@           @ +.                                   
 =                  @                         @      @        #@                            @         -* *=-                                
                  @                            @     @      @@                                @         #@  +:=#@*-                        
               @@                              @     @   .@                                     *@          =*    @+:. =---:::=*%+- ..      
         .==@@                                  @    @ +@                                          @@-                      *     @#- +::   
   @+*@ +   @                  @*                @   @=                                                @@                             @  *- 
  @     :    @               -@                  @-@@                            :                        @@=                           +   
  @     @    -+           #@@.                                                   @ @@@*                    @  @#                            
 @*     @     @       :@@   @                                                   #       @*               @     @@@@@@@.                     
        @     @  @@@       *                                                   @          @@           @      @       @                     
  +@@  @%@@@@@@            #                                                   %             @%       =:      #      @                      
  %     =%                  @                                                 +                 @%    @      @          @                   
       @   @                 %                    @                           @                    @@@      @             @                 
  @   %@@  @                  @                   :                           @                      @ *###.=%      @* =@@                  
                                @                                             @                             @                               
                                  @@.            %@                           @                             @    @%*@@                      
                                                  =@                          *                             =   @                           
                                       @            @@                     @  -                              @@                             
                                        @              @@@             *@@  .:                                                              
                                          @                 *@@@@@@@@#      *                                                               
                                           %                               @                                                                
                                           @                              @                                                                 
                                           @                             @                                                                  
                                           @                             @                                                                  
                                          @                              @                                                                  
                                         @                                @                                                                 
                                        @                                  @                                                                
                                      #-                                    @+                                                              
                                    @@  *@@@@@@@@#                            @  -                                                          
                               @@@                 @@@@               #@@@@@@@+@                                                            
                           +@@                                      .           @                                                           
                        @@                                                       @                                                          
                       @                                                         +-                                                         
                     @.                                                           @                                                         
                    @                                                              +                                                        
                   @                                                               @                                                        
                  @                                                                 @                                                       
                 @                                                                  @                                                       
                 @                                                                  =.                                                      
                @                                                                    @                                                      
               @                                                            =@       @                                                      
               @                  .                       =                  @       +                                                      
              -                  @                        +#                 #        @                                                     
              @                @.                          :@                         @                                                     
             @                @                              @                @       @                                                     
             .               @                                #               @       @                                                     
            @       @                 @@@#@                    @              :       @                                                     
            @       @                @    @                     @             %       @                                                     
           .       +@                @    @                                   #       @                                                     
           @      #@                 @    @      :@@%@                         @      @                                                     
           :    @= @                 .*   @    @                               @      @                                                     
          @@ .@.   @-#%=              @   @  @        @         #@*                   @                                                     
             @            +@@@@@     - *@#@@           @     -@=  =                   @                                                     
           =:                    @ @@%-    @            @: =@      @                  @                                                     
          ==                               @             .          @.                +                                                     
         =:                                *                             :@@@*#####**-@@                                                    
         @                                 +             @                           -                                                      
        @                                   -            @                           @                                                      
        @                                   +             %                           @                                                     
        +                                   +             @                            :                                                     
       @                                    +              *                           -                                                     
       @                                    +              -+                          :   
""")

'''
print("Hey my fellow baddie. I'm Stacy. The big titty goth girl at your service")
name = input("Welcome to the silly land of Lollipop Circle!!! What is your name: ")

if len(name) <= 5:
    print("thats a good name, great choice\n")
elif len(name) <= 10:
    print("Not a great choice but it will do\n")
else:
    print("ew... you are going by Jerry now.\n")
    name = "jerry"

print()
playerType = input("Alright " + name + ". Now what kind of character would you like to be?\nYou can be a warrior, basement dweller, boat man, or ninja... or something else i guess: ")

playerType = playerType.lower()

if playerType in ("warrior", "basement dweller", "boat man", "ninja"):
    print("Niceeeeee. You really know your stuff", name)
    print("You will make a great", playerType)
else:
    print("damn you really gotta be like this huh, couldn't be normal...")
    print("enjoy being a", playerType, "i guess...\n")

print()

color = input("We are almost ready now!!! I now just need your favorite color: ")
color = color.lower()

print("Perfect, this is just something a little silly!! No worries")
print(color + " is amazing\n")

print("Now we are ready for our little journey!")


mainCharacter = Player(playerType, color)

enemy_types = ("goblin", "snake", "turtle", "log")
num_enemies = random.randint(1, 5)

print("You will fight", num_enemies, "enemies.\n")
'''
    
#storeOpen()

name = "george"
playerType = "boat man"
color = "red"

         
badBoy = False

mainCharacter = Player(playerType, color)

enemy_types = ("goblin", "snake", "turtle", "log")
num_enemies = random.randint(1, 5)

print("You will fight", num_enemies, "enemies.")

fight_num = 0

#GAMEPLAY LOOP
while mainCharacter.health > 0:
    
    enemy_name = random.choice(enemy_types)
    enemy = Enemy(enemy_name)

    print("\nEnemy #" + str(fight_num+1) + ": " + enemy_name)

    turn = 1
    print("Current Health: ", mainCharacter.health)
    print("Current Mana: ", mainCharacter.mana)

    #Battle LOOP
    while enemy.health > 0 and mainCharacter.health > 0:

        if turn % 2 == 0:
            # Enemy attacks
            success = random.randint(0, 100)
            dmg = enemy.attack(success)

            reduce = mainCharacter.defend(success, dmg)
            mainCharacter.health -= reduce
            #mainCharacter.armor.durablity -= 1

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
            
            dmg = mainCharacter.attack(success, choice, enemy)

            reduce = enemy.defend(success, dmg)
            enemy.health -= reduce

            print(f"You hit {enemy_name} for {reduce}! Enemy HP = {enemy.health}")

        turn += 1

        if mainCharacter.health <= 0:
            print("GAME OVER!")
            exit()
    print("Congrats!!! You defeated the", enemy_name)
    
    #GET THE DROP
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
                print("dumb ass bitch can't say yes or no...")
                print("You can't get a item drop, monkey money, or baddies next fight")
                badBoy = True
    else:
        print("WOMP WOMP!\nShouldn't have been a bad boy" + name)
    
    mainCharacter.health += 10
    mainCharacter.mana += 15
    fight_num += 1
    
    #STORE TIME
    print("You currently have", mainCharacter.wallet, "monkey money")
    
    storeStop = input("Do you want to stop at Big Top or go to the casino? (store / casino / none) ")

    if badBoy == False:
        while True:

            if storeStop.lower() == "store":
                storeOpen()
                storeStop = input("Do you want to stop at Big Top or go to the casino? (store / casino / none) ")
                continue


            elif storeStop.lower() == "casino":

                # --- CASINO LOOP ---
                while True:

                    # If the player is broke, they must leave
                    if mainCharacter.wallet <= 0:
                        print("You're broke! Get out of my casino!")
                        break

                    print(f"\nYou have {mainCharacter.wallet} monkey money.")

                    # WAGER INPUT
                    try:
                        wager = int(input("How much do you want to bet? "))
                    except ValueError:
                        print("That ain't a number, bucko.")
                        continue

                    if wager > mainCharacter.wallet:
                        print("You don't have that kind of money, silly goose.")
                        continue

                    if wager <= 0:
                        print("Bet must be more than zero.")
                        continue

                    # PLAY BLACKJACK
                    mainCharacter.wallet, game_shoe = BlackJack.blackjack(
                        mainCharacter.wallet,
                        wager,
                        shoe=None
                    )

                    print("Your wallet is now:", mainCharacter.wallet)

                    # If broke after the hand, kick out
                    if mainCharacter.wallet <= 0:
                        print("You're out of moneky money! Skedaddle!")
                        break

                    # ASK TO PLAY AGAIN
                    repeat = input("Would you like to play again? (yes/no) ").lower()

                    if repeat == "no":
                        print("Leaving the casino...")
                        break

                # --- AFTER CASINO: ASK WHERE TO GO NEXT ---
                storeStop = input("\nDo you want to stop at Big Top, the casino, or none? ").lower()
                continue

                

                            

            elif storeStop.lower() == "none":
                print("You continue your journey...")
                break

            else:
                print("Dumb ass bitch can't say a real option...")
                print("You can't get an item drop, gold, or baddies next fight.")
                badBoy = True
                break

    else:
        print("YOU THOUGHT! Hope you learned your lesson silly goose.")
        badBoy = False

"""
    openStorage = input("Would you like to go into storage? ")
    
    if openStorage == "yes":
        mainCharacter.storage()
"""
        

    
        
        
        
        


print("\nYOU WIN THE GAME!")

