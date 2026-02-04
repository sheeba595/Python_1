# Mini Project 4: Simple Banking System (Using while, continue, break, 
# pass, else) 
# Task: 
# Create a Banking System that: 
#  Starts with a balance of ₹10,000. 
#  Allows the user to deposit and withdraw money. 
#  Displays the current balance after every transaction. 
#  Exits when the user types "quit".

print("Simple Banking System")
balance=10000
while True:
    print("1.Deposit money     2.Wihtdraw Money  3.Type quit to exit")
    choice=input("Enter operation: ")
    if(choice.lower()=="quit" or choice=="3"):
        print("Exited")
        break
    elif choice=="1":
        deposit=int (input("Enter deposit amount: "))

        if deposit<=0:
            pass
        else:
             balance+=deposit
             print("Deposited successfully!!!")
             print(f"Balance: {balance}")
             continue
       
    elif choice=="2":
        withdraw = int(input("Enter withdrawal amount: "))
        if withdraw > balance:
            print("Insufficient balance!")
        elif withdraw <= 0:
            pass    
        else:
            balance -= withdraw
            print("Amount withdrawn successfully!")
            print(f"Current Balance: ₹{balance}")
        continue

    else:
        print("Invalid choice! Try again.")
        continue