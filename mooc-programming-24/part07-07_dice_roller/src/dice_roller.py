# Write your solution here
from random import choice


def roll(die: str) -> int:
    dices = {}
    dices["A"] = [3, 3, 3, 3, 3, 6]
    dices["B"] = [2, 2, 2, 5, 5, 5]
    dices["C"] = [1, 4, 4, 4, 4, 4]
    return choice(dices[die])


def play(die1: str, die2: str, times: int) -> tuple:
    result_list = [0, 0, 0]
    roll_list = [0, 0]

    for i in range(times):
        roll_list[0] = roll(die1)
        roll_list[1] = roll(die2)

        if roll_list[0] > roll_list[1]:
            result_list[0] += 1
        elif roll_list[0] < roll_list[1]:
            result_list[1] += 1
        else:
            result_list[2] += 1

    return (result_list[0], result_list[1], result_list[2])
