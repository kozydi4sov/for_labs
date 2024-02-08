class Account():
    def __init__(self,owner,balance = 0, deposit = 0):
        self.owner = owner
        self.balance = balance
        self.deposit = deposit
    def deposit(self, amount):
        self.deposit += amount
        self.balance -= amount
        print(f"Deposited ${amount}, Current balance: ${self.balance}")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ${amount}.Current balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal denied.")
            
owner_name = input("Enter the owner's name: ")
initial_balance = float(input("Enter the initial balance: "))
account1 = Account(owner=owner_name, balance=initial_balance)

deposit_amount = float(input("Enter the deposit amount: "))
account1.deposit(deposit_amount)

withdraw_amount = float(input("Enter the withdrawal amount: "))
account1.withdraw(withdraw_amount)