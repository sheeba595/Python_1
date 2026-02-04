# 1 Write a program to print each character of the string "PYTHON" using a for # loop. 
word='python'
for i in word:
    print(i)
    
# 2.. Create a program that counts the number of vowels in a given string. 
vowel=input("Enter a word: ").lower()
count=0
for i in vowel:

    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count+=1
print(f"Vowel count is {count}")

# 3. Write a program to reverse a string using a for loop. 
string=input("Enetr a string for reversal: ")
rev=""
for i in string:
    rev=i+rev
print(f"reversed string: {rev}")

# 4. Write a program to print numbers from 1 to 20 using range().
for i in range(1,21):
    print(i,end=" ")
print()    
    #5. Create a program that prints only even numbers from 2 to 50 using range(). 
for i in range(2,50):
    if(i%2==0):
        print(i,end=" ")
print()        
# 6.  Write a program to print numbers in reverse order from 10 to 1 using range().
for i in range(10,1,-1):
    print(i,end=" ")
print()
# 7. Write a program that asks the user to enter numbers until they enter 0, then stop the loop using break. 
while True:
     num=input("Enter number: ")
     num=int(num)
     if(num==0):
         break
     print("Enter again!!")
        
print()
# 8. Create a loop that skips multiples of 5 from 1 to 50 using continue. 
for i in range(1,50):
    if(i%5==0):
        continue
    print(i ,end=" ")
print()

#9. Write a program where a for loop iterates through numbers from 1 to 10, and if the number is 5, use pass to do nothing. 
for i in range(1,10):
    if(i==5):
        pass
    print(i,end=',')
print()

# 10. Write a program that iterates through numbers from 1 to 10, and after the loop ends, print "Loop finished successfully" using the else block.
for i in range(1,11):
    print(i)
else:
    print(f"Loop ended successfully!")
    
    # 11. Create a program that prints each character of "HELLO" with its index position using enumerate(). 
    
let="HELLO"
for index,i in enumerate(let,start=0):
    print(f"Index: {index}=>{i}")
    
# 12. Write a program that asks the user for a sentence and prints each word with its position number using enumerate().
sentence=input("Enter a sentence: ")
for index,i in enumerate(sentence):
    if(i==" "):
        print(f"Index: =>space")
    else:
         print(f"Index: {index}=>{i}")
         
print()
# 13. Write a program to print a multiplication table (1 to 10) using a nested loop.
for i in range(1,11):
    print(f"Table {i}")
    for j in range(1,11):
        
        print(f'{i}*{j}={i*j}')
    print()
    
# 14. Create an infinite loop that prints "Hello, World!" continuously. 

    
# 15. Modify the infinite loop to stop printing after 5 seconds. 
import time
start=time.time()
while True:
    print("Hello World")
    if(time.time()-start>=5):
        break
# 16. Write an infinite loop that asks the user for input and prints it back, breaking when "exit" is entered.
while True:
    w=input("Enter word: ")
    if(w=="exit"):
        break
    
# 17. Print all even numbers from 1 to 20 using while and continue.
index=1
while(index<=20):
    if(index%2==1):
        index+=1
        continue
    print(index)
    index+=1
# 18. Ask the user to enter a number. If the number is negative, ignore it and ask again. Stop only when a positive number is entered.
while(True):
    user=int(input("Enter a number: "))
    if(user>0):
        break
#19. Write a while loop that prints all numbers except multiples of 3 between 1 and 30. 
s=1
while(s<=30):
    if(s%3==0):
        s+=1
        continue
    print(s)
    s+=1
 
# 20. Write a number guessing game where the user must guess a number between 1 and 10. Stop the game when the correct number is guessed. 
import random
guess=random.randint(1,10)
while(True):
    num=int(input("Enter a number: "))
    if(num>guess):
        print(f"Too high Try again!")
    elif (num<guess):
        print("Too low try again")
    else:
        print("Correct guess")
        break
    
#21. Create a while loop that keeps asking for the password. Break when the correct password is entered.
password="1234"
while(True):
    pwd=input("Enter password: ")
    if(pwd==password):
        print("Correct Password")
        break
    else:
        print("Incorrect.Try Again!")
        
# 22. Simulate a simple ATM system where the user gets 3 attempts to enter the correct PIN. If they fail, display "Account Locked" and exit. 
pin=12345
attempt=0
while(True):
    atm_pin=int(input("Enter pin: "))
    if(atm_pin==pin):
        print("Correct pin")
        break
    else:
        attempt+=1
        if(attempt==3):
            print("Your account is locked!!")
            break
        else:
            print(f"Attempt remaining: {3-attempt}")
            
# 23. Write a loop that iterates 10 times but does nothing inside the loop using pass. 
for i in range(1,11):
    pass
# 24. Use pass in a loop that will later be implemented but currently does nothing.
for i in range(1,11):
    if(i%2==1):
        pass
    else:
        print("Even")
# 25. Create a while loop that prints numbers from 1 to 5. If the loop completes naturally (without break), print "Loop completed successfully" using else.
number=1
while(number<=5):
    print(number)
    number+=1
else:
    print("Loop completed successfully!!")
    
# 26. Write a while loop that asks the user for a word. If they enter "Python", break the loop. Otherwise, if the loop finishes without "Python", print "You never entered 'Python'!" using else.
inputs=1
while(inputs<=3):
    word=input("Guess the word: ").lower()
    if(word=="python"):
        print("Correct Word")
        break

    input+=1
else:
    print("You never entered python")