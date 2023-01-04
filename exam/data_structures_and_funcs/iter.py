numbers = [1, 2, 3, 4]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator)) 
print(next(iterator))
print(next(iterator))

# Iterate over the iterator using a for loop
print('Iterating over the iterator using a for loop:')

numbers = [1, 2, 3, 4]

iterator = iter(numbers)

for number in iterator:
    print(number)


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



# Iteration in sets

s = {1, 2, 3, 4, 5}

for item in s:
    print(item)



# Iteration in dictionaries 

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)


# Iterate over the keys and values of the dictionary using the items() method
for key, value in d.items():
    print(f'{key}: {value}')



# Iteration in lists

l = [1, 2, 3, 4, 5]

for item in l:
    print(item)



# Iteration in tuples

t = (1, 2, 3, 4, 5)

for item in t:
    print(item)



# Iteration in strings

s = 'Hej'

for char in s:
    print(char)

print('Proving not all string is iterable:')
proof = 'hello\tworld\n'

for char in proof:
    print(char)