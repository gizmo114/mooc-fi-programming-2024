# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __value(self):
        return self.__euros * 100 + self.__cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another) -> bool:
        return self.__value() == another.__value()

    def __gt__(self, another) -> bool:
        return self.__value() > another.__value()

    def __lt__(self, another) -> bool:
        return self.__value() < another.__value()

    def __ne__(self, another) -> bool:
        return self.__value() != another.__value()

    def __add__(self, another):
        result = Money(0, 0)
        result.__euros = self.__euros + another.__euros
        result.__euros += (self.__cents + another.__cents) // 100
        result.__cents = (self.__cents + another.__cents) % 100
        return result

    def __sub__(self, another):
        result = Money(0, 0)
        if self.__value() - another.__value() < 0:
            raise ValueError("a negative result is not allowed")
        result.__euros = self.__euros - another.__euros
        if self.__cents - another.__cents < 0:
            result.__cents = 100 + (self.__cents - another.__cents)
            result.__euros -= 1
        else:
            result.__cents = self.__cents - another.__cents
        return result
