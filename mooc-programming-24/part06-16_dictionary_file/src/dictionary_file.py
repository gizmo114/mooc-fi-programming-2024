# Write your solution here
def add_word(word_list: list):
    write_string = ''
    write_string = word_list[0] + ';' + word_list[1] + '\n'
    with open('dictionary.txt', 'a') as file:
        file.write(write_string)
        file.close()

def search(word: str) -> list:
    return_list = []
    temp = []
    temp_string = ''
    with open('dictionary.txt') as file:
        for line in file:
            line.strip()
            if line.find(word) >= 0:
                temp = line.split(';')
                temp_string = f'{temp[0]} - {temp[1]}' 
                return_list.append(temp_string)
    return return_list

while True:
    print('1 - Add word, 2 - Search, 3 - Quit')
    function = input('Function: ')

    if function == '1':
        temp = []
        finnish = input('The word in Finnish: ')
        english = input('The word in English: ')
        temp.append(finnish)
        temp.append(english)
        add_word(temp)
        print('Dictionary entry added')
    elif function == '2':
        term = input('Search term: ')
        temp = search(term)
        for item in temp:
            print(item)
    else:
        print('Bye!')
        break

