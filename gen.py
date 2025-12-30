# version 1.2

from secrets import choice
import json

# Program create 12-symbols password for registration. 

def create_password(length, symbols):
    syms = [choice(symbols) for _ in range(length)]
    password = "".join(syms)
    return password


def import_settings():
    try:
        with open("settings.json", "r") as file:
            settings = json.load(file)
    
    except FileNotFoundError:
        with open("settings.json", "w") as file:
            settings = {
                "length": 12, 
                "symbols": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&()-_+=;:,./?|`~[]\\"
                }
            json.dump(settings, file, indent=4)
    return settings


def main():
    try:
        settings = import_settings()
        length, symbols = settings.values()
    except ValueError:
        print("Error in file settings.json: incorrect values")
        return
    
    if not isinstance(length, int) or length <= 0:
        print("Error in file settings.json: incorrect length")
        return
    
    if not isinstance(symbols, str) or symbols == "":
        print("Error in file settings.json: incorrect symbols")
        return

    while True:
        print("1. Create password")
        print("0. Exit")
        
        try:
            choice = int(input())
        except ValueError:
            print("Please, enter 1 or 0")
            continue

        if choice == 1:
            password = create_password(length, symbols)
            print(password)
        elif choice == 0:
            return

main()
