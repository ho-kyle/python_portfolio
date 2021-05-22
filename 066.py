a = input('Please enter a letter grade: ')
b = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
c = [4.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0]
sum = 0
n = 0
while a != '':
    n += 1
    for i in range(12):
        if a == b[i]:
            sum += c[i]
            break
    a = input('Please enter a letter grade: ')
print(f'{sum / n}')