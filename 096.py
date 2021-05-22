def checkPassword(a):
    uppercase = False
    lowrecase = False
    num = False
    for ch in a:
        if ch >= 'A' and ch <= 'Z':
            uppercase = True
        if ch >= 'a' and ch <= 'z':
            lowrecase = True
        if ch >= '0' and ch <= '9':
            num = True
    if len(a) >= 8 and uppercase and lowrecase and num:
        return True
    else:
        return False
def main():
    a = input('Please enter a password: ')
    if checkPassword(a):
        print(f'{a} is good.')
    else:
        print(f'{a} isn\'t good.')
if __name__ == '__main__':
    main()