class BankAccount:
    def __init__(self, balance):
        # Define a private attribute to store the balance
        self.__balance = balance

    def get_balance(self):
        # Define a public method to retrieve the balance
        return self.__balance

    def set_balance(self, balance):
        # Define a public method to set the balance
        self.__balance = balance

# Create an instance of the BankAccount class
account = BankAccount(1000)

# Access the balance using the public method
print(account.get_balance())  # prints 1000

# Set the balance using the public method
account.set_balance(2000)

# Access the balance again using the public method
print(account.get_balance())  # prints 2000


