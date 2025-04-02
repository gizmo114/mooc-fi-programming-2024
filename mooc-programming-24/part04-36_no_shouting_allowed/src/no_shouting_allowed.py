# Write your solution here
def  no_shouting(mylist: list):
    return_list = []

    for string in mylist:
        if string.isupper():
            continue
        else:
            return_list.append(string)
    return return_list