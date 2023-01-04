#the Python way:

def calculate_average(numbers):
    return sum(numbers) / len(numbers)


#the Java way (in Python):

def calculateAverage(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

