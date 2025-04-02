# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copy_of_sudoku = []
    for row in sudoku:
        line = []
        for slot in row:
            line.append(slot)
        copy_of_sudoku.append(line)
    copy_of_sudoku[row_no][column_no] = number
    return copy_of_sudoku