numbers = [1, 2, 3, 4]

# Create an iterator from the numbers list
iterator = iter(numbers)

# Use the next() function to get the next element of the iterator
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
print(next(iterator))  # Output: 4


#==================
# Iterate over an iterator: 


numbers = [1, 2, 3, 4]

# Create an iterator from the numbers list
iterator = iter(numbers)

# Iterate over the iterator using a for loop
for number in iterator:
    print(number)

# Output:
# 1
# 2
# 3
# 4

#==================
class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result

# Create an instance of MyIterable
iterable = MyIterable([1, 2, 3, 4, 5])

# Iterate over the iterable using a for loop
for item in iterable:
    print(item)

#===================
# Iteration in sets

# Create a set
s = {1, 2, 3, 4, 5}

# Iterate over the set using a for loop
for item in s:
    print(item)



# Iteration in dictionaries 

# Create a dictionary
d = {'a': 1, 'b': 2, 'c': 3}

# Iterate over the dictionary using a for loop
for key in d:
    print(key)


# Iterate over the keys and values of the dictionary using the items() method
for key, value in d.items():
    print(f'{key}: {value}')



# Iteration in lists

# Create a list
l = [1, 2, 3, 4, 5]

# Iterate over the list using a for loop
for item in l:
    print(item)



# Iteration in tuples

# Create a tuple
t = (1, 2, 3, 4, 5)

# Iterate over the tuple using a for loop
for item in t:
    print(item)



# Iteration in strings

# Create a string
s = 'abcdef'

# Iterate over the string using a for loop
for char in s:
    print(char)
