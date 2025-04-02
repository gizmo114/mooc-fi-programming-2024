from random import choice

def word_generator(characters: str, length: int, amount: int) -> str:
    for i in range(amount):
        word = ""
        for j in range(length):
            word += choice(characters)
        yield word