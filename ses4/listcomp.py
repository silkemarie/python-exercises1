#List comprehensions
l = []
for i in range(10):
    l.append(i)
print(l)


print([i for i in range(10)])

print([i for i in ['Hello', 'text', 'ole']])
print([len(i) for i in ['Hello', 'text', 'ole']])

def last(x):
    return x[-1]

#-------------------------------------------------------------------

#Alphabet List Comprehensions
#Create a list of capital letters in the english alphabet:

#ord = a built in function, gives letters their ascii number
print(ord('A'))
#chr = char. a built in function, returning the char
print(chr(65))

for i in range(65, 91):
    print(chr(i))

#or

print([chr(i) for i in range(65, 90)])

#or

import string
print([i for i in string.ascii_uppercase])

#-------------------------------------------------------------------
#Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.

for i in range(65, 91):
    if i not in [70, 75, 80, 85]:
        print(chr(i))

#or

print([chr(i) for i in range(65, 90) if i not in [70, 75, 80, 85]])

#-------------------------------------------------------------------

#Create a list of capital letter from from the english aplhabet, but exclude every second between F & O

print([chr(i) for i in range(65, 90) if i not in range(70, 80, 2)])

#-------------------------------------------------------------------