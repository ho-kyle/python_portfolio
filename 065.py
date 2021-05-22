from math import sqrt
first_x = eval(input('Please enter the x part of the coordinate: '))
first_y = eval(input('Please enter the y part of the coordinate: '))
prev_x = first_x
prev_y = first_y
x = input('Please enter the x part of the coordinate (blank to quit): ')
perimeter = 0
while x != '':
    x = eval(x)
    y = eval(input('Please enter the y part of the coordinate: '))
    line = sqrt((x - prev_x)**2 + (y - prev_y)**2)
    perimeter += line
    prev_x = x
    prev_y = y
    x = input('Please enter the x part of the coordinate (blank to quit):　')
line = sqrt((prev_x - first_x)**2 + (prev_y - first_y)**2)
perimeter += line
print(f'The perimeter of that polygon is {perimeter}')