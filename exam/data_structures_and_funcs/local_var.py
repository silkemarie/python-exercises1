# Local variables are defined within a function and is only accessible within that function. 
# Local variables are created when a function is called and are destroyed when the function returns. 
# They are different from global variables, which are defined outside of any function and are accessible from anywhere in the program. 


def greet(name):
  greeting = "Hello, " + name  # greeting is a local variable
  print(greeting)

greet("Alice")  # prints "Hello, Alice"
print(greeting)  # causes an error because greeting is not defined outside of the function

