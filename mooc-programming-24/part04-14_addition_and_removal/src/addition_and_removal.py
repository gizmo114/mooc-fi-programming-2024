# Write your solution here
my_list = []
last_item = 0

while True:
    print(f"The list is now {my_list}")
    command = input("a(d)d, (r)emove or e(x)it: ")
    if command == "x":
        break
    elif command == "d":
        last_item += 1
        my_list.append(last_item)
    else:
        my_list.remove(last_item)
        last_item -= 1
print("Bye!")