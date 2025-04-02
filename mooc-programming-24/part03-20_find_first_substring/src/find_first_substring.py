# Write your solution here
string = input("Please provide a string: ")
char = input("Please provide a character: ")

if len(string) - string.find(char) > 3:
    print(string[string.find(char):string.find(char)+3])