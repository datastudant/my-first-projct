#Exercise 1: Calculate the multiplication and sum of two numbers
#Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.


def main():
    number1 = input("Enter the first number: ")
    number2 = input("Enter the second number: ")
    number1, number2 = check_number_isdigit(number1, number2)
    print(type(number2, number1))
    def check_number_isdigit(number1, number2):
         try:
             number1 = int(number1)
             number2 = int(number2)
             return number1, number2
         except ValueError:
             print("Invalid input. Please enter a valid integer.")
             return None, None
            
          
    check_number_isdigit(number2, number1)
    def check_multiplication_number(number1, number2):
        product = number1 * number2 
        if product <= 1000 :
            return product
        else :
            return number2 + number1
    resulet = check_multiplication_number(number1, number2)
    print(f"the result is {resulet}")
        
   
    
        






if __name__ == "__main__":
    main()
    
    
    
  
    


