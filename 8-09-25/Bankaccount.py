class BankAccount():
    def __init__(self,balance,owner="Ravi"):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
    def getBalance(self):
        return self.balance
a=BankAccount(1000)
a.deposit(500)
a.withdraw(200)
print("Balance:",a.getBalance())