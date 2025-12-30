# version 1.2.1

from secrets import choice
import json

# Program create 12-symbols password for registration. 

def create_password(length, symbols):
    """
    Generates a random password based on the settings.

    Args:
        length (int): Length of the password.
        symbols (str): Symbols which function uses for password.

    Returns:
        password (str): The password.
    """
    syms = [choice(symbols) for _ in range(length)]
    password = "".join(syms)

    return password


def import_settings():
    """
    Imports password's settings from JSON-file.

    Returns:
        settings (dict): The dictionary which has length and symbols for password.
    """
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
    """
    The program talks with user and outputs password.

    Returns:
        None
    """
    try:
        settings = import_settings()
        length, symbols = settings.values()
    except ValueError:
        raise ValueError("Error in file settings.json: incorrect values")
    
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Error in file settings.json: incorrect length")
    
    if not isinstance(symbols, str) or symbols == "":
        raise ValueError("Error in file settings.json: incorrect symbols")

    while True:
        print("1. Create password")
        print("0. Exit")
        
        try:
            user_choice = int(input())
        except ValueError:
            print("Please, enter 1 or 0")
            continue

        if user_choice == 1:
            password = create_password(length, symbols)
            print(password)
        elif user_choice == 0:
            return

main()
