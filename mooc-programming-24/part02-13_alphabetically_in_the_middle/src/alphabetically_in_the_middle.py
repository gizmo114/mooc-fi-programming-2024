# Write your solution here
a = input("First letter: ")
b = input("Second letter: ")
c = input("Third letter: ")

if (a > b and a < c) or (a > c and a < b):
    print(f"The letter in the middle is {a}")
elif (b > a and b < c) or (b > c and b < a):
    print(f"The letter in the middle is {b}")
else:
    print(f"The letter in the middle is {c}")