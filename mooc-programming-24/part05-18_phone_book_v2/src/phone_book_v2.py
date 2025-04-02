# Write your solution here
def search(phonebook, name: str):
    if name in phonebook:
        for num in phonebook[name]:
            print(num)
    else:
        print("no number")

def add(phonebook, name, number):
    if name not in phonebook:
        phonebook[name] = []
    phonebook[name].append(number)
    print("ok!")

def main():
    phonebook = {}
    while True:
        command = input("command (1 search, 2 add, 3 quit): ")
        if command == "1":
            name = input("name: ")
            search(phonebook, name)
        elif command == "2":
            name = input("name: ")
            phone = input("number: ")
            add(phonebook, name, phone)
        else:
            print("quitting...")
            break
    
main()