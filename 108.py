l = []
num = input('Please enter an integer(blank to quit): ')
while num != '':
    l.append(eval(num))
    num = input('Please enter an integer(blank to quit): ')
l.sort()
for i in l:
    print(i)