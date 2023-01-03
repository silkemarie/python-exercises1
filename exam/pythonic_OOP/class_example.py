# This class defines a 'Dog' object with two attributes, name and breed, and a method, bark. 

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print("Woof!")


# Create an object of this class:
my_dog = Dog("Buddy", "Labrador")


# Can access the attributes using dot notation
print(my_dog.name)  # prints "Buddy"

# Can call methods using ()
my_dog.bark()  # prints "Woof!"




# Instance variable. Name and breed are instance variables here:

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


# When you create an instance of the Dog class, you can set the name and breed instance variables for that specific instance:

fido = Dog("Fido", "Labrador")
print(fido.name)  # prints "Fido"
print(fido.breed) # prints "Labrador"

# Fido is an instance of the Dog class, with its own set of instance variables; name and breed, with the values: Fido and labrador. 
# These values are specific to the Fido-instance and are not shared with other instances of the Dog class. 



# Define a global variable
# OBS: good practice is to store global variables at the top of your code. These code examples don't have anything to do with each other, which is why I'm not

greeting = "Hello"

def say_hello(name):
    # Access the global variable
    print(greeting + ", " + name)

say_hello("Alice")  # Prints "Hello, Alice"
