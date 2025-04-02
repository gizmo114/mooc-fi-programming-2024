# Write your solution here
from random import choices
from string import ascii_lowercase, digits

def generate_letters(num: int) -> str:
    password_list = choices(ascii_lowercase, k=num)
    password = "".join(password_list)
    return password

def generate_strong_password(num: int, numbers: bool, special_characters: bool) -> str:
    if numbers and special_characters:
        return generate_with_specials_letters_numbers(num)
    elif numbers:
        return generate_with_numbers_letters(num)
    elif special_characters:
        return generate_with_specials_letters(num)
    else:
        return generate_letters(num)

def generate_with_numbers_letters(num: int) -> str:
    pool = ascii_lowercase + digits
    password_list = choices(pool, k=num)
    password = "".join(password_list)
    if any(i in password_list for i in ascii_lowercase) and any(
        i in password_list for i in digits
    ):
        return password
    else:
        return generate_with_numbers_letters(num)


def generate_with_specials_letters(num: int) -> str:
    specials = "!?=+-()#"
    pool = ascii_lowercase + specials
    password_list = choices(pool, k=num)
    password = "".join(password_list)
    if any(i in password_list for i in ascii_lowercase) and any(
        i in password_list for i in specials
    ):
        return password
    else:
        return generate_with_specials_letters(num)


def generate_with_specials_letters_numbers(num: int) -> str:
    specials = "!?=+-()#"
    pool = ascii_lowercase + digits + specials
    password_list = choices(pool, k=num)
    password = "".join(password_list)
    if (
        any(i in password_list for i in ascii_lowercase)
        and any(i in password_list for i in specials)
        and any(i in password_list for i in digits)
    ):
        return password
    else:
        return generate_with_specials_letters_numbers(num)

#print(generate_password(2, False, False))
