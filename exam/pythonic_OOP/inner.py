def outer(x):
    def inner(y):
        return x + y
    return inner

add_two = outer(2)
print(add_two(3))  # prints 5
