class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        max = 0
        for item in my_list:
            count = my_list.count(item)
            if count > max:
                max = count
                return_item = item
        return return_item

    @classmethod
    def doubles(cls, my_list: list):
        return_list = []

        for item in my_list:
            if my_list.count(item) >= 2:
                if item not in return_list:
                    return_list.append(item)
        return len(return_list)
