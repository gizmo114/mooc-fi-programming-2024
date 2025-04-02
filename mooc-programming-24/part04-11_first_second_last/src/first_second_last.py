# Write your solution here
def first_word(sentence):
    i = 0
    word = ""

    while i <= len(sentence):
        if sentence[i] != " ":
            word += sentence[i]
        else: 
            break
        i += 1
    
    return word

def second_word(sentence):
    i = sentence.find(" ")
    word = ""
    
    while i < len(sentence) - 1:
        i += 1
        if sentence[i] != " ":
            word += sentence[i]
        else: 
            break
    
    return word

def last_word(sentence):
    i = -1
    word = ""

    while True:
        if sentence[i] != " ":
            word += sentence[i]
        else:
            break
        i -= 1
    return word[::-1]
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second"
    #print(first_word(sentence))
    print(second_word(sentence))
    #print(last_word(sentence))