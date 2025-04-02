# Write your solution here
def histogram(my_str: str):
    histogram = {}
    for i in range(0, len(my_str)):
        if my_str[i] not in histogram:
            histogram[my_str[i]] = 1
        else:
            histogram[my_str[i]] += 1

    for item, count in histogram.items():
        stars = "*" * count
        print(f"{item} {stars}")   
        