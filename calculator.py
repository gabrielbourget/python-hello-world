num1 = float(input("Enter a number: "))
operator = input("Enter an operation (+, -, *, /): ")
num2 = float(input("Enter another number: "))
result = 0

if operator == "+":
  result = num1 + num2
elif operator == "-":
  result = num1 - num2
elif operator == "*":
  result = num1 * num2
elif operator == "/":
  result = num1 / num2
else: print("Invalid operation entered")

print("calculator result: " + str(result))