# Write your solution here
my_list = []
counter = 0

while True:
    word = input("Word: ")
    if word in my_list:
        break 
    else:
        my_list.append(word)
        counter += 1
print(f"You typed in {counter} different words")