/*
* Name: Dustin Ross
* Course: IT-312
* Date: 10/13/2022
* Project Number: 7-1
*/


#include <cstdlib>
#include <iostream>
#include <fstream>
#include <time.h>
#include <vector>
using namespace std;

// Player class to keep track of player name and score
class Player {

	public:
		string playerName = "";
		int currentScore = 0;

	// Constructor
	Player() {

	}

	// Pair of void methods to set name and score
	void SetName(string name) {
		playerName = name;
	}

	void SetScore(int score) {
		currentScore = score;
	}

	// Pair of methods to return name and score
	string GetName() {
		return playerName;
	}

	int GetScore() {
		return currentScore;
	}
};

// Dice class to have dice act as rollable objects
class Dice {
	
	public:
		int result = 0;

	Dice() {

	}

	int RollDie() {

		// Seed random with time plus a random number to avoid the same result showing up each roll
		srand(time(0) + rand());

		// Roll the die and set the return value to the result
		result = (rand() % 6 + 1);
		return result;
	}
};

// Function to give user scoring options for this roll
void RollScoring(vector <int> rolledDice, int *pdiceToRoll, int *pscore, bool *pendTurn) {

	// ScoreOptions acts as a table of contents to find the potential score in scoreChoices for user
	vector <int> scoreOptions;
	vector <int> scoreChoices;
	int remainingDice = 0;
	int optionCount = 0;
	int rollTotal = 0;
	int optionChoice = 0;
	int countForThree = 0;
	char continueChoice = '_';
	bool validContinueChoice = false;
	bool didScore = false;
	bool didRemove = false;
	bool stillScores = true;

	// Set remaining dice equal to the amount of dice that were passed to it
	remainingDice = rolledDice.size();

	// Loops until there are still scores available or the user chooses to stop setting aside dice
	while (stillScores) {

		// Check if user has a valid 1,000 point score and print the option
		if (count(rolledDice.begin(), rolledDice.end(), 1) >= 3) {
			optionCount += 1;
			scoreOptions.push_back(optionCount);
			scoreChoices.push_back(1000);
			cout << optionCount << ". 1, 1, 1 = 1,000 points" << endl;
		}

		// Check if user has a valid 200 point score and print the option
		if (count(rolledDice.begin(), rolledDice.end(), 2) >= 3) {
			optionCount += 1;
			scoreOptions.push_back(optionCount);
			scoreChoices.push_back(200);
			cout << optionCount << ". 2, 2, 2 = 200 points" << endl;
		}

		// Check if user has a valid 300 point score and print the option
		if (count(rolledDice.begin(), rolledDice.end(), 3) >= 3) {
			optionCount += 1;
			scoreOptions.push_back(optionCount);
			scoreChoices.push_back(300);
			cout << optionCount << ". 3, 3, 3 = 300 points" << endl;
		}

		// Check if user has a valid 400 point score and print the option
		if (count(rolledDice.begin(), rolledDice.end(), 4) >= 3) {
			optionCount += 1;
			scoreOptions.push_back(optionCount);
			scoreChoices.push_back(400);
			cout << optionCount << ". 4, 4, 4 = 400 points" << endl;
		}

		// Check if user has a valid 500 point score and print the option
		if (count(rolledDice.begin(), rolledDice.end(), 5) >= 3) {
			optionCount += 1;
			scoreOptions.push_back(optionCount);
			scoreChoices.push_back(500);
			cout << optionCount << ". 5, 5, 5 = 500 points" << endl;
		}

		// Check if user has a valid 600 point score and print the option
		if (count(rolledDice.begin(), rolledDice.end(), 6) >= 3) {
			optionCount += 1;
			scoreOptions.push_back(optionCount);
			scoreChoices.push_back(600);
			cout << optionCount << ". 6, 6, 6 = 600 points" << endl;
		}
		
		// Check if user has a valid 100 point score and print the option
		if (count(rolledDice.begin(), rolledDice.end(), 1)) {
			optionCount += 1;
			scoreOptions.push_back(optionCount);
			scoreChoices.push_back(100);
			cout << optionCount << ". 1 = 100 points" << endl;
		}

		// Check if user has a valid 50 point score and print the option
		if (count(rolledDice.begin(), rolledDice.end(), 5)) {
			optionCount += 1;
			scoreOptions.push_back(optionCount);
			scoreChoices.push_back(50);
			cout << optionCount << ". 5 = 50 points" << endl;
		}

		// Give result if there are no scoring options left
		if (optionCount < 1) {

			// Determine if user Farkled or simple ran out of scoring dice
			if (didScore == false) {
				cout << "Farkle!" << endl;

				// Set still scores to end the turn
				stillScores = false;

				// Set rollTotal to 0 so the user loses their points
				rollTotal = 0;

				// Set value that pendTurn points to to true to end turn immediately
				*pendTurn = true;
			}
			else {
				cout << "No more valid options!" << endl;
				stillScores = false;
			}
		}

		// Condition statement to print available scoring dice, remove dice, and inform user of remaining dice
		if (stillScores) {
			// Let the user select from the score options available
			cout << endl << "Please select a scoring option from the list above: ";
			cin >> optionChoice;

			// Add the user's choice for this roll to the total score to be returned
			rollTotal += scoreChoices[scoreOptions[optionChoice - 1] - 1];

			// Condition statement to remove already scored dice
			// Removes three 1's
			if (scoreChoices[scoreOptions[optionChoice - 1] - 1] == 1000) {
				for (int i = 0; i < rolledDice.size() && countForThree < 3; i++) {
					if (rolledDice[i] == 1) {
						rolledDice[i] = 0;
						countForThree = countForThree + 1;
					}
				}
				remainingDice = remainingDice - 3;
				didScore = true;
			}

			// Removes three 2's
			else if (scoreChoices[scoreOptions[optionChoice - 1] - 1] == 200) {
				for (int i = 0; i < rolledDice.size() && countForThree < 3; i++) {
					if (rolledDice[i] == 2) {
						rolledDice[i] = 0;
						countForThree = countForThree + 1;
					}
				}
				remainingDice = remainingDice - 3;
				didScore = true;
			}

			// Removes three 3's
			else if (scoreChoices[scoreOptions[optionChoice - 1] - 1] == 300) {
				for (int i = 0; i < rolledDice.size() && countForThree < 3; i++) {
					if (rolledDice[i] == 3) {
						rolledDice[i] = 0;
						countForThree = countForThree + 1;
					}
				}
				remainingDice = remainingDice - 3;
				didScore = true;
			}

			// Removes three 4's
			else if (scoreChoices[scoreOptions[optionChoice - 1] - 1] == 400) {
				for (int i = 0; i < rolledDice.size() && countForThree < 3; i++) {
					if (rolledDice[i] == 4) {
						rolledDice[i] = 0;
						countForThree = countForThree + 1;
					}
				}
				remainingDice = remainingDice - 3;
				didScore = true;
			}

			// Removes three 5's
			else if (scoreChoices[scoreOptions[optionChoice - 1] - 1] == 500) {
				for (int i = 0; i < rolledDice.size() && countForThree < 3; i++) {
					if (rolledDice[i] == 5) {
						rolledDice[i] = 0;
						countForThree = countForThree + 1;
					}
				}
				remainingDice = remainingDice - 3;
				didScore = true;
			}

			// Removes three 6's
			else if (scoreChoices[scoreOptions[optionChoice - 1] - 1] == 600) {
				for (int i = 0; i < rolledDice.size() && countForThree < 3; i++) {
					if (rolledDice[i] == 6) {
						rolledDice[i] = 0;
						countForThree = countForThree + 1;
					}
				}
				remainingDice = remainingDice - 3;
				didScore = true;
			}

			// Removes a single 1
			else if (scoreChoices[scoreOptions[optionChoice - 1] - 1] == 100) {
				for (int i = 0; i < rolledDice.size() && !didRemove; i++) {
					if (rolledDice[i] == 1) {
						rolledDice[i] = 0;
						didRemove = true;
					}
				}
				remainingDice = remainingDice - 1;
				didScore = true;
			}

			// Removes a single 5
			else if (scoreChoices[scoreOptions[optionChoice - 1] - 1] == 50) {
				for (int i = 0; i < rolledDice.size() && !didRemove; i++) {
					if (rolledDice[i] == 5) {
						rolledDice[i] = 0;
						didRemove = true;
					}
				}
				remainingDice = remainingDice - 1;
				didScore = true;
			}

			// Loop to remove any 0's from the rolled dice vector to get rid of set aside dice
			for (int i = 0; i < rolledDice.size(); i++) {
				if (rolledDice[i] == 0) {
					rolledDice.erase(rolledDice.begin() + i);
				}
			}

			// Print new line for readability
			cout << endl;

			// Print the remaining dice for the user
			for (int i = 0; i < rolledDice.size(); i++) {
				if (rolledDice[i] != 0) {
					cout << rolledDice[i] << "   ";
				}
			}

			// Print new line for readability
			cout << endl << endl;

			// Section to check if user would like to score more dice
			cout << "Would you like to set aside more dice? (y - yes, n - no): ";
			while (!validContinueChoice) {
				cin >> continueChoice;
				if (continueChoice == 'y') {
					validContinueChoice = true;
					stillScores = true;
				}
				else if (continueChoice == 'n') {
					validContinueChoice = true;
					stillScores = false;
				}
				else {
					cout << endl << "Invalid choice! Please select between (y - yes, n - no): ";
					validContinueChoice = false;
				}
			}

			// Reset variables and vectors needed to properly go through options with user
			countForThree = 0;
			optionCount = 0;
			scoreOptions.clear();
			scoreChoices.clear();
			validContinueChoice = false;
			didRemove = false;
		}

		// Print new line for readability
		cout << endl;
	}

	// Set remaining dice and score to correct values using pointers
	*pdiceToRoll = remainingDice;
	*pscore = *pscore + rollTotal;
}

// Function to roll and score dice each player turn
int RollAndScore() {

	const int MAX_DICE = 6;
	vector <int> currentRolls;
	Dice gameDice;
	int diceToRoll = MAX_DICE;
	int totalScore = 0;
	int tempScore = 0;
	char continueRolling = '_';
	bool continueRollingValid = false;
	bool endTurn = false;

	// Roll until the user decides to stop or gets a farkle
	while (!endTurn) {

		// Condition statement to check if user is continuing turn but has already set aside all 6 dice
		if (diceToRoll == 0) {
			diceToRoll = MAX_DICE;
		}

		// Display current player's point total for the rolls this turn
		cout << "You are currently at " << tempScore << " points for this turn." << endl << endl;

		// Roll dice for the round
		for (int i = 0; i < diceToRoll; i++) {
			currentRolls.push_back(gameDice.RollDie());
		}

		// Print rolled dice for this round and create readability space upon exiting the loop
		for (int i = 0; i < currentRolls.size(); i++) {
			cout << currentRolls[i] << "   ";
		}
		cout << endl << endl;
		
		// Call RollScoring to increase current player's point total using pointers
		RollScoring(currentRolls, &diceToRoll, &tempScore, &endTurn);

		// Clear out unsaved dice for next roll
		currentRolls.clear();

		// Check if user would like to keep rolling if they did not Farkle
		if (!endTurn) {
			// Check if user would like to continue rolling after printing a new line for readability
			cout << "Would you like to continue rolling? (y - yes, n - no): ";

			// Print new line for readability
			cout << endl;

			// Loop to see if user wants to continue rolling after setting aside dice
			while (!continueRollingValid) {
				cin >> continueRolling;
				if (continueRolling == 'y') {
					endTurn = false;
					continueRollingValid = true;
				}
				else if (continueRolling == 'n') {
					endTurn = true;
					continueRollingValid = true;
				}
				else {
					cout << "Invalid selection! Please enter y for yes or n for no: ";
					continueRollingValid = false;
				}
			}
		}
		else {
			tempScore = 0;
		}

		// Set continueRollingValid back to false
		continueRollingValid = false;
	}

	// Clean up variables to get them ready for next pass
	continueRollingValid = false;
	endTurn = false;
	totalScore = tempScore;

	return totalScore;
}

// Function for the main farkle game to play
void FarkleGame() {
	
	vector <Player> playerList;
	Player currentPlayer;
	Player gameWinner;
	string currentName = "";
	bool completedGame = false;
	bool completedList = false;
	bool finalRound = false;
	int finalRoundCounter = 0;
	int playerNumber = 0;
	int turnNumber = 1;
	int roundTotal = 1;

	// Get number of players from user
	cout << "How many players will be in this game: ";
	cin >> playerNumber;

	// Loop to fill the player list with players
	while (!completedList) {
		for (int i = 0; i < playerNumber; i++) {
			cout << "Please enter the name for Player " << i + 1 << ": ";
			cin >> currentName;
			currentPlayer.SetName(currentName);
			playerList.push_back(currentPlayer);
		}
		completedList = true;
	}

	// Print end line for readability
	cout << endl;
	
	cout << "It is now round " << roundTotal << "!" << endl << endl;
	while (!completedGame) {

		// Check for final round and end of game
		if (currentPlayer.GetScore() >= 10000) {

			// Set the current game winner as the gameWinner
			gameWinner = currentPlayer;

			// Print message informing players that a user has exceeded
			cout << gameWinner.GetName() << " has exceeded 10,000 points with a score of " << gameWinner.GetScore() << "!" << endl << endl;
			cout << "This is the last round!" << endl << endl;

			// Set finalRound boolean to true to start final round
			finalRound = true;
		}

		// Condition statement to restart the turn order, increment the number of rounds the game has taken, and print the current game status
		if (turnNumber > playerNumber) {
			turnNumber = 1;
			roundTotal += 1;
			cout << endl << "It is now round " << roundTotal << "!" << endl << endl;

			// Loop to print current game scores
			cout << "Current score!" << endl;
			for (int i = 0; i < playerList.size(); i++) {
				cout << playerList[i].GetName() << " has " << playerList[i].GetScore() << " points!" << endl;
			}
		}

		// Set turn player
		currentPlayer = playerList[turnNumber - 1];

		// Print message stating current players turn
		cout << endl << "It is now " << currentPlayer.GetName() << "'s turn!" << endl;

		// Enter the function that acts as the player turn and return points that they score
		currentPlayer.SetScore(currentPlayer.GetScore() + RollAndScore());

		// Update PlayerList with current player's new score
		playerList[turnNumber - 1] = currentPlayer;

		// Check if it's final round and if game winner needs to be updated
		if (finalRound) {

			// If current player has a higher score than current game winner, update game winner with current player
			if (currentPlayer.GetScore() > gameWinner.GetScore()) {
				gameWinner = currentPlayer;
			}

			// Increment final round turn counter
			finalRoundCounter = finalRoundCounter + 1;

			// Check if the remaining players have all gotten a turn
			if (finalRoundCounter == playerList.size() - 1) {
				completedGame = true;
			}
		}
		// Increase turn number at the end of turn
		turnNumber += 1;
	}

	// Print messages for the game winner and the number of rounds it took
	cout << "The winner is " << gameWinner.GetName() << " with " << gameWinner.GetScore() << " points!" << endl;
	cout << "The game was played for " << roundTotal << " rounds!" << endl << endl;

	// Loop to print the players and their final scores
	cout << "Final Scores!" << endl;
	for (int i = 0; i < playerList.size(); i++) {
		currentPlayer = playerList[i];
		cout << currentPlayer.GetName() << " - " << currentPlayer.GetScore() << endl;
	}

	// Print new line for readability
	cout << endl;
}

// Function to display rules to user
void DisplayRules() {

	// Use a new line to provide more readability when the rules are printed
	cout << endl;

	// Variable to store the read in character from the in file
	char readChar = '_';

	// Opens the file to read in
	ifstream ruleFile;
	ruleFile.open("FarkleRules.txt");

	// Loop to read in each char from the rules file
	while (ruleFile.good()) {

		// Sets the readChar variable to the next char in the file and prints it
		readChar = ruleFile.get();
		cout << readChar;
	}

	// End line character for future printing and user input
	cout << endl << endl;

	// Closes the in file
	ruleFile.close();
}

// Main function serves as main menu for game
int main() {

	bool endProgram = false;
	// User selection as char to prevent cin error state
	char userSelection = 0;

	// Give user a welcome message
	cout << "Welcome to Farkle!" << endl << endl;

	while (!endProgram) {
		cout << "Please select an option below:" << endl << "1. Play Farkle" << endl << "2. See Rules" << endl << "3. Exit Program" << endl;
		cin >> userSelection;

		if (userSelection == '1') {
			cout << endl;
			// Implement game
			FarkleGame();
		}
		else if (userSelection == '2') {
			DisplayRules();
		}
		else if (userSelection == '3') {
			endProgram = true;
		}
		else {
			cout << "Invalid selection, please try again." << endl;
		}

	}
	return 0;
}
