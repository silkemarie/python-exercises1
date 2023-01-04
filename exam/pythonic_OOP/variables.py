class Dog:
    species = "dog"

    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

dog1 = Dog("Suki", 5, "is my baby")
dog2 = Dog("Yoko", 8, "is an old lady")

print(f"{dog1.name} is a {dog1.species}, is {dog1.age} years old and {dog1.status}.")
print(f"{dog2.name} is a {dog2.species}, is {dog2.age} years old and {dog2.status}.")

