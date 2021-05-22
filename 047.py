a = input('Please enter the month of your birth: ')
b = eval(input('Please enter the day of your birth: '))
c = ['Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius']
d = ['December','Janauary', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']
e = [22, 20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22]
for i in range(12):
    if a == d[i]:
        if b > e[i]:
            f = c[i]
        else:
            f = c[i-1]
        break
print(f'Your zodiac sign is {f}')