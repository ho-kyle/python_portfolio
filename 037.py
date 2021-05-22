a = eval(input('Please enter the number of sides(from 3 to 10): '))
b = ''
if a == 3:
    b = 'triangle'
elif a == 4:
    b = 'quadrilateral'
elif a == 5:
    b = 'pentagon'
elif a == 6:
    b = 'hexagon'
elif a == 7:
    b = 'heptagon'
elif a == 8:
    b = 'octagon'
elif a == 9:
    b = 'nonagon'
elif a == 10:
    b = 'decagon'
else:
    b = 'error'
print(b)