# Find the length of a string
s = "Hello, world!"
print(len(s))  # prints 13

# Find the length of a list
lst = [1, 2, 3, 4, 5]
print(len(lst))  # prints 5

# Find the length of a tuple
t = (1, 2, 3, 4, 5)
print(len(t))  # prints 5

# Find the length of a set
s = {1, 2, 3, 4, 5}
print(len(s))  # prints 5

# Find the length of a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
print(len(d))  # prints 3



# Find len with dunder method:

class MyClass:
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)

obj = MyClass([1, 2, 3, 4, 5])
print(len(obj))  # prints 5
