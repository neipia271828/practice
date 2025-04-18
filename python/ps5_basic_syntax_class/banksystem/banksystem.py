class BankAccount:
    def __init__(self, account_holder=""):
        self.account_holder = account_holder
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        print()
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Error")
    
    def display_balance(self):
        print(f"balance:{self.balance}")

account_A = BankAccount()
account_A.account_holder = "A"

account_A.deposit(50)
account_A.display_balance()
account_A.withdraw(25)
account_A.display_balance()
account_A.withdraw(30)
account_A.display_balance()