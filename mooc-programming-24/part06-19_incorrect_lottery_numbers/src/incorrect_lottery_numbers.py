# Write your solution here
def evaluate_week(word: str) -> bool:
    number = 0
    helper_list = []
    response = True
    helper_list = word.split(' ')
    try:
        number = int(helper_list[1])
    except ValueError:
        response = False
    #print(f'{word} + {response}')
    return response

def evaluate_numbers(word: str) -> bool:
    helper_list = []
    duplicate = []
    value = 0
    response = True
    helper_list = word.split(',')
    if len(helper_list) == 7:
        for number in helper_list:
            try:
                value = int(number)
            except:
                response = False
            if value not in range(1,40):
                response = False
            if value in duplicate:
                response = False
            duplicate.append(value)
    else:
        response = False
    #print(f'{word} + {response}')
    return response

def filter_incorrect():
    open('correct_numbers.csv', 'w').close()
    helper_list = []
    with open('lottery_numbers.csv') as file:
        for line in file:
            line = line.replace('\n', '')
            helper_list = line.split(';')
            if evaluate_week(helper_list[0]) and evaluate_numbers(helper_list[1]):
                line += '\n'
                with open('correct_numbers.csv', 'a') as correct_file:
                    correct_file.write(line)
                    correct_file.close()

#filter_incorrect()

