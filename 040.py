a = []
for i in range(3):
    e = eval(input('Please enter the first lenght of the triangle: '))
    a.append(e)
b = max(a)
c = min(a)
d = sum(a) - b - c
if b == c:
    print('It is an equilateral triangle.')
elif c**2 + d**2 == b**2:
    print('It is an isosceles triangle.')
else:
    print('The triangle is scalene.')