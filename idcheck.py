def idcheck(c):
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',\
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',\
         'Y', 'Z']
    b = ['10', '11', '12', '13', '14', '15', '16', '17', '34', '18',\
         '19', '20', '21', '22', '35', '23', '24', '25', '26', '27',\
         '28', '29', '32', '30', '31', '33']
    n = 0
    if len(str(c)) != 10:
        return '錯誤的身分證字號'
    if not c[0].isalpha():
        return '錯誤的身分證字號'
    for i in a:
        if c[0] == i:
            d = str(b[n])
            e = d[0]
            f = d[1]
            break
        n += 1
    g = eval(e) + 9 * eval(f) + 8 * eval(c[1]) + 7 * eval(c[2]) \
        + 6 * eval(c[3]) + 5 * eval(c[4]) + 4 * eval(c[5]) \
        + 3 * eval(c[6]) + 2 * eval(c[7]) + eval(c[8]) + eval(c[9])
    if g % 10 == 0:
        return '正確的身分證字號'
    else:
        return '錯誤的身分證字號'
def main():
    c = input('請輸入身分字號: ')
    print(f'{idcheck(c)}')
if __name__ == '__main__':
    main()
