# Write your solution here
def anagrams(string1: str, string2: str):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False
