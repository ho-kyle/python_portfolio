a = input('Please enter a position: ')
b = a[0]
c = eval(a[1])
d = ['a', 'c', 'e', 'g']
e = ['b', 'd', 'f', 'h']
for i in range(4):
    if b == d[i]:
        num = c
    elif b == e[i]:
        num = c + 1
if num % 2 == 1:
    print('The color of the square is black.')
else:
    print('The color of the square is white.')
    