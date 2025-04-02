from math import sqrt
# Write your solution here
while True:
    num = int(input("Number: "))
    
    if num == 0:
        break
    elif num < 0:
        print("Invalid number")
    else:
        print(sqrt(num))
print("Exiting...")