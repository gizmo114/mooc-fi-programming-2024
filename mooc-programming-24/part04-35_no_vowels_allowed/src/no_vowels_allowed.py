# Write your solution here
def no_vowels(text: str):
    temp = ""

    temp = text.replace("a", "")
    temp = temp.replace("e", "")
    temp = temp.replace("i", "")
    temp = temp.replace("o", "")
    temp = temp.replace("u", "")

    return temp