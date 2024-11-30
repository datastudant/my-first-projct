# student_scores = [90, 85, 88, 92, 78, 95, 89, 91, 84, 76, 94, 87, 93, 82, 96, 98, 83, 99, 97, 81]
# max = 0
# for score in student_scores:
#   if score > max:
#     max = score
# print(max)
# for i in range(1, 101):
#   if i % 3 == 0 and i % 5 == 0:
#     i = "FizzBuzz"
#   elif i % 3 == 0:
#     i = "Fizz"
#   elif i % 5 == 0:
#     i = "Buzz"
#   print(i)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '[', ']', '{', '}', ';', ':', '<', '>', ',', '.', '/', '?', '~', '|', "*"]
print(" Welcome to the password generator!")
nb_letters = int(input("How many letters would you like in your password? : "))
nb_numbers = int(input("How many numbers would you like in your password? : "))
nb_symbols = int(input("How many symbols would you like in your password? : "))
# print(nb_letters, nb_numbers, nb_symbols)
# nb = nb_letters + nb_numbers + nb_symbols
# print(nb)
password = ""
for i in range(nb_letters):
  # print(i)
  password += random.choice(letters)
  # print(password)
for i in range(nb_numbers):
  password += str(random.randint(1, 9))
  # print(password)
for i in range(nb_symbols):
  password += random.choice(symbols)
  # print(password)
# print(len(password))
def shuffle_word(password):
    word_list = list(password)  # Convert the word into a list of characters
    random.shuffle(word_list)  # Shuffle the list in place
    return ''.join(word_list)  # Join the list back into a string

# Example usage
shuffled_word = shuffle_word(password)
print(f"The shuffled password is: {shuffled_word}")