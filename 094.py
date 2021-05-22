import random
def randomPassword():
    a = random.randrange(7, 11)
    c = ''
    for i in range(a):
        b = random.randrange(33, 127)
        b = chr(b)
        c += b
    return c
def main():
    print(randomPassword())
if __name__ == "__main__":
    main()