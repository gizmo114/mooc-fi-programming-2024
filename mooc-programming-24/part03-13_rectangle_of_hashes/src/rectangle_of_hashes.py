# Write your solution here
# Write your solution here
width = int(input("Windth: "))
height = int(input("Height: "))
line = ""

while width != 0:
    line += "#"
    width -= 1
while height != 0:
    print(line)
    height -= 1