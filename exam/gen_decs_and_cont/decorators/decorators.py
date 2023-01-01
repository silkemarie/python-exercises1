def log_function(func):
    """Decorator function that logs the arguments and return value of a decorated function."""
    def wrapper(*args, **kwargs):
        # Log the arguments
        print(f'Args: {args}, Kwargs: {kwargs}')
        
        # Call the decorated function
        result = func(*args, **kwargs)
        
        # Log the return value
        print(f'Result: {result}')
        
        return result
    return wrapper

# Define a function to be decorated
def add(x, y):
    return x + y

# Decorate the function with the log_function decorator
@log_function
def decorated_add(x, y):
    return x + y

# Call the decorated function
result = decorated_add(3, 4)

# Output:
# Args: (3, 4), Kwargs: {}
# Result: 7
