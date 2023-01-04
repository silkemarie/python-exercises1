# Definer en funktion:
def greet(name):
    return f'Hello, {name}!'

# Assign funktionen til en variabel:
greeting = greet

# Videresend funktionen som et argument til en anden funktion:
def greet_twice(func, name):
    return func(name) + ' ' + func(name)

result = greet_twice(greeting, 'Claus')
print(result)  

# Returnerer funktionen fra en funktion
def create_greeting(name):
    def greeting(name):
        return f'Hello, {name}!'
    return greeting

greeting_func = create_greeting('Jens')
result = greeting_func()
print(result)  

