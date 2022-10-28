class p:
    def __init__(self, name, alias):
        self.name = name #public variable -> property
        self.__alias = alias

#property er et metode-navn. med @ foran bruges metoden som en dekorator

    @property
    def name(self):
        return self.__name #ny variable

    @name.setter
    def name(self, name):
        if type(name) == str:
            self.__name = name #deklarerer den nye variable her
        else: 
            print('no no no')

class p:
    def __init__(self, name, alias):
        if name == 'Claus':
            self.name = name
        else:
            self.name = 'DEFAULT'
        
        self.alias = alias


# Create a Car class.
# When instanciated the object should be able to take 4 attributes
# (Make, Model, bhp, mph).
# They all 4 should be properties.
# (Even though this is not nessary here, you should create properties in order just to try it out).

class Car:
    def __init__(self, make, carmodel, bhp, mph):
        self.make = make
        self.carmodel = carmodel
        self.bhp = bhp
        self.mhp = mph

    @property
    def make(self):
        return self.__make

    @property
    def carmodel(self):
        return self.__carmodel

    @property
    def bhp(self):
        return self.__bhp
    
    @property
    def mph(self):
        return self.__mph

    @make.setter
    def make(self, make):
        if type(make) == str:
            self.__make = make
        else:
            print('not a make')

    @carmodel.setter
    def carmodel(self, carmodel):
        if type(carmodel) == str:
            self.__carmodel = carmodel
        else:
            print('not a model')

    @bhp.setter
    def bhp(self, bhp):
        if type(bhp) == int:
            self.__bhp = bhp
        else:
            print('not a bhp')

    @mph.setter
    def mph(self, mph):
        if type(mph) == int:
            self.__mph = mph
        else:
            print('not a mph')


car = Car("toyota", "2010", 10, 20)

print(car.carmodel)

#================== Claus' version:

class Car:

    def __init__(self, *args):
        self.make = args[0]
        self.model = args[1]
        self.bhp = args[2]
        self.mph = args[3]

    def get_make(self):
        print('in getter')
        return self.__make
    
    def set_make(self, make):
        print('in setter')
        self.__make = make

    make = property(get_make, set_make)

    


#In the exercise from last monday with the bank, account and customer, change the code to use properties instead of the public variables.
#The bank class should futher be change into not taking any accounts as parameters at initialization.
#The accouts should be added afterwards, eithers as a single account one at a time, or as a collection of accounts (many at the sametime).
#Somewhere you should change the code so that a customer only can create one account.
#The Customer class should make sure that the customer is over 18 year of age.

class Bank:
    def __init__(self, account):
        self.account = account

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, account):
        self.__account = account 

class Account:
    def __init__(self, no, cust):
        self.no = no
        self.cust = cust

    @property
    def no(self):
        return self.__no
    
    @property
    def cust(self):
        return self.__cust

    @no.setter
    def no(self, no):
        self.__no = no

    @cust.setter
    def cust(self, cust):
        self.__cust = cust

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
