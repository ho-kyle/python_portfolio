import daysInMonth

def magicDates(day, month, year):
    if day * month == year - 1900:
        return True
def main():
    for year in range(1900, 2000):
        for month in range(1, 13):
            days = daysInMonth.daysInMonth(month, year)
            for day in range(1, days + 1):
                if magicDates(day, month, year):
                    print(f'{year}/{month}/{day}')
main()