# Simple Calculator 
# Taking user input 
num1 = float(input("Enter first number: ")) 
operator = input("Enter an operator (+, -, *, /, %): ") 
num2 = float(input("Enter second number: ")) 
# Performing calculation based on operator 
if operator == "+": 
    result = num1 + num2 
elif operator == "-": 
    result = num1 - num2 
elif operator == "*": 
    result = num1 * num2 
elif operator == "/": 
    if num2 != 0:  # Checking for division by zero 
        result = num1 / num2 
    else: 
        result = "Error! Division by zero." 
elif operator == "%": 
    result = num1 % num2 
else: 
    result = "Invalid operator!" 
print(f"Result: {result}") 