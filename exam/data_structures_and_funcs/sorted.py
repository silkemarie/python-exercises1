words = ['apple', 'banana', 'cherry', 'date']

# Sort the list automatically (alphebetically)
sorted_words = sorted(words)
print(sorted_words) # Output: ['apple', 'banana', 'cherry', 'date']


# Sort the list numerically: 
numbers = [3, 1, 4, 2]
sorted(numbers) # Output: [1, 2, 3, 4]


# Sort the list of words by their length
sorted_words = sorted(words, key=len)
print(sorted_words)  # Output: ['date', 'apple', 'banana', 'cherry']


#with dict:

employees = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 35}]

# Sort the list of employees by their age
sorted_employees = sorted(employees, key=lambda x: x['age'])
print(sorted_employees)  # Output: [{'name': 'Alice', 'age': 25}, {'name': 'John', 'age': 30}, {'name': 'Bob', 'age': 35}]
