# Write your solution here
def column_correct(sudoku: list, column_no: int):
    i = 0
    temp = []
    for i in range(0, 9):
        if sudoku[i][column_no] > 0 and sudoku[i][column_no] in temp:
            return False
        else:
            temp.append(sudoku[i][column_no])
    return True