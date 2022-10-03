#declare a class

class Person:
    pass

#object:
claus = Person()                #creates a new instance of Person
anna = Person()
#man bruger ikke 'new' i python

#create an initializer (initializer = java constructor)
class Person:

    type = 'Mammal'             #class variable

    def __init__(self, name):   #når der skal defines i def, skal første parameter være self. Det svarer til javas 'this'
        self.name = name        #instnace variable

    def __len__(self):
        return 1200


#ting inde i klasser: metoder. Ting udenfor klasser: funktioner


#instance and class variables
#add change instance variables after declaration
#add change class variables after declaration
#overloading

class Person:

    def __init__(self, name):
        self.name = name

    def __init__(self, name, age):
        pass

#inheritance
#superklassen her
class Person:
    def __init__(self, *args):
        self.name = args[0]

class Student(Person):
    def __init__(self, name, stid):
        super().__init__(name)  #kalder super init funktionen her 
        self.student_id = stid


class Instructor:
    pass

class Teacher(Person, Instructor):  #arver både fra person of fra instructor
    def __init__(self, *args):
        Person.__init__(self, name)
        Instructor.__init__(self.age) #fordi vi arver fra flere superklasser, bliver vi nødt til at kalde dem direkte, og kan ikke bruger super(), som tidligere

        