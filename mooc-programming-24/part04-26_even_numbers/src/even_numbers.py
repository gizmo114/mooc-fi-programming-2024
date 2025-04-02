# Write your solution here
def even_numbers(mylist: list):
    return_list = []

    for  i in mylist:
        if i % 2 == 0:
            return_list.append(i)
    
    return return_list