a = eval(input('Please enter the number of seconds: '))
D = a // (24 * 60 * 60)
a %= (24 * 60 * 60)
HH = a // (60 * 60)
a %=  (60 * 60)
MM = a // 60
a %= 60
SS = a
print(f'{D}:{HH}:{MM}:{SS}')