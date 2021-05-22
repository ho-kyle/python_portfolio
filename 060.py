from random import randrange
a = randrange(0, 38)
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
if a == 37:
    print(f'The spin resulted in 00...')
    print(f'Pay 00')
else:
    print(f'The spin resulted in {a}...')
    print(f'Pay {a}')
for i in range(18):
    if a == red[i]:
        print('Pay Red')
        break
    elif a == 0 or a == 00:
        print('Pass')
        break
    else:
        print('Pay Black')
        break
if a > 0 and a < 37:
    if a % 2 == 1:
        print('Pay Odd')
    else:
        print('Pay Even')
if a >= 1 and a <= 18:
    print('Pay 1 to 18')
elif a >= 19 and a <= 36:
    print('Pay 19 to 36')