import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

def main():
    while True:
        players = input("Enter the number of players (2-4): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                break
            else:
                print("Must be between 2 - 4 players")
        else:
            print("Invalid, please enter a number")
    
    max_score = 50
    players_score = [0 for _ in range(players)]
    
    while max(players_score) < max_score:
        for player_idx in range(players):
            current_score = 0
            print(f"Player {player_idx + 1}'s turn. Current score: {players_score[player_idx]}")
            while True:
                should_roll = input("Would you like to roll? (y/n): ")
                if should_roll.lower() == "y":
                    break
                elif should_roll.lower() == "n":
                    print(f"Player {player_idx + 1} ends their turn with a score of {current_score}.")
                    players_score[player_idx] += current_score
                    break
                else:
                    print("Invalid input, please enter 'y' or 'n'.")

            if should_roll.lower() == "y":
                value = roll()
                if value == 1:
                    print("You rolled a 1, turn done!")
                    players_score[player_idx] += current_score  # Add the current score before ending the turn
                    break
                else:
                    current_score += value
                    print(f"You rolled a: {value}. Current score this turn: {current_score}")

            # After rolling, check if player has reached or exceeded the max score
            if players_score[player_idx] >= max_score:
                print(f"Player {player_idx + 1} wins with a score of {players_score[player_idx]}!")
                return

if __name__ == "__main__":
    main()