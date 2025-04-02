# Write your solution here
def distinct_numbers(mylist: list):
    return_list = []

    for i in mylist:
        if i not in return_list:
            return_list.append(i)
    return_list.sort()
    return return_list