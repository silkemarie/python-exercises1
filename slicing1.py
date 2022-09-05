#slicing

#['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
#('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
#'Hello World Huston we are here' -> 'World Huston we'

from audioop import reverse


l1 = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
print(l1[1:5])
print(l1[0:2])
print(l1[4:6])
#kan også løses med: print(l1[4:])

print(l1[4:5])
#kan også løses med: print(l1[-2:])

print(l1[::2])
print(l1[::-1])
#^denne løsning tager listen bagfra

print(l1[0:-1:1])


#-------------------------------------
#Is it a tuple or a list
#Hint: A list is a collection of the same type of data, a tuple is a record

#Claus, 51, male, clbo@kea.dk, 31011970-1313
#Bmw, Toyota, Hyundai, Skoda, Fiat, Volvo
#Claus, Henning, Torben, Carl, Tine
#‘Hello’, ‘World’, ‘Huston’, ‘we’, ‘are’, ‘here’
#Rolling Stones, Goats Head Soup, 31 August 1973, 46:56
#40.730610, -73.935242, New York City, NY, USA; 31.739847, 65.755920, Kandahar, Kandahar Province, Afghanistan;

t1 = ('Claus', 51, 'male', 'clbo@kea.dk', '31011970-1313')
#^forskellige datatyper, derfor tuple

l1 = ['Bmw', 'Toyota', 'Hyundai', 'Skoda', 'Fiat', 'Volvo']
#^samme datatyper, derfor liste

l2 = ['Claus', 'Henning', 'Torben', 'Carl', 'Tine']
l3 = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
#^kan argumentere at det skal være en tuple, hvis det har betydningen, hvilken rækkefølge det er i.

t2 = ('Rolling Stones', 'Goats Head Soup', '31 August 1973', '46:56')
t3 = (40.730610, -73.935242, 'New York City, NY, USA;' '31.739847', '65.755920', 'Kandahar', 'Kandahar Province', 'Afghanistan')
#^datasæt, derfor tuple 

#--------------------------------------

#sort a text
#Create a function that takes a string as a parameter and returns a list.
#The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.

lSort = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(lSort))

l = sorted(lSort, reverse=True)
print(l) 
#^sorteret i omvendt rækkefølge

l = sorted(lSort, key=len)
print(l)
#^sorteret efter længde

l = ['Bob', 'Hans', 'Alice', 'Hans-Erik']
sorted(l)

#funktion med et paramenter(x)
def last_letter(x):
    return x[-1]

sorted(l, key=last_letter)

def five_or_more(x):
    if len(x) >= 5:
        return True
    return False

l1 = sorted(l, key=five_or_more)
print(l1)
#^fra kort til lang

l1 = sorted(l, key=five_or_more, reverse=True)
print(l1)

l1 = sorted(l, key=lambda x: x[-1])
print(l1)



l = ['Bob', 'Alice', 'Bo']
l.sort()
print(l)

