# Write your solution here
import re

def is_dotw(my_string: str) -> bool:
    if re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string):
        return True
    return False

def all_vowels(my_string: str) -> bool:
    if re.search("^[aeiou]+$", my_string):
        return True
    return False

def time_of_day(my_string: str) -> bool:
    if re.search("^([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", my_string):
        return True
    return False