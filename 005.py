a = eval(input('Please enter the number of containers which size is <= 1 liter:'))
b = eval(input('Please enter the number of containers which size is > 1 liter:'))
deposit = 0.1 * a + 0.25 * b
print('The deposit is $%.2f' %deposit)