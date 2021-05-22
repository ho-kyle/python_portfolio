a = eval(input('Please enter the pressure: '))
b = eval(input('Please enter the volume: '))
c = eval(input('Please enter the temperature: '))
n = a * b / (8.134 * (c +
 273.15))
print(f'The number of moles of gas in SCUBA tank is {n}')