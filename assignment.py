#Model an organisation of employees, management and board of directors in 3 sets.

#Board of directors: Benny, Hans, Tine, Mille, Torben, Troels, Søren
#Management: Tine, Trunte, Rane
#Employees: Niels, Anna, Tine, Ole, Trunte, Bent, Rane, Allan, Stine, Claus, James, Lars

directors = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}
management = {"Tine", "Trunte", "Rane"}
employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}


#who in the board of directors is not an employee?
print('Board who is not an employee: ' + str(directors.difference(employees)))

#who in the board of directors is also an employee?
print('Board who is also an employee: ' + str(directors.intersection(employees)))

#how many of the management is also member of the board?
print('Number of management who is also member of board: ' + str(len(directors.intersection(management))))

#All members of the managent also an employee
print('Management who is also an employee: ' + str(management.intersection(employees)))

#All members of the management also in the board?
print('Management also in the board: ' + str(directors.intersection(management)))

#Who is an employee, member of the management, and a member of the board?
print('Employee and management and board: ' + str(directors.intersection(management).intersection(employees)))

#Who of the employee is neither a memeber or the board or management?
print('Employees who are neither board nor management: ' + str(employees.difference(management).difference(directors)))

#--------------------------------------------------------------------
#Using a list comprehension create a list of tuples from the folowing datastructure
#{‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}

datastructure = {'a': 'Alpha', 'b' : 'Beta', 'g': 'Gamma'}
 
# Converting into list of tuple
list = list(datastructure.items())

print(list)

#------------------------------------------------------------------
#From these 2 sets:
#{'a', 'e', 'i', 'o', 'u', 'y'}
#{'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}
#Of the 2 sets create a: Union, Symmetric Difference, Difference, disjoint

setA = {'a', 'e', 'i', 'o', 'u', 'y'}
setB = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

print('Union: ' + str(setA.union(setB)))

print('Symmetric difference: ' + str(setA.symmetric_difference(setB)))

print('Difference: ' + str(setB.difference(setA)))

print('Disjoint:' + str(setA.intersection(setB)))


#------------------------------------------------------------------
#Date Decoder.
#A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.
#Create a dict suitable for decoding month names to numbers.
#Create a function which uses string operations to split the date into 3 items using the "-" character.
#Translate the month, correct the year to include all of the digits.
#The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ).

my_date = "8-MAR-85"

dict = {
  "JAN": 1,
  "FEB": 2,
  "MAR": 3,
  "APR": 4,
  "MAY": 5,
  "JUN": 6,
  "JUL": 7,
  "AUG": 8,
  "SEP": 9,
  "OCT": 10,
  "NOV": 11,
  "DEC": 12
}

split_date = my_date.split("-")

if split_date[2] > '35':
    add_year = int(('19' + split_date[2]))
else:
    add_year = int(('20' + split_date[2]))

correct_month = dict[split_date[1]]

correct_date = int(split_date[0])

correct_tupple = (add_year, correct_month, correct_date)
print(correct_tupple)