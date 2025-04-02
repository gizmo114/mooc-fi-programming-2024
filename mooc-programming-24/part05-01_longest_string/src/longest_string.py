# Write your solution here
def longest(strings: list):
    longest = ""
    for item in strings:
        if len(item) > len(longest):
            longest = item
    return longest