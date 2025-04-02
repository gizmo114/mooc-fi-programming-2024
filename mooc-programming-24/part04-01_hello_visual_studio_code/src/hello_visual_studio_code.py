# Write your solution here
vsc = "visual studio code"

while True:
    answer = input("Editor: ")

    if answer.lower() == vsc:
        break

    if answer.lower() == "word" or answer.lower() == "notepad":
        print("awful")
    else:
        print("not good")
print("an excellent choice!")
    