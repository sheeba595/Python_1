# 1.Print all numbers between 1–100 divisible by 7.
print("numbers between 1–100 divisible by 7 ")
for i in range(1,101):
    if(i%7==0):
        print(i,end=",")
# 2.Find the sum of digits of a number using loop.
def digit(n):
    t=0
    while(n>0):
        t+=n%10
        n//=10
    return t
print("sum of digits of a number: ",digit(int(input("Enter a number: "))))

# 3.Swap two numbers without using third variable.
def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return f"After swap {a} , b:{b}"
print(swap(
     int(input("Enter a : ")),int(input("Enter b : "))))
# 4.Check whether a number is positive, negative, or zero.
def pos(i):
    if i<0:
        return "Negative"
    elif i>0:
        return "positve"
    else:
        return "Neutral"
print(pos(int(input("Enter a number: "))))
# 5.Print all even numbers between two given limits.
l1=int(input("Enter limit 1: "))
l2=int(input("enter limit 2: "))
for i in range(l1,l2):
    print(i,end=" ,")
# 6.Count how many times a digit appears in a number.
def appear(n,digit):
    total=0
    while(n>0):
        d=n%10
        if d==digit:
            count+=1
        n//=10
    return count
print("Digit appears: ",
      appear(int(input("Enter the number: ")),
             int(input("Enter digit you want to count: "))),"times")

# 7.Find the smallest of three numbers using conditions only.
a=int(input("Enter a : "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
if(a<b and a<c):
    print(f"{a} is smaller")
elif (b<a and b<c):
        print(f"{b} is smaller")
else:
        print(f"{c} is smaller")


    
# 8.Reverse a string without slicing.
string=input("Enter a string: ")
rev=""
for i in string:
    rev=i+rev
print("Reversed string: ",rev)
    
# 9.Check whether a number ends with 5.
def end(n):
    if abs(n%10)==5:
        return True
    else:
        return False
print("number ends with 5: ",end(int(input("Enter a number: "))))
# 10.Print first 10 multiples of a given number.
def table(n):
    for i in range(1,11):
        print(f"{i}*{n}={i*n}")
print(table(int(input("Enter a number for table: "))))
# 11.Print numbers from n to 1 (reverse order).
def rev(n):
    for i in range(n,1,-1):
        print(i,end=",")
print("Numbers in reversed: ",rev(int(input("Enter a number: "))))
# 12.Find factorial using loop.
def fact(n):
    fact=1
    for i in range(2,n+1):
        fact*=i
    return fact
r=int(input("Enter a number: "))
sum=0
while(r>0):
    
    sum+=fact(r%10)
    r//=10
print("Factorial: ",sum)
        
# 13.Print sum of even numbers up to n.
def sum(n):
    total=0
    for i in range(1,n+1):
        if(i%2==0):
            total+=i
    return total
print("sum of even numbers up to n : ",sum(int(input("Enter n: "))))
    
        
# 14.Print square of numbers from 1–20.
for i in range(1,21):
    print(i**2,end=",")

# 15.Count how many numbers between 1–100 are divisible by 3 and 5.
count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count+=1
print("numbers between 1–100 are divisible by 3 and 5: ",count)
# 16.Print pattern:
# 1
# 12
# 123
# 1234
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
# 17.Print star pattern increasing left aligned.
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
# 18.Print numbers skipping multiples of 4.
print("numbers skipping multiples of 4")
for i in range(1,101):
    if(i%4==0):
        continue
    else:
        print(i,end=",")
        
    
# 19.Find product of digits of a number.
def mul_digit(n):
    total=1
    while(n>0):
        total*=n%10
        n//=10
    return total
print("product of digit: ",mul_digit(int(input("Enter a number: "))))
        
# 20.Print ASCII values of A–Z.
for i in range(ord("A"),ord("Z")+1):
    print(chr(i),"=",i)
# 21.Count vowels in a string.
def vowel(s):
    v=0
    for i in s:
        if i in "aeiou":
            v+=1
    return v
print("Vowel count: ",vowel(input("Enter a string: ")))
        
# 22.Count consonants in a string.
def consonant(s):
    v=0
    for i in s:
        if i.lower() not in "aeiou" and i.isalpha():
            v+=1
    return v
print("Vowel count: ",consonant(input("Enter a string: ")))
# 23.Remove all spaces from a string.
s=input("Enter a string: ")
print("string without spaces: ",s.strip())
# 24.Check whether string contains only digits.
s=(input("Enter a string: "))
print("string contains only digits: ",s.isdigit())
# 25.Find length of string without using len().
s=input("Enter  a string: ")
c=0
for i in s:
    c+=1
print("Lenght of the string: ",c)
    
# 26.Convert lowercase letters to uppercase manually.
s=input("Enter a string: ")
t=""
for i in s:
    if i>="a" and i<="z":
        t+=chr(ord(i)-32)
    else:
        t+=i
print("Lowercase to uppercase:", t)
        
 
    
# 27.Count words in a sentence.
s=input("Enter a string: ")
s1=s.split()
print("Words in a sentence: ",len(s1))
# 28.Replace all vowels with *.
s=input("Enter a string: ")
y=""
for i in s:
    if i.lower() in "aeiou":
        y+="*"
    else:
        y+=i
print("vowels with replacement: ",s)
    
# 29.Check whether string starts and ends with same character.
s=input("Enter a string: ")
if(s[0]==s[-1]):
    print("Starts and end with same character")
else:
    print("does not Starts and end with same character")
# 30.Find index of first occurrence of a character (without using index()).
s = input("Enter a string: ")
ch = input("Enter character to find: ")

for i in range(len(s)):
    if s[i] == ch:
        print("First occurrence:", i)
        break
else:
    print("Character not found")

        
# 31.Create list of squares from 1–15.
l=[]
for i in range(1,16):
    l.append(i**2)
print("list of squares from 1–15",l)
# 32.Find largest element in a list (without max()).
l1=[1, 4, 9, 16, 25, 36, 49, 64]
max=l1[0]
for i in range(1,len(l1)):
    if max<l1[i]:
        max=l1[i]
print("largest element: ",max) 
# 33.Remove duplicates from list.
l2=[1, 4, 9, 16, 25, 36, 49, 64,1,4,6,2,64]
print("Removes duplicates: ",set(l2))
# 34.Find sum of all elements in list.
l1=[1, 4, 9, 16, 25, 36, 49, 64]
s=0
for i in range(1,len(l1)):
    s+=l1[i]
print("Sum of elements: ",s)
    
# 35.Count even numbers in list.
l1=[1, 4, 9, 16, 25, 36, 49, 64]
c=0
for i in range(1,len(l1)+1):
    if(i%2==0):
        c+=1
print("even numbers in list: ",c)
# 36.Reverse a list without using reverse().
l1=[1, 4, 9, 16, 25, 36, 49, 64]
for i in range(len(l1)-1,0,-1):
    print(l1[i],end=",")
# 37.Insert element at specific position.
l1 = [1, 4, 9, 16, 25, 36, 49, 64]

def insert(n, value):
    l1.insert(n, value)
    return l1

print(insert(int(input("Enter index: ")),
             int(input("Enter value: "))))

    
    
# 38.Remove all negative numbers from list.
l1 = [1, -4, 9, -16, 25, -36, 49, 64]
result=[]
for i in range(len(l1)):
    if(l1[i]>=0):
        result.append(l1[i])
print("Afeter removing negative numbers: ",result)
# 39.Find average of list elements.
l1 = [1, 4, 9, 16, 25, 36, 49, 64]
print("Average of elements: ",sum(l1)/len(l1))
# 40.Merge two lists element-wise.
l1 = [1, 2, 3]
l2 = [4, 5, 6]

merged = []

for i in range(len(l1)):
    merged.append(l1[i] + l2[i])

print("Merged list:", merged)

# 41.Create function to check even or odd.
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(int(input("Enter a number: "))))

# 42.Function to return sum of two numbers.
def add(a, b):
    return a + b

print("Sum:", add(10, 20))

# 43.Function to check palindrome string.
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome(input("Enter string: ")))

# 44.Function to return list of prime numbers up to n.
def primes_upto(n):
    prime_list = []
    for num in range(2, n+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_list.append(num)
    return prime_list

print(primes_upto(20))

# 45.Function to count uppercase letters in string.
def count_upper(s):
    count = 0
    for i in s:
        if i.isupper():
            count += 1
    return count

print(count_upper(input("Enter string: ")))

# 46.Create simple calculator using functions.
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+ - * /): ")

if op == "+": print(add(a,b))
elif op == "-": print(sub(a,b))
elif op == "*": print(mul(a,b))
elif op == "/": print(div(a,b))

# 47.Build number guessing game (loop + random).
import random

num = random.randint(1, 10)

while True:
    guess = int(input("Guess number (1-10): "))
    if guess == num:
        print("Correct!")
        break
    else:
        print("Try again")

# 48.Create menu-driven program for basic arithmetic.
while True:
    print("1.Add 2.Sub 3.Multiply 4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 4:
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Result:", a + b)
    elif choice == 2:
        print("Result:", a - b)
    elif choice == 3:
        print("Result:", a * b)

# 49.Create mini student result program (total + grade).
m1 = int(input("Enter mark1: "))
m2 = int(input("Enter mark2: "))
m3 = int(input("Enter mark3: "))

total = m1 + m2 + m3
avg = total / 3

if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Total:", total)
print("Grade:", grade)

# 50.Build simple login check (hardcoded username & password).
username = "admin"
password = "1234"

u = input("Enter username: ")
p = input("Enter password: ")

if u == username and p == password:
    print("Login Successful")
else:
    print("Invalid credentials")

