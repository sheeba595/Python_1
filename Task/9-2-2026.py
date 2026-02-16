# 1.Store your name and age in variables and print them.
name=input("Ente your name: ")
age=int(input("Enter age: "))
print(f"Name: {name},Age: {age}")
# 2.Input two numbers and display their sum.
n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))
print(f"Sum: {n1+n2}")
# 3.Convert a float number into an integer.
n3=float(input("Enter a number: "))
print(f"Integer number: {int(n3)} ")
# 4.Concatenate a string and an integer using type casting.
name_1=input("Enter name: ")
age_1=int(input("Enter age: "))
print(f"{name}:{str(age)}")
# 5.Store an int, float, and string and print their data types.
num=10
decimal=12.9
sentence='hello'
print(type(num))
print(type(decimal))
print(type(sentence))
# 6.Input two numbers and display all arithmetic operations.
num_1=int(input("Enter n1: "))
num_2=int(input("Enter n2: "))
print(f"Add: {n1+n2}")
print(f"Sub: {n1-n2}")
print(f"Mul: {n1*n2}")
if(num_2==0):
    print("Not divisible by zero")
else:
    print(f"Division: {n1/n2}")



# 7.Check whether a number is even or odd.
odd=int(input("Enter a nm=umber: "))
if(odd%2==0):
    print("Even")
else:
    print("odd")
# 8.Check whether a number is divisible by both 3 and 5.
div=int(input("Enter a number: "))
if(div%3==0 and div%5==0):
    print(f"{div} divisible by both 3 and 5")
else:
    print(f"{div} not divisible by 3 and 5")
# 9.Find the greater of two numbers.
g1=int(input("Enter n1: "))
g2=int(input("Enter n2: "))
if(g1>g2):
    print(f"{g1} is larger")
else:
    print(f"{g2} is larger")
# 10.Swap two numbers without using a third variable.
v1=int(input("Enter v1: "))
v2=int(input("Enter v2: "))
print(f"Before swapping: v1:{v1},v2:{v2}")
v1=v1+v2
v2=v1-v2
v1=v1-v2
print(f"After swapping: v1:{v1},v2:{v2}")
# 11.Input marks and print Pass or Fail.
mark=int(input("Enter mark: "))
if(mark>90):
    print("Grade A")
elif(mark>80 and mark<=90):
    print("Grade B")
elif(mark>=50  and mark<=80):
    print("Grade C")
else:
    print("Fail")
    
# 12.Input age and check voting eligibility.
age_3=int(input("Enter age: "))
if(age>=18):
    print("Eligible for voting")
else:
    print("Not eligible")
# 13.Input temperature and print Hot / Normal / Cold.
temp=int(input('Enter temperature: '))
if(temp>35):
    print("Hot")
elif(temp>=20 and temp<=35):
    print("Normal")
else:
    print("Cold")
# 14.Check whether a number is positive, negative, or zero.
n=int(input("Enter a number: "))
if(n<0):
    print("Negative")
elif(n>0):
    print("Positive")
else:
    print("Zero")
# 15.Create a simple calculator using if–elif.
user=int(input("Enter operation to perform :  1.Add 2.Subtract 3.Multiply 4.Divide"))
if(user==4):
    num_1=int(input("Enter n1: "))
    num_2=int(input("Enter n2: "))
    print(print(f"Add: {n1+n2}"))
elif(user==2):
    num_1=int(input("Enter n1: "))
    num_2=int(input("Enter n2: "))
    print(print(f"Subtraction: {n1-n2}"))
elif(user==3):
    num_1=int(input("Enter n1: "))
    num_2=int(input("Enter n2: "))
    print(print(f"Product: {n1*n2}"))
elif(user==4):
    num_1=int(input("Enter n1: "))
    num_2=int(input("Enter n2: "))
    if(num_2==0):
        print("Not divisible by zero")
    else:
        print(f"Division: {n1/n2}")
else:
    print("Invalid choice")

# 16.Print numbers from 1 to 10.
for i in range(1,11):
    print(i,end=" ")
# 17.Print numbers from 10 to 1.
for i in range(10,0,-1):
    print(i,end=" ")
# 18.Print the multiplication table of a given number.
m=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{i}*{m}={i*m}")
# 19.Find the sum of first N natural numbers.
sum=0
s=int(input("Enter number: "))
for i in range(1,s+1):
    sum+=i
print(f"Sum of {s} antural numbers: {sum}")
# 20.Count the number of even numbers between 1 and 100.
count=0
for i in range(1,101):
    if(i%2==0):
        count+=1
print(f"Count of even numbers between 1 and 100 is: {count}")
# 21.Find the length of a string.
string=input("Enter a string: ")
print(len(string))
# 22.Convert a string to uppercase and lowercase.
word=input("Enter a word: ")
print("Lowercase: ",word.lower())
print("Uppercase: ",word.upper())
# 23.Count vowels in a string.
char=input("Enter a word: ")
vowel=0
for i in char:
    for j in "aeiou":
        if(i==j):
            vowel+=1
print(f"Vowel count: {vowel}")
            
# 24.Reverse a string.
w1=input("Enter a string: ")
print("Reversal of a string: ",w1[::-1])
# 25.Check whether a string is a palindrome.
w2=input("Enter a word: ")
if(w2.lower()==w2[::-1].lower()):
    print("Palindrome")
else:
    print("Not a Palindrome")
# 26.Find the largest of three numbers.
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
if(a>b and a>c):
    print(f"{a} is larger")
elif (b>a and b>c):
    print(f"{b} is larger")
else:
    print(f"{c} is larger")
# 27.Check whether a year is a leap year.
year=int(input("Enter a year: "))
if((year%4==0 and year%100!=0) or year%400==0) :
    print(f"{year} is a leap year")
else:
    print(f"{year} not a leap year")
# 28.Print all even numbers between two given numbers.
num1=int(input("Enter n1: "))
num2=int(input("Enter n2: "))
for i in range(num1,num2+1):
    if(i%2==0):
        print(i,end=",")
        
    # 29.Check whether a number is prime.
    prime=int(input("Enter a number: "))
    isPrime=True
    if(prime<=1):
        print("Not a prime number")
    else:
        for i in range(2,int(prime/2)+1):
    
            if(prime%i==0):
                isPrime=False
                break
        if isPrime:
            print(f"{prime} is a prime number")
        else:
            print(f"{prime} is not a prime number")
    
# 30.Print all prime numbers between 1 and 100.
u1=int(input("Enter n1: "))
u2=int(input("Enter n2: "))

for i in range(u1,u2+1):
    is_prime=True
    if(i<=1):
        continue
    for j in range(2,int(i/2)+1):
        if(i%j==0):
            is_prime=False
            break
    if is_prime:
        print(i,end=" ")
    
        
# 31.Find the factorial of a number.
f=int(input("Enter a number: "))
fact=1
for i in range(f,1,-1):
    fact*=i
print("Factorial: ",fact)
 
    
# 32.Print the Fibonacci series up to N terms.
N=int (input("How many fibanocci terms you want: "))
e1,e2=0,1
if(N<0):
    print("Enter a positive number")
elif N==1:
    print(e1)
else:
    print(e1,e2,end=" ")
    for i in range(2,N):
        e3=e1+e2
        print(e3,end=" ")
        e1=e2
        e2=e3

 
    
# 33.Count the number of digits in a number.
def digit(number):
    d=0
    if(number==0):
        d=1
    while(number>0):
        number//=10
        d+=1
    return(f"Digit count: {d}")
nb=int(input("Enter a  number: "))
print("Count: ",digit(nb))

# 34.Reverse a number using a loop.

def reverse(nb):
    rev=0
    while(nb>0):
        digit=nb%10
        rev=(rev*10)+digit
        nb//=10
    return("reversed num is : ",rev)
num = int(input("Enter a number: "))
print("Reversed number is:", reverse(num))
# 35.Check whether a number is an Armstrong number.
n = int(input("Enter a number: "))
num = n
sum = 0

num_digits = len(str(n))

while num > 0:
    digit = num % 10
    sum += digit ** num_digits
    num //= 10

if sum == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")

    

# 36.Count the number of words in a sentence.
word=input("Enter a sentence: ")
w3=word.split()
w3_len=len(w3)
print("Word count: ",w3_len)


# 37.Find the frequency of each character in a string.
string2=input("Enter a  string: ")
freq={}
for i in string2:
    if i in string2:
        freq[i]+=1
    else:
        freq[i]=1
for key,value in freq.items():
    print(f"{key}:{value}")
# 38.Remove spaces from a string.
s1=input("Enter a string: ")
print(s1.strip())
# 39.Replace all vowels in a string with *.
s2=input("Enter a word: ")
s3=""
for i in s2:
     if i.lower() in "aeiou":
         s3+="*"
     else:
        s3+=i
         
print(s3)

 
# 40.Find the longest word in a sentence.
w2=input("Enter a string: ")
max_lenght=0
longest_word=""
new_w2=w2.split()
for i in new_w2:
    if(len(i)>max_lenght):
        longest_word=new_w2
        max_lenght=len(i)
print("Longest word: ",longest_word)
        

# 41.Write a function to add two numbers.
def add(n1,n2):
    return n1+n2
print(add(10,20))
# 42.Write a function to check whether a number is even or odd.
def Odd(n):
    if(n%2==0):
        return "Even"
    else:
        return "Odd"
print(Odd(11))
# 43.Write a function to find the factorial of a number.
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        fact=1
        for i in range(2,n+1):
            fact*=i
        return fact
print(factorial(5))
# 44.Write a function to check whether a string is a palindrome.
def palindrome(string):
    if string.lower()==string[::-1].lower():
        return "Palindrome"
    else:
        return "Not a Palindrome"
print(palindrome("Malayalam"))
# 45.Write a function to count vowels in a string.
def vowel_count(string):
    count=0
    for i in string:
         
            if(i.lower() in "aeiou"):
                count+=1
    return f"Vowel Count: {count}"
                
# 46.Create a simple login system using username and password.
username=input("Enter username: ")
password=input("Enter password: ")
if(username=="123Abc" and password=="123478"):
    print(f"Logged in successfully")
    
# 47.Create a menu-driven calculator using functions.
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
# 48.Create a student marks calculator using functions.
def total_marks(marks):
    sum=0
    for i in marks:
        sum+=i
    return sum
def average(marks):
    avg= total_marks(marks)/len(marks)
    return avg
def grade_cal(marks):
    if(average(marks)>=90):
        return "Grade A"
    elif (average(marks)>=80):
        return "Grade B"
    elif (average(marks)>=50):
        return "Grade C"
    else:
        return "Fail"
marks=[]
for i in range(1,6):
    m=int(input("Enter your marks: "))
    marks.append(m)
print("Total : ",total_marks(marks))
print("Average: ",average(marks))
print("Grade: ",grade_cal(marks))
    
        

# 49.Create a simple ATM simulation program.
balance=1000
def deposit(money):
    global balance
    balance+=money
    print("Money deposited successfully!")
def withdraw(money):
    global balance
    if(balance<money):
        print("insufficient balance")
    else:
        balance-=money
        print("Remaining balance: ",balance)
        print("Amount withdrawed successfully!")
def show():
    global balance
    print("Balance: ",balance)
balance=1000
while True:
    m1=int(input("1.Deposit money  2.Withdraw money 3.Show balance 4.Exit"))
    match m1:
        case 1:
            money=int(input("Enter amount for deposit: "))
            deposit(money)
        case 2:
            money=int(input("Enter amount for withdrawal: "))
            withdraw(money)
        case 3:
            show()
        case 4:
            break
        case _:
            print("Invalid choice")



# 50.Create a password strength checker program.
pwd=input("Enter password: ")
hasUpper=False
hasLower=False
hasDigit=False
isSpecial=False
special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>/?"
for i in pwd:
    if i.isupper():
        hasUpper=True
    elif i.islower():
        hasLower=True
    elif i.isdigit():
        hasDigit=True
    elif i in special_chars:
        isSpecial=True
if(hasUpper and hasLower and hasDigit and isSpecial and (len(pwd)>=8)):
    print("Strong password")
else:
    print("Weak password.")
    
    
        