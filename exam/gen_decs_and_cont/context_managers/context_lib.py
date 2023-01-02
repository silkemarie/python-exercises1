from contextlib import contextmanager

@contextmanager
def greet(name):
    print("Hello, " + name)
    yield
    print("Goodbye, " + name)

with greet("Alice"):
    print("Doing some work")


