# Task: Your job is, to write a decorator function that can time any piece of code.
# You can read about time by starting your interpretor and write:

import time
#print(help(time))

def decorator(func):
    def inner(*args):
        time.time()
        start = time.time()
        result = func(*args)
        end = time.time()
        print(end - start)
        return result
    return inner


@decorator
def start(*args):
    return args[0]
print(start(1))