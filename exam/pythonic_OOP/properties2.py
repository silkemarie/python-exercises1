# Example of a class Person, that uses properties to control access to the _age instance variable

class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age


person = Person(30)
print(person.age)
person.age = 35
print(person.age)

#'age' property allows us to get and set the value of the __age instance variable, while still keeping the attribute private

