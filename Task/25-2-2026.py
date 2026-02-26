# 1. Even or Odd
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

# 2. Larger of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Larger:", max(a,b))

# 3. Pass or Fail
marks = int(input("Enter marks: "))
print("Pass" if marks >= 35 else "Fail")

# 4. Factorial
n = int(input("Enter a number: "))
fact = 1
for i in range(1,n+1): fact *= i
print("Factorial:", fact)

# 5. Reverse String
s = input("Enter a string: ")
print("Reversed:", s[::-1])

# 6. Even Numbers from List
nums = list(map(int,input("Enter numbers: ").split()))
print("Even numbers:", [x for x in nums if x%2==0])

# 7. Sum of Digits
num = int(input("Enter a number: "))
print("Sum of digits:", sum(int(d) for d in str(num)))

# 8. Leap Year Check
year = int(input("Enter year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("Leap Year")
else:
    print("Not Leap Year")

# 9. Smallest Element in List
nums = list(map(int,input("Enter numbers: ").split()))
print("Smallest:", min(nums))

# 10. Palindrome Check
word = input("Enter a word: ")
print("Palindrome" if word == word[::-1] else "Not Palindrome")

# 11. Prime Numbers from List
def is_prime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True
nums = list(map(int,input("Enter numbers: ").split()))
print("Primes:", [x for x in nums if is_prime(x)])

# 12. Sort Three Numbers
nums = list(map(int,input("Enter 3 numbers: ").split()))
nums.sort()
print("Ascending:", nums)

# 13. Count Words in Sentence
sentence = input("Enter a sentence: ")
print("Word count:", len(sentence.split()))

# 14. Remove Duplicates
nums = list(map(int,input("Enter numbers: ").split()))
print("Updated list:", list(dict.fromkeys(nums)))

# 15. Fibonacci Sequence
N = int(input("Enter N: "))
fib = [0,1]
for i in range(2,N):
    fib.append(fib[-1]+fib[-2])
print("Fibonacci sequence:", fib[:N])

# 16. Average Marks
marks = list(map(int,input("Enter marks: ").split()))
print("Average:", sum(marks)/len(marks))

# 17. Vowels and Consonants
s = input("Enter string: ").lower()
vowels = sum(1 for c in s if c in 'aeiou')
consonants = sum(1 for c in s if c.isalpha() and c not in 'aeiou')
print("Vowels:", vowels, "Consonants:", consonants)

# 18. Check Anagrams
s1 = input("Enter first string: ").replace(" ","").lower()
s2 = input("Enter second string: ").replace(" ","").lower()
print("Anagram" if sorted(s1) == sorted(s2) else "Not Anagram")

# 19. Second Largest Element
nums = list(map(int,input("Enter numbers: ").split()))
unique_nums = list(set(nums))
unique_nums.sort()
print("Second Largest:", unique_nums[-2] if len(unique_nums)>1 else "Not enough elements")

# 20. Longest Word in Sentence
sentence = input("Enter sentence: ")
words = sentence.split()
print("Longest word:", max(words,key=len))

# 21. Common Elements from Two Lists
l1 = list(map(int,input("List 1: ").split()))
l2 = list(map(int,input("List 2: ").split()))
print("Common elements:", list(set(l1)&set(l2)))

# 22. Move Zeros to End
nums = list(map(int,input("Enter numbers: ").split()))
non_zero = [x for x in nums if x!=0]
zeros = [0]*nums.count(0)
print("Updated list:", non_zero+zeros)

# 23. Login Simulation
username = "user"
password = "pass"
u = input("Username: ")
p = input("Password: ")
print("Login Successful" if u==username and p==password else "Login Failed")

# 24. Highest Scorer from Dictionary
students = {'Alice':90,'Bob':85,'Charlie':95}
max_scorer = max(students,key=students.get)
print("Highest Scorer:", max_scorer, students[max_scorer])

# 25. Armstrong Number
num = int(input("Enter number: "))
order = len(str(num))
sum_pow = sum(int(d)**order for d in str(num))
print("Armstrong" if sum_pow==num else "Not Armstrong")

# 26. Frequency of Elements
nums = list(map(int,input("Enter numbers: ").split()))
freq = {x:nums.count(x) for x in set(nums)}
print("Frequency:", freq)

# 27. First Non-Repeating Character
s = input("Enter string: ")
for c in s:
    if s.count(c)==1:
        print("First non-repeating:", c)
        break
else:
    print("No non-repeating character")

# 28. Flatten Nested List
nested = [[1,2],[3,4],[5]]
flat = [item for sub in nested for item in sub]
print("Flattened list:", flat)

# 29. ATM Withdrawal Simulation
balance = 1000
amt = int(input("Enter withdrawal amount: "))
if amt <= balance:
    balance -= amt
    print("Withdrawal successful. Remaining balance:", balance)
else:
    print("Insufficient balance.")

# 30. Multiplication Tables 1 to 5
for i in range(1,6):
    print(f"Table of {i}")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()

# 31. Character Frequency in Sentence
sentence = input("Enter sentence: ").replace(" ","")
freq = {}
for c in sentence:
    freq[c] = freq.get(c,0)+1
print("Frequency:", freq)

# 32. Pairs with Target Sum
nums = list(map(int,input("Enter numbers: ").split()))
target = int(input("Enter target: "))
pairs = [(nums[i],nums[j]) for i in range(len(nums)) for j in range(i+1,len(nums)) if nums[i]+nums[j]==target]
print("Pairs:", pairs)

# 33. Reverse Each Word
sentence = input("Enter sentence: ")
rev_words = ' '.join(word[::-1] for word in sentence.split())
print("Reversed words:", rev_words)

# 34. Check if List is Sorted
nums = list(map(int,input("Enter numbers: ").split()))
print("Sorted" if nums==sorted(nums) else "Not Sorted")

# 35. Bus Seat Booking Simulation
seats = 10
book = int(input("Seats to book: "))
if book <= seats:
    seats -= book
    print("Booking successful. Remaining seats:", seats)
else:
    print("Not enough seats.")

# 36. Contact Dictionary Search
contacts = {'Alice':'123','Bob':'456'}
name = input("Enter name to search: ")
print("Number:", contacts.get(name,"Not Found"))

# 37. Remove Punctuation
import string
s = input("Enter string: ")
print("Without punctuation:", ''.join(c for c in s if c not in string.punctuation))

# 38. Star Pyramid
n = int(input("Enter number of rows: "))
for i in range(1,n+1):
    print(' '*(n-i) + '*'*(2*i-1))

# 39. Count Lines in File
filename = input("Enter filename: ")
with open(filename,'r') as f:
    print("Number of lines:", sum(1 for _ in f))

# 40. Maximum Occurring Element
nums = list(map(int,input("Enter numbers: ").split()))
max_elem = max(set(nums), key=nums.count)
print("Maximum occurring element:", max_elem)

# 41. Elements divisible by 3 and 5
nums = list(map(int,input("Enter numbers: ").split()))
print("Divisible by 3 and 5:", [x for x in nums if x%3==0 and x%5==0])

# 42. Merge Two Dictionaries
d1 = {'a':1,'b':2}
d2 = {'b':3,'c':4}
merged = {**d1, **d2}
print("Merged:", merged)

# 43. Word Frequency in Sentence
sentence = input("Enter sentence: ")
freq = {}
for w in sentence.split():
    freq[w] = freq.get(w,0)+1
print("Word frequency:", freq)

# 44. Total Bill from Prices
prices = list(map(float,input("Enter prices: ").split()))
print("Total bill:", sum(prices))

# 45. Balanced Brackets Check
expr = input("Enter expression: ")
stack=[]
pairs={'(':')','{':'}','[':']'}
for c in expr:
    if c in pairs: stack.append(c)
    elif c in pairs.values():
        if not stack or pairs[stack.pop()]!=c:
            stack.append('x'); break
print("Balanced" if not stack else "Not Balanced")

# 46. Pascal's Triangle
rows = int(input("Enter number of rows: "))
triangle = [[1]*(i+1) for i in range(rows)]
for i in range(2,rows):
    for j in range(1,i):
        triangle[i][j] = triangle[i-1][j-1]+triangle[i-1][j]
for row in triangle: print(row)

# 47. Remove Negative Numbers
nums = list(map(int,input("Enter numbers: ").split()))
print("Non-negative numbers:", [x for x in nums if x>=0])

# 48. Student Class with Grade
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def grade(self):
        if self.marks>=90: return 'A'
        elif self.marks>=75: return 'B'
        elif self.marks>=50: return 'C'
        else: return 'F'
s = Student(input("Name: "), int(input("Marks: ")))
print(f"{s.name} -> Marks: {s.marks}, Grade: {s.grade()}")

# 49. Perfect Number Check
num = int(input("Enter number: "))
sum_div = sum(i for i in range(1,num) if num%i==0)
print("Perfect Number" if sum_div==num else "Not Perfect Number")

# 50. Voting System with Percentage
votes = {'A':0,'B':0}
n = int(input("Number of voters: "))
for i in range(n):
    v = input("Vote (A/B): ").upper()
    if v in votes: votes[v]+=1
total = sum(votes.values())
for k in votes: print(f"{k}: {votes[k]} votes, {votes[k]/total*100:.2f}%")