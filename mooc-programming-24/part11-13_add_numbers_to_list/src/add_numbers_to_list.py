def add_numbers_to_list(numbers: list) -> None:
    if len(numbers) % 5 != 0:
        numbers.append(numbers[-1] + 1)
        add_numbers_to_list(numbers)