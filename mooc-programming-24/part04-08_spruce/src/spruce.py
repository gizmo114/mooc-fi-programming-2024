# Write your solution here
def spruce(num):
    print("a spruce!")
    i = 1

    while i <= num:
        space = num - i
        stars = 2 * i - 1
        print(" " * space + "*" * stars)
        i += 1
    
    print(" " * (num - 1) + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)