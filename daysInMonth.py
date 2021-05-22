def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
def daysInMonth(month, year):
    a = [1, 3, 5, 7, 8, 10, 12]
    b = [4, 6, 9, 11]
    days = 0
    for i in range(7):
        if month == a[i]:
            return 31
    for i in range(4):
        if month == b[i]:
            return 30
    if isLeapYear(year):
        return 29
    else:
        return 28
    
def main():
    year = eval(input('Please enter the year: '))
    month = eval(input('Please enter the month: '))
    print(f'There are {daysInMonth(month, year)} days in {year}/{month}')
if __name__ == '__main__':
    main()