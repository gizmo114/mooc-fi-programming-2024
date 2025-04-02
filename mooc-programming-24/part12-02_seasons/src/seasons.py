def sort_by_seasons(items: list) -> list:
    def helper(item: dict):
        return item['seasons']
    
    return sorted(items, key=helper)