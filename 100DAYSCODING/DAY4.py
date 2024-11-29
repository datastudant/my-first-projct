import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# index = random.choice(friends)
# print(len(friends))
# 
is_running = True
while is_running:
  print("=====================GAME STARE=======================")
  game_emoji = ["✂️", "📄", "🤜"]
  bot= random.choice(game_emoji)
  player_choice = int(input("Choice 1 for Scissors ✂️, 2 for Paper 📄, 3 for Rock🤜: "))
  choice = game_emoji[player_choice-1]
  print("=======================================================")
  print(f"Bot : {bot}")
  print(f"Player : {choice}")
  if bot == choice :
    print("It's a tie")
  elif (bot == "✂️" and choice == "📄") or (bot == "📄" and choice == "🤜") or (bot == "🤜" and choice == "✂️"):
    print("Player wins!")
  else:
    print("You loos")
  print("=======================================================")
  play_again = input("Do you want to play again? (Y/N): ").upper()
  if not play_again == "Y":
    is_running = False
  
