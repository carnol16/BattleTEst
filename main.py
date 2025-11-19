import random
from places.casino import BlackJack
from classes.items import StoreItems
from classes.enemy import Enemy
from classes.player.createPlayer import Player
from classes.player.specials import Special
from classes.player.armor import Armor
from classes.player.weapon import Weapon
from places.store.StoreOpen import storeOpen
from places.casino.CasinoOpen import openCasino
from places.blacksmith.BlackSmithOpen import openBlacksmith


name = "george"
playerType = "boat man"
color = "red"

print(
    r"""
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
"""
)
"""
# Hey my fellow baddie. I'm Stacy. The big titty goth girl at your service
"""

"""
print("Hey my fellow baddie. I'm Stacy.")
name = input("Welcome to the silly land of Lollipop Circle!!! What is your name: ")

if len(name) <= 5:
    print("thats a good name, great choice\n")
elif len(name) <= 10:
    print("Not a great choice but it will do\n")
else:
    print("ew... you are going by Jerry now.\n")
    name = "jerry"

print()
playerType = input(
    "Alright "
    + name
    + ". Now what kind of character would you like to be?\nYou can be a warrior, basement dweller, boat man, or ninja... or something else i guess: "
)

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
"""


mainCharacter = Player(playerType, color, name)

enemy_types = ("goblin", "snake", "turtle", "log")

badBoy = False

enemy_types = ("goblin", "snake", "turtle", "log", "Razer DAWG")
# num_enemies = random.randint(1, 5)

# print("You will fight", num_enemies, "enemies.")

fight_num = 0

# GAMEPLAY LOOP
while mainCharacter.health > 0:
    
    enemy_name = random.choice(enemy_types)
    enemy = Enemy(enemy_name)

    print("\nEnemy #" + str(fight_num + 1) + ": " + enemy_name)

    turn = 1
    print("Current Health: ", mainCharacter.health)
    print("Current Mana: ", mainCharacter.mana)

    # Battle LOOP
    while enemy.health > 0 and mainCharacter.health > 0:

        if turn % 2 == 0:
            # Enemy attacks
            success = random.randint(0, 100)
            dmg = enemy.attack(success)

            reduce = mainCharacter.defend(success, dmg)
            mainCharacter.health -= reduce
            # mainCharacter.armor.durablity -= 1

            print(f"Enemy hits you for {reduce}! Your HP = {mainCharacter.health}")

        else:
            # Player attacks
            success = random.randint(0, 10)
            print("\nBattle Menu:")
            print("1. Base Attack")
            print("2. Special Attack")
            print("3. Use Item")
            print("4. Defend")
            
            choice = input("Choose an action (1-4): ").strip()

            if choice not in ("1", "2", "3", "4"):
                print("\nwasted a turn because you can't read smh")

                
            else:
                dmg = mainCharacter.attack(success, choice, enemy)

                reduce = enemy.defend(success, dmg)
                enemy.health -= reduce

                print(f"\nYou hit {enemy_name} for {reduce}! Enemy HP = {enemy.health}")

        turn += 1

        if mainCharacter.health <= 0:
            print("GAME OVER!")
            exit()
    print("Congrats!!! You defeated the", enemy_name)

    # GET THE DROP
    if badBoy == False:
        mainCharacter.wallet += random.randint(0, 15)
        itemDropped = enemy.getDrop()

        if itemDropped == "gold":
            mainCharacter.wallet += random.randint(5, 30)

        else:
            print("YAYYYYYYY, they dropped " + itemDropped.name)

            # If item is armor, convert it
            if itemDropped.armor:
                print(f"{itemDropped.name} is armor!")

                equip = input("Do you want to equip it now? (yes/no): ").lower()

                if equip == "yes":
                    newArmor = Armor(itemDropped.name, itemDropped.amount)

                    # remove old armor bonus if exists

                    if mainCharacter.armor:
                        mainCharacter.armor.detach(mainCharacter)

                    newArmor.attach(mainCharacter)
                    # skip storage
            elif itemDropped.weapon:
                print(f"{itemDropped.name} is weapon!")

                equip = input("Do you want to equip it now? (yes/no): ").lower()

                if equip == "yes":
                    newWeapon = Weapon(itemDropped.name, itemDropped.amount)

                    # remove old armor bonus if exists

                    if mainCharacter.weapon:
                        mainCharacter.weapon.detach(mainCharacter)

                    newWeapon.attach(mainCharacter)
                    # skip storage
            else:

                addStorage = input("would you like to put this in your inventory: ")

                if addStorage.lower() == "yes":
                    mainCharacter.quickStorage(itemDropped)

                elif addStorage.lower() == "no":
                    print("okayyyyyy")

                else:
                    print("dumb ass bitch can't say yes or no...")
                    print(
                        "You can't get a item drop, monkey money, or baddies next fight"
                    )
                    badBoy = True
    else:
        print("WOMP WOMP!\nShouldn't have been a bad boy" + name)

    mainCharacter.health += 10
    mainCharacter.mana += 15
    fight_num += 1

    # STORE TIME
    print("You currently have", mainCharacter.wallet, "monkey money")

    stop = input(
        "Do you want to stop at Big Top, Casino, Blacksmith, Storage, or nothing? (store / casino / blacksmith / storage /  none) "
    ).lower()

    if badBoy == False:
        while True:

            if stop.lower() == "store":
                storeOpen(mainCharacter)
                stop = input(
                    "Do you want to stop at Big Top, Casino, Blacksmith, Storage, or nothing? (store / casino / blacksmith / storage /  none) "
                ).lower()
                continue

            elif stop.lower() == "casino":
                openCasino(mainCharacter)
                stop = input(
                    "Do you want to stop at Big Top, Casino, Blacksmith, Storage, or nothing? (store / casino / blacksmith / storage /  none) "
                ).lower()
                continue
            
            elif stop.lower() == "blacksmith":
                openBlacksmith(mainCharacter)
                stop = input(
                    "Do you want to stop at Big Top, Casino, Blacksmith, Storage, or nothing? (store / casino / blacksmith / storage /  none) "
                ).lower()
                continue
            
            elif stop.lower() == "storage":
                mainCharacter.storage()
                stop = input(
                   "Do you want to stop at Big Top, Casino, Blacksmith, Storage, or nothing? (store / casino / blacksmith / storage /  none) "
                ).lower()
                continue

            elif stop.lower() == "none":
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


print("\nYOU WIN THE GAME!")
