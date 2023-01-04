colors = {'red', 'green', 'blue'}

print('red' in colors)  

print('yellow' in colors)  

colors.add('yellow')
print(colors)  

colors.remove('red')
print(colors)  


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union: 
print(A.union(B))  

# Intersection: 
print(A.intersection(B))  

# Difference: 
print(A.difference(B))  
