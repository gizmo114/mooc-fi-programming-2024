# Write your solution here
def formatted(mylist: list):
    return_list = []

    for i in mylist:
        num = "{:.2f}".format(i)
        return_list.append(num)
    return return_list
