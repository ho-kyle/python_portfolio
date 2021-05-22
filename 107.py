l = []
a = input('Please enter a word(blank line to quit): ')
while a != '':
    if a not in l:
        l.append(a)
    a = input('Please enter a word(blank line to quit): ')
for word in l:
    print(word)