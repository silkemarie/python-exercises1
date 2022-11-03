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
print(compute())

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
        pass



compute = Compute()
print(compute)

#==================================================

#Iterator class

#next: når jeg har et iteratable object, så kalder next den næste