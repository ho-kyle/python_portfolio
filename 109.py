l = []
def properDivisor(n):
    n = eval(n)
    for i in range(1, n):
        if n % i == 0:
            l.append(i)
    return l
def main():
    a = input('Please enter an integer(blank line to quet): ')
    print(properDivisor(a))
main()