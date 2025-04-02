from datetime import date


def list_years(dates: list) -> list:
    return_list = []
    for entry in dates:
        return_list.append(entry.year)
    return sorted(return_list)

