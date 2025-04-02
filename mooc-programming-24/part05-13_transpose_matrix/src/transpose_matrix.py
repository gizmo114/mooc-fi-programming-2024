# Write your solution here
def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp