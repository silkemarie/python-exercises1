#============ For

# Print the numbers from 1 to 10
for i in range(1, 11):
    print(i)

# Iterate over a list of names
names = ['Claus', 'Jens', 'Silke', 'Kristian']
for name in names:
    print(name)


#============ While

# Print the numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# Prompt the user for input until they enter a valid password
password = ''
while password != 'secret':
    password = input('Enter password: ')


#============ Do-while

# Prompt the user for input until they enter a valid password
password = ''
while True:
    password = input('Enter password: ')
    if password == 'secret':
        break


#============ Loop control

# Print the numbers from 1 to 10, but skip 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Print the numbers from 1 to 10, but exit the loop when i reaches 5
for i in range(1, 11):
    if i == 5:
        break
    print(i)

#============ List comprehension

# Create a list of the squares of the integers from 1 to 10 using a for loop
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Create a list of the squares of the integers from 1 to 10 using list comprehension
squares = [i ** 2 for i in range(1, 11)]
print(squares)  # Output:
