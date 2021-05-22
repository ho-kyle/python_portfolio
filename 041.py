C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88
a = input('Please enter two character note name, such as C4: ')
name = a[0]
number = eval(a[1])
if name == 'C':
    freq = C4
elif name == 'D':
    freq = D4
elif name == 'E':
    freq = E4
elif name == 'F':
    freq = F4
elif name == 'G':
    freq = G4
elif name == 'A':
    freq = A4
elif name == 'B':
    freq = B4
Freq = freq * 2**(4 - number)
print(f'The frequency of {a} is {Freq}')
