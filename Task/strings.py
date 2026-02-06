# -------------------------------
# Task 1: Create and Print a String
# -------------------------------
greeting = "Hello, Python!"
print(greeting)


# -------------------------------
# Task 2: Access Specific Characters in a String
# -------------------------------
text = "PythonProgramming"

# First character
print("First character:", text[0])

# Last character
print("Last character:", text[-1])

# Middle character
middle_index = len(text) // 2
print("Middle character:", text[middle_index])


# -------------------------------
# Task 3: Slice a String
# -------------------------------
text2 = "Python Developer"

# Extract the word "Python"
print(text2[:6])

# Extract the word "Developer"
print(text2[7:])

# Print the string in reverse order
print(text2[::-1])


# -------------------------------
# Task 4: Try Modifying a String (String Immutability)
# -------------------------------
word = "Immutable"

# Strings are immutable, so this will cause an error
# word[0] = "A"   # TypeError: 'str' object does not support item assignment

print("Strings cannot be modified because they are immutable.")


# -------------------------------
# Task 5: Delete a String
# -------------------------------
temp = "Temporary String"
del temp

# print(temp)  # NameError: name 'temp' is not defined
print("Variable deleted, cannot be accessed.")


# -------------------------------
# Task 6: Update a String
# -------------------------------
text3 = "Hello, World!"

# Update to "Hello, Python!" using slicing and concatenation
updated_text = text3[:7] + "Python!"
print(updated_text)


# -------------------------------
# Task 7: Use String Methods
# -------------------------------
text4 = "Python is Amazing!"

print(text4.upper())
print(text4.lower())
print(text4.title())
print(text4.replace("Amazing", "Powerful"))


# -------------------------------
# Task 8: Check String Properties
# -------------------------------
text5 = "Hello123"

print("Only alphabets:", text5.isalpha())
print("Only digits:", text5.isdigit())
print("Contains letters and numbers:", text5.isalnum())


# -------------------------------
# Task 9: Concatenating and Repeating Strings
# -------------------------------
str1 = "Python"
str2 = "Programming"

# Concatenate with space
print(str1 + " " + str2)

# Repeat string
print("Python! " * 5)


# -------------------------------
# Task 10: Format a String Using f-strings
# -------------------------------
name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello, my name is {name} and I am {age} years old.")


# -------------------------------
# Task 11: Find and Replace a Word in a String
# -------------------------------
sentence = "I love Java!"
updated_sentence = sentence.replace("Java", "Python")
print(updated_sentence)


# -------------------------------
# Task 12: Count the Occurrences of a Character
# -------------------------------
fruit = "banana"
count_a = fruit.count("a")

print(f"The letter 'a' appears {count_a} times.")


 # Task 13: Reverse Words in a Sentence
sentence2 = "Python is fun"

# Reverse the order of words
reversed_words = " ".join(sentence2.split()[::-1])
print(reversed_words)
