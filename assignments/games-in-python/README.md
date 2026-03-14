
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game that uses random word selection, loops, and conditionals. By the end of this assignment, you will manage game state, process letter guesses, and determine win or loss outcomes.

## 📝 Tasks

### 🛠️ Initialize the Game

#### Description
Set up the starting state of your Hangman program using the provided starter code.

#### Requirements
Completed program should:

- Store a predefined list of possible words (at least 5 words).
- Randomly select one secret word from the list.
- Initialize variables to track guessed letters, incorrect guesses, and maximum incorrect attempts.
- Display the current word progress using underscores separated by spaces (example: `_ _ _ _ _`).

### 🛠️ Build the Guessing Loop

#### Description
Create the main game loop where the player guesses one letter at a time and the game state updates after each guess.

#### Requirements
Completed program should:

- Prompt the player for a single-letter guess each turn.
- Validate input so only one alphabetic character is accepted.
- Reveal all matching positions when the guessed letter is correct.
- Decrease remaining attempts only when the guess is incorrect.
- Continue the loop until the word is fully guessed or attempts run out.
- Example interaction:
	```text
	Word: _ _ _ _ _ _
	Guess a letter: a
	Correct! Word: _ a _ _ _ a
	Attempts remaining: 6
	```

### 🛠️ Finish the Game and Report Results

#### Description
Handle the end-of-game conditions and provide clear feedback to the player.

#### Requirements
Completed program should:

- Display a win message when the player guesses the full word.
- Display a lose message when attempts reach zero.
- Reveal the secret word when the player loses.
- End the game immediately after a win or loss condition is reached.
