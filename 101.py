def greatestCommonDivisor(n, m):
    a = min(n, m)
    while n % a != 0 or m % a != 0:
        a -= 1
    return a
def lowestFractoin(num, den):
    if num == 0:
        return (0, 1)
    divisor = greatestCommonDivisor(num, den)
    num = int(num / divisor)
    den = int(den / divisor)
    return (num, den)
def main():
    num, den = eval(input('Please enter a numberator and denominator: '))
    num, den = lowestFractoin(num, den)
    print(f'The reduced fraction: {num}/{den}')
main()