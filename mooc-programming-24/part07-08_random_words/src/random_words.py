from random import choices


def words(n: int, beginning: str) -> list:
    with open("words.txt") as file:
        cache = []
        for word in file:
            word.strip()
            if word.startswith(beginning):
                cache.append(word)

    if len(cache) < n:
        raise ValueError("There are not enough words matching your parameters!")

    return choices(cache, k=n)
