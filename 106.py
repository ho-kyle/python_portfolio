def removeOutlier(a, remove):
    a.sort()
    for i in range(remove):
        a.pop()
    for i in range(remove):
        a.pop(0)
    return a
def main():
    list = []
    value = ''
    value = input('Please enter a value(blank line to quit): ')
    while value != '':
        value = eval(value)
        list.append(value)
        value = input('Please enter a value(blank line to quit): ')
    remove = eval(input('Please enter a value: '))
    if len(list) < 4:
        print('You didn\'t enter enough value.')
    else:
        print(f'{list}')
        print(f'{removeOutlier(list, remove)}')
        print(f'{list}')
main()