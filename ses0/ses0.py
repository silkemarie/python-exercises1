# Ex 0.1: Slicing
#['World', 'Huston', 'we', 'are']
#['Hello', 'World']
#['are', 'here']
#['are']
#['Hello', 'Huston', 'are']
#['here', 'are', 'we', 'Huston', 'World', 'Hello']
#['World', 'Huston', 'we', 'are']


houston = ['Hello', 'World', 'Huston', 'we', 'are', 'here']

print(houston[1:5])
print(houston[0:2])
print(houston[4:]) #eller 4:6
print(houston[4:5])
print(houston[::2])
print(houston[::-1])
print(houston[1:5])

# Create a function that takes a string as a parameter and returns a list.
# The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.

def sort_func(s):
    for i in ['a', 'e', 'i', 'o', 'u', 'y', ' ']:
        s = s.lower().replace(i,'')
    
    return sorted(s)

print(sort_func('Hello world'))

# Sort a list
# Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
# Sort this list by using the sorted() build in function.
# Sort the list in reversed order.
# Sort the list on the lenght of the name.
# Sort the list based on the last letter in the name.
# Sort the list with the names where the letter ‘a’ is in the name first.

my_pets = ('Suki', 'Yoko', 'Sarii', 'Artax', 'Babe the Pig')

sorted_pets = sorted(my_pets)
print('Sorted: ')
print(sorted_pets)

reverse_sorted_pets = sorted(my_pets, reverse=True)
print('Reverse sorted: ')
print(reverse_sorted_pets)

len_sorted_pets = sorted(my_pets, key=len)
print('Length sorted: ')
print(len_sorted_pets)

def last(s):
    return s[-1]

last_sorted_pets = sorted(my_pets, key=last)
print('Sorted by last letter: ')
print(last_sorted_pets)

def letter_a(s):
    if 'a' in s.lower():
        return False
    return True

a_sorted_pets = sorted(my_pets, key=letter_a)
print('Sorted by A: ')
print(a_sorted_pets)


#===========================================
# Count the number of characters including blank spaces.
# Count the number of characters excluding blank spaces.
# Count the number of words.

s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'

print('Character count incl blank spaces: ')
print(len(s))

print('Character count excl blank spaces: ')
nospace = s.replace(' ', '')
print(len(nospace))

wordsplit = s.split(' ')
print(len(wordsplit))

