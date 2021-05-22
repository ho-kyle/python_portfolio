from random import randint
a = list(range(5))

b = []
for i in range(5):
    b.append(a.pop(randint(0,len(a) - 1)))
print(b)