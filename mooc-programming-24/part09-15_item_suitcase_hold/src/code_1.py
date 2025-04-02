class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight

class Suitcase:
    def __init__(self, max_weight: int):
        self.__items = []
        self.__max_weight = max_weight
        self.__total = 0

    def add_item(self, item: Item):
        if (self.__total + item.weight()) <= self.__max_weight:
            self.__items.append(item)
            self.__total += item.weight()
    
    def print_items(self):
        for item in self.__items:
            print(f"{item.name()} ({item.weight()} kg)\n")
    
    def weight(self) -> int:
        return self.__total

    def __str__(self):
        if len(self.__items) == 1:
            return f"{len(self.__items)} item ({self.weight()} kg)"
        else:
            return f"{len(self.__items)} items ({self.weight()} kg)"
    
    def heaviest_item(self):
        heaviest = None
        max_weight = 0
        for item in self.__items:
            if item.weight() > max_weight:
                heaviest = item
                max_weight = item.weight()
        return heaviest
    
class CargoHold:
    def __init__(self, max_weight: int):
        self.__suitcases = []
        self.__max_weight = max_weight
        self.__total = 0
    
    def add_suitcase(self, suitcase: Suitcase):
        if (self.__total + suitcase.weight()) <= self.__max_weight:
            self.__suitcases.append(suitcase)
            self.__total += suitcase.weight()
    
    def __str__(self):
        if len(self.__suitcases) == 1:
            return f"{len(self.__suitcases)} suitcase, space for {self.__max_weight - self.__total} kg"
        else:
            return f"{len(self.__suitcases)} suitcases, space for {self.__max_weight - self.__total} kg"
    
    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()
        