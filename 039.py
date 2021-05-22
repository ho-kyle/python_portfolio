a = eval(input('Please enter the sound level in decibels: '))
b = [130, 106, 70, 40]
c = ['Jackhammer', 'Gas lawnmower', 'Alarm clock', 'Quiet room']
for i in range(4):
    if a == b[i]:
        print(f'The sound level in decibel is {c[i]}')
for i in range(3):
    if a < b[i] and a > b[i + 1]:
        print(f'The sound level in decibel is between c{i} and c{i + 1}')
if a < 130 or a > 40:
    print('Please enter the sound level in decibel between 40 ~ 130')