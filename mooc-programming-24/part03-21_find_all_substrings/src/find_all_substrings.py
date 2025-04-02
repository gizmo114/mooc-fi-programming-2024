# Write your solution here
string = input("Please provide a string: ")
char = input("Please provide a character: ")
i = 0

while i < len(string) - 2:
    if string[i] == char:
        print(string[i:i+3])
    i += 1