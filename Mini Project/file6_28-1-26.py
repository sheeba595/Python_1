# #1.  Mini Project: Discount Calculator for a Shopping Store
# Create a program that asks the user for the total bill amount and applies a 
# discount based on the following conditions: 
#  Discount Rules: 
#  If the bill is ₹5000 or more, give a 20% discount. 
#  If the bill is between ₹3000 and ₹4999, give a 10% discount. 
#  If the bill is between ₹1000 and ₹2999, give a 5% discount. 
#  If the bill is less than ₹1000, no discount. 

total_bill=int(input("Enter the total bill:  "))
if(total_bill>=5000 ):
    discount=total_bill*(20/100)
    print("Discout applied: ",discount)
    print(f"Final Bill amount: {total_bill-discount}")
elif(total_bill>=3000 and total_bill<5000):
    discount=total_bill*(10/100)
    print("Discout applied: ",discount)
    print(f"Final Bill amount: {total_bill-discount}")
elif (total_bill>=1000 and total_bill<3000):
    discount=total_bill*(5/100)
    print("Discout applied: ",discount)
    print(f"Final Bill amount: {total_bill-discount}")
else:
    print("No discount")
    
# Create a Rock, Paper, Scissors game where the user plays against the computer. 
# The computer randomly selects Rock, Paper, or Scissors, and the user inputs their 
# choice. The winner is determined using these rules: 
#  Rock beats Scissors 
#  Scissors beats Paper 
#  Paper beats Rock 
#  If both choices are the same, it's a tie! 

import random
user=input("Enter your choice (rock, paper, scissors): ").lower()
choices=['rock','paper','scissors']
computer=random.choice(choices)  #random is a module where choice is a function it is used to randomly choose from a set of choices given by the user.
print(f"Computer choose: {computer}")
if((user=='rock' and computer=='scissors') or (user=='scissors' and computer=='paper') or (user=='paper' and computer=='rock')):
    print("you Win!")
else:
    print("Computer Wins!")