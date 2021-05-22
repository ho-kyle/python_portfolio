i = 2
a = 3
n = 1
print(3)
while i < 30:
    d = (-1)**(n + 1) * 4 / (i * (i + 1) * (i + 2))
    a += d
    i = i + 2
    n += 1
    print(a)