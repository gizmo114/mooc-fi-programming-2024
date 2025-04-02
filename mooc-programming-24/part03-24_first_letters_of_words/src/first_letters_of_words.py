# Write your solution here
string = input("Please provide your string: ")
result = string[0]
i = 1
j = 0

while i < len(string):
    if string[i] == " ":
        if string[i + 1] != " ":
            result += string[i + 1]
        else:
            continue
    i += 1

while j <= len(result) - 1:
    print(result[j])
    j += 1