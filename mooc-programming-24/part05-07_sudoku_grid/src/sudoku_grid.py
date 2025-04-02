# Write your solution here
def row_correct(sudoku: list, row_no: int):
    temp = []
    for slot in sudoku[row_no]:
        if slot > 0 and slot in temp:
            return False
        else:
            temp.append(slot)
    return True

def column_correct(sudoku: list, column_no: int):
    i = 0
    temp = []
    for i in range(0, 9):
        if sudoku[i][column_no] > 0 and sudoku[i][column_no] in temp:
            return False
        else:
            temp.append(sudoku[i][column_no])
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    temp = []
    for i in range(row_no, row_no + 3):
        for j in range (column_no, column_no + 3):
            if sudoku[i][j] > 0 and sudoku[i][j] in temp:
                return False
            else:
                temp.append(sudoku[i][j])
    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(0, 9):
        if not row_correct(sudoku, i):
            return False
    for i in range(0, 9):
        if not column_correct(sudoku, i):
            return False
    for row in range(0,9,3):
        for column in range(0,9,3):
            if not block_correct(sudoku, row, column):
                return False
    return True

    