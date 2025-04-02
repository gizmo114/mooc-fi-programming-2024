# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.total = 0

    def add_number(self, number: int):
        self.numbers += 1
        self.total += number

    def count_numbers(self) -> int:
        return self.numbers

    def get_sum(self) -> int:
        return self.total

    def average(self) -> float:
        if self.numbers > 0:
            return self.total / self.numbers
        else:
            return 0


stats = NumberStats()
odd = NumberStats()
even = NumberStats()

while True:
    num = int(input("Please provide a number, -1 to exit: "))
    if num != -1:
        if num % 2 == 0:
            even.add_number(num)
            stats.add_number(num)
        else:
            odd.add_number(num)
            stats.add_number(num)
    else:
        print(f"Sum of numbers: {stats.get_sum()}")
        print(f"Mean of numbers: {stats.average()}")
        print(f"Sum of even numbers: {even.get_sum()}")
        print(f"Sum of odd numbers: {odd.get_sum()}")
        break
