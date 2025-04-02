class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f"{self.day}.{self.month}.{self.year}"

    def __value(self):
        return self.day + (self.month * 30) + (self.year * 360)

    def __value_to_simple_date(self, value: int):
        result = SimpleDate(0, 0, 0)
        result.year = value // 360
        result.month = (value % 360) // 30
        result.day = (value % 360) % 30
        return result

    def __eq__(self, another) -> bool:
        return self.__value() == another.__value()

    def __ne__(self, another) -> bool:
        return self.__value() != another.__value()

    def __gt__(self, another) -> bool:
        return self.__value() > another.__value()

    def __lt__(self, another) -> bool:
        return self.__value() < another.__value()

    def __add__(self, another):
        return self.__value_to_simple_date(self.__value() + another)

    def __sub__(self, another):
        return abs(self.__value() - another.__value())
