# concession stand program
menu = {
  "pizza" : 3.00,
  "nachos" : 4.50,
  "popcorn" : 6.00,
  "fries" : 3.50,
  "chips" :1.00,
  "pretzel" : 3.50,
  "soda" : 3.00,
  "lemonade" : 4.00
  }
cart = []
total = 0
print("---------MENU---------")
for key, valeu in menu.items():
  print(f"{key:10}: $ {valeu:.2f}")
print("----------------------")
while True:
  food = input("Select an item (q to quit): ").lower()
  if food == "q":
    break
  elif menu.get(food) is not None:
    cart.append(food)
print("--------YOUR ORDER--------")
for food in cart:
  total += menu.get(food)
  print(f"{food} ,", end=" ")
print()
print(f"Total is : $ {total:.2f}")