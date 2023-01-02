# Simple first-class vs simple inner
# First-class:

def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print(add_five(3))


# Inner:

def outer(x):
    def inner(y):
        return x + y

add_five(3)

