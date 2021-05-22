from math import pi, tan
s = eval(input('Please enter the value of s: '))
n = eval(input('Please enter the value of n: '))
area = n * s**2 / 4 * tan(pi / n)
print(f'The area of the regular polygon constructed is {area}')