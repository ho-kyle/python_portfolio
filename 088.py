def validTriangle(a, b, c):
    Max = max(a, b, c)
    if Max < a + b + c - Max:
        isValidTriangle = True
        return(isValidTriangle)
    else:
        isValidTriangle = False
        return(isValidTriangle)
def main():
    a, b, c = eval(input('Please enter 3 lengths: '))
    if a > 0 and b > 0 and c > 0:
        if validTriangle(a, b, c):
            print('It is a valid triangle')
        else:
            print('It is not a valid triangle')
    else:
        print('error')
main()