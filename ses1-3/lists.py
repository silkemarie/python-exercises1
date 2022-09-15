#Introduktion til lists og tuples. 

l = [1, 'Hello, True']
print(l)

l[1:3]
print(l)

s = 'Hello world'
print(s[1:4])

tal = (1, 2, 3)

print(len(tal))
print(max(tal))

#zip() = en builtin function

t1 = (1, 2, 3, 4)
print(t1)
l1 = [1, 2, 3, 4]
print(l1)
l1.append(5)
print(l1)

l = ['Hello', 12]
# l = en liste her. []
t = ('Hello', 12)
# t = en tuple her. ()

#Loop:
for i in [1, 2, 3, 4]:
    print(i)

#range
#hvis jeg kun har et tal med, starter den på 0 og går op til dét tal
for i in range(1, 10):
    print(i)

for i in l[0:5]:
    print(i)