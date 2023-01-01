# Define a function
def greet(name):
    return f'Hello, {name}!'

# Assign the function to a variable
greeting = greet

# Pass the function as an argument to another function
def greet_twice(func, name):
    return func(name) + ' ' + func(name)

result = greet_twice(greeting, 'Alice')
print(result)  
# Output: Hello, Alice! Hello, Alice!


# Return the function from a function
def create_greeting(name):
    def greeting(name):
        return f'Hello, {name}!'
    return greeting

greeting_func = create_greeting('Bob')
result = greeting_func()
print(result)  
# Output: Hello, Bob!
