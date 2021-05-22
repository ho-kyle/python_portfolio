a = eval(input('Please enter the cost of the meal:'))
tax = a * 0.1
tip = a * 0.18
total = a + tax + tip
print('The tax amount is %.2f' %tax)
print('The tip amount is %.2f' %tip)
print('The grand total for the meal is %.2f' %total)