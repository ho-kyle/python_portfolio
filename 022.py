from math import sqrt
s1 = eval(input('Please enter the lengths of the sides of a triangle: '))
s2 = eval(input('Please enter the lengths of the sides of a triangle: '))
s3 = eval(input('Please enter the lengths of the sides of a triangle: '))
s = (s1 + s2 + s3) / 2
area = sqrt(s * (s - s1) * (s - s2) * (s - s3))
print(f'The area is {area}')