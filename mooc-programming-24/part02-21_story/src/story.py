# Write your solution here
last_word = ""
story = ""

while True:
    word = input("Please type in a word: ")
    if last_word == word or word == "end":
        break
    story += word + " "
    last_word = word
print(story)