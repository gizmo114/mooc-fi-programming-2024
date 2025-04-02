# Write your solution here
def all_the_longest(mylist: list):
    return_list = []
    return_list.append(mylist[0])

    for i in mylist:
        if len(i) > len(return_list[0]):
            return_list.clear()
            return_list.append(i)
        elif len(i) == len(return_list[0]) and i not in return_list:
            return_list.append(i)
    return return_list