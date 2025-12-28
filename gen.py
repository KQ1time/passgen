from random import choices

# Program create 12-symbols password for registration. 

symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&()-_+=;:,./?|`~[]"

def create_password():
    password = "".join(choices(symbols, k=12))
    return password

print(create_password())