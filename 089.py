def capitalize(s):
    s = s[0].upper() + s[1:len(s)]
    pos = 0
    while pos < len(s):
        if s[pos] == '.' or s[pos] == '!' or s[pos] == '?':
            pos += 1
            while pos < len(s) and s[pos] == ' ':
                pos += 1
            if pos < len(s):
                s = s[0 : pos] + s[pos].upper() + s[pos + 1 : len(s)] 
        pos += 1
    return(s)
def main():
    a = input('Please enter a string: ')
    a = capitalize(a)
    print(a)
main()