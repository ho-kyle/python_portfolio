ans = 0
print('猜數字遊戲，請心中想一個 0 - 7 之間的數字，然後回答問題')
print('有沒有看到心中的數字:')
print('1, 3, 5, 7')
a = input('輸入y或Y代表有，其他代表無:')
if a == 'y' or a == 'Y':
    ans += 1
print('有沒有看到心中的數字:')
print('2, 3, 6, 7')
a = input('輸入y或Y代表有，其他代表無:')
if a == 'y' or a == 'Y':
    ans += 2
print('有沒有看到心中的數字:')
print('4, 5, 6, 7')
a = input('輸入y或Y代表有，其他代表無:')
if a == 'y' or a == 'Y':
    ans += 4
print(f'讀者心中所想的數字是: {ans}')