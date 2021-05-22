import idcheck

f = open('suspect.txt', 'r')
for line in f:
    print(f'{line.strip()}:{idcheck.idcheck(line.strip())}')
f.close()