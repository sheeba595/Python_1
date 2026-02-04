# Taking user input 
name = input("Enter your name: ") 
age = int(input("Enter your age: ")) 
height = float(input("Enter your height in cm: ")) 
# Checking types 
print(f"Type of name: {type(name)}")  # str 
print(f"Type of age: {type(age)}")  # int 
print(f"Type of height: {type(height)}")  # float 
# Printing formatted user details 
print("\n===== Personal Information =====") 
print(f"Hello {name}, you are {age} years old and {height} cm tall.")