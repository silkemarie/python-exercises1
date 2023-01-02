# 'greet' function is a first-class function, because it can be assigned to a variable, passed as an argument to a function, and returned as a result from a function.

def greet(name):
    print("Hello, " + name)

# Assign the function to a variable
greeting = greet

# Pass the function as an argument to another function
def say_hello(func):
    func("Alice")

say_hello(greeting)  # prints "Hello, Alice"

# Return the function as a result from a function
def make_greeting(name):
    def greet(name):
        print("Hello, " + name)
    return greet

greeting = make_greeting("Bob")
greeting()  # prints "Hello, Bob"


# Example 2
# 'greet' is again a first-class function

from contextlib import contextmanager

@contextmanager
def greet(name):
    print("Hello, " + name)
    yield
    print("Goodbye, " + name)

with greet("Alice"):
    print("Doing some work")


# Example 3
# 'log' is a first-class function. It is a decorator that takes a function as an argument and returns a wrapper function that logs the arguments and return value of the decorated function

def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log
def add(x, y):
    return x + y

add(1, 2)


# Example 4
# 'countdown' is a first-class function. It is a generator that yields the numbers from 'n' down to 1, one at a time, when it is iterated over

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)


#======================
# A simple version
# again, 'greet' is a first-class function. It takes a name as an argument and prints a greeting. 

def greet(name):
    print("Hello, " + name)

def greet_twice(greeting_func, name):
    greeting_func(name)
    greeting_func(name)

greet_twice(greet, "Claus")



# ====================
# Different ways to define a first-class function


# A first-class function on its own:

def greet(name):
    print("Hello, " + name)

greet("Alice")


# A first-class function within another function:

def outer(x):
    def inner(y):
        return x + y
    return inner

add_two = outer(2)
print(add_two(3))  # prints 5


# A first-class function assigned to a variable:

def greet(name):
    print("Hello, " + name)

say_hello = greet
say_hello("Bob")  # prints "Hello, Bob"


# A first-class function passed as an argument:

def greet(name):
    print("Hello, " + name)

def say_something(func, phrase):
    func(phrase)

say_something(greet, "how are you?")  # prints "Hello, how are you?"


# A first-class function returned from a function:

def outer(x):
    def inner(y):
        return x + y
    return inner

add_two = outer(2)
print(add_two(3))  # prints 5




# NOT first-class functions
# Built-in functions, lambda functions, method functions. Example of method function is bark:

class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.bark()  # prints "Woof!"


