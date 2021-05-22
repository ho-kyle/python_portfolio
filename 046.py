a = input('Please enter the name of the month: ')
b = eval(input('Please enter the day number: '))
if a == 'April' or a == 'May':
    c = 'Spring'
elif a == 'March':
    if b >= 20:
        c = 'Spring'
    else:
        c = 'Winter'
elif a == 'June':
    if b >= 21:
        c = 'Summer'
    else:
        c = 'Spring'
elif a == 'July' or a == 'August':
    c = 'Summer'
elif a == 'September':
    if b >= 22:
        c = 'Fall'
    else:
        c = 'Summer'
elif a == 'Octorber' or a == 'November':
    c = 'Fall'
elif a == 'December':
    if b >= 21:
        c = 'Winter'
    else:
        c = 'Fall'
print(f'The season is {c}.')