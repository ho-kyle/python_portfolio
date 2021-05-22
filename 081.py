def hypotenuse():
    a, b = eval(input('Please enter the lengths of the two shorter sides \
of a right triangle: '))
    square_c = a**2 + b**2
    c = square_c**0.5
    print(f'The length of hypotenuse: {c}')
hypotenuse()