a = input('Please enter the binary number: ')
sum = 0
for i in range(len(a)):
    b = eval(a[i]) * 2**(len(a) - i - 1)
    sum += b
print(sum)