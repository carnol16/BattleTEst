from gameplay.gameplay import characterBuildIntro, enemyBattle, postCombat
from classes.player.createPlayer import Player


name = "george"
mainCharacter = Player("warrior", "blue", "Greg" )
#mainCharacter = characterBuildIntro()                                                                                                            
fightNum = 0

# GAMEPLAY LOOP
while mainCharacter.health > 0:

    fightNum = enemyBattle(mainCharacter, fightNum)
    
    postCombat(mainCharacter)