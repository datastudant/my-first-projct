import random

def number_guessing_game():
    # Define the range for the guessing game
    lowest_num = 1
    highest_num = 100
    answer = random.randint(lowest_num, highest_num)
    guesses = 0
    is_running = True

    print("Welcome to the Python Number Guessing Game!")
    print(f"Please select a number between {lowest_num} and {highest_num}.")

    while is_running:
        guess = input("Enter your guess: ")

        if guess.isdigit():
            guess = int(guess)
            guesses += 1

            # Check if the guess is out of the defined range
            if guess < lowest_num or guess > highest_num:
                print("That number is out of range.")
                print(f"Please select a number between {lowest_num} and {highest_num}.")
            elif guess < answer:
                print("Too low! Try again.")
            elif guess > answer:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! The correct answer was {answer}.")
                print(f"Number of guesses: {guesses}")
                is_running = False
        else:
            print("Invalid input. Please enter a valid number.")
            print(f"Select a number between {lowest_num} and {highest_num}.")

if __name__ == "__main__":
    number_guessing_game()