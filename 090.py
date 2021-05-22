def isInteger(s):
    s = s.strip()
    if (s[0] == '+' or s[0] == '-') and s[1:len(s)].isdigit():
        return True
    if s.isdigit():
        return True
    else:
        return False
def main():
    a = input('Please enter a string: ')
    if isInteger(a):
        print(f'{a} represent an integer.')
    else:
        print(f'{a} does not represent an integer.')
main()