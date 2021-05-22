a = eval(input('Please enter the pressure in kilopascals: '))
b = a * 0.145037738
c = a * 7.50061683
d = a * 0.00986923267
print(f'The equivalent pressure in pounds per square inch is {b:.2f}, in millimeters of mercury is {c:.2f}, in atmospheres is {d:.2f}')