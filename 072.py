a = input('Please enter a string: ')
for i in range(len(a) // 2):
    b = len(a) - 1 - i
    if a[i] != a[b]:
        print('It is not a palindrome.')
        break
    else:
        print('It is a palindrome.')
        
