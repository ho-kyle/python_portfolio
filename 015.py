inch = 1/12
yard = 3
mile = 5280
a = eval(input('Please enter the measurement in feet: '))
print(a // mile,'miles')
a %= mile
print(a // yard,'yard')
a %= yard
print(a // inch,'inch')