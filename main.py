import os
import time
import sys
# Mob ASCII Art
dog = r"""
                                             |\_/|                  
                                             | @ @   Woof! 
                                             |   <>              _  
                                             |  _/\------____ ((| |))
                                             |               `--' |   
                                         ____|_       ___|   |___.' 
                                        /_/_____/____/_______|

"""
cat = r"""
                                         ,_     _
                                         |\\_,-~/
                                         / _  _ |    ,--.
                                        (  @  @ )   / ,-'
                                         \  _T_/-._( (
                                         /         `. \
                                        |         _  \ |
                                         \ \ ,  /      |
                                          || |-_\__   /
                                         ((_/`(____,-'
"""
fatCat = r"""
                                            /\_____/\
                                           /  o   o  \
                                          ( ==  ^  == )
                                           )         (  
                                          (           ) 
                                         ( (  )   (  ) )
                                        (__(__)___(__)__) 
"""

passageway = r"""
                    |\                                          /|
                    |  \                                      /  |
                    |    \                                  /    |
                    |      \                              /      |
                    |      | \                          / |      |
                    |      |   \                      /   |      |
                    |      |    |\                  /|    |      |
                    |      |    |  \              /  |    |      |
                    |      |    |   |            |   |    |      |
                    |      |    |   |            |   |    |      |
                    |      |    |  /              \  |    |      |
                    |      |    |/                  \|    |      |
                    |      |   /                      \   |      |
                    |      | /                          \ |      |
                    |      /                              \      |
                    |    /                                  \    |
                    |  /                                      \  |
                    |/                                          \|
"""
snake = r"""
                                                   /^\/^\
                                                 _|__|  O|
                                        \/     /~     \_/ \
                                         \____|__________/  \
                                                \_______      \
                                                        `\     \                 \
                                                          |     |                  \
                                                         /      /                    \
                                                        /     /                       \\
                                                      /      /                         \ \
                                                     /     /                            \  \
                                                   /     /             _----_            \   \
                                                  /     /           _-~      ~-_         |   |
                                                 (      (        _-~    _--_    ~-_     _/   |
                                                  \      ~-____-~    _-~    ~-_    ~-_-~    /
                                                    ~-_           _-~          ~-_       _-~
                                                       ~--______-~                ~-___-~

"""

trex = r"""
                                                ,
                                               /|
                                              / |
                                             /  /
                                            |   |
                                           /    |
                                           |    \_
                                           |      \__
                                           \       __\_______
                                            \                 \_
                                            | /                 \
                                            \/                   \
                                             |                    |
                                             \                   \|
                                             |                    \
                                             \                     |
                                             /\    \_               \
                                            / |      \__ (   )       \
                                           /  \      / |\\  /       __\____
                                           |  ,     |  /\ \ \__    |       \_
                                           \_/|\___/   \   \}}}\__|  (@)     )
                                            \)\)\)      \_\---\   \|       \ \
                                                          \>\>\>   \   /\__o_o)
                                                                    | /  VVVVV
                                                                    \ \    \
                                                                     \ \MMMMM                 
                                                                      \______/ 
"""

gryphon = r"""
                                           ____       ____
                                          /    )     (    \
                                         /    (  ^_^  )    \
                                        |  {   \('v')/   }  |
                                        |   {   /   \   }   |
                                        |_)(   /\   /\   )(_|
                                        |)  (_ | \|/  |_)  (|
                                        '     "--^^^^--"    '
"""

lich = r"""
                                           ,    ,    /\   /\
                                          /( /\ )\  _\ \_/ /_
                                          |\_||_/| < \_   _/ >
                                          \______/  \|0   0|/
                                            _\/_   _(_  ^  _)_
                                           ( () ) /`\|V"'"V|/`\
                                             {}   \  \_____/  /
                                             ()   /\   )=(   /\
                                             {}  /  \_/\=/\_/  \
"""

kobold = r"""
                                            |\     ____
                                            | \.-./ .-'
                                             \ _  _(
                                             | .)(./
                                             |   \(
                                             |     \   |
                                             |  \vvv   |
                                             |  |__    |
                                            /      `-. |
"""

fairy = r"""
                                           _   vvvvvvvvv   _
                                          ( `-._\...../_.-' )
                                           \   ((('_')))   /
                                            )   ))) (((   (
                                           (   ((( v )))   )
                                            )`--' )X( `-._(
                                           /   _./   \._   \
                                          /  .' /     \ `.  \
                                         (__/  /       \  \__)
                                              /         \
                                             /           \
     """
deathAngel = r"""
                                                         /\
                                                         ||
                                           ____ (((+))) _||_
                                          /.--.\  .-.  /.||.\
                                         /.,   \\(0.0)// || \\
                                        /;`";/\ \\|m|//  ||  ;\
                                        |:   \ \__`:`____||__:|
                                        |:    \__ \T/ (@~)(~@)|
                                        |:    _/|     |\_\/  :|
                                        |:   /  |     |  \   :|
                                        |'  /   |     |   \  '|
                                         \_/    |     |    \_/
                                                |     |
                                                |_____|
                                                |_____|
"""
grimReaper = r"""
                                                     ___          
                                                    /   \\        
                                               /\\ | . . \\       
                                             ////\\|     ||       
                                           ////   \\ ___//\       
                                          ///      \\      \      
                                         ///       |\\      |     
                                        //         | \\  \   \    
                                        /          |  \\  \   \   
                                                   |   \\ /   /   
                                                   |    \/   /    
                                                   |     \\/|     
                                                   |      \\|     
                                                   |       \\     
                                                   |        |     
                                                   |_________\
"""
ghost = r"""
                                         .-.
                                        (o o) boo!
                                        |   \
                                         \   \
                                          `~~~'
"""

gator = r"""
                                                        _ ___                /^^\ /^\  /^^\_
                                            _          _@)@) \            ,,/ '` ~ `'~~ ', `\.
                                          _/o\_ _ _ _/~`.`...'~\        ./~~..,'`','',.,' '  ~:
                                         / `,'.~,~.~  .   , . , ~|,   ,/ .,' , ,. .. ,,.   `,  ~\_
                                        ( ' _' _ '_` _  '  .    , `\_/ .' ..' '  `  `   `..  `,   \_
                                         ~V~ V~ V~ V~ ~\ `   ' .  '    , ' .,.,''`.,.''`.,.``. ',   \_
                                          _/\ /\ /\ /\_/, . ' ,   `_/~\_ .' .,. ,, , _/~\_ `. `. '.,  \_
                                         < ~ ~ '~`'~'`, .,  .   `_: ::: \_ '      `_/ ::: \_ `.,' . ',  \_
                                          \ ' `_  '`_    _    ',/ _::_::_ \ _    _/ _::_::_ \   `.,'.,`., \-,-,-,_,_,
                                           `'~~ `'~~ `'~~ `'~~  \(_)(_)(_)/  `~~' \(_)(_)(_)/ ~'`\_.._,._,'_;_;_;_;_;
"""

chest = r"""
                                                ,     \    /      ,        
                                               / \    )\__/(     / \       
                                              /   \  (_\  /_)   /   \      
                                         ____/_____\__\@  @/___/_____\____ 
                                        |             |\../|              |
                                        |              \VV/               |
                                        |        ----------------         |
                                        |_________________________________|
                                         |    /\ /      \\       \ /\    | 
                                         |  /   V        ))       V   \  | 
                                         |/     `       //        '     \| 
                                         `              V                '
"""
wyvern = r"""
                                                      /|                                           |\                 
                                                     /||             ^               ^             ||\                
                                                    / \\__          //               \\          __// \               
                                                   /  |_  \         | \   /     \   / |         /  _|  \              
                                                  /  /  \  \         \  \/ \---/ \/  /         /  /     \             
                                                 /  /    |  \         \  \/\   /\/  /         /  |       \            
                                                /  /     \   \__       \ ( 0\ /0 ) /       __/   /        \           
                                               /  /       \     \___    \ \_/|\_/ /    ___/     /\         \          
                                              /  /         \_)      \___ \/-\|/-\/ ___/      (_/\ \      `  \         
                                             /  /           /\__)       \/  oVo  \/       (__/   ` \      `  \        
                                            /  /           /,   \__)    (_/\ _ /\_)    (__/         `      \  \       
                                           /  '           //       \__)  (__V_V__)  (__/                    \  \      
                                          /  '  '        /'           \   |{___}|   /         .              \  \     
                                         /  '  /        /              \/ |{___}| \/\          `              \  \    
                                        /     /        '       .        \/{_____}\/  \          \    `         \  \   
                                             /                ,         /{_______}\   \          \    \         \     
                                                             /         /{___/_\___}\   `          \    `
"""
dragon = r"""
                                                         ___====-_  _-====___
                                                   _--^^^#####//      \\#####^^^--_
                                                _-^##########// (    ) \\##########^-_
                                               -############//  |\^^/|  \\############-
                                             _/############//   (@::@)   \\############\_
                                            /#############((     \\//     ))#############\
                                           -###############\\    (oo)    //###############-
                                          -#################\\  / VV \  //#################-
                                         -###################\\/      \//###################-
                                        _#/|##########/\######(   /\   )######/\##########|\#_
                                        |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
                                        `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
                                           `   `  `      `   / | |  | | \   '      '  '   '
                                                            (  | |  | |  )
                                                           __\ | |  | | /__
                                                          (vvv(VVV)(VVV)vvv)
"""
signDragon = r"""
                                                     __.-/|
                                                     \`o_O'
                                                      =( )=  +-----+
                                                        U|   | BOB |
                                              /\  /\   / |   +-----+
                                             ) /^\) ^\/ _)\     |
                                             )   /^\/   _) \    |
                                             )   _ /  / _)  \___|_
                                         /\  )/\/ ||  | )_)\___,|))
                                        <  >      |(,,) )__)    |
                                         ||      /    \)___)\
                                         | \____(      )___) )____
                                          \______(_______;;;)__;;;)
"""
alien = r"""
                                              ____                    
                                             /___/\_                               
                                            _\   \/_/\__                          
                      "Beep Boop"         __\       \/_/\                       
                                          \   __    __ \ \                    
                                         __\  \_\   \_\ \ \   __               
                                        /_/\\   __   __  \ \_/_/\           
                                        \_\/_\__\/\__\/\__\/_\_\/          
                                           \_\/_/\       /_\_\/             
                                              \_\/       \_\/        
"""
titleName = r"""

         ▓█████▄  █    ██  ███▄    █   ▄████ ▓█████  ▒█████   ███▄    █                
         ▒██▀ ██▌ ██  ▓██▒ ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▒██▒  ██▒ ██ ▀█   █                
         ░██   █▌▓██  ▒██░▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▒██░  ██▒▓██  ▀█ ██▒               
         ░▓█▄   ▌▓▓█  ░██░▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██   ██░▓██▒  ▐▌██▒               
         ░▒████▓ ▒▒█████▓ ▒██░   ▓██░░▒▓███▀▒░▒████▒░ ████▓▒░▒██░   ▓██░               
          ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒                
          ░ ▒  ▒ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░               
          ░ ░  ░  ░░░ ░ ░    ░   ░ ░ ░ ░   ░    ░   ░ ░ ░ ▒     ░   ░ ░                
            ░       ░              ░       ░    ░  ░    ░ ░           ░                
          ░                                                                            
                                  ▒█████    █████▒                                     
                                 ▒██▒  ██▒▓██   ▒                                      
                                 ▒██░  ██▒▒████ ░                                      
                                 ▒██   ██░░▓█▒  ░                                      
                                 ░ ████▓▒░░▒█░                                         
                                 ░ ▒░▒░▒░  ▒ ░                                         
                                   ░ ▒ ▒░  ░                                           
                                 ░ ░ ░ ▒   ░ ░                                         
                                     ░ ░                                               
                                                                                       
      ▄▄▄█████▓ ██░ ██ ▓█████     ██▓███ ▓██   ██▓▄▄▄█████▓ ██░ ██  ▒█████   ███▄    █ 
      ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██░  ██▒▒██  ██▒▓  ██▒ ▓▒▓██░ ██▒▒██▒  ██▒ ██ ▀█   █ 
      ▒ ▓██░ ▒░▒██▀▀██░▒███      ▓██░ ██▓▒ ▒██ ██░▒ ▓██░ ▒░▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒
      ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒██▄█▓▒ ▒ ░ ▐██▓░░ ▓██▓ ░ ░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒
        ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██▒ ░  ░ ░ ██▒▓░  ▒██▒ ░ ░▓█▒░██▓░ ████▓▒░▒██░   ▓██░
        ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ▒▓▒░ ░  ░  ██▒▒▒   ▒ ░░    ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
          ░     ▒ ░▒░ ░ ░ ░  ░   ░▒ ░     ▓██ ░▒░     ░     ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
        ░       ░  ░░ ░   ░      ░░       ▒ ▒ ░░    ░       ░  ░░ ░░ ░ ░ ▒     ░   ░ ░ 
                ░  ░  ░   ░  ░            ░ ░               ░  ░  ░    ░ ░           ░ 
                                          ░ ░                                          

"""
theEnd = r"""

            ███        ▄█    █▄       ▄████████         ▄████████ ███▄▄▄▄   ████████▄  
        ▀█████████▄   ███    ███     ███    ███        ███    ███ ███▀▀▀██▄ ███   ▀███ 
         ▀███▀▀██   ███    ███     ███    █▀         ███    █▀  ███   ███ ███    ███ 
           ███   ▀  ▄███▄▄▄▄███▄▄  ▄███▄▄▄           ▄███▄▄▄     ███   ███ ███    ███ 
          ███     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀          ▀▀███▀▀▀     ███   ███ ███    ███ 
          ███       ███    ███     ███    █▄         ███    █▄  ███   ███ ███    ███ 
          ███       ███    ███     ███    ███        ███    ███ ███   ███ ███   ▄███ 
         ▄████▀     ███    █▀      ██████████        ██████████  ▀█   █▀  ████████▀  
                                                                               

"""
# Player stats
spells = ["BLAZE", "FREEZE","BOLT","HEAL"]
playerSpells = ["BLAZE", "FREEZE","BOLT"]
healSpells = ["HEAL"]
stats = [10,3,1]
playerItems = []
playerStat = 0
damage = 0
playerHP = stats[0]
playerMana = stats[2]
playerAlive = True

# Enemy stats
enemyStats = [10,2,2]
enemyHP = enemyStats[0]
battleNum = 1
deadBool = False

# Misc
gameRunning = True
userInput = ""
inputBool = False

# Beginning Message
def beginning ():
    print(titleName)
    input("Press any key to continue...")
    print(
        "\nYou have entered the Dungeon of the Python\nFight your way through 9 progressively harder battles to make your escape!\n")
    input("Press any key to continue...")
    print(
        "\nTo Attack type 'A' or 'Attack' and hit enter\n\nTo use a spell type the name of the spell ex: 'Heal' or 'Heal2' if you want to use a level 2 Heal\n")
    print("To use an Item type the name of the Item\n\nYour starting Stats are:\n")
    print_stats(stats)
    print("\nGood luck!\n\n")
    return
# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Spell damage
def spell_damage(spellLevel,spellName,enemyName):
    spellDamage = 7

    if "2" in spellName:
        spellLevel = 2
    elif "3" in spellName:
        spellLevel = 3

    if spellLevel == 2:
        spellDamage = 19
    elif spellLevel == 3:
        spellDamage = 47
    if spellName == "BOLT" and (enemyName == 2 or enemyName == 4 or enemyName == 6):
        spellDamage = spellDamage * 1.2
    elif spellName == "BLAZE" and (enemyName == 1 or enemyName == 5 or enemyName == 7):
        spellDamage = spellDamage * 1.2
    elif spellName == "FREEZE" and (enemyName == 8 or enemyName == 3 or enemyName == 10):
        spellDamage = spellDamage * 1.2
    spellDamage = round(spellDamage)
    if "BLAZE" in spellName:
        print("\nA scorching fireball scalds the creature, dealing " + str(spellDamage) + " points of damage")
    elif "FREEZE" in spellName:
        print("\nAn icy hail assails the creature, dealing " + str(spellDamage) + " points of damage")
    elif "BOLT" in spellName:
        print("\nYou smell ozone as a lightning bolt zaps the creature, dealing " + str(spellDamage) + " points of damage")
    return spellDamage

#Heal Spell
def heal_spell(spellName, healthAmount):

    healAmount = 7
    playerHealth = healAmount
    spellLevel = 1

    if "2" in spellName:
        spellLevel = 2
    elif "3" in spellName:
        spellLevel = 3

    if spellLevel == 2:
        healAmount = 19
    elif spellLevel == 3:
        healAmount = 47

    playerHealth = healthAmount + healAmount

    if playerHealth > stats[0]:
        playerHealth = stats[0]

    print("\nYou heal yourself for " + str(healAmount) + " HP\n")
    return playerHealth

# Attack Damage
def attack_damage(attackStat,weapon):
    damage = attackStat + weapon
    return damage
# LevelUp
def level_up(statList, i = 0):
    for x in statList:
        if i == 0:
            statList[i] = round((x + 3) * 1.2)
        else:
            statList[i] = round((x + 2) * 1.2)
        i +=1
    return statList

# Level Up Print
def level_print(statList, i = 0):
    for x in statList:
        if i == 0:
            print("\nHp: " + str(x))
        elif i == 1:
            print("Attack: " + str(x))
        else:
            print("Magic: " + str(x) + "\n")
        i +=1
    return

# Monster Level Up
def monster_up(statList, i = 0):
    health = 10
    for x in statList:
        if i == 0:
            health = x
            statList[i] = round((x + 4) * 1.3)
        else:
            statList[i] = round(((health + 3) * 1.2)/6)
        i +=1
    return statList

# Print Stats
def print_stats(statList, i = 0):
    for x in statList:
        if i == 0:
            print("HP: " + str(x))
        elif i == 1:
            print("Attack: " + str(x))
        elif i == 2:
            print("Magic: "+ str(x))
        i +=1
    return

# Load Encounter
def encounter(battleNumber, health):
    if battleNumber == 1:
        print(kobold + "\nKobold HP: " + str(health))
    elif battleNumber == 2:
        print(gator + "\nGator HP: " + str(health))
    elif battleNumber == 3:
        print(gryphon + "\nGryphon HP: " + str(health))
    elif battleNumber == 4:
        print(deathAngel + "\nAvenging Angel HP: " + str(health))
    elif battleNumber == 5:
        print(lich + "\nLich HP: " + str(health))
    elif battleNumber == 6:
        print(wyvern + "\nWyvern HP: " + str(health))
    elif battleNumber == 7:
        print(alien + "\nAlien? HP: " + str(health))
    elif battleNumber == 8:
        print(trex + "\nTrex HP: " + str(health))
    elif battleNumber == 9:
        print(snake + "\nPython HP: " + str(health))
    return

# Damage Calc
def damage_calc(attackType,statNum,enemyName):
    damageNum = 0
    spellLvl = 0
    if attackType == ("A" or "ATTACK"):
        damageNum = (statNum)
    elif attackType in playerSpells:
        damageNum = spell_damage(spellLvl,attackType,enemyName)
    return damageNum

# Check Enemy HP
def health_check(enemyHealth):
    encounterBool = False
    if enemyHealth <= 0:
        encounterBool = True
    return encounterBool

# Player Death Check
def player_death(playerHealth):
    aliveBool = True

    if playerHealth <= 0:
        aliveBool = False
    return aliveBool

# Rewards
def rewards():
    inputBoolean = False
    rewardNum = ""
    print(chest + "\nCongratulations you have slain an enemy! A chest appears before you\n")
    print("Choose your reward\n1. Strength +1 2. A Random Item 3. Nothing")
    while not inputBoolean:
        rewardNum = input("Enter 1, 2 or 3 to choose a reward")
    if rewardNum == "1":
        stats[1] = (stats[1] + 1)
    elif rewardNum == "2":
        item_assign()
    return

# Assign Items
def item_assign():
    return

# Mana Check
def mana_check(spellName):
    manaAmount = playerMana
    manaCost = 1

    if "2" in spellName:
        manaCost = 6
    elif "3" in spellName:
        manaCost = 13

    manaAmount = manaAmount - manaCost

    return  manaAmount


# Spell Level Up
def spell_increase(encounterNum):
    if encounterNum == 4:
        playerSpells.append("BLAZE2")
        playerSpells.append("BOLT2")
        playerSpells.append("FREEZE2")
        healSpells.append("HEAL2")
        print("\nYou have gained access to the BLAZE2, FREEZE2, BOLT2 and Heal2 spells.")
        print("They each cost 6 mana to cast\n")
        input("Press any key to continue...")
    elif encounterNum == 7:
        playerSpells.append("BLAZE3")
        playerSpells.append("BOLT3")
        playerSpells.append("FREEZE3")
        healSpells.append("HEAL3")
        print("\nYou have gained access to the BLAZE3, FREEZE3, BOLT3 and Heal3 spells.")
        print("They each cost 13 mana to cast\n")
        input("Press any key to continue...")
    return

# Game Over
def game_over():
    print("Despite your best efforts you have died")
    time.sleep(3)
    sys.exit(1)


# Bob the Dragon
def bob_the_dragon():
    print(signDragon)
    print("Bob says 'You're halfway there! Keep it up!'\n")
    input("Press any key to continue...")
    return

# Ending
def ending():
    print("\nCongratulations! You made it to the end of the dungeon and find a sparkling chest\n")
    print(chest)
    input("\nPress any key to open it...")
    print("\nThe Queen of the Fairies emerges and thanks you for freeing her from the Python!\n\n She casts a spell and whisks you both out of the dungeon to safety")
    print(fairy)
    time.sleep(3)
    print(theEnd)
    print("\nThanks for playing!")
    input("\nPress any key to close program...")
    sys.exit(1)

# Game Start
beginning()
roundStart = True
while gameRunning:
    if roundStart:
        playerHP = stats[0]
        playerMana = stats[2]
        enemyHP = enemyStats[0]
    print("Player HP: " + str(playerHP))
    print("Player MP: " + str(playerMana))
    inputBool = False
    deadBool = health_check(enemyHP)
    if deadBool:
        roundStart = True
        playerHP = stats[0]
        playerMana = stats[2]
        print("\nYou have leveled up!\n")
        stats = level_up(stats)
        level_print(stats)
        input("Press any key to continue...")
        enemyStats = monster_up(enemyStats)
        battleNum +=1
        enemyHP = enemyStats[0]
        # Bob and Spell Level check
        if battleNum == 6:
            bob_the_dragon()
        elif battleNum == 4:
            spell_increase(battleNum)
        elif battleNum == 7:
            spell_increase(battleNum)
        elif battleNum == 10:
            ending()
        print("\nYou move further down the corridor and encounter another monster\n")
        print(passageway)
        input("Press any key to continue...")
    else:
        roundStart = False



    encounter(battleNum, enemyHP)

    while not inputBool:
        userInput = input("Your action: ")
        userInput = userInput.upper()
        if userInput == ("A" or "ATTACK"):
            damage = damage_calc(userInput,stats[1],battleNum)
            enemyHP = enemyHP - damage
            print("\nCrack! You strike the creature, dealing " + str(damage) + " points of damage")
            inputBool = True
        elif userInput in playerSpells:
            playerMana = mana_check(userInput)
            if playerMana >= 0:
                damage = damage_calc(userInput, stats[2], battleNum)
                enemyHP = enemyHP - damage
                inputBool = True
            else:
                playerMana = 0
                print("You do not have enough Mana to cast the spell\n")
        elif userInput in healSpells:
            playerMana = mana_check(userInput)
            if playerMana >= 0:
                playerHP = heal_spell(userInput, playerHP)
                inputBool = True
        else:
            userInput = input("Your action: ")
    if enemyHP > 0:
        print("\nThe creature attacks you, dealing " + str(enemyStats[1]) + " damage\n")
        playerHP = playerHP - enemyStats[1]
    playerAlive = player_death(playerHP)

    if not playerAlive:
        game_over()
    clear()