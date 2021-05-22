from random import randrange
flip_number = 0
for i in range(10):
    a = randrange(3, 5)
    b = 0
    b += a
    n = 1
    c = ''
    c += str(a)
    if a == 3:
        print('H', end = ' ')
    else:
        print('T', end = ' ')
    while b != 9 and b != 12:
        a = randrange(3, 5)
        b += a
        n += 1
        c += str(a)
        if a == 3:
            print('H', end = ' ')
        else:
            print('T', end = ' ')
        if n > 3:
            e = eval(c[n-4])
            b -= e
    print(f'({n} flips)')
    flip_number += n
flip_number /= 10
print(f'On average, {flip_number} flips were needed.')