from math import acos, sin, cos, radians
t1 = eval(input('Please enter the value of t1: '))
g1 = eval(input('Please enter the value of g1: '))
t2 = eval(input('Please enter the value of t2: '))
g2 = eval(input('Please enter the value of g2: '))
distanse = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))
print(f'The distanse between the points is {distanse}')
