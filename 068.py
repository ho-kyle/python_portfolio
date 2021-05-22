a = input('Please enter 8 bits: ')
while a != '':
    if a.count('0') + a.count('1') != 8 or len(a) != 8:
        print('error')
    else:
        if a.count('1') % 2 == 0:
            print('the parity bit should be 0')
        else:
            print('the parity bit should be 1')
    a = input('Please enter 8 bits: ')