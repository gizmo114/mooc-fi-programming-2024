# Write your solution here:


class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compare_to: "RealProperty") -> bool:
        return self.square_metres > compare_to.square_metres

    def price_difference(self, compare_to: "RealProperty") -> int:
        return abs(
            (self.square_metres * self.price_per_sqm)
            - (compare_to.square_metres * compare_to.price_per_sqm)
        )

    def more_expensive(self, compare_to: "RealProperty") -> bool:
        return (self.square_metres * self.price_per_sqm) > (
            compare_to.square_metres * compare_to.price_per_sqm
        )
