# Mini Project 2: Banking System with OOP and Functions

total_transactions = 0   

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        global total_transactions
        self.balance += amount
        total_transactions += 1
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        global total_transactions

        def can_withdraw():
            return self.balance >= amount

        if can_withdraw():
            fee = (lambda amt: amt * 0.02)(amount)
            self.balance -= (amount + fee)
            total_transactions += 1
            print(f"Withdrawn ₹{amount}, Fee ₹{fee}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance


def apply_interest(balance, interest_func):
    return interest_func(balance)



account = BankAccount("Sheeba", 5000)
account.deposit(2000)

account.withdraw(3000)

print("Current Balance:", account.get_balance())

interest_rate = lambda bal: bal * 1.05   # 5% interest
new_balance = apply_interest(account.get_balance(), interest_rate)

print("Balance after interest:", new_balance)

print("Total Transactions:", total_transactions)
