#1. Get user name and age
name = input("Enter name: ")
age = int(input("Enter age: "))
print(name, age)

#2. Input two numbers and print sum
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(a + b)

#3. Convert integer to float
x = int(input("Enter integer: "))
print(float(x))

#4. Concatenate string and number
name = "Age is "
age = 20
print(name + str(age))

#5. Store different datatypes & print type
a = 10
b = 2.5
c = "Python"
d = True
print(type(a), type(b), type(c), type(d))

#6. Arithmetic operations
a = int(input())
b = int(input())
print(a+b, a-b, a*b, a/b)

#7. Even or Odd
n = int(input())
print("Even" if n % 2 == 0 else "Odd")

#8. Larger of two numbers (ternary)
a = int(input())
b = int(input())
print(a if a > b else b)

#9. Divisible by 3 and 5
n = int(input())
print("Yes" if n%3==0 and n%5==0 else "No")

#10. Increment & Decrement
x = 5
x += 1
print(x)
x -= 1
print(x)

#11. Pass or Fail
marks = int(input())
print("Pass" if marks >= 40 else "Fail")

#12. Voting eligibility
age = int(input())
print("Eligible" if age >= 18 else "Not Eligible")

#13. Temperature check
t = int(input())
if t > 30:
    print("Hot")
elif t >= 20:
    print("Normal")
else:
    print("Cold")

#14. Positive / Negative / Zero
n = int(input())
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# 15. Simple calculator
a = int(input())
b = int(input())
op = input()
if op == '+': print(a+b)
elif op == '-': print(a-b)
elif op == '*': print(a*b)
elif op == '/': print(a/b)

# 16. Print 1 to 10
for i in range(1, 11):
    print(i)

# 17. Print 10 to 1
for i in range(10, 0, -1):
    print(i)

# 18. Multiplication table
n = int(input())
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

# 19. Sum of first n natural numbers
n = int(input())
print(n*(n+1)//2)

# 20. Count even numbers (1–50)
count = 0
for i in range(1, 51):
    if i % 2 == 0:
        count += 1
print(count)

# 21. Length of string
s = input()
print(len(s))

# 22. Uppercase & Lowercase
s = input()
print(s.upper())
print(s.lower())

# 23. Count vowels
s = input().lower()
count = 0
for ch in s:
    if ch in "aeiou":
        count += 1
print(count)

# 24. Palindrome check
s = input()
print("Palindrome" if s == s[::-1] else "Not Palindrome")

# 25. Tax calculation
salary = int(input())
if salary <= 250000:
    tax = 0
elif salary <= 500000:
    tax = salary * 0.05
else:
    tax = salary * 0.1
print(tax)

# 26. Electricity bill
units = int(input())
if units <= 100:
    bill = units * 2
elif units <= 300:
    bill = units * 3
else:
    bill = units * 5
print(bill)

# 27. Leap year
year = int(input())
print("Leap" if year%4==0 and (year%100!=0 or year%400==0) else "Not Leap")

# 28. Largest of three
a,b,c = map(int, input().split())
print(max(a,b,c))

# 29. Grade based on marks
m = int(input())
if m >= 90: print("A")
elif m >= 70: print("B")
elif m >= 40: print("C")
else: print("Fail")

# 30. Factorial
n = int(input())
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

# 31. Fibonacci series
n = int(input())
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a+b

# 32. Prime check
n = int(input())
flag = True
for i in range(2, n):
    if n % i == 0:
        flag = False
        break
print("Prime" if flag and n>1 else "Not Prime")

# 33. Prime numbers (1–100)
for n in range(2, 101):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)

# 34. Count digits
n = input()
print(len(n))

# 35. Count words
s = input()
print(len(s.split()))

# 36. Character frequency
s = input()
for ch in set(s):
    print(ch, ":", s.count(ch))

# 37. Remove spaces
s = input()
print(s.replace(" ", ""))

# 38. Replace vowels with *
s = input()
for v in "aeiouAEIOU":
    s = s.replace(v, "*")
print(s)

# 39. Longest word
s = input().split()
print(max(s, key=len))

# 40. Add two numbers
def add(a, b):
    return a + b
print(add(2, 3))

# 41. Factorial using function
def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
print(fact(5))

#42. Reverse string
def reverse(s):
    return s[::-1]
print(reverse("python"))

# 43. Prime check function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 44. Count vowels function
def count_vowels(s):
    return sum(1 for ch in s if ch in "aeiouAEIOU")

# 45. ATM Simulation
balance = 5000
amt = int(input("Withdraw: "))
if amt <= balance:
    balance -= amt
print("Balance:", balance)

# 46. Login system
user = "admin"
pwd = "1234"
u = input()
p = input()
print("Login Success" if u==user and p==pwd else "Invalid")

# 47. Menu-driven calculator
def calc(a,b,op):
    if op=='+': return a+b
    if op=='-': return a-b
    if op=='*': return a*b
    if op=='/': return a/b

# 48. Student marks using function
def result(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg

# 49. Password strength checker
pwd = input()
if len(pwd)>=8 and any(ch.isdigit() for ch in pwd):
    print("Strong")
else:
    print("Weak")

# 50. Reverse a string
s = input()
print(s[::-1])