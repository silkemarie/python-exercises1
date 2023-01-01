colors = {'red', 'green', 'blue'}

print('red' in colors)  
# Output: True

print('yellow' in colors)  
# Output: False

colors.add('yellow')
print(colors)  
# Output: {'red', 'green', 'blue', 'yellow'}

colors.remove('red')
print(colors)  
# Output: {'green', 'blue', 'yellow'}


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union: gets all the items that are in either set
print(A.union(B))  
# Output: {1, 2, 3, 4, 5, 6}

# Intersection: gets the items that are in both sets
print(A.intersection(B))  
# Output: {3, 4}

# Difference: gets the items that are in the first set but not in the second set
print(A.difference(B))  
# Output: {1, 2}
