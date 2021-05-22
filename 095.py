import random
import string

def randomLicensePlate():
    oldEng = 3
    newEng = 4
    num = 4
    a = random.randint(oldEng, newEng)
    b = ''
    if a == oldEng:
        for i in range(oldEng):
            c = random.choice(string.ascii_uppercase)
            b += c
        for i in range(num):
            c = random.choice(string.digits)
            b += c
    if a == newEng:
        for i in range(newEng):
            c = random.choice(string.ascii_uppercase)
            b += c
        for i in range(num):
            c = random.choice(string.digits)
            b += c
    return b
def main():
    print(randomLicensePlate())
main()