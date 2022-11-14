#Context Managers

f = open('testfiles/bohr.txt')
print(f.readline())
f.close()

with open('testfiles/bohr.txt') as f:
    print(f.read())

class MyOpen:
    def __init__(self, filename):
        self.filename = filename
        
    def __enter__(self):
        print('__enter__')
        f = open(self.filename)
        return f
    def __exit__(self, *args):
        print('__exit__')
        f.close()


with MyOpen('testfiles/bohr.txt') as f:
    print(f.readline())

from contextlib import contextmanager

@contextmanager
def xxx():
    f = open('testfiles/bohr.txt')
    yield f
    f.close()


with xxx() as f:
    print(f.readline())


def contextmanager(func):
    def inner(*args):
        #jhdfgkjhdk
        #lkdglkgdjflg
    
        return #sdjkfdshkfhs
    return inner

#VIGTIGT

## Decorator under en context manager
"""
from contextLib import contextManager

@contextManager
def bob():
    file = open('silke.txt')
    yield file
    file.close()


#connect er en context manager 
#enter og exit metoder
"""