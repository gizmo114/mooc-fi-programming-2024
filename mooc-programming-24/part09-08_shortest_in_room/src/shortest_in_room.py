# WRITE YOUR SOLUTION HERE:


class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"


class Room:
    def __init__(self) -> None:
        self.persons = []

    def add(self, person: Person) -> None:
        self.persons.append(person)

    def is_empty(self) -> bool:
        return len(self.persons) == 0

    def print_contents(self):
        for person in self.persons:
            print(person)

    def shortest(self):
        if self.is_empty():
            return None
        shortest = self.persons[0]
        for person in self.persons:
            if person.height < shortest.height:
                shortest = person
        return shortest

    def remove_shortest(self):
        if not self.is_empty():
            removed = self.shortest()
            self.persons.remove(removed)
            return removed
        return None
