a = eval(input('Please enter an year: '))
b = [x for x in range(12)]
c = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Hare', 'Dragon', 'Snake', 'Horse', 'Sheep']
for i in range(12):
    if a % 12 == b[i]:
        d = c[i]
        break
print(f'The animal is {d}.')