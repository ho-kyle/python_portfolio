import sys
sys.path.append(r'C:\Users\user\OneDrive\桌面\python模組\randomPassword.zip')
sys.path.append(r'C:\Users\user\OneDrive\桌面\python模組\checkPassword.zip')

import randomPassword
import checkPassword

def main():
    password = randomPassword.randomPassword()
    n = 1
    while not checkPassword.checkPassword(password):
            password = randomPassword.randomPassword()
            n += 1
    print(f'{password} is a good password.')
    print(f'It needs {n} attempt(s) to generate a good password.')
main()