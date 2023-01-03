class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Create two Point objects
point1 = Point(1, 2)
point2 = Point(3, 4)

# Use the __str__ method to print the objects
print(point1)  # prints "Point(1, 2)"
print(point2)  # prints "Point(3, 4)"

# Use the __add__ method to add the points
point3 = point1 + point2
print(point3)  # prints "Point(4, 6)"


