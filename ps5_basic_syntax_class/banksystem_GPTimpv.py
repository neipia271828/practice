class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f"Error: 残高不足です。（現在の残高: {self.balance} 円）")
    
    def display_balance(self):
        print(f"📝 現在の残高: {self.balance} 円")

# 口座を作成
account_A = BankAccount("A")

# 入金・出金の処理
account_A.deposit(50)
account_A.display_balance()
account_A.withdraw(25)
account_A.display_balance()
account_A.withdraw(30)
account_A.display_balance()