#Started: September 30, 2021
#Last Updated: May 20, 2022
#Author: Dustin Ross

#Imports
import random as rando
import PySimpleGUI as sg

#Class Definitions
class TypeMatchup:

    def __init__(self):
        #Create multiple dictionaries for type matchups
        self.normal = normalType = {'NORMAL':1,'FIGHTING':1,'FLYING':1,'POISON':1,
                                    'GROUND':1,'ROCK':0.5,'BUG':1,'GHOST':0,
                                    'STEEL':0.5,'FIRE':1,'WATER':1,'GRASS':1,
                                    'ELECTRIC':1,'PSYCHIC':1,'ICE':1,'DRAGON':1,
                                    'DARK':1,'FAIRY':1}
        self.fighting = fightingType = {'NORMAL':2,'FIGHTING':1,'FLYING':0.5,
                                    'POISON':0.5,'GROUND':1,'ROCK':2,'BUG':0.5,
                                    'GHOST':0,'STEEL':2,'FIRE':1,'WATER':1,
                                    'GRASS':1,'ELECTRIC':1,'PSYCHIC':0.5,'ICE':2,
                                    'DRAGON':1,'DARK':2,'FAIRY':0.5}
        self.flying = flyingType = {'NORMAL':1,'FIGHTING':2,'FLYING':1,'POISON':1,
                                    'GROUND':1,'ROCK':0.5,'BUG':2,'GHOST':1,'STEEL':0.5,
                                    'FIRE':1,'WATER':1,'GRASS':2,'ELECTRIC':0.5,
                                    'PSYCHIC':1,'ICE':1,'DRAGON':1,'DARK':1,'FAIRY':1}
        self.poison = poisonType = {'NORMAL':1,'FIGHTING':1,'FLYING':1,'POISON':0.5,
                                    'GROUND':0.5,'ROCK':0.5,'BUG':1,'GHOST':0.5,
                                    'STEEL':0,'FIRE':1,'WATER':1,'GRASS':2,'ELECTRIC':1,
                                    'PSYCHIC':1,'ICE':1,'DRAGON':1,'DARK':1,'FAIRY':2}
        self.ground = groundType = {'NORMAL':1,'FIGHTING':1,'FLYING':0,'POISON':2,
                                    'GROUND':1,'ROCK':2,'BUG':0.5,'GHOST':1,
                                    'STEEL':2,'FIRE':2,'WATER':1,'GRASS':0.5,
                                    'ELECTRIC':2,'PSYCHIC':1,'ICE':1,'DRAGON':1,
                                    'DARK':1,'FAIRY':1}
        self.rock = rockType = {'NORMAL':1,'FIGHTING':0.5,'FLYING':2,'POISON':1,
                                    'GROUND':0.5,'ROCK':1,'BUG':2,'GHOST':1,
                                    'STEEL':0.5,'FIRE':2,'WATER':1,'GRASS':1,
                                    'ELECTRIC':1,'PSYCHIC':1,'ICE':2,'DRAGON':1,
                                    'DARK':1,'FAIRY':1}
        self.bug = bugType = {'NORMAL':1,'FIGHTING':0.5,'FLYING':0.5,'POISON':0.5,
                                    'GROUND':1,'ROCK':1,'BUG':1,'GHOST':0.5,
                                    'STEEL':0.5,'FIRE':0.5,'WATER':1,'GRASS':2,
                                    'ELECTRIC':1,'PSYCHIC':2,'ICE':1,'DRAGON':1,
                                    'DARK':2,'FAIRY':0.5}
        self.ghost = ghostType = {'NORMAL':0,'FIGHTING':1,'FLYING':1,'POISON':1,
                                    'GROUND':1,'ROCK':1,'BUG':1,'GHOST':2,
                                    'STEEL':1,'FIRE':1,'WATER':1,'GRASS':1,
                                    'ELECTRIC':1,'PSYCHIC':2,'ICE':1,'DRAGON':1,
                                    'DARK':0.5,'FAIRY':1}
        self.steel = steelType = {'NORMAL':1,'FIGHTING':1,'FLYING':1,'POISON':1,
                                    'GROUND':1,'ROCK':2,'BUG':1,'GHOST':1,
                                    'STEEL':0.5,'FIRE':0.5,'WATER':0.5,'GRASS':1,
                                    'ELECTRIC':0.5,'PSYCHIC':1,'ICE':2,'DRAGON':1,
                                    'DARK':1,'FAIRY':2}
        self.fire = fireType = {'NORMAL':1,'FIGHTING':1,'FLYING':1,'POISON':1,
                                    'GROUND':1,'ROCK':0.5,'BUG':2,'GHOST':1,
                                    'STEEL':2,'FIRE':0.5,'WATER':0.5,'GRASS':2,
                                    'ELECTRIC':1,'PSYCHIC':1,'ICE':2,'DRAGON':0.5,
                                    'DARK':1,'FAIRY':1}
        self.water = waterType = {'NORMAL':1,'FIGHTING':1,'FLYING':1,'POISON':1,
                                    'GROUND':2,'ROCK':2,'BUG':1,'GHOST':1,
                                    'STEEL':1,'FIRE':2,'WATER':0.5,'GRASS':0.5,
                                    'ELECTRIC':1,'PSYCHIC':1,'ICE':1,'DRAGON':0.5,
                                    'DARK':1,'FAIRY':1}
        self.grass = grassType = {'NORMAL':1,'FIGHTING':1,'FLYING':0.5,'POISON':0.5,
                                    'GROUND':2,'ROCK':2,'BUG':0.5,'GHOST':1,
                                    'STEEL':0.5,'FIRE':0.5,'WATER':2,'GRASS':0.5,
                                    'ELECTRIC':1,'PSYCHIC':1,'ICE':1,'DRAGON':0.5,
                                    'DARK':1,'FAIRY':1}
        self.electric = electricType = {'NORMAL':1,'FIGHTING':1,'FLYING':2,'POISON':1,
                                    'GROUND':0,'ROCK':1,'BUG':1,'GHOST':1,
                                    'STEEL':1,'FIRE':1,'WATER':2,'GRASS':0.5,
                                    'ELECTRIC':0.5,'PSYCHIC':1,'ICE':1,'DRAGON':0.5,
                                    'DARK':1,'FAIRY':1}
        self.psychic = psychicType = {'NORMAL':1,'FIGHTING':2,'FLYING':1,'POISON':2,
                                    'GROUND':1,'ROCK':1,'BUG':1,'GHOST':1,
                                    'STEEL':0.5,'FIRE':1,'WATER':1,'GRASS':1,
                                    'ELECTRIC':1,'PSYCHIC':0.5,'ICE':1,'DRAGON':1,
                                    'DARK':0,'FAIRY':1}
        self.ice = iceType = {'NORMAL':1,'FIGHTING':1,'FLYING':2,'POISON':1,
                                    'GROUND':2,'ROCK':1,'BUG':1,'GHOST':1,
                                    'STEEL':0.5,'FIRE':0.5,'WATER':0.5,'GRASS':2,
                                    'ELECTRIC':1,'PSYCHIC':1,'ICE':0.5,'DRAGON':2,
                                    'DARK':1,'FAIRY':1}
        self.dragon = dragonType = {'NORMAL':1,'FIGHTING':1,'FLYING':1,'POISON':1,
                                    'GROUND':1,'ROCK':1,'BUG':1,'GHOST':1,
                                    'STEEL':0.5,'FIRE':1,'WATER':1,'GRASS':1,
                                    'ELECTRIC':1,'PSYCHIC':1,'ICE':1,'DRAGON':2,
                                    'DARK':1,'FAIRY':0}
        self.dark = darkType = {'NORMAL':1,'FIGHTING':0.5,'FLYING':1,'POISON':1,
                                    'GROUND':1,'ROCK':1,'BUG':1,'GHOST':2,
                                    'STEEL':1,'FIRE':1,'WATER':1,'GRASS':1,
                                    'ELECTRIC':1,'PSYCHIC':2,'ICE':1,'DRAGON':1,
                                    'DARK':0.5,'FAIRY':0.5}
        self.fairy = fairyType = {'NORMAL':1,'FIGHTING':2,'FLYING':1,'POISON':0.5,
                                    'GROUND':1,'ROCK':1,'BUG':1,'GHOST':1,
                                    'STEEL':0.5,'FIRE':0.5,'WATER':1,'GRASS':1,
                                    'ELECTRIC':1,'PSYCHIC':1,'ICE':1,'DRAGON':2,
                                    'DARK':2,'FAIRY':1}
        
    def getMatchup(self, moveType, defenderType):
        if(moveType == 'NORMAL'):
            if(defenderType in self.normal):
                return self.normal.get(defenderType, None)
        elif(moveType == 'FIGHTING'):
            if(defenderType in self.fighting):
                return  self.fighting.get(defenderType, None)
        elif(moveType == 'FLYING'):
            if(defenderType in self.flying):
                return self.flying.get(defenderType, None)
        elif(moveType == 'POISON'):
            if(defenderType in self.poison):
                return self.poison.get(defenderType, None)
        elif(moveType == 'GROUND'):
            if(defenderType in self.ground):
                return self.ground.get(defenderType, None)
        elif(moveType == 'ROCK'):
            if(defenderType in self.rock):
                return self.rock.get(defenderType, None)
        elif(moveType == 'BUG'):
            if(defenderType in self.bug):
                return self.bug.get(defenderType, None)
        elif(moveType == 'GHOST'):
            if(defenderType in self.ghost):
                return self.ghost.get(defenderType, None)
        elif(moveType == 'STEEL'):
            if(defenderType in self.steel):
                return self.steel.get(defenderType, None)
        elif(moveType == 'FIRE'):
            if(defenderType in self.fire):
                return self.fire.get(defenderType, None)
        elif(moveType == 'WATER'):
            if(defenderType in self.water):
                return self.water.get(defenderType, None)
        elif(moveType == 'GRASS'):
            if(defenderType in self.grass):
                return self.grass.get(defenderType, None)
        elif(moveType == 'ELECTRIC'):
            if(defenderType in self.electric):
                return self.electric.get(defenderType, None)
        elif(moveType == 'PSYCHIC'):
            if(defenderType in self.psychic):
                return self.psychic.get(defenderType, None)
        elif(moveType == 'ICE'):
            if(defenderType in self.ice):
                return self.ice.get(defenderType, None)
        elif(moveType == 'DRAGON'):
            if(defenderType in self.dragon):
                return self.dragon.get(defenderType, None)
        elif(moveType == 'DARK'):
            if(defenderType in self.dark):
                return self.dark.get(defenderType, None)
        elif(moveType == 'FAIRY'):
            if(defenderType in self.fairy):
                return self.fairy.get(defenderType, None)
   
class Pokemon:

    currentHP = 0
    currentStatus = ""
    i = 0
    
    def __init__(self, pkmnName, pkmnType1, pkmnType2, pkmnLevel, baseHitPoints, baseAttack, baseDefense, 
                 baseSpAttack, baseSpDefense, baseSpeed, pkmnMove1, pkmnMove2, pkmnMove3, pkmnMove4):
        self.pkmnName=pkmnName
        self.pkmnType1=pkmnType1
        self.pkmnType2=pkmnType2
        self.pkmnLevel=pkmnLevel
        self.baseHitPoints=baseHitPoints + 60
        self.baseAttack=baseAttack
        self.baseDefense=baseDefense
        self.baseSpAttack=baseSpAttack
        self.baseSpDefense=baseSpDefense
        self.baseSpeed=baseSpeed
        self.pkmnMove1=pkmnMove1
        self.pkmnMove2=pkmnMove2
        self.pkmnMove3=pkmnMove3
        self.pkmnMove4=pkmnMove4
        self.currentHP=self.baseHitPoints
        self.currentStatus=None
        self.moveList = []
        self.moveList.append(pkmnMove1)
        self.moveList.append(pkmnMove2)
        self.moveList.append(pkmnMove3)
        self.moveList.append(pkmnMove4)

    def __repr__(self):
        if(self.pkmnType2 == None):
            return ("I am a " + self.pkmnName + " with a type of " + self.pkmnType1
                    + " at level " + str(self.pkmnLevel))
        else:
            return ("I am a " + self.pkmnName + " with a type of " + self.pkmnType1
                    + " and " + self.pkmnType2 + " at level " + str(self.pkmnLevel))

class Trainer:

    team = []
    
    def __init__(self, trainerName, pkmn1, pkmn2, pkmn3, pkmn4, pkmn5, pkmn6):
        self.trainerName=trainerName
        self.pkmn1=pkmn1
        self.pkmn2=pkmn2
        self.pkmn3=pkmn3
        self.pkmn4=pkmn4
        self.pkmn5=pkmn5
        self.pkmn6=pkmn6
        self.team=[]
        self.team.append(pkmn1)
        self.team.append(pkmn2)
        self.team.append(pkmn3)
        self.team.append(pkmn4)
        self.team.append(pkmn5)
        self.team.append(pkmn6)

    def __repr__(self):
        return ("My name is " + self.trainerName +  " and I have: "
                + self.pkmn1.pkmnName + ", " + self.pkmn2.pkmnName + ", "
                + self.pkmn3.pkmnName + ", " + self.pkmn4.pkmnName + ", " 
                + self.pkmn5.pkmnName + ", " + self.pkmn6.pkmnName)

    def printTeam(self):
        for i in range(0, 6):
            print(self.team[i].pkmnName)
    
class Move:

    def __init__(self, moveName, moveType, contactType, movePower, moveAccuracy):
        self.moveName=moveName
        self.moveType=moveType
        self.contactType=contactType
        self.movePower=movePower
        self.moveAccuracy=moveAccuracy

    def __repr__(self):
        return ("I am " + self.moveName + " with a type of " + self.moveType
                + " a contact type of " + self.contactType + " a power of "
                + str(self.movePower) + " and an accuracy of " + str(self.moveAccuracy))

class PokemonRoster:

    roster = []
    #Creates a roster of Pokemon in the game that are accessible through their roster slot
    #Sorted by Nation Dex number
    def __init__(self):
        self.roster.append(Pokemon("Venusaur", "Grass", "Poison", 50, 80, 82, 83, 100, 100, 80, Solarbeam, Earthquake, BodySlam, SludgeBomb))
        self.roster.append(Pokemon("Charizard", "Fire", "Flying", 50, 78, 84, 78, 109, 85, 100, Flamethrower, Solarbeam, WingAttack, Earthquake))
        self.roster.append(Pokemon("Blastoise", "Water", None, 50, 79, 83, 100, 85, 105, 78, Surf, Earthquake, BodySlam, IcePunch))
        self.roster.append(Pokemon("Pikachu", "Electric", None, 50, 35, 55, 40, 50, 50, 90, Thunderbolt, Surf, BodySlam, ThunderPunch))
        self.roster.append(Pokemon("Raichu", "Electric", None, 50, 60, 90, 55, 90, 80, 110, ThunderPunch, Surf, BodySlam, Thunderbolt))
        self.roster.append(Pokemon("Nidoqueen", "Poison", "Ground", 50, 90, 92, 87, 75, 85, 76, Earthquake, Thunderbolt, BodySlam, SludgeBomb))
        self.roster.append(Pokemon("Clefable", "Fairy", None, 50, 95, 70, 73, 95, 90, 60, BodySlam, Thunderbolt, Earthquake, FirePunch))
        self.roster.append(Pokemon("Wigglytuff", "Normal", "Fairy", 50, 140, 70, 45, 85, 50, 45, BodySlam, IcePunch, FirePunch, ThunderPunch))
        self.roster.append(Pokemon("Golduck", "Water", "Psychic", 50, 80, 82, 78, 95, 80, 85, Surf, Thunderbolt, Psychic, SludgeBomb))
        self.roster.append(Pokemon("Poliwrath", "Water", "Fighting", 50, 90, 95, 95, 70, 90, 70, Surf, IcePunch, BodySlam, CloseCombat))
        self.roster.append(Pokemon("Machamp", "Fighting", None, 50, 90, 130, 80, 65, 85, 55, CloseCombat, Earthquake, BodySlam, ThunderPunch))
        self.roster.append(Pokemon("Rhydon", "Rock", "Ground", 50, 105, 130, 120, 45, 45, 40, Earthquake, FirePunch, BodySlam, RockSlide))
        self.roster.append(Pokemon("Gyarados", "Water","Flying", 50, 95, 125, 79, 60, 100, 81, Surf, Hyperbeam, Flamethrower, Thunderbolt))
        self.roster.append(Pokemon("Ditto", "Normal", None, 50, 48, 48, 48, 48, 48, 48, BodySlam, Flamethrower, Thunderbolt, Surf))
        self.roster.append(Pokemon("Aerodactyl", "Rock", "Flying", 50, 80, 105, 65, 60, 75, 130, BodySlam, Earthquake, RockSlide, WingAttack))
        self.roster.append(Pokemon("Snorlax", "Normal", None, 50, 160, 110, 65, 65, 110, 30, BodySlam, Earthquake, RockSlide, Thunderbolt))
        self.roster.append(Pokemon("Dragonite", "Dragon", "Flying", 50, 91, 134, 95, 100, 100, 80, BodySlam, FirePunch, Thunderbolt, Surf))
        self.roster.append(Pokemon("Typholsion", "Fire", None, 50, 78, 84, 78, 109, 85, 100, Flamethrower, Solarbeam, Earthquake, BodySlam))
        self.roster.append(Pokemon("Politoed", "Water", None, 50, 90, 75, 75, 90, 100, 70, Surf, IcePunch, Thunderbolt, BodySlam))
        self.roster.append(Pokemon("Granbull", "Fairy", None, 50, 90, 120, 75, 60, 60, 45, BodySlam, CloseCombat, Earthquake, IcePunch))
        self.roster.append(Pokemon("Scizor", "Steel", "Bug", 50, 70, 130, 100, 55, 80, 65, CloseCombat, Solarbeam, WingAttack, BodySlam))
        self.roster.append(Pokemon("Porygon2", "Normal", None, 50, 85, 80, 90, 105, 95, 60, Hyperbeam, Thunderbolt, Flamethrower, SludgeBomb))
        self.roster.append(Pokemon("Tyranitar", "Rock", "Dark", 50, 100, 134, 110, 95, 100, 61, Earthquake, BodySlam, RockSlide, FirePunch))
        self.roster.append(Pokemon("Gallade", "Psychic", "Fighting", 50, 68, 125, 65, 65, 115, 80, ThunderPunch, CloseCombat, PsychoCut, FirePunch))

class TrainerRoster:

    roster = []

    def __init__(self):
        self.roster.append(Trainer("Leon", PokemonRoster.roster[23], PokemonRoster.roster[22], PokemonRoster.roster[4], PokemonRoster.roster[16], PokemonRoster.roster[17], PokemonRoster.roster[18]))
        self.roster.append(Trainer("Red", PokemonRoster.roster[9], PokemonRoster.roster[0], PokemonRoster.roster[3], PokemonRoster.roster[12], PokemonRoster.roster[14], PokemonRoster.roster[15]))
        self.roster.append(Trainer("Blue", PokemonRoster.roster[20], PokemonRoster.roster[1], PokemonRoster.roster[8], PokemonRoster.roster[10], PokemonRoster.roster[21], PokemonRoster.roster[11]))
        self.roster.append(Trainer("Green", PokemonRoster.roster[7], PokemonRoster.roster[2], PokemonRoster.roster[13], PokemonRoster.roster[6], PokemonRoster.roster[5], PokemonRoster.roster[19]))
         
#Function Definitions
def CharacterMenu():
    
    playerChoice = 0
    playerSelect = False
    playerTrainer = None
    opponentChoice = 0
    opponentSelect = False
    opponentTrainer = None
    i = 0

    while(playerSelect != True):
        while(i < len(TrainerRoster.roster)):
            print(str(i+1) + " " + TrainerRoster.roster[i].trainerName)
            i += 1

        playerChoice = input("Please select your trainer: ")

        if(int(playerChoice)-1 < len(TrainerRoster.roster)):
            playerTrainer = TrainerRoster.roster[int(playerChoice)-1]
            playerSelect = True
        else:
            print("Please select an option listed.")

    i = 0
    while(opponentSelect != True):
        while(i < len(TrainerRoster.roster)):
            print(str(i+1) + " " + TrainerRoster.roster[i].trainerName)
            i += 1

        opponentChoice = input("Please select opponent trainer: ")

        if(int(opponentChoice)-1 < len(TrainerRoster.roster)):
            opponentTrainer = TrainerRoster.roster[int(opponentChoice)-1]
            opponentSelect = True
        else:
            print("Please select an option listed.")
            
    print()
    playerTrainer.team = PokemonSelect(playerTrainer)
    opponentTrainer.team = PokemonSelect(opponentTrainer)
    TrainerBattle(playerTrainer, opponentTrainer)

def PokemonSelect(trainerTeam):

    currentOrder = []
    selection = 0
    passes = 0
    i = 0

    print("Select team order")

    while(passes < 6):
        while(i < len(trainerTeam.team)):
            print(str(i + 1) + ". " + trainerTeam.team[i].pkmnName)
            i = i + 1
        selection = int(input("Select number for next Pokemon: ")) - 1
        if(selection < len(trainerTeam.team)):
            currentOrder.append(trainerTeam.team[selection])
            trainerTeam.team.pop(selection)
            i = 0
            passes = passes + 1
        else:
            print("Please selection a valid option.")

    #while(i < len(currentOrder)):
        #print(str(i + 1) + ". " + currentOrder[i].pkmnName)
        #i = i + 1

    return currentOrder
    
def Damage(attacker, attackMove, defender):

    typeChart = TypeMatchup()

    #Damage Function variables
    calculatedDamage = 0
    critChance = rando.randint(1, 100)
    typeEffectiveness = 0.0
    if(attackMove.contactType == "Physical"):
        calculatedDamage = (((((2*attacker.pkmnLevel)/5)+2)*attackMove.movePower*(attacker.baseAttack/defender.baseDefense))/50+2)
    elif(attackMove.contactType == "Special"):
        calculatedDamage = (((((2*attacker.pkmnLevel)/5)+2)*attackMove.movePower*(attacker.baseSpAttack/defender.baseSpDefense))/50+2)

    #Check for critical hit
    if(critChance >= 94):
        calculatedDamage = calculatedDamage * 1.5
        print("Critical Hit!")
        
    #Check for same type attack bonus
    if(attacker.pkmnType1 == attackMove.moveType or attacker.pkmnType2 == attackMove.moveType):
        calculatedDamage = calculatedDamage * 1.5

    #Check for move effectiveness
    typeEffectiveness = typeChart.getMatchup(attackMove.moveType.upper(), defender.pkmnType1.upper())
    if(defender.pkmnType2 != None):
        typeEffectiveness = typeEffectiveness * typeChart.getMatchup(attackMove.moveType.upper(), defender.pkmnType2.upper())
    calculatedDamage = calculatedDamage * typeEffectiveness
    if(typeEffectiveness >= 2):
        print("It's super-effective!")
    elif(typeEffectiveness > 0 and typeEffectiveness <= 0.5):
        print("It's not very effective!")
    elif(typeEffectiveness == 0):
        print("It has no effect!")
    
    print(str(calculatedDamage))
    return calculatedDamage

def AccuracyCheck(attack):

    hit = False
    hitChance = rando.randint(1, 100)

    if(hitChance <= attack.moveAccuracy):
        hit = True
    else:
        hit = False

    return hit

def Switch(trainerTeam):

    i = 0
    switchSelection = 0
    validSelection = False
    
    while(validSelection != True):
        while(i < len(trainerTeam.team)):
            if(trainerTeam.team[i].currentStatus != "KO"):
                print(str(i + 1) + ". " + trainerTeam.team[i].pkmnName)
                i = i + 1
            else:
                print(str(i + 1) + ". " + trainerTeam.team[i].pkmnName + " - " + trainerTeam.team[i].currentStatus)
                i = i + 1

        switchSelection = int(input("Select the Pokemon you want to switch in: ")) - 1

        if(switchSelection >= len(trainerTeam.team)):
            print("Please make a valid selection!")
        elif(trainerTeam.team[switchSelection].currentStatus == "KO"):
            print("Cannot select a knocked out Pokemon!")
        else:
            tempPoke = trainerTeam.team[switchSelection]
            trainerTeam.team[switchSelection] = trainerTeam.team[0]
            trainerTeam.team[0] = tempPoke
            validSelection = True

def BattleMenu():

    selection = ""
    valid = False

    while(valid == False):
        selection = input("1. Attack\n2. Switch\nSelect an option: ")
        if(selection == "1"):
            valid = True
            return 1
        elif(selection == "2"):
            valid = True
            return 2
        else:
            print("Please selection valid option.")

def AttackMenu(attacker):

    selection = 0
    i = 0
    validSelection = False
    
    while(validSelection == False):
        while(i < len(attacker.moveList)):
            print(str(i + 1) + ". " + attacker.moveList[i].moveName)
            i = i + 1

        selection = input("Please select from the moves listed: ")

        if(int(selection) > len(attacker.moveList)):
            print("Please make a valid selection!")
        else:
            validSelection = True

    return int(selection) - 1
        
def Combat(attacker, move, defender):

    typeChart = TypeMatchup()
    hit = AccuracyCheck(move)

    print(attacker.pkmnName + " used " + move.moveName + "!")
    if(hit == True):
        defender.currentHP = defender.currentHP - Damage(attacker, move, defender)
        if(defender.currentHP <= 0):
            defender.currentStatus = "KO"
            print(attacker.pkmnName + " knocked out " + defender.pkmnName + "!")
    else:
        print(attacker.pkmnName + "'s attack missed!")

def TrainerBattle(player1, player2):

    p1MoveChoice = 0
    p2MoveChoice = 0
    playerChoice = 0
    opponentChoice = 0
    battleEnd = False
    i = 0 

    while(battleEnd != True):

        #Display each players' current Pokemon, HP/MaxHP, and Status
        print(player1.team[0].pkmnName + "  " + str(player1.team[0].currentHP) + "/" + str(player1.team[0].baseHitPoints) + " HP   Status: " + str(player1.team[0].currentStatus))
        print(player2.team[0].pkmnName + "  " + str(player2.team[0].currentHP) + "/" + str(player2.team[0].baseHitPoints) + " HP   Status: " + str(player2.team[0].currentStatus))
        
        #Get player selections for this round
        print("Player 1 please choose an option")
        playerChoice = BattleMenu()
        if(playerChoice == 1):
            p1MoveChoice = AttackMenu(player1.team[0])

        print("Player 2 please choose an option")
        opponentChoice = BattleMenu()
        if(opponentChoice == 1):
            p2MoveChoice = AttackMenu(player2.team[0])

        #Handle Pokemon switching if the players chose to switch
        if(playerChoice == 2):
            Switch(player1)
        if(opponentChoice == 2):
            Switch(player2)
            
        #Battle calculations
        #Player 1 & 2 choose attack
        if(playerChoice == 1 and opponentChoice == 1):
            if(player1.team[0].baseSpeed >= player2.team[0].baseSpeed):
                Combat(player1.team[0], player1.team[0].moveList[p1MoveChoice], player2.team[0])
                if(player2.team[0].currentStatus != "KO"):
                    Combat(player2.team[0], player2.team[0].moveList[p2MoveChoice], player1.team[0])
                    if(player1.team[0].currentStatus == "KO"):
                        battleEnd = endOfBattle(player1)
                        if(battleEnd != True):
                            Switch(player1)
                else:
                    battleEnd = endOfBattle(player2)
                    if(battleEnd != True):
                        Switch(player2)
            else:
                Combat(player2.team[0], player2.team[0].moveList[p2MoveChoice], player1.team[0])
                if(player1.team[0].currentStatus != "KO"):
                    Combat(player1.team[0], player1.team[0].moveList[p1MoveChoice], player2.team[0])
                    if(player2.team[0].currentStatus == "KO"):
                        battleEnd = endOfBattle(player2)
                        if(battleEnd != True):
                            Switch(player2)
                else:
                    battleEnd = endOfBattle(player1)
                    if(battleEnd != True):
                        Switch(player1)

        #Player 1 chose attack, but player 2 chose switch
        elif(playerChoice == 1 and opponentChoice == 2):
            Combat(player1.team[0], player1.team[0].moveList[p1MoveChoice], player2.team[0])
            if(player2.team[0].currentStatus == "KO"):
                battleEnd = endOfBattle(player2)
                if(battleEnd != True):
                    Switch(player2)

        #Player 1 chose switch, but player 2 chose attack
        elif(playerChoice == 2 and opponentChoice == 1):
            Combat(player2.team[0], player2.team[0].moveList[p2MoveChoice], player1.team[0])
            if(player1.team[0].currentStatus == "KO"):
                battleEnd = endOfBattle(player1)
                if(battleEnd != True):
                    Switch(player1)
        
def endOfBattle(playerTeam):
    
    endBattle = False
    numKnocks = 0
    i = 0

    while(i < len(playerTeam.team)):
        if(playerTeam.team[i].currentStatus == "KO"):
            numKnocks += 1
        i += 1

    if(numKnocks >= len(playerTeam.team)):
        endBattle = True

    return endBattle

#Moves
BodySlam = Move("Body Slam", "Normal", "Physical", 85, 100)
PsychoCut = Move("Psycho Cut", "Psychic", "Physical", 70, 100)
Psychic = Move("Psychic", "Psychic", "Special", 90, 100)
ThunderPunch = Move("Thunder Punch", "Electric", "Physical", 75, 100)
FirePunch = Move("Fire Punch", "Fire", "Physical", 75, 100)
IcePunch = Move("Ice Punch", "Ice", "Physical", 75, 100)
Surf = Move("Surf", "Water", "Special", 95, 100)
Thunderbolt = Move("Thunderbolt", "Electric", "Special", 95, 100)
Flamethrower = Move("Flamethrower", "Fire", "Special", 95, 100)
Hyperbeam = Move("Hyperbeam", "Normal", "Special", 150, 100)
Solarbeam = Move("Solarbeam", "Grass", "Special", 120, 100)
CloseCombat = Move("Close Combat", "Fighting", "Physical", 120, 100)
Earthquake = Move("Earthquake", "Ground", "Physical", 100, 100)
SludgeBomb = Move("Sludge Bomb", "Poison", "Special", 90, 100)
WingAttack = Move("Wing Attack", "Flying", "Physical", 60, 100)
RockSlide = Move("Rock Slide", "Rock", "Physical", 75, 90)
SwordsDance = Move("Swords Dance", "Normal", "Status", None, 100)

#Start of program
#layout = [[sg.Text("Pokemon Stadium 3")], [sg.Button("Start")], [sg.Button("Close")]]
#window = sg.Window("Pokemon Stadium 3", layout)

#while True:
#    event, values = window.read()
    # End program if user closes window or
    # presses the Close button
#   if event == "Close" or event == sg.WIN_CLOSED:
#        break
#    elif event == "Start":
#        CharacterMenu()

#window.close()

PokemonRoster()
TrainerRoster()

CharacterMenu()
