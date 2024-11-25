class BankAccount:
    def __init__(self,balance,accountNum):
        self.balance = balance
        self.accountNum = accountNum
    def deposit(self,amountd):
        self.balance = self.balance+amountd
    def withdrawal(self,amountw):
        self.balance = self.balance-amountw
    def show(self):
        print(f"Balance : {self.balance}")
        print(f"AccountNumber : {self.accountNum}")

A1 = BankAccount(1000,123)
A1.deposit(200)
A1.show()
A1.withdrawal(1000)
A1.show()