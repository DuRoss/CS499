"""
Farkle game designed by Dustin Ross to be ported from C++ to Python

Program Description:
This program was designed to mimic the dice game Farkle. The game allows users to enter their names
and roll and score dice in a race to reach 10,000 points. The RollScoring function assists the 
scoring of the game by listing the potential scoring options for users and allowing them to choose
from these. This also cuts down on potential user error in selecting and using multiple dice. The 
program also has an option for listing the Farkle rules for first time players and uses prompts to
help guide them through the experience.
"""

#Imports
import random as rando

#Class Definitions
#Player class to keep track of player names and scores
class Player():
    playerName = ""
    currentScore = 0

    def __init__ (self, name):
        self.playerName = name

#Dice class for rolling dice during game
class Dice():

    numSides = 0

    def __init__ (self, sides):
        self.numSides = sides

    def RollDie(self):
        return rando.randint(1, self.numSides)
    
#Function Definitions
#Takes the current rolls from the player's turn and assists with scoring and removing dice
def RollScoring(diceList, diceNum):
    scoreOptions = []
    rollTotal = 0
    countForThree = 0
    remainingDice = 0
    optionCount = 0
    optionSelection = 0
    continueScoring = ''
    optionChoice = ''
    stillScores = True
    didScore = False
    didRemove = False
    validInput = False

    #Set remainingDice equal to the number of dice passed
    remainingDice = len(diceList)

    #Loop until there are no score options left or the user chooses to stop
    while(stillScores == True):

        #Print remaining dice for user
        for i in range(0, len(diceList)):
            print(str(diceList[i]) + ", ", end= "")

        #Print newline for readability
        print("\n")

        #Check for potential 1,000 points
        if(diceList.count(1) >= 3):
            optionCount += 1
            scoreOptions.append(1000)
            print(str(optionCount) + ": 1, 1, 1 = 1,000 points")

        #Check for potential 200 points
        if(diceList.count(2) >= 3):
            optionCount += 1
            scoreOptions.append(200)
            print(str(optionCount) + ": 2, 2, 2 = 200 points")

        #Check for potential 300 points
        if(diceList.count(3) >= 3):
            optionCount += 1
            scoreOptions.append(300)
            print(str(optionCount) + ": 3, 3, 3 = 300 points")

        #Check for potential 400 points
        if(diceList.count(4) >= 3):
            optionCount += 1
            scoreOptions.append(400)
            print(str(optionCount) + ": 4, 4, 4 = 400 points")

        #Check for potential 500 points
        if(diceList.count(5) >= 3):
            optionCount += 1
            scoreOptions.append(500)
            print(str(optionCount) + ": 5, 5, 5 = 500 points")

        #Check for potential 600 points
        if(diceList.count(6) >= 3):
            optionCount += 1
            scoreOptions.append(600)
            print(str(optionCount) + ": 6, 6, 6 = 600 points")

        #Check for potential 100 points
        if(diceList.count(1) >= 1):
            optionCount += 1
            scoreOptions.append(100)
            print(str(optionCount) + ": 1 = 100 points")

        #Check for potential 50 points
        if(diceList.count(5) >= 1):
            optionCount += 1
            scoreOptions.append(50)
            print(str(optionCount) + ": 5 = 50 points")

        #Check if there are any score options available, and determine if Farkle or all possible dice are used
        if(optionCount < 1):
            if(didScore == False):
                print("Farkle!\n")
                stillScores = False
            else:
                print("There are no remaining valid scoring options.")
                stillScores = False

        #Add on the selected score to the rollTotal and remove the dice
        if(stillScores == True):
            #Loop to ensure user selects a valid option
            while(validInput == False):
                optionChoice = input("\nPlease select from the available scoring options: ")

                #Checks if user choice is numeric before converting it to an int for index use
                if(optionChoice.isnumeric() == True):

                    #Converts optionChoice to the int optionSelection for index use purposes, and checks if it is a valid selection
                    optionSelection = int(optionChoice)
                    if(optionSelection > 0 and optionSelection <= len(scoreOptions)):
                        optionSelection -= 1
                        rollTotal += scoreOptions[optionSelection]
                        validInput = True
                    else:
                        print("Invalid selection! Please select a scoring option listed.")
                else:
                    print("Invalid selection! Please select a scoring option listed.")

            #Set validInput back to False for future use
            validInput = False

            #Condition statement to remove appropriate dice, and set didScore to True for the roll
            #Remove three dice that show 1 from the dice pool and use didScore to show user scored this roll
            if(scoreOptions[optionSelection] == 1000):
                for i in range(0, len(diceList)):
                    if(diceList[i] == 1 and countForThree < 3):
                        diceList[i] = 0
                        countForThree += 1
                remainingDice -= 3
                didScore = True

            #Remove three dice that show 2 from the dice pool and use didScore to show user scored this roll
            elif(scoreOptions[optionSelection] == 200):
                for i in range(0, len(diceList)):
                    if(diceList[i] == 2 and countForThree < 3):
                        diceList[i] = 0
                        countForThree += 1
                remainingDice -= 3
                didScore = True

            #Remove three dice that show 3 from the dice pool and use didScore to show user scored this roll
            elif(scoreOptions[optionSelection] == 300):
                for i in range(0, len(diceList)):
                    if(diceList[i] == 3 and countForThree < 3):
                        diceList[i] = 0
                        countForThree += 1
                remainingDice -= 3
                didScore = True

            #Remove three dice that show 4 from the dice pool and use didScore to show user scored this roll
            elif(scoreOptions[optionSelection] == 400):
                for i in range(0, len(diceList)):
                    if(diceList[i] == 4 and countForThree < 3):
                        diceList[i] = 0
                        countForThree += 1
                remainingDice -= 3
                didScore = True

            #Remove three dice that show 5 from the dice pool and use didScore to show user scored this roll
            elif(scoreOptions[optionSelection] == 500):
                for i in range(0, len(diceList)):
                    if(diceList[i] == 5 and countForThree < 3):
                        diceList[i] = 0
                        countForThree += 1
                remainingDice -= 3
                didScore = True

            #Remove three dice that show 6 from the dice pool and use didScore to show user scored this roll
            elif(scoreOptions[optionSelection] == 600):
                for i in range(0, len(diceList)):
                    if(diceList[i] == 6 and countForThree < 3):
                        diceList[i] = 0
                        countForThree += 1
                remainingDice -= 3
                didScore = True

            #Remove one die that shows 1 from the dice pool and use didScore to show user scored this roll
            elif(scoreOptions[optionSelection] == 100):
                for i in range(0, len(diceList)):
                    if(diceList[i] == 1 and didRemove == False):
                        diceList[i] = 0
                        didRemove = True
                remainingDice -= 1
                didScore = True

            #Remove one die that shows 1 from the dice pool and use didScore to show user scored this roll
            elif(scoreOptions[optionSelection] == 50):
                for i in range(0, len(diceList)):
                    if(diceList[i] == 5 and didRemove == False):
                        diceList[i] = 0
                        didRemove = True
                remainingDice -= 1
                didScore = True

            #Confirm if user would like to set aside more dice and ensure valid input
            while(validInput == False):
                continueScoring = input("\nWould you like to continue scoring current dice? (y - yes, n - no): ")
                if(continueScoring == 'y'):
                    stillScores = True
                    validInput = True
                elif(continueScoring == 'n'):
                    stillScores = False
                    validInput = True
                else:
                    print("Invalid input! Please enter y for yes or n for no.")
            
        #Remove dice changed to 0's to simulate set aside dice
        while(0 in diceList):
              diceList.remove(0)

        #Reset counting variables, clear lists, and set validating booleans back to False
        scoreOptions.clear()
        optionCount = 0
        countForThree = 0
        didRemove = False
        validInput = False
        diceNum = remainingDice

    #Return the score for the roll and the remaining dice to roll
    return rollTotal, diceNum

#Runs the turn for active player by rolling dice, calling the RollScoring function, and ending the turn when appropriate
def PlayerTurn():

    MAX_DICE_AMOUNT = 6
    currentDiceNum = MAX_DICE_AMOUNT
    rollScore = 0
    turnScore = 0
    continueChoice = ''
    endTurn = False
    validInput = False
    diceList = []
    die = Dice(6)

    #Loop until the user's turn has ended, either through choice or a forced end through a Farkle
    while(endTurn != True):

        #Roll number of dice equal to available dice
        for i in range(0, currentDiceNum):
            diceList.append(die.RollDie())

        #Send the list of dice for the roll to the RollScoring function, and return the score choices and unused dice number
        rollScore, currentDiceNum = RollScoring(diceList, currentDiceNum)

        #Condition statement that forces end of turn if a Farkle occurs, or offers the turn player the chance to continue rolling
        if(rollScore == 0):
            turnScore = 0
            endTurn = True
        else:
            #Loops section until user provides proper input
            while(validInput == False):
                continueChoice = input("\nWould you like to continue rolling? (y - yes, n - no): ")
                if(continueChoice == 'n'):
                    turnScore += rollScore
                    endTurn = True
                    validInput = True
                elif(continueChoice == 'y'):
                    turnScore += rollScore
                    diceList.clear()
                    validInput = True
                else:
                    print("Invalid input! Please enter y for yes or n for no.")
            
            #Set validInput to false for future looping
            validInput = False
            
    #Return the player's score for the turn
    return turnScore

#Main game setup function, this function creates the list of players and handles the turn/round tracking and monitors for a winning score
def FarkleGame():
    
    gameWinner = Player("temp")
    playerList = []
    numPlayersToPlay = ''
    turnPlayer = 0
    finalRoundCounter = 0
    roundCounter = 1
    addedPlayerName = ""
    validInput = False
    gameFinished = False
    finalRound = False

    #Loop to determine the number of players and account for incorrect input
    while(validInput == False):

        numPlayersToPlay = input("\nPlease enter the number of players for the game: ")

        #Check if user input is a number before attempting to use as an int
        if(numPlayersToPlay.isnumeric()) == True:

            #Check for valid input
            if(int(numPlayersToPlay) > 0):
                validInput = True
            else:
                print("\nInvalid input! Please enter a number that is more than zero.")

        else:
            print("\nInvalid input! Please enter a number that is more than zero.")

    #Set validInput to False for later use
    validInput = False

    #For loop to get each player's name and add them to the playerList
    for i in range(0, int(numPlayersToPlay)):

        addedPlayerName = input("Please enter player " + str(i + 1) + "'s name: ")
        playerList.append(Player(addedPlayerName))

    print("\nIt is now round 1!")

    #Loop until the game is finished
    while(gameFinished != True):

        #Print message listing the players and their current scores
        for i in range(0, len(playerList)):
            print(playerList[i].playerName + ": " + str(playerList[i].currentScore))

        print("\nIt is now " + playerList[turnPlayer].playerName + "'s turn!")
        
        #Call PlayerTurn function and set the turn player's score equal to the return value
        playerList[turnPlayer].currentScore += PlayerTurn()

        #REMEMBER CHANGE BACK TO 10000 WHEN DONE WITH TESTING
        if(playerList[turnPlayer].currentScore >= 10000 and finalRound == False):
            gameWinner = playerList[turnPlayer]
            finalRound = True
            print("\n" + gameWinner.playerName + " has passed 10,000 points! It is now the final round!")
            
        #Check if it is the final round
        if(finalRound == True):

            #Check if turn player has surpassed current winner
            if(playerList[turnPlayer].currentScore >= gameWinner.currentScore):
                gameWinner = playerList[turnPlayer]

            finalRoundCounter += 1

            #If every player has gotten a turn in the final round, bring the game to an end
            if(finalRoundCounter == len(playerList)):
                gameFinished = True

        #Increment the turn player to begin the next player's turn, or start a new round if it is the final player's turn
        turnPlayer += 1

        if(turnPlayer == numPlayersToPlay and gameFinished == False):
            turnPlayer = 0
            roundCounter += 1
            print("\nIt is now round " + str(roundCounter) + "!\nThe current scores are:")

    #Print message declaring game winner and congratulate them
    print("\nCongratulations " + gameWinner.playerName + "!\n\nFinal Scores:")
    for i in range(0, len(playerList)):
        print(playerList[i].playerName + ": " + str(playerList[i].currentScore))
                 
#START OF PROGRAM
menuChoice = ''
readRules = ""

#Print welcome message for users starting program
print("Welcome to Farkle!")

#Loop for main menu selections
while(menuChoice != '3'):

    #List menu options for the user
    menuChoice = input("\n1. Play Farkle\n2. See Rules\n3. Exit Program\n\nPlease select a menu option: ")

    #If statement to perform proper action based on user selection
    #Begins the main Farkle game
    if(menuChoice == '1'):
        FarkleGame()

    #Prints rules of the game for users who are unfamiliar
    elif(menuChoice == '2'):

        #Uses with to open the rules file and close it after the contents are printed
        with open('FarkleRules.txt') as rules:
            readRules = rules.read()
            print(readRules)

    #Exits the program
    elif(menuChoice == '3'):
        print("\nThank you for playing Farkle!")

    #Accounts for potential incorrect input from the user
    else:
        print("\nPlease select a valid option listed above")