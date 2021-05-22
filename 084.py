def median(a, b, c):
    Max = max(a, b, c)
    Min = min(a, b, c)
    Median = a + b + c - Max - Min
    return(Median)
def alternativeMedian(a, b, c):
    if a > b and a < c or a > c and a < b:
        return(a)
    if b > a and b < c or b > c and b < a:
        return(b)
    if c > a and c < b or c > b and c < a:
        return(c)
def main():
    a, b, c = eval(input('Please enter three values: '))
    print(f'The median is: {median(a, b, c)}')
    print(f'Other method : {alternativeMedian(a, b, c)}')
main()