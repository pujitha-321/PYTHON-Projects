num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator: ")
if operator == '+':
   result = num1+num2
   print(result)
elif operator =='-':
   result = num1-num2
   print(result)
elif operator == '*':
   result = num1*num2
   print(result)
elif operator =='/':
   result =num1/num2
   print(result)
else:
   print("Enter valid opearator")

