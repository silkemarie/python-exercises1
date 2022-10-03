#All classes should be in a single file.
#The bank class should be able to hold many account.
#You should be able to add new accounts.
#The Account class should have relevant details.
#The Customer class Should also have relevant details.
#Stick to the techniques we have covered so far.
#Add the abillity for your __init__ method to handle different inputs (parameters).

class Bank:
    def __init__(self, name):
        self.name = name

class Account(Bank, Customer):
    def __init__(self, amount):
        Bank.__init__(self.name)
        Customer.__init__(self.owner_name, self.credit_score)
        self.amount = amount

class Customer():
    def __init__(self, owner_name, credit_score, owner_id):
        self.owner_name = owner_name
        self.credit_score = credit_score
        self.owner_id = owner_id