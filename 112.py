a = input('Please enter a number(blank line to quit): ')
sum = 0
l = []
while a != '':
    sum += eval(a)
    l.append(eval(a))
    a = input('Please enter a number(blank line to quit): ')
l.sort()
average = sum / len(l)
print(average)
print(l)