a = eval(input('Please enter the mass of water: '))
b = eval(input('Please enter the temperature change: '))
q = a * 4.186 * b 
print(f'Require {q} J.')
kwh = 2.777e - 7
price = 8.9
c = q * kwh * price
print(f'The cost of boiling water for a cup of coffee is {c}')