def formattingList(l):
    s = ''
    if len(l) == 0:
        return '<error>'
    if len(l) == 1:
        return l[0]
    if len(l) >= 2:
        for i in range(len(l) - 2):
            s = s + l[i] + ', '
        s = s + l[-2] + ' and ' + l[-1]
        return s
def main():
    l = []
    a = input('Please enter an item(blank line to quit): ')
    while a != '':
        a = input('Please enter an item(blank line to quit): ')
        print(formattingList(l))
main()