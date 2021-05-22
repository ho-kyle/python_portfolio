a = eval(input('Please enter an integer: '))
b = eval(input('Please enter an integer: '))
c = min(a, b)
while a % c != 0 or b % c != 0:
    c -= 1
print(f'The greatest common divisor is {c}')