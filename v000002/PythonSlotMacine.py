# Python Slot Machine Game
# Author: [Rida]
import random
def spin_row():
  symbols = ["🍒", "🍊", "🍑", "🍓", "🍇"]
  return [random.choice(symbols) for _ in range(3)]
def print_row(row):
  print("*****************")
  print(" | ".join(row))
  print("*****************")
def get_payout(row, bet):
  if row[0] == row[1] == row[2]:
    if row[0] == "🍒":
      return bet * 3
    elif row[0] == "🍊":
      return bet * 4
    elif row[0] == "🍑":
      return bet * 5
    elif row[0] == "🍓":
      return bet * 10
    elif row[0] == "🍇":
      return bet * 20
  return 0
def main():
  # Initialize the game logic her 
  balance = 100
  print("***************************")
  print("  Welcome to the Slot Machine Game  ")
  print("Symbols : 🍒 , 🍊, 🍑, 🍓, 🍇")
  print("***************************")
  while balance > 0:
    print(f"Current Balance: {balance}")
    bet = input("Enter your bet: ")
    if not bet.isdigit():
      print("Invalid bet. Please enter a number.")
      continue
    bet = int(bet)
    if bet > balance:
      print("Insufficient Funds")
      continue
    if bet <= 0:
      print("bet most be greater than ")
      continue
    balance -= bet
    row = spin_row()
    #print(spin_row())
    print("Spinning ...\n")
    print_row(row)
    payout = get_payout(row, bet)
    balance += payout
    if payout > 0:
      print(f"You won {payout}!")
      print(f"Your Balanc new is: {balance:.2f}")
    else:
      print("Better luck next time")
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
      break
    









if __name__ == "__main__":
  main()