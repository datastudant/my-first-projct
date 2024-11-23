import random

# List of words for the game
words = ("apple", "banana", "cherry", "date", "elderberry")

# Hangman art dictionary
hangman_art = {
    0: ("  ",
        "  ",
        "  "),
    1: (" o ",
        "   ",
        "   "),
    2: ("  o ",
        "  | ",
        "    "),
    3: ("  o  ",
        " <| ",
        "    "),
    4: ("  o  ",
        " <|> ",
        "   "),
    5: ("  o  ",
        " <|> ",
        " /  "),
    6: ("  o  ",
        " <|> ",
        " / \\")
}

def display_hangman(wrong_guesses, hangman_art):
    """Display the current state of the hangman based on wrong guesses."""
    print("******************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("******************")

def display_hint(hint):
    """Display the current hint with guessed letters and underscores."""
    print(" ".join(hint))

def get_guess():
    """Prompt the user for a valid letter guess and return it in lowercase."""
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        print("Invalid input! Please enter a single letter.")

def update_hint(answer, hint, guess):
    """Update the hint with the correctly guessed letter."""
    for index, letter in enumerate(answer):
        if letter == guess:
            hint[index] = letter

def main():
    # Choose a random word from the list
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    max_wrong_guesses = len(hangman_art) - 1
    is_running = True

    while is_running:
        # Display current hangman state and hint
        display_hangman(wrong_guesses, hangman_art)
        display_hint(hint)

        # Get the user's guess
        guess = get_guess()

        # Update hint or increment wrong guesses
        if guess in answer:
            update_hint(answer, hint, guess)
        else:
            wrong_guesses += 1

        # Check for win/lose conditions
        if "_" not in hint:
            print("Congratulations! You've guessed the word:", answer)
            is_running = False
        elif wrong_guesses >= max_wrong_guesses:
            display_hangman(wrong_guesses, hangman_art)
            print("Game over! The word was:", answer)
            is_running = False

# Run the game
if __name__ == "__main__":
    main()
