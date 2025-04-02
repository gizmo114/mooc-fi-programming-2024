# Write your solution here
def dict_of_numbers():
    final = {}
    numbers = []
    
    for i in range(0, 100):
        numbers.append(i)
    
    word_zero = ["zero"]
    word_up_to_nine = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    word_ten = ["ten"]
    word_up_to_nineteen = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    word_tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    rest = []
    word_total = []

    for i in word_tens:
        rest.append(i)
        for j in word_up_to_nine:
            rest.append(i + "-" + j)
    
    word_total.append(word_zero[0])
    for i in word_up_to_nine:
        word_total.append(i)
    word_total.append(word_ten[0])
    for i in word_up_to_nineteen:
        word_total.append(i)
    for i in rest:
        word_total.append(i)
    
    for i in range(len(numbers)):
        final[i] = word_total[i]
    return final
    