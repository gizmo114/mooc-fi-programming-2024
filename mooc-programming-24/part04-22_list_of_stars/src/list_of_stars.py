# Write your solution here
def list_of_stars(my_list: list):
    i = 0
    j = 0
    for i in my_list:
        j = 0
        while j < i:
            print("*", end="")
            j += 1
        print()