from random import randint

a = list(range(1,50))
b = []
for i in range(6):
    b.append(a.pop(randint(0, len(a) - 1)))
print(sorted(b))