a = eval(input('Please enter the deposit:'))
for i in range(1,4):
    a *= 1.04
    print(f'The saving after {i} year(s) is {a:.2f}')
    