# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    counter = 0
    for i in my_matrix:
        for number in i:
            if number == element:
                counter += 1
    return counter