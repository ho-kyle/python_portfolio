def onlyWord(s):
    l = s.split(' ')
    for i in range(len(l)):
        if not l[i][-1].isalnum():
            print(l[i])
            l[i] = l[i][:-1]
            print(l[i])
    return l
def main():
    a = input('Please enter a string: ')
    print('All of the words in the string with the punctuation marks removed.')
    print(f'{onlyWord(a)}')
main()