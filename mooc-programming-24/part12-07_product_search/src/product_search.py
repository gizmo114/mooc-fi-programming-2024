def search(products: list, criterion: callable) -> list:
    result = []
    for item in products:
        if criterion(item):
            result.append(item)
    return result