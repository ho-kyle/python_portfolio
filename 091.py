def precedence(s):
    if s == '+' or s =='-':
        return 1
    elif s == '*' or s == '/':
        return 2
    elif s == '^':
        return 3
    else:
        return -1
def main():
    a = input('Please enter an operator: ')
    if precedence(a) == -1:
        print(f'{a} is not an operator')
    else:
        print(f'The precedence of {a} is {precedence(a)}')
main()