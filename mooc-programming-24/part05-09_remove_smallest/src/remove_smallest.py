# Write your solution here
def remove_smallest(numbers: list):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    numbers.remove(smallest)