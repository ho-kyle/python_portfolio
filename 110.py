import properDivisor

def perfectNumber(n):
    l = properDivisor.properDivisor(str(n))
    Sum = 0
    for i in l:
        Sum += i
    if n == Sum:
        return True
    else:
        return False
def main():
    Limit = 10000
    print('All of th perfect numbers between 1 and 10000')
    for i in range(1, Limit + 1):
        if perfectNumber(i):
            print(i)
main()