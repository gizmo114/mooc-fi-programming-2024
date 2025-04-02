# Write your solution here
def everything_reversed(mylist: list):
    return_list = []

    for i in mylist:
        return_list.append(i[::-1])
    
    return return_list[::-1]