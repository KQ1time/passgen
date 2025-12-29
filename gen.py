# version 1.1

from secrets import choice
from json import load

# Program create 12-symbols password for registration. 

def create_password(length, symbols):
    syms = [choice(symbols) for _ in range(length)]
    password = "".join(syms)
    return password

def import_settings():
    with open("settings.json", "r") as file:
        settings = load(file)
    return settings

def main():
    settings = import_settings()   
    length, symbols = settings.values()

    while True:
        print("1. Create password")
        print("0. Exit")

        choice = int(input())

        if choice == 1:
            password = create_password(length, symbols)
            print(password)
        elif choice == 0:
            return

main()

