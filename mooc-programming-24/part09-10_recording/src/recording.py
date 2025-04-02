class Recording:
    def __init__(self, length: int):
        if length > 0:
            self.__length = length
        else:
            raise ValueError("The lenght must be bigger than zero!")

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        if length > 0:
            self.__length = length
        else:
            raise ValueError("The length must be bigger than zero!")
