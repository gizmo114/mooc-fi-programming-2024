# Write your solution here
def most_common_character(text: str):
    most_common = text[0]

    for character in text:
        if text.count(character) > text.count(most_common):
            most_common = character
    return most_common