# Write your solution here
string = input("Please provide string: ")
i = len(string)  - 1

while i >= 0:
    print(string[i:len(string)])
    i -= 1