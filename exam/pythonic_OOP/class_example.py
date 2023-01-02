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

