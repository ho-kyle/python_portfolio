a = eval(input('Please enter a rating : '))
if a == 0.0:
    b = 'unacceptable'
elif a == 0.4:
    b = 'acceptable'
elif a >= 0.6:
    b = 'meritorious'
else:
    b = ''
if b == '':
    print('error')
else:
    print(f'The performance was {b}.')
    print(f'The amoumt of the employee\'s raise is {2400.00 * a}.')