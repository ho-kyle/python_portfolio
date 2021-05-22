a = eval(input('Please enter a value: '))
sum = 0
n = 0
if a == 0:
    print('error')
else:
    while a != 0:
        sum += a
        n += 1
        a = eval(input())
    average = round(sum / n, 2)
    print(average)
