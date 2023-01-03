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



# Private attributes

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

point = Point(1, 2)
print(point._x)  # prints 1
print(point._y)  # prints 2

"""In this example, the _x and _y attributes are marked as private by prefixing their names with an underscore. 
However, there is nothing stopping us from accessing or modifying these attributes from outside the Point object. 
We can simply use the dot notation to access them, as shown in the example above."""

