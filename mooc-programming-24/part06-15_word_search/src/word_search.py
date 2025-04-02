# Write your solution here
def compare_by_dot(search_term: str, word: str) -> bool:
    same = True
    for i in range(len(search_term)):
        if search_term[i] != '.' and search_term[i] != word[i]:
            same = False
    return same
                
def find_words(search_term: str) -> list:
    return_list = []
    with open('words.txt') as file:
        for line in file:
            line = line.strip()
            #.search
            if '.' in search_term and len(line) == len(search_term):
                if compare_by_dot(search_term, line):
                    return_list.append(line)
            #*search
            elif search_term.startswith('*'):
                if line.endswith(search_term[1:]):
                    return_list.append(line)
            elif search_term.endswith('*'):
                if line.startswith(search_term[:-1]):
                    return_list.append(line)
            else:
                if search_term == line:
                    return_list.append(line)

    return return_list


