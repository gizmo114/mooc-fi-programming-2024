# Write your solution here
def who_won(game_board: list):
    one = 0
    two = 0
    for array in game_board:
        for slot in array:
            if slot == 1:
                one += 1
            elif slot == 2:
                two += 1
    if one > two:
        return 1
    elif two > one:
        return 2
    else:
        return 0