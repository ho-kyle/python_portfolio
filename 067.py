'''
baby = 0
child = 14.00
senior = 18.00
otherGuest = 23.00

baby_age <= 2
chile_age <= 12
otherGuest_age <= 64
senior_age >= 65
'''
age = input('Please enter the age of the guest (blank to finish): ')
cost = 0
while age != '':
    age = eval(age)
    if age <= 2:
        cost += 0
    elif age <= 12:
        cost += 14
    elif age <= 64:
        cost += 23
    else:
        cost += 18
    age = input('Please enter the age of the guest (blank to finish): ')
print(f'The admission cost for the group is {cost}.')