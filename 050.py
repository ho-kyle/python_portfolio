a = eval(input('Please enter the value of a: '))
b = eval(input('Please enter the value of b: '))
c = eval(input('Please enter the value of c: '))
D = b**2 - 4 * a * c
D_sqrt = pow(D, 0.5)
r1 = ((-b) + D_sqrt) / (2 * a)
r2 = ((-b) - D_sqrt) / (2 * a)
print(D_sqrt)
if D > 0:
    print(f'The number of the real roots is 2.')
    print(f'The value of the real roots is {r1} and {r2}.')
if D == 0:
    print(f'The number of the real roots is 1.')
    print(f'The value of the real roots is {r1}.')
if D < 0:
    print(f'The number of the real roots is 0.')