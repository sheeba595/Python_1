# 1.Display the largest digit present in a given number.
n=int(input("Enter a number: "))
max_num=0
while(n>0):
    digit=n%10
    
    if(digit>max_num):
        max_num=digit
    n//=10
print("Largest digit: ",max_num)
# 2.Show the product of all digits in a number.
n1=int(input("Enter a number: "))
p=1
while(n>0):
    digit=n%10
    p*=digit
    n//=10
print("Product of digits: ",p)
    
# 3.Determine whether the last digit of a number is odd.
n2=int(input("Enter a number: "))
if((n2%10)%2==0):
    print("last digit is even")
else:
    print("Last digit is odd")
# 4.Print the first 10 multiples of a given value.
m=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{i}*{m}={i*m}",end=",")
    
# 5.Identify whether a number lies outside the range 100–200.
e1=int(input("enter number: "))
if(e1<100 and e1>200):
    print("Lies outside the range 100 and 200")
else:
    print("Inside the range")
    
# 6.Extract and print the first digit of a number.
d=int(input("Entr the number: "))
while(d>9):
    d//=10
print("First digit of the number is: ",d)
# 7.Convert total minutes into hours and remaining minutes.
time=int(input("Enter hours: "))
hours=time//60
min=time%60
print("Hours: ",hours)
print("Minutes: ",min)
 
# 8.Check whether two entered numbers share the same last digit.
n1=abs(int(input("enter n1: ")))
n2=abs(int(input("enter n2: ")))
if(n1%10==n2%10):
    print("These tow numbers share the same last digit")
else:
    print("No they dont share the same last digit")
# 9.Calculate the difference between the square and cube of a number.
num=int(input("enter a number: "))
print("diffrenece between square and cube: ",abs((num*num)-(num**3)))
# 10.Determine whether a number is divisible by both 6 and 8.
n=int(input("Entr a number: "))
if(n%6==0 and n%8==0):
    print("number is divisible by both 6 and 8")
else:
    print("number is not divisible by both 6 and 8")
# 11.Display all numbers from 1 to N that are divisible by 3.
a=int(int(input("Enter a number: ")))
for i in range(1,n+1):
    if(i%3==0):
        print(i,end=",")
    
# 12.Print numbers between two given limits.
n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))
for i in range(n1,n2+1):
    print(i,end=",")

# 13.Count how many digits in a number are greater than 5.
d=int(input("Enter a number: "))
count=0
while(d>0):
    temp=d%10
    if(temp>5):
        count+=1
    d//=10
print("Digit count greater than 5:  ",count)
    
    
    
# 14.Reverse a three-digit number only.
 
num = int(input("Enter a three-digit number: "))

if 100 <= abs(num) <= 999:
    last = abs(num) % 10
    middle = (abs(num) // 10) % 10
    first = abs(num) // 100

    reversed_num = last * 100 + middle * 10 + first

    if num < 0:
        reversed_num = -reversed_num

    print("Reversed number:", reversed_num)
else:
    print("Please enter a valid three-digit number.")

# 15.Identify whether a number contains the digit 7.
n=int(input("enter a number: "))
while(n>0):
    temp=n%10
    if(temp==7):
        print("Number contains digit 7")
        break
    else:
        n//=10
else:
    print("Numebr does not contain 7")        
 
# 16.Print numbers from N to 100.
a=int(input("Enter a : "))
for i in range(100,a,-1):
    print(i,end=",")
# 17.Display numbers between 1–50 that are not divisible by 4.
for i in range(1,51):
    if(i%4==0):
        continue
    else:
        print(i,end=',')
# 18.Calculate the average of three numbers.
def avg(*args):
    t=0
    for i in args:
        t+=i
    average=t/len(args)
    print("Average: ",average)
avg(
    int(input("Enter a : ")),
        int(input("Enter b: ")),
       int( input("Enter c: ")))       

# 19.Show whether the sum of two numbers is even or odd.
def add(a,b):
    if (a+b)%2==0:
        print("Even")
    else:
        print("odd")
add(
    int(input("Enter a: ")),
    int(input("Enter b: "))
)
# 20.Determine if a number is a perfect square.
import math
num=int(input("Enter a number: "))
root=int(math.sqrt(num))
if(root*root==num):
    print("Perfect square")
else:
    print("Not a perfect square")
# 21.Convert a string entirely to lowercase without using .lower().
s=int(input("Enter a string: "))
result=""
for i in s:
    if i>="A" and i<="Z":
        result+=chr(ord(i)+32)
    else:
        result+=i
print("Lowercase: ",result)
# 22.Count the number of spaces in a sentence.
s=(input("Enter a string: "))
c=0
for i in s:
    if i==" ":
        c+=1
print("Number of spaces: ",c)
# 23.Replace all occurrences of letter 'a' with '@'.
s=input("Enter a string: ")
res=""
for i in s:
    if(i=="a"):
        res+="@"
    else:
        res+=i
print("occurrences of letter 'a'",res)
        
    
# 24.Display the ASCII value of a character.
s=input("Enter a character: ")
print("Ascii value: ",ord(s))
# 25.Convert an ASCII value into its character form.
ascii=int(input("Enter ascii value: "))
print("ASCII value into its character form.",chr(ascii))
# 26.Count how many numbers between 1–150 are divisible by 5 and 7.
count=0
for i in range(1,151):
    if(i%5==0 and i%7==0):
        count+=1
print("numbers between 1–150 are divisible by 5 and 7",count)
# 27.Print numbers between 1–200 whose last digit is 3.
for i in range(1,201):
    if(i%10==3):
        print(i,end=",")

# 28.Calculate the sum of odd numbers between 1–100.
f=0
for i in range(1,101):
    if(i%2==0):
        continue
    else:
        f+=i
print("Sum of odd numbers: ",f)
    
# 29.Count how many numbers between 1–100 have more than one digit.
def count(n):
    n=abs(n)
    count=0
    while(n>0):
        n//=10
        count+=1
    return count>1
t=0
for i in range(1,101):
   
    if count(i):
        t+=1
print("numbers between 1–100 have more than one digit.",t)
        
# 30.Identify numbers between 10–99 whose digits add up to 9.
def nine(num):
    temp=0
    while(num>0):
        temp+=num%10
        num//=10
    return temp==9
        
for i in range(10,100):
    if(nine(i)):
        print(i,end=",")
    
# 31.Print all two-digit numbers where both digits are even.
def first(n):
    while(n>9):
        n//=10
    return n
def two(n):
    n=abs(n)
    count=0
    while(n>0):
        n//=10
        count+=1
    return count==2
for i in range(1,100):
    if two(i):
        if ((i%10)%2==0 and first(i)%2==0):
            print(i,end=",")
            
    
# 32.Determine how many times digit 5 appears in a number.
def five(num):
    count=0
    while(num>0):
        temp=num%10
        if(temp==5):
            count+=1
        num//=10
    return count
print("five appeared: ",five(int(input("Enter a number: ")))," times")
        
# 33.Remove all vowels from a string.
s=input("Enter a string: ")
res=""
for i in s:
    if i in "aeiou":
        continue
    else:
        res+=i
print(".Remove all vowels from a string.",res)
        

# 34.Count words that contain more than 3 letters.
s=input("enter a string: ")
word=s.split()
total=0
for w in word:
    if(len(word)>3):
        total+=1
print('words that contain more than 3 letters',total)
        
# 35.Extract all numeric characters from a mixed string.
s=input("Enter a string: ")
r=""
for i in s:
    if i.isdigit():
        r+=i
    else:
        continue
print("Extract all numeric characters from a mixed string",r)
    
# 36.Create a function that returns the greater of two numbers.
def greater(a,b):
    if(a>b):
        return a
    else:
        return b
print("Number greater is : ",greater(
    int(input("enter a : ")),
    int(input("enter b: "))
))
# 37.Build a function that checks if a string ends with a digit.
def string(s):
    return s[-1].isdigit()
print("string ends with a digit",string(
    input("Enter a string: ")
))
        
# 38.Write a function that calculates the total of digits in a number.
def total(n):
    total=0
    while(n>0):
        total+=n%10
        n//=10
    return total
print("total of digits in a number",total(int(input("Enter a number: "))))
        
# 39.Create a function that swaps first and last characters of a string.
def swap(s):
     if(len(s)>2):
         return s[-1]+s[1:-1]+s[0]
print(" swaps first and last characters of a string",swap(input("Enter a string: ")))
        
# 40.Develop a function that returns the count of consonants in a string.
def consonant(s):
    total=0
    for i in s:
         if i.isalpha() and i.lower() not in "aeiou":
            total+=1
    return total
print("count of consonants in a string.",consonant(input("Enter a string: ")))
            
        
# 41.Design a program that repeatedly accepts numbers until 0 is entered and then prints their total.
def prg():
    total = 0
    while True:
        a = int(input("Enter a number: "))
        if a == 0:
            break
        total += a
    return total

print("Total:", prg())


        
        
# 42.Create a menu-driven program to calculate simple interest.
# 42.Create a menu-driven program to calculate simple interest.

while True:
    print("\n---- MENU ----")
    print("1. Calculate Simple Interest")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        p = float(input("Enter Principal: "))
        r = float(input("Enter Rate of Interest: "))
        t = float(input("Enter Time: "))

        si = (p * r * t) / 100
        print("Simple Interest =", si)

    elif choice == 2:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please select 1 or 2.")


# 43.Build a function that verifies whether a string contains only uppercase letters.
def upper(s):
    for i in s:
        if i<"A" or i>"Z":
            return False
    return True
        
print("string contains only uppercase letters",
      upper(input("Enter  a string: ")))
            
# 44.Write a program to count how many numbers between 1–100 are multiples of 11.
integer=0
for i in range(1,101):
    if(i%11==0):
        integer+=1
print("numbers between 1–100 are multiples of 11 count: ",integer)
    
    
# 45.Design a loop that prints numbers whose square is less than 500.
print("Numbers whose square is less than 500:")

i = 1
while i * i < 500:
    print(i, end=", ")
    i += 1

# 46.Construct a simple password validator (minimum 6 characters, must contain digit).
pwd=input("Enter password for validation: ")
hasdigit=False
for i in pwd:
    if i.isdigit():
        hasdigit=True
        break
if len(pwd)>=6 and hasdigit:
    print("Password valid")
else:
    print("Not valid")
# 47.Build a program that prints alternate characters from a string.
s = input("Enter a string: ")

print("Alternate characters:", s[::2])

# 48.Create a function that returns the smallest digit in a number.
def small(n):
    min_digit=n%10
    n//=10
    while(n>0):
        temp=n%10
        if(temp<min_digit):
            min_digit=temp
        n//=10
    return (f"Smallest digit: {min_digit}")
print(small(int(input("Enter a number: "))))
        
# 49.Write a program that calculates how many numbers between 1–300 end with digit 2.
cal=0
for i in range(1,301):
    if(i%10==2):
        cal+=1
print("numbers between 1–300 end with digit 2.",cal)
        
# 50.Develop a looping program that keeps asking for a password until the correct one is entered.
password="1234"
while True:
    pwd=input("Enter password: ")
    if (pwd==password):
        break
    else:
        print("Wrong password .Try again")
    
