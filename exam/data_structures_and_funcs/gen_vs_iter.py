# Iter function
"""
# Create a list of integers
numbers = [1, 2, 3, 4, 5]

# Obtain an iterator from the list using the iter() function
iterator = iter(numbers)

# Print the first value of the iterator
print(next(iterator))  # Output: 1

# Print the next value of the iterator
print(next(iterator))  # Output: 2

# Print the remaining values of the iterator
for value in iterator:
    print(value)  # Output: 3, 4, 5

"""
#================

#Generators

# Define a generator function that produces values one at a time
def countdown(n):
    while n > 0:
        yield n
        n -= 1

countdown_generator = countdown(5)

print(next(countdown_generator))
print(next(countdown_generator))
print(next(countdown_generator))
print(next(countdown_generator))
print(next(countdown_generator)) 

"""
#==============

# Generator expressions:

# Create a list of the squares of the integers from 1 to 10 using a for loop
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Create a generator of the squares of the integers from 1 to 10 using a generator expression
squares_generator = (i ** 2 for i in range(1, 11))

# Print the values produced by the generator
print(next(squares_generator))  # Output: 1
print(next(squares_generator))  # Output: 4
print(next(squares_generator))  # Output: 9
print(next(squares_generator))  # Output: 16
print(next(squares_generator))  # Output: 25
"""