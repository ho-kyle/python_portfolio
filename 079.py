from random import randrange
max_range = 100
max = randrange(1, max_range + 1)
print(max)
n = 0
for i in range(100):
    a = randrange(1, max_range + 1)
    if a > max:
        max = a
        print(f'{max} <== Update')
        n += 1
    else:
        print(a)
print(f'The maximum value found was {max}')
print(f'The maximum value was Updated {n} times')