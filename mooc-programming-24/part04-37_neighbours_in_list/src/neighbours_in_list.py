# Write your solution here
def longest_series_of_neighbours(my_list: list):
    longest = 1
    result = 1
    for i in range(1, len(my_list)):
        if abs(my_list[i-1]-my_list[i]) == 1:
            result += 1
        else:
            result = 1
        longest = max(longest, result)
    return longest