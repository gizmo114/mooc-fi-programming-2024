# Write your solution here
def sum_of_positives(mylist: list):
    i = 0
    sum = 0
    for i in mylist:
        if i > 0:
            sum += i
    return sum