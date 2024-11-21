#Exercise 1: Calculate the multiplication and sum of two numbers
#Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
number_1 = input("Enter the first number: ")
number_2 = input("Enter the second number: ")
while True :
    if number_1.isdigit() and number_2.isdigit():
        number_1 = int(number_1)
        number_2 = int(number_2)
        if number_1 * number_2 <= 1000:
            print(f"multiplication : {number_1 * number_2}") 
            break
        else :
            print(f"some: {number_1 + number_2}")
            break
    else:
        print("Invalid input. Please enter a valid integer number.")
        number_1 = input("Enter the first number: ")
        number_2 = input("Enter the second number: ")


    
        






    
  
    


