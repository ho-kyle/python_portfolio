x = eval(input('Please enter x: '))
guess = x / 2
while guess**2 - x > 10**(-12) or x - guess**2 > 10**(-12):
    guess = (guess + x / guess)/ 2
print(guess)