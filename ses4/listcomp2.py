#List comprehension
#Excercise 2

#From 2 lists, using a list comprehension, create a list containing:
#[(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']


#list comprehension med et nested loop:
print([(c,s) for c in colors for s in sizes])

#---------------------------------------------------------------------------------------

#If the tuple pair is in the following list, it should not be added to the comprehension generated list.

sold_out = [('Black', 'm'), ('White', 's')]

print([(c,s) for c in colors for s in sizes if (c,s) not in sold_out])

#print([(i,j) for i in colors for j in sizes if (i,j) not in (sold_out)])
#---------------------------------------------------------------------------------------


