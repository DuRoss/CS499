#Farkle game designed by Dustin Ross to be ported from C++ to Python

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
    optionChoice = 0
    countForThree = 0
    remainingDice = 0
    optionCount = 0
    continueScoring = ''
    stillScores = True
    didScore = False
    didRemove = False

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

        #Check if there are any score options available
        if(optionCount < 1):
            if(didScore == False):
                print("Farkle!\n")
                stillScores = False
            else:
                print("There are no remaining valid scoring options.")
                stillScores = False

        #Add on the selected score to the rollTotal and remove the dice
        if(stillScores == True):
            optionChoice = int(input("\nPlease select from the available scoring options: "))
            optionChoice -= 1
            rollTotal += scoreOptions[optionChoice]

            #Remove three dice that show 1 from the dice pool and use didScore to show user scored this roll
            if(scoreOptions[optionChoice] == 1000):
                for i in range(0, len(diceList)):
                    if(diceList[i] == 1 and countForThree < 3):
                        diceList[i] = 0
                        countForThree += 1
                remainingDice -= 3
                didScore = True

            #Remove three dice that show 2 from the dice pool and use didScore to show user scored this roll
            elif(scoreOptions[optionChoice] == 200):
                for i in range(0, len(diceList)):
                    if(diceList[i] == 2 and countForThree < 3):
                        diceList[i] = 0
                        countForThree += 1
                remainingDice -= 3
                didScore = True

            #Remove three dice that show 3 from the dice pool and use didScore to show user scored this roll
            elif(scoreOptions[optionChoice] == 300):
                for i in range(0, len(diceList)):
                    if(diceList[i] == 3 and countForThree < 3):
                        diceList[i] = 0
                        countForThree += 1
                remainingDice -= 3
                didScore = True

            #Remove three dice that show 4 from the dice pool and use didScore to show user scored this roll
            elif(scoreOptions[optionChoice] == 400):
                for i in range(0, len(diceList)):
                    if(diceList[i] == 4 and countForThree < 3):
                        diceList[i] = 0
                        countForThree += 1
                remainingDice -= 3
                didScore = True

            #Remove three dice that show 5 from the dice pool and use didScore to show user scored this roll
            elif(scoreOptions[optionChoice] == 500):
                for i in range(0, len(diceList)):
                    if(diceList[i] == 5 and countForThree < 3):
                        diceList[i] = 0
                        countForThree += 1
                remainingDice -= 3
                didScore = True

            #Remove three dice that show 6 from the dice pool and use didScore to show user scored this roll
            elif(scoreOptions[optionChoice] == 600):
                for i in range(0, len(diceList)):
                    if(diceList[i] == 6 and countForThree < 3):
                        diceList[i] = 0
                        countForThree += 1
                remainingDice -= 3
                didScore = True

            #Remove one die that shows 1 from the dice pool and use didScore to show user scored this roll
            elif(scoreOptions[optionChoice] == 100):
                for i in range(0, len(diceList)):
                    if(diceList[i] == 1 and didRemove == False):
                        diceList[i] = 0
                        didRemove = True
                remainingDice -= 1
                didScore = True

            #Remove one die that shows 1 from the dice pool and use didScore to show user scored this roll
            elif(scoreOptions[optionChoice] == 50):
                for i in range(0, len(diceList)):
                    if(diceList[i] == 5 and didRemove == False):
                        diceList[i] = 0
                        didRemove = True
                remainingDice -= 1
                didScore = True

            continueScoring = input("\nWould you like to continue scoring current dice? (y - yes, n - no): ")

            if(continueScoring == 'y'):
                stillScores = True
            elif(continueScoring == 'n'):
                stillScores = False
            
        #Remove dice changed to 0's to simulate set aside dice
        while(0 in diceList):
              diceList.remove(0)

        #Reset counting variables and clear lists
        scoreOptions.clear()
        optionCount = 0
        countForThree = 0
        didRemove = False
        diceNum = remainingDice

    return rollTotal, diceNum

#Player turn function
def PlayerTurn():
    MAX_DICE_AMOUNT = 6
    currentDiceNum = MAX_DICE_AMOUNT
    rollScore = 0
    turnScore = 0
    continueChoice = ''
    endTurn = False
    diceList = []
    die = Dice(6)

    while(endTurn != True):

        #Roll number of dice equal to available dice
        for i in range(0, currentDiceNum):
            diceList.append(die.RollDie())

        rollScore, currentDiceNum = RollScoring(diceList, currentDiceNum)

        if(rollScore == 0):
            turnScore = 0
            endTurn = True
        else:
            continueChoice = input("\nWould you like to continue rolling? (y - yes, n - no): ")
            if(continueChoice == 'n'):
                turnScore += rollScore
                endTurn = True
            elif(continueChoice == 'y'):
                turnScore += rollScore
                diceList.clear()
            

    return turnScore

#Main game setup function
def FarkleGame():
    
    gameWinner = Player("temp")
    playerList = []
    numPlayersToPlay = 0
    turnPlayer = 0
    finalRoundCounter = 0
    roundCounter = 1
    addedPlayerName = ""
    validInput = False
    gameFinished = False
    finalRound = False

    #Loop to determine the number of players and account for incorrect input
    while(validInput == False):
        
        numPlayersToPlay = int(input("\nPlease enter the number of players for the game: "))

        #Check for valid input
        if(numPlayersToPlay > 0):
            validInput = True
        else:
            print("\nInvalid input! Please enter a number that is more than zero!")

    #Set validInput to False for later use
    validInput = False

    #For loop to get each player's name and add them to the playerList
    for i in range(0, numPlayersToPlay):

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
menuChoice = 0
readRules = ""

#Print welcome message for users starting program
print("Welcome to Farkle!")

#Loop for main menu selections
while(menuChoice != 3):

    #List menu options for the user
    menuChoice = int(input("\n1. Play Farkle\n2. See Rules\n3. Exit Program\n\nPlease select a menu option: "))

    #If statement to perform proper action based on user selection
    if(menuChoice == 1):
        FarkleGame()

    elif(menuChoice == 2):

        #Uses with to open the rules file and close it after the contents are printed
        with open('FarkleRules.txt') as rules:
            readRules = rules.read()
            print(readRules)

    elif(menuChoice == 3):
        print("\nThank you for playing Farkle!")

    else:
        print("\nPlease select a valid option listed above")