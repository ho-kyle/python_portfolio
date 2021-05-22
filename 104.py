l = []
a = eval(input('Please enter a value(0 exit) :'))
while a != 0:
    l.append(a)
    a = eval(input('Please enter a value(0 exit) :'))
l.sort()
for i in l:
    print(i)