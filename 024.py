a = eval(input('Please enter the number of days: '))
b = eval(input('Please enter the number of hours: '))
c = eval(input('Please enter the number of minutes: '))
d = eval(input('Please enter the number of seconds: '))
e = a * 24 * 60 * 60 + b * 60 * 60 + c * 60 + d
print(f'The total number of seconds is {e}')