# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        largest = 0
        for line in new_file:
            line = line.replace("\n", "")
            num = int(line)
            if num > largest:
                largest = num
    return largest
