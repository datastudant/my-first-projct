sum_odd_digits = 0
sum_even_digits = 0
total = 0
# step 1
card_number = input("enter a credit card : ")
crad_number = card_number.replace(" ","")
crad_number = crad_number.replace("-","")
crad_number = crad_number[::-1]
# STEP 2
for x in crad_number[::2]:
  sum_odd_digits += int(x)
# step 3
for x in card_number[1::2]:
  x = int(x) * 2
  if x >= 10 :
    sum_even_digits += (1 + x % 10)
  else:
    sum_even_digits += x
#step 4
sum_total = sum_even_digits + sum_odd_digits
if sum_total % 10 == 0:
  print("Valid")
else:
  print("Invalid")