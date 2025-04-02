# Write your solution here
def length_of_longest(mylist: list):
    best = ""

    for i in mylist:
        if len(i) > len(best):
            best = i
    return len(best)