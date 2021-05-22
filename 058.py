a = input('Please enter a date: ')
year = eval(a[0:4])
month = a[5:7]
date = a[8:10]
if year % 400 == 0:
    isLeapYear = True
elif year % 100 == 0:
    isLeapYear = False
elif year % 4 == 0:
    isLeapYear = True
else:
    isLeapYear = False
if isLeapYear:
    if date == '31' and month == '01' or month == '03' or month == '05' \
        or month == '07' or month == '08' or month == '10':
        print(f'{year}-{eval(a[6]) + 1}-01')
    elif date == '31' and month == '12':
        print(f'{eval(year) + 1}-{month}-{date}')
    elif date == '30' and month == '04' or month == '06' or month == '09' \
        or month == '11':
        print(f'{year}-{eval(a[6]) + 1}-01')
    elif date == '29' and month == '02':
        print(f'{year}-{eval(a[6]) + 1}-01')
    else:
        if a[8] == 0:
            print(f'{year}-{month}-0{a[9] + 1}')
        else:
            print(f'{year}-{month}-{eval(date) + 1}')
if not isLeapYear:
    if date == '31' and month == '01' or month == '03' or month == '05' \
        or month == '07' or month == '08' or month == '10':
        print(f'{year}-{eval(a[6]) + 1}-01')
    elif date == '31' and month == '12':
        print(f'{eval(year) + 1}-{month}-{date}')
    elif date == '30' and month == '04' or month == '06' or month == '09' \
        or month == '11':
        print(f'{year}-{eval(a[6]) + 1}-01')
    elif date == '28' and month == '02':
        print(f'{year}-{eval(a[6]) + 1}-01')
    else:
        if a[8] == 0:
            print(f'{year}-{month}-0{a[9] + 1}')
        else:
            print(f'{year}-{month}-{eval(date) + 1}')