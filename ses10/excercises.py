"""
Based on the Student class below, create a PythonStudents class that acts as a 
collection of students. The class should implement the iterations protocol 
(iter(), next() and StopIteration). When iterated the Pythod_students object 
should return the name of each student in the list.
"""



"""
class PythonStudents:

    def __init__(self, studentList):
          self.studentList = studentList
          #studentList.name = args[0]
          #studentList.cpr = args[1]

    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        if self.last > len(self.studentList):
            raise StopIteration
        else:
            li = self.studentList[self.last].name
            self.last += 1
            return li
"""


class Student:

     def __init__(self, name, cpr):
        self.name = name
        self.cpr = cpr

     @property
     def name(self):
             return self.__name

     @name.setter
     def name(self, name):
             self.__name = name.capitalize()

     def __add__(self, student):
             return Student('Anna the daugther', 1234)

     def __str__(self):
             return f'{self.name}, {self.cpr}'

     def __repr__(self):
             return f'{self.__dict__}'



#Claus' løsning:

class PythonStudents:

    def __init__(self):
          self.students = []

    def __add__(self, student):
        self.students.append(student)

    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        self.temp = self.last
        self.last += 1
        if self.last > len(self.students):
            raise StopIteration()
        return self.students[self.temp]

students = PythonStudents()
students + Student('Claus', 1234)
students + Student('Anna', 4321)
it = iter(students)

for i in students:
    print(i)


"""
studentOne = Student('Jørgen', 34)
studentTwo = Student('Bo', 34)
studentThree = Student('Hans', 34)
studentFour = Student('Tom', 34)

students = [studentOne, studentTwo, studentThree, studentFour]

compute = PythonStudents(students)


it = iter(compute)

print(next(it))
for i in compute:
    print(i)
"""

"""
#==========================================================
from random import randrange
names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def students_list(num_students):
    li = []
    id = 1

    for i in num_students:
        li.append({'id': id, 'name': names[randrange(0,len(names))], 'major': majors[randrange(0, len(majors))]})
        id += 1
    return li

def students_generator(num_students):
    pass

people = students_list(1000000)
people = students_generator(1000000)
"""