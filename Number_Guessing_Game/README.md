# Number Guessing Game

The **Number Guessing Game** is a fun interactive project that helps users practice logical thinking and understand how programs handle user input, conditions, and game logic. In this game, the program randomly selects a number (using `random.randint(1, 10)`), and the user must guess the correct number within a limited number of attempts.

The user is allowed **three attempts** to guess the correct number. After each guess, the program displays a message telling the user whether their guess is correct or wrong. If the user guesses the correct number within the given attempts, a **winning message is displayed**. If all attempts are used and the user fails to guess the number, an **out-of-attempts** message is shown.

To improve the user experience, the project includes a Reset Attempts button. This button resets the attempt counter and allows the user to play the game again without restarting the program.

The guessing range is set between **1 and 10**, but this range can easily be increased or modified in the code to make the game more challenging.

## Key Features
- Random number generation for the guessing game
- 3 attempts to guess the correct number
- Messages for:
    - Correct guess (winning message)
    - Wrong guess
    - Out of attempts
- Reset button to restart the game attempts
- Number range from 1 to 10 (can be expanded for difficulty levels)

## Video Demo
[!Project_demo](https://github.com/user-attachments/assets/51783a8d-a44c-4df6-b075-d3b486cbb9cd)

## Concepts Learned from Number Guessing Game
- **Python GUI Development** – Building a graphical game interface using CustomTkinter.
- **Random Number Generation** – Using the `random` module to generate a secret number.
- **Variables and State Management** – Storing and updating the secret number and attempts counter.
- **Conditional Statements** – Using `if-else` logic to check correct, wrong, and empty inputs.
- **User Input Handling** – Getting and processing user input from entry fields.
- **Event Handling** – Triggering functions when buttons are clicked (Submit and Reset).
- **Global Variables** – Using `global` to modify variables inside functions.
- **GUI Layout Management** – Using `grid()` and `frame` configuration for UI positioning.
- **Dynamic UI Updates** – Updating labels in real time based on game results.
- **Basic Game Logic** – Implementing attempts, win/lose conditions, and reset functionality.
