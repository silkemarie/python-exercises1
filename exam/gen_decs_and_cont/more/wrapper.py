# Wrapper
# add_five is a wrapper function that takes another function. 

def add_five(func):
    def wrapper(x):
        return func(x) + 5
    return wrapper

@add_five
def square(x):
    return x**2

print(square(3))  # prints 14
