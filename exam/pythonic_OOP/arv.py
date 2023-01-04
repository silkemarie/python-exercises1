class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def is_good(self):
        print("Is pretty good")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def is_good(self):
        print("Is the best")

dog1 = Dog("Suki", "Schapendoes")
print(dog1.name)
print(dog1.species)
print(dog1.breed)
dog1.is_good()



