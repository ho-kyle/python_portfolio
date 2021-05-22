a = eval(input('Please enter an integer (2 or greater): '))
if a < 2:
    print('error')
factor = 2
while factor <= a:
    if a % factor == 0:
        print(factor)
        a = a // factor
    else:
        factor += 1