# Sorting through a list:

words = ['apple', 'banana', 'cherry', 'date']

sorted_words = sorted(words)
print(sorted_words)

numbers = [3, 1, 4, 2]
sorted(numbers) 


sorted_words = sorted(words, key=len)
print(sorted_words)


# Sorting through a dict:

employees = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 35}]

# Sort by age:
sorted_employees = sorted(employees, key=lambda x: x['age'])
print(sorted_employees) 