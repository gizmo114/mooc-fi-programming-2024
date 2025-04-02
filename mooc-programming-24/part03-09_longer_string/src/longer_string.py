# Write your solution here
string1 = input("String 1: ")
string2 = input("String 2: ")

if len(string1) > len(string2):
    print(f"{string1} is longer")
elif len(string1) < len(string2):
    print(f"{string2} is longer")
else:
    print("The strings are equally long")