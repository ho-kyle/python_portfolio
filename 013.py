toonie = 200
loonie = 100
quarter = 25
dime = 10
nickle = 5
a = eval(input('Please enter the number of cents: '))
print(a // toonie,'toonies')
a %= toonie
print(a // loonie,'loonies')
a %= loonie
print(a // quarter,'quarters')
a %= quarter
print(a // dime,'dimes')
a %= dime
print (a // nickle,'nickles')
a %= nickle
print(a,'cents')