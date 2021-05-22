a = eval(input('Please enter the grade point: '))
b = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0]
c = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
if a >= 4.0:
    d = 'A+'
else:
    for i in range(11):
        if a == b[i]:
            d = c[i]
        if a < b[i] and b[i + 1] < a:
            if a >= (b[i] + b[i + 1]) / 2:
                d = c[i]
            else:
                d = c[i + 1]
print(f'The letter grade is {d}.')