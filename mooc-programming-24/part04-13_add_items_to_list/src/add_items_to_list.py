# Write your solution here
my_list = []
i = 1

items = int(input("How many items: "))

while i <= items:
    item = int(input(f"Item {i}: "))
    my_list.append(item)
    i += 1
print(my_list)
