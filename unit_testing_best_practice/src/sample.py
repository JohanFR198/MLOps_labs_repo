
def func(x):
    return x + 2


import re


def validate_username(username: str) -> bool:
    return bool(username) and " " not in username



def validate_password(password: str) -> bool:
    if len(password) < 8:
        return False

    has_letter = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special = True

    return has_letter and has_digit and has_special


def validate_email(email: str) -> bool:
    return "@" in email and "." in email



def register_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    if not validate_username(username):
        print("Invalid username")
        return

    if not validate_email(email):
        print("Invalid email")
        return

    if not validate_password(password):
        print("Invalid password")
        return

    print("User registered successfully!")


if __name__ == "__main__":
    register_user()
