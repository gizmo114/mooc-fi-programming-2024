def file_2_list(filename) -> list:
    result = []
    with open(filename) as file:
        for line in file:
            for word in line.split(' '):
                result.append(word.rstrip('.,!?\n'))
    return result


def most_common_words(filename: str, lower_limit: int) -> dict:
    words = file_2_list(filename)
    return {word: words.count(word) for word in words if words.count(word) >= lower_limit}

#print(file_2_list("comprehensions.txt"))