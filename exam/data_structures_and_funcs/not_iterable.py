# Can iter over (because its a list, not an int):

for x in [1, 2, 3]:
    print(x)

# Cannot iter over (because it's an int):

for x in 5:
    print(x)


# Iterating over a string:

string = "hello"

for char in string:
    print(char)

# Output:
# h
# e
# l
# l
# o

# Can't iterate over a string that contains special characters, like a tab or a newline
string = "hello\tworld\n"

for char in string:
    print(char)

# Output:
# h
# e
# l
# l
# o
# 	
# w
# o
# r
# l
# d
# 
