# Write your solution here
string = input("String: ")
i = 20 - len(string)
line = ""

while i != 0:
    line += "*"
    i -= 1
print(f"{line}{string}")
