class BankAccount:
    def __init__(self, balance):
        self.balance = balance 

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount

account = BankAccount(1000)

account.withdraw(500)

print(account.balance)


