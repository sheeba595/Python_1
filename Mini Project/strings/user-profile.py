# ----------------------------------
# Mini Project 1: User Profile Formatter
# ----------------------------------

# Step 1: Take user input for full name, age, and favorite quote
full_name = input("Enter your full name: ")
age = input("Enter your age: ")
favorite_quote = input("Enter your favorite quote: ")

# Step 2: Capitalize the first letter of each word in the name
formatted_name = full_name.title()

# Step 3: Ensure that the age is in string format
age = str(age)

# Step 4: Convert the favorite quote to uppercase
formatted_quote = favorite_quote.upper()

# Step 5: Display the formatted output
print("\nUser Profile:")
print("-------------------------")
print(f"Name           : {formatted_name}")
print(f"Age            : {age}")
print(f'Favorite Quote : "{formatted_quote}"')
