def my_func():
    return 'From my_func'
print(type(my_func))

class MyClass:
    pass

print('Class type: ')
print(type(MyClass))

#how to write a function through a class?
#you make the object of that class callable
#et objekt er ikke callable

#en klasse med en call metode:
class MyClass:
    def __call__(self):
        return 'From MyClass´s call method'

my_func = MyClass()

print('Is my_func callable?')
print(callable(my_func))

#this means that anything you would define in a function could be defined in a class's __call__ method.
#===============================================

#Compute

def compute():
    li = []
    for i in range(10):
        li.append(i)
    return li

print(compute())

class Compute:
    def __call__():
        li = []
        for i in range(10):
            li.append(i)
        return li

compute = Compute()


#def compute() og class Compute: gør her det samme. Det er bare forskellige måder at skrive det på.
#===============================================

#Generators

from time import sleep

def compute():
    li = []
    for i in range(10):
        sleep(.5)
        li.append(i)
    return li

print(compute())

class Compute:
    """
    def __call__(self):
        li = []
        for i in range(10):
            sleep(.5)
            li.append(i)
        return li
    """

    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        if self.last > 9:
            raise StopIteration
        self.last += 1
        return self.last


compute = Compute()
#it = compute()

it = iter(compute)
print(next(it))

#==================================================

#Iterator class

#next: når jeg har et iteratable object, så kalder next den næste

#==================================================

#Generator function
print('Vi er i generator function')

def compute():
    yield 1

print(type(compute()))

def compute():
    for i in range(10):
        yield i

# print(compute())
# ^ bliver til <generator object compute at 0x000000246539E5E00>

it = compute()
for i in compute:
    print(i)

#Generator expression

[i for i in range(10)] #list
(i for i in range(10)) #generator object, generator expression
