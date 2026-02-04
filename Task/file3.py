#Write a program that prints your full name using print(). 
print("Sheeba")

#Use print() to display a welcome message on multiple lines. 
print("""Hello there!
      Welocome
      It is a pleasure to see you here
      How are you doing in your life? """)

#Create variables for your name, age, and favorite color. Print them. 
name="Sheeba"
age=22
color="Skyblue"
print(f"""Name: {name}
      Age: {age}
    Color: {color}""")

#Define different types of variables (string, integer, float, boolean) and print their 
# types using type(). 

sentence="hello world"
number=1
floated=1.0
value=True
character='a'
print(type(sentence))
print(type(number))
print(type(floated))
print(type(value))
print(type(character))

#Ask the user to enter their name and print a welcome message. 
user=input("Enter your name: ")
print(f"Hello {user}!")

# Take two numbers as input, convert them to integers, add them, and display the 
# result. 
num_1=int(input("Enter number 1: "))
num_2=int(input("Enter number 2: "))
print(num_1+num_2)

#Ask the user to enter a number, print its type, convert it to a float, and print its 
# new type. 

user_1=input("Enter a value: ")
print(type(user_1))
user_2=float(user_1)
print(user_2)
#Ask the user for their name, age, and city, and display a sentence using an f-string.
user_name="john"
user_age=30
user_city="NYC"
print(f"Name: {user_name} Age: {user_age}  City: {user_city}")

#Take the length and width of a rectangle as input and calculate the area using an f
# string. 
length=30
breadth=2
print(f"{length*breadth}")

# Ask the user for an item name, quantity, and price, then display a formatted bill 
# using f-strings.
item_name="Vivo V27"
item_qty=1
item_price=50000
print(f"""Product Name: {item_name}
      Quantity: {item_qty}
      Price: {item_price}""")
#Take two numbers from the user and swap them without using a third variable.
a=10
b=20
print(f"before swap a:{a}, b:{b}")
a,b=b,a
print("After swap a:{a},b:{b}")

# Take a temperature in Celsius as input, convert it to Fahrenheit, and display it 
# using an f-string. 
celcius=float(input("Enter the valeu: "))
fahrenheit=(celcius*9/5)+32
print(f"Fahrenheit: {fahrenheit}")

#Simple Profile Display 
# Take the user's name, age, height, and favorite hobby, then display a formatted 
# profile. 

name_user="Doe"
age_user=33
user_height="155cm"
hobby="Sports"
print("*****Profile Display*****")
print(f"""
      Name: {name_user}
      Age: {age_user}
      Hobby: {hobby}
      Height: {user_height}""")