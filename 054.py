a = eval(input('Please enter a wavelength: '))
b = [380, 450, 495, 570, 590, 620, 750]
c = ['violet', 'blue', 'green', 'yellow', 'orange', 'red']
for i in range(6):
    if a >= b[i] and a < b[i + 1]:
        d = c[i]
if a < 380 or a >= 750:
    print('error')
else:
    print(d)