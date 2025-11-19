
import random

class Enemy:
    def __init__(self, kind):
        self.kind = kind

        if kind == "goblin":
            self.health = 80
            self.damage = 10
            self.defense = 6
        elif kind == "snake":
            self.health = 15
            self.damage = 20
            self.defense = 1
        elif kind == "turtle":
            self.health = 100
            self.damage = 30
            self.defense = 10
        else:
            self.health = 50
            self.damage = 5
            self.defense = 3

    def attack(self, success):
        if success % 2 == 0:
            base = self.damage
            if random.random() < 0.2:
                print("AWESOME CRIT")
                return int(base * 1.5)
            return base
        return 0

    def defend(self, success, incoming_damage):
        if success % 8 == 0:
            if random.random() < 0.1:
                print("nice dodge")
                return 0
            reduced = incoming_damage - self.defense
            return max(reduced, 1)
        return incoming_damage


class Player:
    def __init__(self, type, color):
        self.type = type
        self.color = color

        if type == "warrior":
            self.health = 200
            self.damage = 10
            self.defense = 4
        elif type == "basement dweller":
            self.health = 150
            self.damage = 8
            self.defense = 10
        elif type == "boat man":
            self.health = 180
            self.damage = 10
            self.defense = 10
        elif type == "ninja":
            self.health = 80
            self.damage = 7
            self.defense = 15
        else:
            self.health = 10
            self.damage = 1
            self.defense = 0

        if color == "blue":
            self.health += 10
        elif color == "red":
            self.health -= 8
            self.damage += 2

    def attack(self, success):
        if success % 2 == 0:
            base = self.damage
            if random.random() < 0.2:
                print("YOU HIT A CRIT")
                return int(base * 1.5)
            return base
        return 0

    def defend(self, success, incoming_damage):
        if success % 2 == 0:
            if random.random() < 0.1:
                print("GOOD DODGE")
                return 0
            reduced = incoming_damage - self.defense
            return max(reduced, 1)
        return incoming_damage

num_enemies = random.randint(1, 10)

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
print(f"There are {num_enemies} enemies that we are going to encounter!\nSo get ready to rumble\n")

mainCharacter = Player(playerType, color)

enemy_types = ("goblin", "snake", "turtle", "log")
num_enemies = random.randint(1, 5)

print("You will fight", num_enemies, "enemies.\n")

for fight_num in range(num_enemies):

    enemy_name = random.choice(enemy_types)
    enemy = Enemy(enemy_name)

    print("Enemy #" + str(fight_num + 1) + ": " + enemy_name)

    turn = 1

    while enemy.health > 0 and mainCharacter.health > 0:

        if turn % 2 == 0:
            success = random.randint(0, 100)
            dmg = enemy.attack(success)
            reduce = mainCharacter.defend(success, dmg)
            mainCharacter.health -= reduce
            print(f"Enemy hits you for {reduce}! Your HP = {mainCharacter.health}")

        else:
            success = random.randint(0, 100)
            dmg = mainCharacter.attack(success)
            reduce = enemy.defend(success, dmg)
            enemy.health -= reduce
            print(f"You hit {enemy_name} for {reduce}! Enemy HP = {enemy.health}")

        turn += 1

        if mainCharacter.health <= 0:
            print("GAME OVER!")
            exit()
            


print("\nYOU WIN THE GAME!")
