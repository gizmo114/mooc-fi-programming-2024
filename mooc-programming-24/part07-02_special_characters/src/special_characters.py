# Write your solution here
import string

def separate_characters(my_string: str) -> tuple:
    letters = ''
    punctuation = ''
    others = ''
    for i in range(0,len(my_string)):
        if my_string[i] in string.ascii_letters:
            letters += my_string[i]
        elif my_string[i] in string.punctuation:
            punctuation += my_string[i]
        else:
            others += my_string[i]
    response = (letters, punctuation, others)
    return response
