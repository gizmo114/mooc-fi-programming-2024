# Write your solution here
def evaluate(operation: str, result: str) -> bool:
    if operation.find('+') >= 0:
        temp = operation.split('+')
        if int(temp[0]) + int(temp[1]) == int(result):
            return True
        else:
            return False
    else:
        temp = operation.split('-')
        if int(temp[0]) - int(temp[1]) == int(result):
            return True
        else:
            return False

def filter_solutions():
    open('correct.csv','w').close()
    open('incorrect.csv','w').close()
    with open('solutions.csv') as new_file:
        for line in new_file:
            line = line.replace('\n', '')
            temp = line.split(';')
            if evaluate(temp[1], temp[2]):
                with open('correct.csv', 'a') as file:
                    file.write(f'{line}\n')
                    file.close()
            else:
                with open('incorrect.csv', 'a') as file:
                    file.write(f'{line}\n')
                    file.close()   