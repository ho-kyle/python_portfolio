from random import randrange
Min = 1
Max = 49
num = 6
l = []
s = ''
for i in range(num):
    a = randrange(Min, Max + 1)
    while a in l:
        a = randrange(Min, Max + 1)
    l.append(a)
l.sort()
print(l)