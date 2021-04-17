import random

def password(n):
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    num = input("Password Length: ")
    num = int(num)
    password = ''
    for i in range(num):
        password += random.choice(chars)
    print(password)