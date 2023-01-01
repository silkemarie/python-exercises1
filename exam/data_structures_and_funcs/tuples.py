coordinates = (4, 5)

print(coordinates[0])  
# Output: 4

print(coordinates[1])  
# Output: 5

print(coordinates[-1])  
# Output: 5

print(coordinates[-2])  
# Output: 4

# Will produce an error, since tuples are immutable:
coordinates[0] = 3

# Instead you can assign a new tuple to the same variable:
coordinates = (3, 5)

