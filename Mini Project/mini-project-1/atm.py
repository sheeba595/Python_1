balance = 5000

while True:
    print("1.Check Balance  2.Deposit  3.Withdraw  4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amt = int(input("Enter amount: "))
        balance += amt

    elif choice == 3:
        amt = int(input("Enter amount: "))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient Balance")

    elif choice == 4:
        break
