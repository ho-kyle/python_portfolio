a = input('Please enter the name of a month: ').upper()
day = 31
if a == 'APRIL' or a =='JUNE' or a == 'SEPTENBER' or a == 'NOVEMBER':
    day = 30
elif a.upper() == 'FEBRUARY':
    day = '28 or 29'
print(f'{a} has {day} days in it.')