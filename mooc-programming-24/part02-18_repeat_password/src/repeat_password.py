# Write your solution here
password = input("Password: ")

while True:
    confirm = input("Repeat password: ")
    if confirm != password:
        print("They do not match!")
    else:
        break
print("User account created!")