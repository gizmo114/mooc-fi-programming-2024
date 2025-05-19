# Write your solution here
def squared(text, times):
    i = 0
    j = 0
    line = ""
    line += text * (times * times // len(text))

    while i <= times * times % len(text) - 1:
        line += text[i]
        i += 1

    while j <= len(line) - 1:
        print(line[j], end="")
        j += 1
        if j % (times) == 0:
            print()


# Testing the function
if __name__ == "__main__":
    squared("abc", 4)
