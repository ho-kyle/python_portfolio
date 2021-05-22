a = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
b = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]
n = eval(input('Please enter a frequency: '))
for i in range(7):
    if n == b[i]:
        print(f'The name of the note is {a[i]}.')