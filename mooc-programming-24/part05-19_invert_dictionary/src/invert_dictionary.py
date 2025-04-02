# Write your solution here
def invert(dictionary: dict):
    temp = {}

    for key, value in dictionary.items():
        temp[value] = key
    
    dictionary.clear()

    for key, value in temp.items():
        dictionary[key] = value