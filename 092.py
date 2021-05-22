def prime(a):
    if a <= 1:
        return False
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True
def main():
    a = eval(input('Please enter an integer: '))
    if prime(a):
        print(f'{a} is a prime number.')
    else:
        print(f'{a} is not a prime number.')
main()