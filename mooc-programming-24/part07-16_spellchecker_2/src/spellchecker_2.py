import difflib

vocabulary = []
with open("wordlist.txt") as file:
    for line in file:
        vocabulary.append(line.strip())
text_list = input("Please type in a line of text: ").split(" ")

spell_checked = []
bad_words = []
for word in text_list:
    if word.lower() not in vocabulary:
        spell_checked.append("*" + word + "*")
        bad_words.append(word)
    else:
        spell_checked.append(word)
return_line = " ".join(spell_checked)
print(return_line)
print("suggestions: \n")
for word in bad_words:
    suggestions = difflib.get_close_matches(word, vocabulary)
    line = f"{word}: " + ", ".join(suggestions)
    print(line)
