students = 3
exams = 4

studentGrades = [[77, 68, 86, 73], \
                 [96, 87, 89, 78], \
                 [70, 90, 86, 81]]

print('The list is:')

print('                 [0]  [1]  [2]  [3]')

for i in range(students):

    print('studentGrades[%d] ' % i, end = '')

    for j in range(exams):
        print('%-5d' % studentGrades[i][j], end = '')
    
    print()