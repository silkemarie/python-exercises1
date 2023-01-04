# Use list comprehension to create a list of even numbers from a range
even_numbers = [n for n in range(10) if n % 2 == 0]
print(even_numbers)  
# Output: [0, 2, 4, 6, 8]


# Use list comprehension to create a list of tuples that represent the coordinates of points on a grid
points = [(x, y) for x in range(5) for y in range(5)]
print(points)  
# Output: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]


#=============

# For loop for comparison:

# Using for loop:
squares = []

for i in range(1, 11):
    squares.append(i ** 2)

print(squares)


# Using list comprehension:
squares = [i ** 2 for i in range(1, 11)]

print(squares)