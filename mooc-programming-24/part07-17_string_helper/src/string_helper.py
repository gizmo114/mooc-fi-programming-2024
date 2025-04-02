from string import ascii_lowercase, ascii_uppercase, digits


def change_case(orig_string: str) -> str:
    return_string = ""
    for char in orig_string:
        if char.islower():
            return_string += char.upper()
        else:
            return_string += char.lower()
    return return_string


def split_in_half(orig_string: str) -> tuple:
    half = len(orig_string) // 2
    return orig_string[:half], orig_string[half:]


def remove_special_characters(orig_string: str) -> str:
    return_string = ""
    for char in orig_string:
        if (
            char in ascii_lowercase
            or char in ascii_uppercase
            or char in digits
            or char == " "
        ):
            return_string += char
    return return_string


if __name__ == "__main__":
    print(change_case("Well hello there!"))
    print(split_in_half("Well hello there!"))
    print(remove_special_characters("Well hello there!"))
