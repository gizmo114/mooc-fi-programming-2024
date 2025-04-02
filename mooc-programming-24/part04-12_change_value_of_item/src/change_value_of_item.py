# Write your solution here000
my_list = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))
    if index == -1:
        break
    value = int(input("Value: "))

    my_list[index] = value
    print(my_list)

    
