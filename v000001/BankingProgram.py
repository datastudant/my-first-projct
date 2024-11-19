# Python Banking Program
def show_balance(balance):
  print(f"Your Balance is : ${balance:.2f}")

def deposit():
  amount = float(input("Enter the amount to deposit: "))
  if amount > 0 :
    return amount
  else:
    print("Amount will be 0 > pleass enter a valid amount")
    return 0
def withdraw(balance):
  print(f"Your Balance is : ${balance:.2f}")
  amount = float(input("Enter Amount to be withdrawn  : "))
  if amount > balance:
    print("Insufficient Balance")
    return 0
  elif amount < 0 :
    print("Amount will be 0 > pleass enter a valid amount ")
    return 0
  else:
    return amount
balance = 0
is_running = True
  
def main():
  balance = 0
  is_running = True
  while is_running :
    print("---------------------------")
    print("Banking Program")
    print("---------------------------")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter Your chois (1-4) : ")
    if choice == "1":
      print("---------------------------")
      show_balance(balance)
    elif choice == "2":
      print("---------------------------")
      balance += deposit()
    elif choice =="3":
      print("---------------------------")
      balance -= withdraw(balance)
    elif choice == "4":
      
      is_running = False
    else:
      print("---------------------------")
      print("Invalid choice. Please choose a valid option.")
  print("---------------------------")
  print("Thank You ! have a Nice Day ")
  print("---------------------------")
if __name__ == "__main__":
  main()