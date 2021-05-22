a = eval(input('Please enter the value of the air temperature: '))
b = eval(input('Please enter the value of the wind speed: '))
WCI = 13.12 + 0.6215 * a - 11.37 * b**0.16 + 0.3965 * a * b**0.16
print(f'The wind chill index is {WCI:.0f}')