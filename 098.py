def hex2int(n):
    a = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f']
    b = ['10', '10', '11', '11', '12', '12', '13', '13', '14', '14', '15', '15']
    for i in range(12):
        if n == a[i]:
            n = b[i]
            break
    return n
def int2hex(n):
    a = ['10', '11', '12', '13', '14', '15']
    b = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(6):
        if n == a[i]:
            n = b[i]
            break
    return n
def main():
    a = input('Please enter a value: ')
    if a == 'A' or a == 'a' or a == 'B' or a == 'b' or a == 'C' or a == 'c' \
    or a == 'D' or a == 'd' or a == 'E' or a == 'e' or a == 'F' or a == 'f':
        print(hex2int(a))
    elif a == '0' or a == '1' or a == '2' or a == '3' or a == '4' or a == '5' \
      or a == '6' or a == '7' or a == '8' or a == '9' or a == '10' or  a == '11'\
      or a == '12' or a == '13' or a == '14' or  a == '15':
        print(int2hex(a))
    else:
        print('error')
main()