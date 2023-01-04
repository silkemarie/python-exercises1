from contextlib import contextmanager

@contextmanager
def greet(name):
    print("Hello, " + name)
    yield
    print("Goodbye, " + name)

with greet("Claus"):
    print("Doing some python")


