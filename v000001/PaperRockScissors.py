# call random 
import random 
# tubel
options = ("rock","paper","scissors")
# start whille loop
running = True
while running:
  # Game logic here
  player = None
  computer = random.choice(options)
  # check input
  while player not in options:
    player = input("Enter a choice (rock, paper, scissors): ")
  print(f"Player : {player}")
  print(f"Computer: {computer}")
  # check winer and loser 
  if player == computer :
    print("It's a tie !")
  elif player == "rock" and computer == "scissors":
    print("You win!")
  elif player == "paper" and computer == "rock":
    print("You win!")
  elif player == "scissors" and computer == "paper":
    print("You win!")
  else:
    print("You lose!")
  # check if play again or not 
  if not input("Play again? (y/n): ").lower() == "y":
    break