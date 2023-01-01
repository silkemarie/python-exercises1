#the Python way:

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers)


#the Java way (in Python):
def calculateAverage(numbers):
    """Calculate the average of a list of numbers."""
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)
