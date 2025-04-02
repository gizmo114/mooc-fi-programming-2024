# write your solution here
def matrix_sum():
    with open("matrix.txt") as new_file:
        matrix_sum = 0
        for line in new_file:
            line = line.replace("\n", "")
            numbers = line.split(",")
            for number in numbers:
                matrix_sum += int(number)
    return matrix_sum

def matrix_max():
    with open("matrix.txt") as new_file:
        matrix_max = 0
        for line in new_file:
            line = line.replace("\n", "")
            numbers = line.split(",")
            for number in numbers:
                if int(number) > matrix_max:
                    matrix_max = int(number)
    return matrix_max

def row_sums():
    with open("matrix.txt") as new_file:
        row_sums = []
        for line in new_file:
            row_sum = 0
            line = line.replace("\n", "")
            numbers = line.split(",")
            for number in numbers:
                row_sum += int(number)
            row_sums.append(row_sum)
    return row_sums
