# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    temp = []
    for i in range(row_no, row_no + 3):
        for j in range (column_no, column_no + 3):
            if sudoku[i][j] > 0 and sudoku[i][j] in temp:
                return False
            else:
                temp.append(sudoku[i][j])
    return True