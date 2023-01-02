class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Define a name property using the @property decorator
    @property
    def name(self):
        return self._name

    # Define a setter for the name property using the @name.setter decorator
    @name.setter
    def name(self, value):
        self._name = value

    # Define an age property using the @property decorator
    @property
    def age(self):
        return self._age

    # Define a setter for the age property using the @age.setter decorator
    @age.setter
    def age(self, value):
        self._age = value

# Create an instance of the Person class
p = Person("Alice", 30)

# Access the name and age properties using dot notation
print(p.name)  # prints "Alice"
print(p.age)  # prints 30

# Set the name and age properties using dot notation
p.name = "Bob"
p.age = 35

# Access the name and age properties again using dot notation
print(p.name)  # prints "Bob"
print(p.age)  # prints 35


