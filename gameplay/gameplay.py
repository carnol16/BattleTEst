import random
from classes.enemy import Enemy, Boss
from classes.player.armor import Armor
from classes.player.weapon import Weapon
from places.store.StoreOpen import openStore
from places.casino.CasinoOpen import openCasino
from places.blacksmith.BlackSmithOpen import openBlacksmith
from classes.player.createPlayer import Player



def characterBuildIntro():
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
    print("Hey my fellow baddie. I'm Stacy. The big titty goth girl at your service I'm Stacy.")
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

    return Player(playerType, color, name)

def enemyBattle(mainCharacter, fightNum):


    enemy_types = ("goblin", "snake", "turtle", "log", "Razer DAWG")
    enemy_name = random.choice(enemy_types)
    enemy = Enemy(enemy_name)

    print("\nEnemy #" + str(fightNum + 1) + ": " + enemy_name)

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
            print("\n===== Battle Menu =====")
            print("1. Base Attack")
            print("2. Special Attack")
            print("3. Use Item")
            print("4. Defend")
            
            choice = input("> ").strip()
            print("")

            if choice not in ("1", "2", "3", "4"):
                print("\nwasted a turn because you can't read smh")

                
            else:
                dmg = mainCharacter.attack(success, choice, enemy)

                reduce = enemy.defend(success, dmg)
                enemy.health -= reduce
                
                if enemy.health <= 0:
                    print(f"\nYou hit {enemy_name} for {reduce}! Enemy HP = 0")
                else:
                    print(f"\nYou hit {enemy_name} for {reduce}! Enemy HP = {enemy.health}")

        turn += 1

        if mainCharacter.health <= 0:
            print("\n\n\nGAME OVER!")
            exit()
    print("\nCongrats!!! You defeated the", enemy_name)

    # GET THE DROP
    if mainCharacter.badBoy == False:
        mainCharacter.wallet += random.randint(0, 15)
        itemDropped = enemy.getDrop()

        if itemDropped == "gold":
            mainCharacter.wallet += random.randint(5, 30)

        else:
            print(f"{enemy.kind} dropped {itemDropped.name}\n")

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

                addStorage = input("would you like to put this in your inventory (yes/no): ")

                if addStorage.lower() == "yes":
                    mainCharacter.quickStorage(itemDropped)

                elif addStorage.lower() == "no":
                    print("okayyyyyy")

                else:
                    print("dumb ass bitch can't say yes or no...")
                    print(
                        "You can't get a item drop, monkey money, or baddies next fight"
                    )
                    mainCharacter.badBoy = True
    else:
        print("WOMP WOMP!\nShouldn't have been a bad boy" + mainCharacter.name)

    mainCharacter.health += 10
    mainCharacter.mana += 15
    fightNum += 1
    return fightNum

def bossBattle(mainCharacter, fightNum):

    mult = fightNum / 5
    enemy_types = ("Carl", "BENJAMIN")
    enemy_name = random.choice(enemy_types)
    enemy = Boss(enemy_name, fightNum)

    print("\nBoss #" + str(fightNum / 5) + ": " + enemy_name)

    turn = 1
    print("Current Health: ", mainCharacter.health)
    print("Current Mana: ", mainCharacter.mana)

    # Battle LOOP
    while enemy.health > 0 and mainCharacter.health > 0:

        if turn % 2 == 0:
            # Enemy attacks
            success = random.randint(0, 100)
            if success % 4 == 0:
                dmg = Boss.attackBoss(enemy)
            else:
                dmg = Boss.attack(enemy, success)
            
            dmg  *= mult
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
                
                dmg *= mult
                reduce = enemy.defend(success, dmg)
                enemy.health -= reduce

                print(f"\nYou hit {enemy_name} for {reduce}! Enemy HP = {enemy.health}")

        turn += 1

        if mainCharacter.health <= 0:
            print("GAME OVER!")
            exit()
    print("Congrats!!! You defeated the", enemy_name)

    # GET THE DROP
    if mainCharacter.badBoy == False:
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
                    mainCharacter.badBoy = True
    else:
        print("WOMP WOMP!\nShouldn't have been a bad boy" + mainCharacter.name)

    mainCharacter.health += 10
    mainCharacter.mana += 15
    fightNum += 1
    return fightNum

def postCombat(mainCharacter):
    # STOP TIME
    print("\n\nYou currently have", mainCharacter.wallet, "monkey money")

    if mainCharacter.badBoy == False:
        while True:
            print("\n===== POST FIGHT MENU =====")
            print("1. BIG TOP")
            print("2. Casino")
            print("3. Blacksmith")
            print("4. Storage")
            print("5. Next Fight")

            stop = input("> ").strip()

            if stop.lower() == "1":
                openStore(mainCharacter)

                continue

            elif stop.lower() == "2":
                openCasino(mainCharacter)

                continue
            
            elif stop.lower() == "3":
                openBlacksmith(mainCharacter)

                continue
            
            elif stop.lower() == "4":
                mainCharacter.storage()

                continue

            elif stop.lower() == "5":
                print("\nYou continue your journey...\n\n")
                break

            else:
                print("\nDumb ass bitch can't say a real option...")
                print("You can't get an item drop, gold, or baddies next fight.\n\n")
                mainCharacter.badBoy = True
                break

    else:
        print("\nYOU THOUGHT! Hope you learned your lesson silly goose.\n\n")
        mainCharacter.badBoy = False