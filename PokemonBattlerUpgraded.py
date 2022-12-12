#Started: September 30, 2021
#Last Updated: December 11, 2022
#Author: Dustin Ross

"""
Program Description:
This program is designed to recreate the experience of Pokemon battles in the popular Nintendo game. It recreates 
the experience by mimicking Pokemon and characters from the actual series and letting users take control of them for
battling. In its current state the game uses official moves, Pokemon, and damage calculations along with tactical 
influences like move accuracy and status conditions to create a similar experience to the real world equivalent.
"""

#Imports
import random as rando

#Class Definitions
#Creates a table for reference during damage calculation that is based on the type match ups exhibited in Pokemon games
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
        
    #Returns a damage multiplier based on the type matchup.
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

#Creates a Pokemon class to define multiple Pokemon
#Pokemon consist of a name, type/types, level, base stats for calculation, and a list of four moves to use in battle
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

#Creates trainer class for players to choose from for Pokemon battles
#Trainers are pre-made player characters who command a team of Pokemon in battle
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
    
#Creates a Move class to define multiple moves
#Moves consist of a name, type, contact type to determine if it uses Pokemon attack or special attack stats, power,
#accuracy, a status condition, and a percent chance of inflicting that status condition
class Move:

    def __init__(self, moveName, moveType, contactType, movePower, moveAccuracy, statusCondition, statusPercent):
        self.moveName=moveName
        self.moveType=moveType
        self.contactType=contactType
        self.movePower=movePower
        self.moveAccuracy=moveAccuracy
        self.statusCondition=statusCondition
        self.statusPercent=statusPercent

    def __repr__(self):
        return ("I am " + self.moveName + " with a type of " + self.moveType
                + " a contact type of " + self.contactType + " a power of "
                + str(self.movePower) + " and an accuracy of " + str(self.moveAccuracy))

#Changed Pokemon declarations to a roster for potentially allowing the user to create their own team in the future
class PokemonRoster:

    roster = []
    #Creates a roster of Pokemon in the game that are accessible through their roster slot
    #Sorted by National Dex number as definied by official Pokemon video games
    def __init__(self):
        self.roster.append(Pokemon("Venusaur", "Grass", "Poison", 50, 80, 82, 83, 100, 100, 80, Solarbeam, Earthquake, PoisonPowder, SludgeBomb))
        self.roster.append(Pokemon("Charizard", "Fire", "Flying", 50, 78, 84, 78, 109, 85, 100, Flamethrower, Solarbeam, WingAttack, Earthquake))
        self.roster.append(Pokemon("Blastoise", "Water", None, 50, 79, 83, 100, 85, 105, 78, Surf, Earthquake, BodySlam, IcePunch))
        self.roster.append(Pokemon("Pikachu", "Electric", None, 50, 35, 55, 40, 50, 50, 90, Thunderbolt, Surf, BodySlam, ThunderWave))
        self.roster.append(Pokemon("Raichu", "Electric", None, 50, 60, 90, 55, 90, 80, 110, Thunderbolt, Surf, BodySlam, ThunderWave))
        self.roster.append(Pokemon("Nidoqueen", "Poison", "Ground", 50, 90, 92, 87, 75, 85, 76, Earthquake, Thunderbolt, BodySlam, SludgeBomb))
        self.roster.append(Pokemon("Clefable", "Fairy", None, 50, 95, 70, 73, 95, 90, 60, BodySlam, Thunderbolt, Earthquake, FirePunch))
        self.roster.append(Pokemon("Wigglytuff", "Normal", "Fairy", 50, 140, 70, 45, 85, 50, 45, BodySlam, IcePunch, FirePunch, ThunderPunch))
        self.roster.append(Pokemon("Golduck", "Water", "Psychic", 50, 80, 82, 78, 95, 80, 85, Surf, Thunderbolt, Psychic, ThunderWave))
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
        self.roster.append(Pokemon("Butterfree", "Psychic", "Flying", 50, 60, 45, 50, 90, 80, 70, Psychic, StunSpore, PoisonPowder, SleepPowder))

#Changed Trainer declarations to a roster
class TrainerRoster:

    roster = []

    #Trainers are characters taken from the official manga based on the games
    def __init__(self):
        self.roster.append(Trainer("Leon", PokemonRoster.roster[22], PokemonRoster.roster[24], PokemonRoster.roster[4], PokemonRoster.roster[16], PokemonRoster.roster[17], PokemonRoster.roster[18]))
        self.roster.append(Trainer("Red", PokemonRoster.roster[9], PokemonRoster.roster[0], PokemonRoster.roster[3], PokemonRoster.roster[12], PokemonRoster.roster[14], PokemonRoster.roster[15]))
        self.roster.append(Trainer("Blue", PokemonRoster.roster[20], PokemonRoster.roster[1], PokemonRoster.roster[8], PokemonRoster.roster[10], PokemonRoster.roster[21], PokemonRoster.roster[11]))
        self.roster.append(Trainer("Green", PokemonRoster.roster[7], PokemonRoster.roster[2], PokemonRoster.roster[13], PokemonRoster.roster[6], PokemonRoster.roster[5], PokemonRoster.roster[19]))
         
#Function Definitions
#Runs through the player and opponent character selection process to reduce redundancy
def TrainerSelect():
    
    trainerChoice = ''
    trainerSelect = False
    selectedTrainer = None
    validInput = False
    i = 0

    #Loop until both players have made valid trainer selections
    while(trainerSelect != True):

        #Prints the list of available trainers for players to select from
        while(i < len(TrainerRoster.roster)):
            print(str(i+1) + " " + TrainerRoster.roster[i].trainerName)
            i += 1

        #Gets the active player's trainer choice and validates the input
        while(validInput != True):

            #Get trainer choice from the player
            trainerChoice = input("Please select your trainer: ")

            #If a valid choice is made sets the selectedTrainer to the player's choice
            if(trainerChoice.isnumeric() == True):
                if(int(trainerChoice)-1 < len(TrainerRoster.roster)):
                    selectedTrainer = TrainerRoster.roster[int(trainerChoice)-1]
                    trainerSelect = True
                    validInput = True
                else:
                    print("Please select an option listed.")
            else:
                print("Invalid selection! Please enter a number for the corresponding trainer.")

    #Return trainer based on validated user selection
    return selectedTrainer

#Displays a menu of trainers for players to select from
def CharacterMenu():
    
    playerTrainer = None
    opponentTrainer = None

    #Uses TrainerSelect to set the trainer for each player
    playerTrainer = TrainerSelect()
    opponentTrainer = TrainerSelect()
        
    #Allow each player select their team order before beginning the Trainer Battle
    playerTrainer.team = PokemonSelect(playerTrainer)
    opponentTrainer.team = PokemonSelect(opponentTrainer)
    TrainerBattle(playerTrainer, opponentTrainer)

#Allows the player to select the order of their Pokemon before entering battle
def PokemonSelect(trainerTeam):

    currentOrder = []
    selection = ''
    validInput = False
    passes = 0
    i = 0

    #Print a message instructing the user to select the order that their trainer's team will appear in
    print("\nSelect team order")

    #Passes through the trainer's team six times to allow individual selections for each Pokemon on the team
    while(passes < 6):

        #Print a list of remaining Pokemon for the next team slot
        while(i < len(trainerTeam.team)):
            print(str(i + 1) + ". " + trainerTeam.team[i].pkmnName)
            i = i + 1

        #Gets the selection for the next team slot from the user and validates it as good input
        while(validInput != True):
            selection = input("Select number for next Pokemon: ")
            if(selection.isnumeric() == True):
                if((int(selection) - 1) < len(trainerTeam.team)):
                    currentOrder.append(trainerTeam.team[int(selection) - 1])
                    trainerTeam.team.pop(int(selection) - 1)
                    i = 0
                    passes = passes + 1
                    validInput = True
                else:
                    print("Invalid selection! Please select a number corresponding to a Pokemon.")
            else:
                print("Invalid selection! Please select a number corresponding to a Pokemon.")

        #Set validInput to False to prepare for next pass and selection to an empty string
        validInput = False

    #Print a newline and the order that the player selected for their team
    print()
    while(i < len(currentOrder)):
        print(str(i + 1) + ". " + currentOrder[i].pkmnName)
        i = i + 1

    return currentOrder
    
#Used to calculate damage during battle
def Damage(attacker, attackMove, defender):

    typeChart = TypeMatchup()

    #Damage Function variables
    calculatedDamage = 0
    critChance = rando.randint(1, 100)
    statusChance = rando.randint(1,100)
    typeEffectiveness = 0.0

    #Determine if the attack move should use the attacker's attack or special attack
    if(attackMove.contactType == "Physical"):
        calculatedDamage = (((((2*attacker.pkmnLevel)/5)+2)*attackMove.movePower*(attacker.baseAttack/defender.baseDefense))/50+2)
    elif(attackMove.contactType == "Special"):
        calculatedDamage = (((((2*attacker.pkmnLevel)/5)+2)*attackMove.movePower*(attacker.baseSpAttack/defender.baseSpDefense))/50+2)

    #Check for critical hit
    if(critChance >= 94):
        calculatedDamage = calculatedDamage * 1.5
        print("Critical Hit!")
        
    #Check for same type attack bonus if attacker and move are of the same type
    if(attacker.pkmnType1 == attackMove.moveType or attacker.pkmnType2 == attackMove.moveType):
        calculatedDamage = calculatedDamage * 1.5

    #Check for move effectiveness based on the type matchup table
    typeEffectiveness = typeChart.getMatchup(attackMove.moveType.upper(), defender.pkmnType1.upper())
    if(defender.pkmnType2 != None):
        typeEffectiveness = typeEffectiveness * typeChart.getMatchup(attackMove.moveType.upper(), defender.pkmnType2.upper())
    calculatedDamage = calculatedDamage * typeEffectiveness

    #Print a message informing the player of the effectiveness of their selected move
    if(typeEffectiveness >= 2 and attackMove.contactType != "Status"):
        print("It's super-effective!")
    elif(typeEffectiveness > 0 and typeEffectiveness <= 0.5 and attackMove.contactType != "Status"):
        print("It's not very effective!")
    elif(typeEffectiveness == 0):
        print("It has no effect!")

    #Check if the attacker is burned and using a physical attack, and if they are cut the final damage in half
    if(attacker.currentStatus == "BRN" and attackMove.contactType == "Physical"):
        calculatedDamage = calculatedDamage / 2

    #Check for status condition on attacking move, generate random number based on statusPercent, and apply status if successful
    if(typeEffectiveness != 0 and attackMove.statusCondition != None and defender.currentStatus == None):
        if(statusChance <= attackMove.statusPercent):
            defender.currentStatus = attackMove.statusCondition
            if(defender.currentStatus == "PAR"):
                print(defender.pkmnName + " was paralyzed!")
            if(defender.currentStatus == "BRN"):
                print(defender.pkmnName + " was burned!")
            if(defender.currentStatus == "FRZ"):
                print(defender.pkmnName + " was frozen!")
            if(defender.currentStatus == "PSN"):
                print(defender.pkmnName + " was poisoned!")
            if(defender.currentStatus == "SLP"):
                print(defender.pkmnName + " was put to sleep!")
    
    #Newline for readability and return the total damage calculated
    print()
    return calculatedDamage

#Checks to see if a move lands
def AccuracyCheck(attack):

    hit = False
    hitChance = rando.randint(1, 100)

    #Uses the randomly generated hitChance to determine if the hitChance falls below the move's accuracy and causes a miss
    if(hitChance <= attack.moveAccuracy):
        hit = True
    else:
        hit = False

    #Return whether the attack was a successful hit or a failure
    return hit

#Allows players to switch the active member to a non-knocked out member
def Switch(trainerTeam):

    i = 0
    switchSelection = ''
    validSelection = False
    
    #List out the player's current Pokemon and their status's, and validate that they select a valid switch option
    while(validSelection != True):
        while(i < len(trainerTeam.team)):
            if(trainerTeam.team[i].currentStatus == None):
                print(str(i + 1) + ". " + trainerTeam.team[i].pkmnName)
                i = i + 1
            else:
                print(str(i + 1) + ". " + trainerTeam.team[i].pkmnName + " - " + trainerTeam.team[i].currentStatus)
                i = i + 1

        switchSelection = input("Select the Pokemon you want to switch in: ")

        #Validate that the switchSelection is a number to avoid crashes
        if(switchSelection.isnumeric() == True):
            #Inform user if they make a selection that is invalid or cannot be switched in
            if(int(switchSelection) >= len(trainerTeam.team)):
                print("Please make a valid selection!")
            elif(trainerTeam.team[int(switchSelection)].currentStatus == "KO"):
                print("Cannot select a knocked out Pokemon!")
            else:
                #Swap the switching Pokemon's place in team order with the Pokemon to be switched in
                tempPoke = trainerTeam.team[int(switchSelection)]
                trainerTeam.team[int(switchSelection)] = trainerTeam.team[0]
                trainerTeam.team[0] = tempPoke
                validSelection = True
        else:
            print("Invalid selection! Please select a number corresponding to a Pokemon listed.")

#Menu to let players choose to attack or switch
def BattleMenu():

    selection = ""
    valid = False

    #Checks that the active player makes a valid selection and performs the requested action
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

#Display active Pokemon's attacks for players to choose from
def AttackMenu(attacker):

    selection = ''
    i = 0
    validSelection = False
    
    #List the active Pokemon's available attacks
    while(validSelection == False):
        while(i < len(attacker.moveList)):
            print(str(i + 1) + ". " + attacker.moveList[i].moveName)
            i = i + 1

        #Receive the user's selected move and validate the selection
        selection = input("Please select from the moves listed: ")

        if(selection.isnumeric() == True):
            if(int(selection) > len(attacker.moveList)):
                print("Please make a valid selection!")
            else:
                validSelection = True
        else:
            print("Invalid input! Please select a number corresponding to an attack as listed.")

    #Return the selected attack as an int to use for indexing
    return int(selection) - 1
        
#Simulates combat between the two active Pokemon
def Combat(attacker, move, defender):

    typeChart = TypeMatchup()
    hit = AccuracyCheck(move)
    moveChance = rando.randint(1, 100)
    canMove = False

    #Determine if the Pokemon can move based on current status
    if(attacker.currentStatus == "SLP"): 

        #Determine if the Pokemon wakes up from their sleep
        if(moveChance <= 50):
            canMove = False
        else:
            print(attacker.pkmnName + " woke up!")
            attacker.currentStatus = None
            canMove = True

    elif(attacker.currentStatus == "PAR"):

        #Determine if the user is unable to move due to paralysis
        if(moveChance <= 25):
            canMove = False
        else:
            canMove = True

    elif(attacker.currentStatus == "FRZ"):

        #Determine if the user thaws from their frozen state or not
        if(moveChance <= 20):
            canMove = False
        else:
            print(attacker.pkmnName + " thawed out!")
            attacker.currentStatus = None
            canMove = True

    else:
        canMove = True

    #Perform the move that the player selected if the Pokemon can move
    if(canMove == True):
        print(attacker.pkmnName + " used " + move.moveName + "!")
        if(hit == True):
            defender.currentHP = defender.currentHP - Damage(attacker, move, defender)
            if(defender.currentHP <= 0):
                defender.currentStatus = "KO"
                print(attacker.pkmnName + " knocked out " + defender.pkmnName + "!")
        else:
            print(attacker.pkmnName + "'s attack missed!")

    #If user can not move print a status alerting the player as to why it could not move
    else:
        if(attacker.currentStatus == "SLP"):
            print(attacker.pkmnName + " is fast asleep!")
        elif(attacker.currentStatus == "PAR"):
            print(attacker.pkmnName + " can't move due to paralysis!")
        elif(attacker.currentStatus == "FRZ"):
            print(attacker.pkmnName + " is frozen and can't move!")

#Where player menu selections take place while they do battle
def TrainerBattle(player1, player2):

    p1MoveChoice = 0
    p2MoveChoice = 0
    playerChoice = 0
    opponentChoice = 0
    speedTieBreaker = rando.randint(1, 2)
    battleEnd = False

    #Loops until the battle has come to an end
    while(battleEnd != True):

        #Display each players' current Pokemon, HP/MaxHP, and Status
        print(player1.team[0].pkmnName + "  " + str(player1.team[0].currentHP) + "/" + str(player1.team[0].baseHitPoints) + " HP   Status: " + str(player1.team[0].currentStatus))
        print(player2.team[0].pkmnName + "  " + str(player2.team[0].currentHP) + "/" + str(player2.team[0].baseHitPoints) + " HP   Status: " + str(player2.team[0].currentStatus))
        
        #Get player selections for this round
        print("\nPlayer 1 please choose an option")
        playerChoice = BattleMenu()
        if(playerChoice == 1):
            p1MoveChoice = AttackMenu(player1.team[0])

        print("\nPlayer 2 please choose an option")
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

            #If player 1's active Pokemon has a higher speed than player 2's, player 1 moves first
            if(player1.team[0].baseSpeed > player2.team[0].baseSpeed):
                Combat(player1.team[0], player1.team[0].moveList[p1MoveChoice], player2.team[0])

                #Checks if player 2's Pokemon has been knocked out before continuing combat
                if(player2.team[0].currentStatus != "KO"):
                    Combat(player2.team[0], player2.team[0].moveList[p2MoveChoice], player1.team[0])

                    #If player 1's Pokemon has been knocked out check for the end of battle, and if they still have remaining Pokemon force a switch
                    if(player1.team[0].currentStatus == "KO"):
                        battleEnd = endOfBattle(player1)
                        if(battleEnd != True):
                            Switch(player1)
                
                #If player 2's Pokemon has been knocked out check for the end of battle, and if they still have remaining Pokemon force a switch
                else:
                    battleEnd = endOfBattle(player2)
                    if(battleEnd != True):
                        Switch(player2)

            #If player 2's active Pokemon has higher speed than player 1's player 2 moves first
            elif(player2.team[0].baseSpeed > player1.team[0].baseSpeed):
                Combat(player2.team[0], player2.team[0].moveList[p2MoveChoice], player1.team[0])

                #Checks if player 1's Pokemon has been knocked out before continuing combat
                if(player1.team[0].currentStatus != "KO"):
                    Combat(player1.team[0], player1.team[0].moveList[p1MoveChoice], player2.team[0])

                    #If player 2's Pokemon has been knocked out check for the end of battle, and if they still have remaining Pokemon force a switch
                    if(player2.team[0].currentStatus == "KO"):
                        battleEnd = endOfBattle(player2)
                        if(battleEnd != True):
                            Switch(player2)

                #If player 1's Pokemon has been knocked out check for the end of battle, and if they still have remaining Pokemon force a switch
                else:
                    battleEnd = endOfBattle(player1)
                    if(battleEnd != True):
                        Switch(player1)

            #Uses the speedTieBreak to simulate a coin flip and determine who goes first when the active speed stat is tied
            else:

                #If speedTieBreak is one, proceed with player 1 moving first
                if(speedTieBreaker == 1):
                    Combat(player1.team[0], player1.team[0].moveList[p1MoveChoice], player2.team[0])
                    if(player2.team[0].currentStatus != "KO"):
                        Combat(player2.team[0], player2.team[0].moveList[p2MoveChoice], player1.team[0])
                        if(player1.team[0].currentStatus == "KO"):
                            battleEnd = endOfBattle(player1)
                            if(battleEnd != True):
                                Switch(player1)

                #If speedTieBreak is one, proceed with player 2 moving first
                else:
                    Combat(player2.team[0], player2.team[0].moveList[p2MoveChoice], player1.team[0])
                    if(player1.team[0].currentStatus != "KO"):
                        Combat(player1.team[0], player1.team[0].moveList[p1MoveChoice], player2.team[0])
                        if(player2.team[0].currentStatus == "KO"):
                            battleEnd = endOfBattle(player2)
                            if(battleEnd != True):
                                Switch(player2)

        #Player 1 chose attack, but player 2 chose switch, perform player 1's attack on the switched in Pokemon
        elif(playerChoice == 1 and opponentChoice == 2):
            Combat(player1.team[0], player1.team[0].moveList[p1MoveChoice], player2.team[0])
            if(player2.team[0].currentStatus == "KO"):
                battleEnd = endOfBattle(player2)
                if(battleEnd != True):
                    Switch(player2)

        #Player 1 chose switch, but player 2 chose attack, perform player 1's attack on the switched in Pokemon
        elif(playerChoice == 2 and opponentChoice == 1):
            Combat(player2.team[0], player2.team[0].moveList[p2MoveChoice], player1.team[0])
            if(player1.team[0].currentStatus == "KO"):
                battleEnd = endOfBattle(player1)
                if(battleEnd != True):
                    Switch(player1)

        #Check for poison and burn status, apply damage, and check for KO for player1's active pokemon
        if(player1.team[0].currentStatus == "PSN" or player1.team[0].currentStatus == "BRN"):
            player1.team[0].currentHP = player1.team[0].currentHP - (player1.team[0].baseHitPoints/8)
            if(player1.team[0].currentStatus == "PSN"):
                print(player1.team[0].pkmnName + " was damaged by poison!")
            if(player1.team[0].currentStatus == "BRN"):
                print(player1.team[0].pkmnName + " was damaged by its burn!")
            if(player1.team[0].currentHP <= 0):
                player1.team[0].currentStatus = "KO"
                print(player1.team[0].pkmnName + " fainted!")
                Switch(player1)

        #Check for poison and burn status, apply damage, and check for KO for player2's active pokemon
        if(player2.team[0].currentStatus == "PSN" or player2.team[0].currentStatus == "BRN"):
            player2.team[0].currentHP = player2.team[0].currentHP - (player2.team[0].baseHitPoints/8)
            if(player2.team[0].currentStatus == "PSN"):
                print(player2.team[0].pkmnName + " was damaged by poison!")
            if(player2.team[0].currentStatus == "BRN"):
                print(player2.team[0].pkmnName + " was damaged by its burn!")
            if(player2.team[0].currentHP <= 0):
                player2.team[0].currentStatus = "KO"
                print(player2.team[0].pkmnName + " fainted!")
                Switch(player2)
        
#Checks if battle should
def endOfBattle(playerTeam):
    
    endBattle = False
    numKnocks = 0
    i = 0

    #Counts the number of knocked out Pokemon on the passed player's team
    while(i < len(playerTeam.team)):
        if(playerTeam.team[i].currentStatus == "KO"):
            numKnocks += 1
        i += 1

    #If the number of knocked out Pokemon is equal to the whole team, end the battle
    if(numKnocks >= len(playerTeam.team)):
        endBattle = True

    return endBattle

#Moves that are currently available
BodySlam = Move("Body Slam", "Normal", "Physical", 85, 100, "PAR", 30)
PsychoCut = Move("Psycho Cut", "Psychic", "Physical", 70, 100, None, 0)
Psychic = Move("Psychic", "Psychic", "Special", 90, 100, None, 0)
ThunderPunch = Move("Thunder Punch", "Electric", "Physical", 75, 100, "PAR", 10)
FirePunch = Move("Fire Punch", "Fire", "Physical", 75, 100, "BRN", 10)
IcePunch = Move("Ice Punch", "Ice", "Physical", 75, 100, "FRZ", 10)
Surf = Move("Surf", "Water", "Special", 95, 100, None, 0)
Thunderbolt = Move("Thunderbolt", "Electric", "Special", 95, 100, "PAR", 10)
Flamethrower = Move("Flamethrower", "Fire", "Special", 95, 100, "BRN", 10)
IceBeam = Move("Ice Beam", "Ice", "Special", 90, 100, "FRZ", 10)
Hyperbeam = Move("Hyperbeam", "Normal", "Special", 150, 100, None, 0)
Solarbeam = Move("Solarbeam", "Grass", "Special", 120, 100, None, 0)
CloseCombat = Move("Close Combat", "Fighting", "Physical", 120, 100, None, 0)
Earthquake = Move("Earthquake", "Ground", "Physical", 100, 100, None, 0)
SludgeBomb = Move("Sludge Bomb", "Poison", "Special", 90, 100, "PSN", 0)
WingAttack = Move("Wing Attack", "Flying", "Physical", 60, 100, None, 0)
RockSlide = Move("Rock Slide", "Rock", "Physical", 75, 90, None, 0)
ThunderWave = Move("Thunder Wave", "Electric", "Status", 0, 90, "PAR", 100)
PoisonPowder = Move("Poison Powder", "Poison", "Status", 0, 75, "PSN", 100)
SleepPowder = Move("Sleep Powder", "Grass", "Status", 0, 75, "SLP", 100)
StunSpore = Move("Stun Spore", "Grass", "Status", 0, 75, "PAR", 100)

#Start of program

PokemonRoster()
TrainerRoster()

#Print welcome message and display character menu
print("Welcome to the Pokemon Battler!\n")
CharacterMenu()