# Write your solution here
def print_sudoku(board: list):
    line_count = 0
    item_count = 0
    for line in board:
        for item in line:
            if item > 0:
                print(f"{item} ", end="")
            else:
                print("_ ", end="")
            item_count += 1
            if item_count % 3 == 0:
                print(" ", end="")
        print()
        line_count += 1
        if line_count % 3 ==0:
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number
    return sudoku