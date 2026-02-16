# 1.Take a number as input and display whether it is below 50 or not.
n1=int(input("Enter n1: "))
if(n1<50):
    print("Below 50")
else:
    print("Above 50")
# 2.Accept two integers and print the positive difference between them.
a=int(input("Enter a: "))
b=int(input("Enter b: "))
diff=abs(a-b)
print("Positive difference: ",diff)
# 3.Get an integer value and display only its last digit.
n2=int(input("Enter n2: "))
print("Last digit: ",n2%10)
# 4.Accept a decimal number and display it rounded to two decimal places.
num=float(input("Enter number: "))
print("Rounded to 2 decimal places: ",round(num,2))
# 5.Input a number and check if it lies within the two-digit range.
# 9.Enter an integer and verify whether it contains exactly two digits.
n3=int(input("Enter number: "))
c=0
temp=abs(n3)
while(temp>0):
    temp//=10
    c+=1
if(c==2):
    print("Has two digit places")
else:
    print("More than two digits")
# 6.Given a number, determine whether it is a multiple of 4.
four=int(input("Enter number: "))
if(four%4==0):
    print(f"{four} is divisible by four")
else:
    print(f"{four} is not divisible by four")
# 7.Accept three values and display the smallest among them.
v1=int(input("Enter n1: "))
v2=int(input("Enter n2: "))
v3=int(input("Enter n3: "))
if(v1<v2 and v1<v3):
    print(f"{v1} is smaller")
elif(v2<v1 and v2<v3):
    print(f"{v2} is smaller")
else:
    print(f"{v3} is smaller")
    
# 8.Input one number and display both its square and cube.
s=int(input("Enter a number: "))
print("Square: ",s*s)
print("Cube: ",s**3)

# 10.Accept two integers and print the quotient and remainder.
e1=int(input("Enter n1: "))
e2=int(input("Enter n2: "))
if(e2==0):
    print("Can not be divisible by zero")
else:
    print("Quotient: ",e1//e2)
    print("Remainder: ",e1%e2)
# 11.Input a single character and identify whether it is a vowel or consonant.
char=input("Enter a character: ")
if char.lower() in "aeiou":
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")
# 12.Given a number, calculate and display the sum of its digits.
number=int(input("Enter a number: "))
sum=0
while(number>0):
    sum+=number%10
    number//=10
print("Sum of digits: ",sum)
    
    
# 13.Enter a number and find how many digits it contains.
number=int(input("Enter number: "))
digit=0
while(number>0):
    number//=10
    digit+=1
print("Digit count: ",digit)
# 14.Store two numbers and exchange their values using a temporary variable.
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
print("Before swapping: a:",a,"b: ",b)
temp=a
a=b=temp
print(f"After swapping: a:{a},b:{b}")
# 15.Enter a value and check if it is an even number between 20 and 40.
num=int(input("Enter a number: "))
if(num>20 and num<40):
    print(f"{num} is greater than 20 and less than 40")
else:
    print(f"{num} is not greater than 20 and less than 40")
    # 16.Provide a number and display the next nearest multiple of 5.
    n=int(input("enter number: "))
    remainder=n%5
    if(remainder==0):
        print("next nearest multiple: ",n+5)
    else:
        print(f"Next nearest multiple: {n+(5-remainder)}")
# 17.Accept a word and print its length.
word=input("Enter a word: ")
print("Word length: ",len(word))
# 18.Enter a string and display its first and last characters.
w1=input("enter a string: ")
print("First character: ",w1[0])
print("Last characetr: ",w1[-1])

# 19.Input a text value and print it three times (one per line).
text=input("Enter a text: ")
for i in range(1,4):
    print(text)
# 20.Enter a string and verify whether it is empty or not.
string=input("Enter a string: ")
if(string==""):
    print("String is empty")
else:
    print("String is not empty")
# 21.Display numbers starting from 5 up to 50 with a gap of 5.
for i in range(5,51,5):
    print(i,end=",")
# 22.Print all values between 1 and 100 that are divisible by 9.
for i in range(1,101):
    if(i%9==0):
        print(i,end=",")
    
# 23.Enter a number and print its reverse.
n=int(input("Enter a number: "))
print("Reverse of the number: ",str(n)[::-1])
# 24.Accept a value N and display numbers from N down to 1.
N=int(input("enter a number: "))
for i in range(N,0,-1):
    print(i,end=",")
# 25.Calculate the total of numbers from 1 to N.
N=int(input("Enter number: "))
s=0
for i in range(1,N+1):
    s+=i
print("Total: ",s)
    
# 26.Display all numbers between 1 and 200 that end with digit 6.
for i in range(1,201):
    if(i%10==6):
        print(i,end=",")
# 27.Accept a string and count how many lowercase letters it contains.
s1=input("Enter a string: ")
t=0
for i in s1:
    if i.islower():
        t+=1
print("total lower letters: ",t)
        
# 28.Given a text value, calculate the number of uppercase characters.
t1=input("Enter a text: ")
t2=0
for i in t1:
    if i.isupper():
        t2+=1
print(f"Total upper letters: {t2}")
# 29.Input an alphanumeric string and count the digits present.
alpha=input("Enter alphanumeric text: ")
count=0
for i in alpha:
     if i.isdigit():
         count+=1
print("Total numeric characters: ",count)
# 30.Enter a sentence and remove all blank spaces.
sen=input("Enter a sentence: ")
print(sen.strip())
# 31.Accept a sentence and display each word on a separate line.
sentence=input("Enter a sentence: ").split()
for i in sentence:
    print(i)
# 32.Given a string, print characters located at even index positions.
s3=input("Enter a string: ")
for index,char in enumerate(s3):
    if index%2==0:
        print(char)
     
         
# 33.Enter a word and check whether it begins with a vowel.
s4=input("Enter a word: ")
if(s4[0].lower() in "aeiou"):
    print("it is a vowel")
else:
    print("it is not a vowel")
# 34.Remove the first and last characters from a given string.
t5=input("Enter a text: ")
if(len(t5)<=2):
    print("Character length is too short.")
else:
    print(t5[1:-1])
# 35.Accept two strings and print the one with greater length.
x1=input("enter s1: ")
x2=input("Enter s2: ")
if(len(x1)>len(x2)):
    print(f"{x1} has greater length")
else:
    print(f"{x2} has greater length")
    
# 36.Create a function that returns the square of a given number.
g=int(input("enter a number: "))
print("Square: ",g*g)
# 37.Write a function to identify the maximum among three numbers.
def max(a,b,c):
    if(a>b and a>c):
        print(f"{a} is greater")
    elif (b>a and b>c):
        print(f"{b} is greater")
    else:
        print(f"{c} is greater")
max(10,20,30)
# 38.Develop a function that returns the digit count of a number.
def digit(num):
    
    d=0
    while num>0:
        num//=10
        d+=1
    return d
n=int(input("Enter number: "))
print("digit count: ",digit(n))
 
        
# 39.Create a function to verify whether a number ends with zero.
def zero(n):
    if(n%10==0):
        print("Number ends with zero")
    else:
        print("Number does not end with zero")
number=int(input("Enter a number: "))
zero(number)
# 40.Write a function that calculates the sum of even digits in a number.
def even(num):
    total=0
    
    while(num>0):
        d=num%10
        if(d%2==0):
            total+=d
        num//=10
    return total
e=int(input("Enter a number: "))
print("Total sum of even numbers: ",even(e))
# 41.Build a menu-driven program to perform add, subtract, and multiply operations.
def add(a,b):
    return a+b
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    if(n2==0):
        return "Not divisible by zero"
    else:
        return n1//n2
while True:
    user_1=int(input("1.Add 2.Sub 3.Multiply 4.Division 5.Exit Enter which operation to perform: "))
    match user_1:
        case 1:
            a=int(input("Enter a: "))
            b=int(input("Enter b: "))
            print(add(a,b))
        case 2:
            a=int(input("Enter a: "))
            b=int(input("Enter b: "))
            print(sub(a,b))
        case 3:
            a=int(input("Enter a: "))
            b=int(input("Enter b: "))
            print(mul(a,b))
        case 4:
            a=int(input("Enter a: "))
            b=int(input("Enter b: "))
            print(div(a,b))
        case 5:
            break
        case _:
            print("Invalid choice")
# 42.Create a menu system to check number length or last digit.
while True:
    o1=input("1.Check length 2.Last digit  3.Exit Enter operation to perform: ")
    match o1:
        case 1:
            n=int(input("Enter number: "))
            print("Length: ",len(n))
        case 2:
            n=int(input("Enter number: "))
            print("Length: ",n%10)
        case 3:
            break
        case _:
            print("Invalid choice")
        
    
# 43.Define a function to extract the middle character of a string.
def middle_char(s):
    length = len(s)
    if length % 2 == 0:  # even length
        mid1 = length // 2 - 1
        mid2 = length // 2
        return s[mid1] + s[mid2]  # return both middle characters
    else:  # odd length
        mid = length // 2
        return s[mid]

s1 = input("Enter a string: ")
print("Middle character(s):", middle_char(s1))
# 44.Write a function that determines whether string length is even or odd.
s5=input("Enter a string: ")
if(len(s5)%2==0):
    print("Even length")
else:
    print("odd Length")
# 45.Create a function that returns the position of the first vowel in a string.
def first_vowel_pos(word):
    for index, char in enumerate(word):
        if char.lower() in "aeiou":
            return index  # return index of first vowel
    return -1  # if no vowel found

word = input("Enter a word: ")
position = first_vowel_pos(word)

if position != -1:
    print(f"The first vowel is at position {position}")
else:
    print("No vowel found in the word")

# 46.Count how many times digit 3 appears between numbers 1 and 100.
count=0
for i in range(1,101):
    count+=str(i).count('3')
     
print("3 has appeared ",count," times")
# 47.Print all numbers between 1 and 100 whose digit sum exceeds 10.
def sum(num):
    total=0
    while(num>0):
        total+=(num%10)
        num//=10
    return total
for i in range(1,101):
    if(sum(i)>10):
        print(i,end=" ")
        
# 48.Display numbers from 1 to 500 that have the same first and last digit.
def first(num):
    while(num>9):
        num//=10
    return num
for i in range(1,501):
    if(first(i)==i%10):
        print(i,end=",")
# 49.Remove duplicate characters from a string without changing order.
word=input("Enter a word: ")
result=""
for i in word:
    if i not in result:
        result+=i
print("Removed duplicates: ",result)
        
        

# 50.Design a simple text-based menu system using a loop.
while True:
    print("\n=== Main Menu ===")
    print("1. Say Hello")
    print("2. Add two numbers")
    print("3. Display a message")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Hello! Hope you are having a great day.")
    elif choice == "2":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum:", a + b)
    elif choice == "3":
        msg = input("Enter a message to display: ")
        print("Your message:", msg)
    elif choice == "4":
        print("Exiting... Goodbye!")
        break  # exit the loop
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")

