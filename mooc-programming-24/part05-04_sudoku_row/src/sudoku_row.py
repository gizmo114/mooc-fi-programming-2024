# Write your solution here
def row_correct(sudoku: list, row_no: int):
    temp = []
    for slot in sudoku[row_no]:
        if slot > 0 and slot in temp:
            return False
        else:
            temp.append(slot)
    return True

