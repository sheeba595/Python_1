# 1. Write a program that takes two numbers as input and prints their sum, 
# difference, product, quotient, and remainder. 

num_1=int(input("Enter num1: "))
num_2=int(input("Enter num2: "))
print("Sum: ",num_1+num_2)
print("Difference: ",num_1-num_2)
print("Product: ",num_1*num_2)
print("Quotient: ",num_1/num_2)
print("Remainder: ",num_1%num_2)

# 2. Write a program that asks the user for two numbers and prints whether the 
# first number is greater than, less than, or equal to the second number. 
n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))
if(n1>n2):
    print("n1 is greater than n2")
elif (n1<n2):
    print("n1 less than n2")
elif (n1!=n2):
    print("n1 not equal to n2")
else:
    print("n1 equal to n2")
    
#  3   . Swap two numbers using arithmetic operators (addition and subtraction or 
# multiplication and division).

a=13
b=1
print("Before swapping","a: ",a,"b: ",b)
a=a+b
b=a-b
a=a-b
print("After swapping","a: ",a,"b: ",b)

# 4. Take a year as input and use the modulus (%) operator to check if it is a leap 
# year.
year=2000
if(year%400==0) or (year%100==4 and year%100!=0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
    
#  5   . Ask the user for three numbers and determine which is the largest using 
# comparison operators.
num1=int(input("Enter n1: "))
num2=int(input("Enter n2: "))
num3=int(input("Enter n3: "))
if (num1>num2) and (num1>num3):
    print(f"{num1} is greater")
elif (num2>num1) and (num2>num3):
    print(f"{num2} is greater")
else:
    print(f"{num3} id greater")


# 6. Take the radius as input and calculate the area using the formula: area = π * 
# r² (Use 3.14 for π) 
    radius=int(input("Enter radius: "))
    pi=3.14
    area=pi*((radius)**2)
    print(f" Area: {area}")
    
#  7   . Write a program that takes a number as input and checks if it is positive, 
# negative, or zero using conditional statements. 
number=int(input("enter number: "))
if(number>0):
    print("Positive")
elif(number<0):
    print("Negative")
else:
    print("Zero")
    
    
# . Ask the user for their age and print whether they are eligible to vote (age >= 
# 18). 
age=int(input("Enter your age: "))
if(age>=18):
    print("Eligible for Vote")
elif(age>0):
    print("Not eligible for vote")
else:
    print("Invalid age")
    
    
# 9. Take marks as input and assign grades based on these conditions: 90+  → A   
# 80-89 → B   
# 70-79 → C   
# 60-69 → D   
# Below 60 → Fail
mark=int(input("Enter mark: "))
if(mark>=90):
    print("A")
elif (mark>=80 and mark<=89):
    print("B")
elif(mark>=70 and mark<=79):
    print("C")
elif(mark>=60 and mark<=69):
    print("D")
else:
    print("Fail")
    
#     10. Simple ATM Withdrawal Program 
#  Set an initial account balance (e.g., 5000). 
#  Ask the user how much they want to withdraw. 
#  If the amount is greater than the balance, print "Insufficient funds." 
# Otherwise, subtract the amount and print the remaining balance. 

initial_amount=5000
withdraw=int(input("How much you wnat to withdraw? :  "))
if(withdraw>initial_amount):
    print("Insufficinet balance")
else:
    print("Remaining balanace: ",initial_amount-withdraw)
    
#     11. Write a program that asks for a number and checks if it is divisible by 
# both 5 and 11. 
num=int(input("Enter number: "))
if(num%5 and num%11):
    print(f"{num} is divisible by both 5 and 11")
    
#     12. Take a single character input and determine if it is a vowel (a, e, i, o, u) or a 
# consonant. 
char=input("Enter a character: ")
if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U'):
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")
    
# 13. Rewrite the even/odd program using a ternary (single-line) if-else statement
value=int(input("Enter number: "))
print("Even" if value%2==0 else "Odd")