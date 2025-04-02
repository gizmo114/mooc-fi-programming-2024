# Write your solution here
str1 = input("1st word: ")
str2 = input("2nd word: ")

if str1 > str2:
    print(f"{str1} comes alphabetically last.")
elif str2 > str1:
    print(f"{str2} comes alphabetically last.")
else:
    print(f"You gave the same word twice.")