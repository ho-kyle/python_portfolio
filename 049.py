a = eval(input('Please enter a magnitude: '))
b = ['Micro', 'Very minor', 'Minor', 'Light', 'Moderate', 'Strong', 'Major', 'Great', 'Meteoric']
for i in range(2, 11):
    if a < i:
        c = b[i - 2]
        break
    else:
        c = 'Meteoric'
print(f'The appropriate descriptor is {c}.')