a = input('Please enter a string of characters: ')
if len(a) == 6 and a[0] >= 'A' and a[0] <= 'Z' and \
    a[1] >= 'A' and a[1] <= 'Z' and a[2] >= 'A' and \
    a[2] <= 'Z' and a[3] >= '0' and a[3] <= '9' and \
    a[4] >= '0' and a[4] <= '9' and a[5] >= '0' and \
    a[5] <= '9':
    print('The plate is valid older style plate.')
elif len(a) == 7 and a[0] >= '0' and a[0] <= '9' and \
    a[1] >= '0' and a[1] <= '9' and a[2] >= '0' and \
    a[2] <= '9' and a[3] >= '0' and a[3] <= '9' and \
    a[4] >= 'A' and a[4] <= 'Z' and a[5] >= 'A' and \
    a[5] <= 'Z' and a[6] >= 'A' and a[6] <= 'Z':
    print('The plate is valid newer style plate.')
else:
    print('The plate is not valid.')
