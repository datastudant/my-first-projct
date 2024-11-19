# Python Slot Machine Game
# Author: [Rida]
import random
def spin_row():
  symbols = ["🍒", "🍊", "🍑", "🍓", "🍇"]
  return [random.choice(symbols) for _ in range(3)]
def print_row():
  pass
def get_payout():
  pass
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








if __name__ == "__main__":
  main()