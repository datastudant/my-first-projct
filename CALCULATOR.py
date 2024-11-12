#PYTHON 
status = True  # Initialize status variable

try:
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
except ValueError:  # Catch specific exception
    status = False
    print("Invalid input! Please enter numeric values.")
   
#function for check operator 
#print(num1, num2)


def check_operator():
  op = input("Enter operator (+, -, *, /) : ")
  while op not in ('+', '-', '*', '/'):
       if op not in ('+', '-', '*', '/') and len(op) == 1:
          op = input("Error: pleass Enter coreact operator (+, -, *, /) : ")
       else:
          op = input("Error: pleass Enter one operator (+, -, *, /) : ")
  return op
#check operator
op_status = check_operator()
#program calculator

def calculator(num1, num2, op_status):
   if op_status == '+':
      ruselt = num1 + num2
      print(ruselt)
   elif op_status == '-':
      ruselt = num1 - num2
      print(ruselt)
   elif op_status == '/' :
      ruselt = num1 / num2
      print(ruselt)
   else:
      ruselt = num1 * num2
      print(ruselt)
while status:
   check_operator()
   calculator(num1, num2, op_status)
   break  
      
     
 
   




  











