# Write your solution here
def store_personal_data(person: tuple):
    print(person)
    write_string = f'{person[0]};{person[1]};{person[2]}\n'
    with open('people.csv', 'a') as file:
        file.write(write_string)
        file.close()
