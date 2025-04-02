# Write your solution here
string = input("String: ")
edge = "******************************"
spaces = 30 - 2 - len(string)

print(edge)
if spaces % 2 == 0:
    print("*" + " " * int(spaces/2) + string + " " * int(spaces/2) + "*")
else:
    print("*" + " " * int((spaces+1)/2) + string + " " * int(spaces/2) + "*")
print(edge)