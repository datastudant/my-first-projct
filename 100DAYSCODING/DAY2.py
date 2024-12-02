# # The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:



# bmi is equal to the person's weight divided by the person's height squared.



# Convert this sentence into code on line 6
# height = 1.65 
# weight = 84

# # Write your code here.
# def calculate_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     return bmi
# # Calculate the bmi using weight and height.
# bmi =int( calculate_bmi(weight, height))

# print(bmi)


# print(6 + 4 / 2 - (1 * 2))
print("================Welcome To The tip calaculator==================")
Total_bill = float(input("Enter the total bill: $"))
Total_bill = round(Total_bill,2)
tip = int(input("How much tip would you like to give? ( 10, 12, or 15) %"))
people = int(input("How many people to split the bill? "))
# programe to calculate the tip and total bill
tip = (tip / 100) + 1
final_price = Total_bill * tip / people
print(f"Total bill: ${final_price:.2f}")
print("Hello World")













