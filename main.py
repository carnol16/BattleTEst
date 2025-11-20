from gameplay.gameplay import characterBuildIntro, enemyBattle, postCombat, bossBattle
from classes.player.createPlayer import Player


#mainCharacter = Player("boat man", "blue", "Greg" )
mainCharacter = characterBuildIntro()                                                                                                            
fightNum = 0

# GAMEPLAY LOOP
while mainCharacter.health > 0:

    if fightNum % 5 == 0 and fightNum != 0:
        fightNum = bossBattle(mainCharacter, fightNum)
    else:
        fightNum = enemyBattle(mainCharacter, fightNum)
    
    postCombat(mainCharacter)