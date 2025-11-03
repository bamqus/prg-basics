###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input("Give me the first number: "))
number2 = int(input("Give me the second number: "))
operator = str(input("Give me the symbol to use (+, -, *, /): "))

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 * number2
else:
    print("That's not what I asked for!")



print(f"{number1} {operator} {number2} = {result}")