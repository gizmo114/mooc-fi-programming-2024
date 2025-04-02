# Write your solution here
from random import shuffle

def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    numbers = list(range(lower, upper+1))
    shuffle(numbers)
    return_list = numbers[0:amount]
    return sorted(return_list)

