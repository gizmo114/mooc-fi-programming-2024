def even_numbers(beginning: int, maximum: int):
    i = beginning
    while i <= maximum:
        if i % 2 == 0:
            yield i
        i += 1
    