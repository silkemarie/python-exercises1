# Pythonic: use parentheses
result = (2 + 3) * 4
print(result)  # Output: 20

# Non-pythonic: not using parentheses
result = 2 + 3 * 4
print(result)  # Output: 14



# Pythonic: // operator for integer division
result = 10 // 3
print(result)  # Output: 3

# Non-pythonic: using /
result = 10 / 3
print(result)  # Output: 3.3333333333333335



# Pythonic: Using ** for exponentiation
result = 2 ** 3
print(result)  # Output: 8

# Non-pythonic: using pow
result = pow(2, 3)
print(result)  # Output: 8



# Pythonic: Use the += and -= operators for incrementing and decrementing variables
count = 0
count += 1
count -= 1

# Non-pythonic:
count = 0
count = count + 1
count = count - 1
# Python also provides the ++ and -- operators as seen in Java. This is also considered non-pythonic though.



# Pythonic: "is" and "is not" operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)  # Output: False
print(x is z)  # Output: True
print(x is not y)  # Output: True

# Non-pythonic:
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x == y)  # Output: True
print(x == z)  # Output: True
print(x != y)  # Output: False
