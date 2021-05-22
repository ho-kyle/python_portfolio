a = eval(input('Please enter the human years: '))
if a < 0:
    print('error')
elif a < 2:
    b = a * 10.5
    print('The dog years are:', b)
else:
    b = 21 + (a - 2) * 4
    print('The dog years are:', b)