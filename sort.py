# Sort a text
# Create a function that takes a string as a parameter and returns a list.
# The function should remove all vowels and sort the consonants in alphabetic order, and the return the result


# __________________________________________________
# Sort a list
# Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
# Sort this list by using the sorted() build in function.
# Sort the list in reversed order.
# Sort the list on the lenght of the name.
# Sort the list based on the last letter in the name.
# Sort the list with the names where the letter ‘a’ is in the name first.


# __________________________________________________
# Text editor plugin simulation
from posixpath import split
from typing import Counter


s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'
# Count the number of characters including blank spaces.
# Count the number of characters excluding blank spaces.
# Count the number of words.

counter = Counter(s)
print('Number of characters incl blank spaces: ' + str(len(s)))

exclcounter = len(s) - counter[' ']
print('Number of characters excl blank spaces: ' + str(exclcounter))

words = len(s.split())
print('Number of words: ', words)


# __________________________________________________
# Files
# Create a file and call it lyrics.txt (it does not need to have any content)
# Create a new file and call it songs.docx and in this file write 3 lines of text to it.
# open and read the content and write it to your terminal window. * you should use both the read(), readline(), and readlines() methods for this. (so 3 times the same output).

with open('lyrics.txt', 'w') as f:
    f.write('test')

with open('songs.docs', 'w') as f:
    f.write('Linje 1 af min sang \n')
    f.write('Linje 2 af min sang \n')
    f.write('Linje 3 af min sang \n')
   

f = open('songs.docs', 'r')
print(f.read())

f = open('songs.docs', 'r')
print(f.readline(), f.readline(), f.readline())

f = open('songs.docs', 'r')
print(f.readlines())

# __________________________________________________
# Tuples
# Sort a list of tuples
# Based on this list of tuples: [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]
l = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]
# 2. Sort the list so the result looks like this: [(2, 1), (3, 1), (10, 1), (1, 2), (2, 2), (2, 2), (3, 2), (10, 4), (1, 5)]

#l1 = sorted(l, key=lambda x: x[1])
l1 = sorted(l, key=lambda x: (x[1], x[0]))
print(l1)