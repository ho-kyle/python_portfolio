a = eval(input('Please enter the frequency of the radiation: '))
b = [3 * 10**9, 3 * 10**12, 4.3 * 10**14, 7.5 * 10**14, 3 * 10**17, 3 * 10**19]
c = ['radio waves', 'microwaves', 'infrared light', 'visible light', 'ultraviolet light', 'x-rays', 'gamma rays']
if a >= 3 * 10**19:
    d = 'gamma rays'
for i in range(6):
    if a < b[i]:
        d = c[i]
        break
print(d)
    