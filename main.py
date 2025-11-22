from gameplay.gameplay import characterBuildIntro, enemyBattle, postCombat, bossBattle
from classes.player.createPlayer import Player
import os


mainCharacter = Player("warrior", "blue", "Greg" )
#mainCharacter = characterBuildIntro()      
print("Part 1")                                                                                                      
fightNum = 0
part = 1
# GAMEPLAY LOOP
while mainCharacter.health > 0:

    if fightNum % 5 == 0 and fightNum != 0:
        fightNum = bossBattle(mainCharacter, fightNum)
        os.system('cls' if os.name == 'nt' else 'clear')
        part += 1
        print(f"Now we begin part {part} ")
        
    else:
        fightNum = enemyBattle(mainCharacter, fightNum)
    
    postCombat(mainCharacter)