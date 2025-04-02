# Write your solution here
def factorial(num: int):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


def factorials(n: int):
    dicty = {}
    for i in range(1, n + 1):
        dicty[i] = factorial(i)
    return dicty