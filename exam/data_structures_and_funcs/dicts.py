person = {'name': 'Silke', 'age': 30, 'country': 'Denmark'}

print(person['name'])  

print(person['age'])  


print(person.get('name'))  

print(person.get('age'))  

person['age'] = 31
print(person)  

person['city'] = 'Copenhagen'
print(person)  


for key, value in person.items():
    print(f'{key}: {value}')

for key, value in person.items():
    print(value)

for key in person:
    print(key)

