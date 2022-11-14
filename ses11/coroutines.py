#Coroutines
#Routine/subroutine pattern

class Api:
    def do_this_first(self):
        return 'from 1. method'
    def do_this_second(self):
        return 'from 2. method'
    def do_this_third(self):
        return 'from 3. method'
    
    def run(self):
        self.do_this_first()
        self.do_this_second()
        self.do_this_third()


x = Api()

def api():
    yield x.do_this_first()
    yield x.do_this_second()
    yield x.do_this_third()

y = api()
#print(next(y))
#print('Her gør jeg noget finurligt!')
#print(next(y))
#print('her er jeg næsten færdig')
#print(next(y))

#Coroutine pattern

def api2():
    x = yield 'Coroutine satrted'
    yield x * x

x = api2()
next(x)

x.send(12)

#Coroutine to Compute a Running Average Change the function below into a coroutine (generator)
#that calculates a running avarage. So instead of returning an avarage based on the parameter
#it should calculate an avarage based on the values inserted into the coroutine with the .send() method.

"""
def averager(*args):
     sum = 0
     for i in args:
            sum += i
            print(i)
            print(sum)
     return sum/len(args)


averager(12, 8, 4)
"""


def averager(x):
    sum = 0
    counter = 0
    avg = None
    while True:
        term = yield avg
        sum += term
        counter += 1
        avg = sum / counter

x = averager(1)
next(x)
x.send(12)


for i in range(10, 0 ,-1):
    print(x.send(i))


####

def xxx():
    yy = yield 'Hello'
    yy = yield yy

x = xxx()
next(x)

x.send(3636)

#==========================
