def sort_by_ratings(items: list) -> list:
    def helper(item: dict):
        return item['rating']
    
    return sorted(items, key=helper, reverse=True)