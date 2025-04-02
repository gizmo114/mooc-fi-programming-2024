# write your solution here
text = input("Write text: ")
words = text.split(" ")
dictionary = []

with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.strip()
        dictionary.append(line)

for word in words:
    if word.lower() in dictionary:
        print(word+" ", end="")
        continue
    else:
        print("*"+word+"* ", end="")

            