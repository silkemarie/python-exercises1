def count_up_to(max):
    """Generate a sequence of numbers from 0 to max."""
    count = 0
    while count < max:
        yield count
        count += 1

# Create a generator object
counter = count_up_to(5)

# Use the generator object in a for loop
for number in counter:
    print(number)

# Output:
# 0
# 1
# 2
# 3
# 4


#========== pythonic vs non-pythonic

# Pythonic generator function
def squares(n):
    for i in range(n):
        yield i ** 2

# Non-pythonic loop
def squares_loop(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result



# Use the generator function
for x in squares(10):
    print(x)

# Output: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81


# Use the loop function
result = squares_loop(10)
print(result)

# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
