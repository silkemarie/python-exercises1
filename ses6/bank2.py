# Claus'

class Bank:
    def __init__(self):
        self.accounts = []

class Customer:
    def __init__(self, name, acc):
        self.name = name
        self.acc = acc

    def __repr__(self):
        return f'{self.name}, {self.acc}' #svarer til en toString i Java 

class Account:

    def __init__(self, accno):
        self.accno = accno

    def __str__(self):
        return f'Account number xxxx'

    def __repr__(self) -> str:
        return 'Account from repr'


#kan holde mange accounts + kan adde accounts 