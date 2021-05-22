name = {1 : 'George Washington',
        2 : 'Thomas Jefferson',
        5 : 'Abraham Lincoln',
        10 : 'Alexander Hamilton',
        20 : 'Andrew Jackson',
        50 : 'Ulysses S.Grant',
        100 : 'Benjamin Franklin'}
a = eval(input('Please enter the denomination of a banknote: '))
if a == 1 or a == 2 or a == 5 or a == 10 or a == 20 or a == 50 or a == 100:
    print(f'The name of individual that appears on the bankrote is {name[a]}.')