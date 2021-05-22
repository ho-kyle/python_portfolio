import sys
sys.path.append(r"C:\Users\user\OneDrive\桌面\python模組\mymodule.zip")

import isprime
def nextPrime(n):
    while not isprime.prime(n + 1):
        n += 1
    return n + 1
def main():
     a = eval(input('Enter an integer: '))
     print(f'{nextPrime(a)} is the first prime number larger than {a}')
main()