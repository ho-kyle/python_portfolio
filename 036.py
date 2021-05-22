a = input('Please enter a letter of the alphabet: ')
if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
    print(a.upper(), 'is vowel.')
elif a == 'y':
    print('Sometimes',a ,'is vowel, and sometimes',a ,'is a consonant.')
else:
    print(a.upper(), 'is consonant.')