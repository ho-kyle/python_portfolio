a = eval(input('Please enter the number of minutes\
 used in a month: '))
b = eval(input('Please enter the number of text messages\
 used in a month: '))
baseCharge = 15.00
addMinutesCharge = (a - 50) * 0.25
addTextMessageCharge = (b - 50) * 0.15
the911Fee = 0.44
tax = (baseCharge + addMinutesCharge +\
 addTextMessageCharge + the911Fee) * 0.05
totalBillAmount = baseCharge + addMinutesCharge + \
addTextMessageCharge + the911Fee + tax
print(f'base charge: {baseCharge:.2f}')
if a > 50:
    print(f'additional minute: {addMinutesCharge:.2f}')
if b > 50:
    print(f'additional text message charge: {addTextMessageCharge:.2f}')
print(f'911 fee: {the911Fee:.2f}')
print(f'tax: {tax:.2f}')
print(f'total bill amount: {totalBillAmount:.2f}')
