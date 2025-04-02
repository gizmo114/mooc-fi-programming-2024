class Present:
    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight

    def __str__(self) -> str:
        return f"{self.name} ({self.weight} kg)"


class Box:
    def __init__(self) -> None:
        self.presents = []

    def add_present(self, present: Present) -> None:
        self.presents.append(present)

    def total_weight(self) -> int:
        total_weight = 0
        for present in self.presents:
            total_weight += present.weight
        return total_weight

