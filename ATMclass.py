class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.is_authenticated = False
    def login(self, pin):
        if pin == self.pin:
            self.is_authenticated = True
            return "Access Granted"
        else:
            return "Access Denied"
    def check_balance(self):
        return f"Balance: {self.balance}"
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}"
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return f"Withdrew {amount}"
atm = ATM(1234, 500)
print(atm.login(1234))
print(atm.deposit(200))
print(atm.withdraw(100))
print(atm.check_balance())
