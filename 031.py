a = eval(input('Please enter a four-digit integer: '))
b = a % 10
c = (a // 10) % 10
d = (a // 100) % 10
e = a // 1000
sum = b + c + d + e
print(f'{e} + {d} + {c} + {b} = {sum}')