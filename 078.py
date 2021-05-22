a = eval(input('Please enter the decimal number: '))
b = a % 2
c = a // 2
d = ''
d = str(b) + d
while c > 0:
    b = c % 2
    c = c // 2
    d = str(b) + d
print(d)