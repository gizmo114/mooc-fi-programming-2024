
def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True
    string = [char for char in my_string if char in '[]()']
    if (string[0] == '(' and string[-1] == ')') or (string[0] == '[' and string[-1] == ']'):
        return balanced_brackets(string[1:-1])
    
    return False