def count_up_to(max):
    """Generate a sequence of numbers from 0 to max."""
    count = 0
    while count < max:
        yield count
        count += 1

# Create a generator object
counter = count_up_to(5)

# Use the generator object in a for loop
for number in counter:
    print(number)

# Output:
# 0
# 1
# 2
# 3
# 4
