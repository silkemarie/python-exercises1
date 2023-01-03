# Define the base class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

# Define the derived class
class Cat(Animal):
    def __init__(self, name, breed, toy):
        # Call the superclass constructor to initialize the name and species attributes
        super().__init__(name, species="Cat")
        # Initialize the breed and toy attributes
        self.breed = breed
        self.toy = toy

    def make_sound(self):
        # Override the make_sound method from the superclass
        print("Meow!")

# Create an instance of the Cat class
cat = Cat("Kitty", "Siamese", "Ball")

# Access the attributes and methods inherited from the Animal class
print(cat.name)  # prints "Kitty"
print(cat.species)  # prints "Cat"
cat.make_sound()  # prints "Meow!"

# Access the attributes and methods unique to the Cat class
print(cat.breed)  # prints "Siamese"
print(cat.toy)  # prints "Ball"
