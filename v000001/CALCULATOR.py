#PYTHON 
status = True  # Initialize status variable

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

num1 = get_float_input("Enter the 1st number: ")
num2 = get_float_input("Enter the 2nd number: ")

#function for check operator 
def check_operator():
    op = input("Enter operator (+, -, *, /) : ")
    while op not in ('+', '-', '*', '/'):
        if op not in ('+', '-', '*', '/') and len(op) == 1:
            op = input("Error: please enter correct operator (+, -, *, /) : ")
        else:
            op = input("Error: please enter one operator (+, -, *, /) : ")
    return op

#check operator
op_status = check_operator()

#program calculator
def calculator(num1, num2, op_status):
    if op_status == '+':
        result = num1 + num2
        print(result)
    elif op_status == '-':
        result = num1 - num2
        print(result)
    elif op_status == '/':
        result = num1 / num2
        print(result)
    else:
        result = num1 * num2
        print(result)

while status:
    calculator(num1, num2, op_status)
    break
