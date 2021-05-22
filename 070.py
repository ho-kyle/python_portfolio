a = input('Please enter the message: ')
shift = eval(input('Please enter the shift amount: '))
new_message = ''
for ch in a:
    if ch > 'a' and ch < 'z':
        b = ord(ch) - ord('a')
        c = (b + shift) % 26 + ord('a')
        d = chr(c)
        new_message += d
    elif ord(ch) > ord('A') and ord(ch) < ord('Z'):
        b = ord(ch) - ord('A')
        c = (b + shift) % 26 + ord('A')
        d = chr(c)
        new_message += d
    else:
        new_message += ch
print(new_message)