Holiday = ['New year\'s day', 'Canada day', 'Christmas day']
Date = ['Januray 1', 'July 1', 'December 25']
a = input('Please enter a month and date: ')
for i in range(3):
    if a == Date[i]:
        print(Holiday[i])
        break
else:
    print('The entered month and day do not correspond to a fixed-day')