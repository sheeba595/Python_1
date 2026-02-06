# ----------------------------------
# Mini Project 2: Simple Password Generator
# ----------------------------------

# Step 1: Take user input for first name, last name, and secret keyword
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
secret_keyword = input("Enter a secret keyword: ")

# Step 2: Use string slicing
# a. First three letters of the first name
first_part = first_name[:3]

# b. Last three letters of the last name
last_part = last_name[-3:]

# c. Reverse the secret keyword
reversed_keyword = secret_keyword[::-1]

# Step 3: Concatenate values and convert to mix of uppercase and lowercase
password = first_part.capitalize() + last_part.lower() + reversed_keyword.upper()

# Step 4: Display the generated password in a formatted way
print("\nGenerated Password")
print("------------------")
print(f"Your password is: {password}")
