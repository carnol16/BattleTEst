from gameplay.gameplay import characterBuildIntro, enemyBattle, postCombat, bossBattle
from classes.player.createPlayer import Player, NPC
import os
from audioMixer import SoundManager
import json
import datetime

SoundManager(sound_enabled = False)


mainCharacter = Player("boat man", "blue", "Dmytro" )
#mainCharacter.activeParty = (NPC("Parim the Iguana", "blue"))

#mainCharacter = characterBuildIntro()      
print("Part 1")                                                                                                      
fightNum = 0
part = 1
# GAMEPLAY LOOP
while mainCharacter.health > 0:
    
    mainCharacter.fightNum = fightNum

    if fightNum % 5 == 0 and fightNum != 0:
        fightNum = bossBattle(mainCharacter, fightNum)
        os.system('cls' if os.name == 'nt' else 'clear')
        part += 1
        print(f"Now we begin part {part} ")
        
    else:
        fightNum = enemyBattle(mainCharacter, fightNum)
    
    postCombat(mainCharacter)

