# Write your solution here
def shortest(mylist: list):
    best = mylist[0]

    for i in mylist:
        if len(i) < len(best):
            best = i
    return best