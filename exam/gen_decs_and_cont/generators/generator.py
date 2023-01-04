# General example of a generator:

def count_up_to(max):
    count = 0
    while count < max:
        yield count
        count += 1

counter = count_up_to(5)

for number in counter:
    print(number)


#========== pythonic vs non-pythonic

# Pythonic generator function
def squares(n):
    for i in range(n):
        yield i ** 2


# Use either this for loop or next()
for x in squares(10):
    print(x)

"""
iterator = squares(10)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
"""

def squares_loop(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

result = squares_loop(10)
print(result)
