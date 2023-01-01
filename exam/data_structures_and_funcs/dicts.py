person = {'name': 'John', 'age': 30, 'country': 'USA'}

print(person['name'])  
# Output: 'John'

print(person['age'])  
# Output: 30


print(person.get('name'))  
# Output: 'John'

print(person.get('age'))  
# Output: 30

person['age'] = 31
print(person)  
# Output: {'name': 'John', 'age': 31, 'country': 'USA'}

person['city'] = 'New York'
print(person)  
# Output: {'name': 'John', 'age': 31, 'country': 'USA', 'city': 'New York'}
