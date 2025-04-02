# Write your solution here
string = input("Please provide a string: ")
substring = input("Please provide a substring: ")
new_string = ""
buffer = 0

if string.find(substring) != -1:
    buffer = string.find(substring) + len(substring)
    new_string = string[string.find(substring) + len(substring):]
    if new_string.find(substring) != -1:
        print(f"The second occurrence of the substring is at index {buffer + new_string.find(substring)}.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")


