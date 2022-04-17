import numpy as np

# Make matrix
def make_matrix(n):
    return [[0] * n for i in range(n)]

# Set matrix
def set_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            ele = input('Enther element at row %d, col %d\n>>> ' %(i, j))
            matrix[i][j].append(ele)

matrix = np.array([[0, 0, 0, 0, 0], 
 [0, 1, 1, 0, 0],
 [0, 1, 1, 0, 0],
 [0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0]])

# Set status
def set_status(matrix):
    n = matrix.shape[0]
    matrix_cop = np.copy(matrix)
    for r in range(2, n):
        for c in range(2, n):
            sum = np.sum(matrix[r-2:r+1, c-2:c+1])
            if matrix_cop[r-1][c-1] == 1:
                if sum-1 == 2 or sum-1 == 3: 
                    matrix_cop[r-1][c-1] = 1
                else:
                    matrix_cop[r-1][c-1] = 0
            else:
                if sum == 3: 
                    matrix_cop[r-1][c-1] = 1
                else: 
                    matrix_cop[r-1][c-1] = 0

    print('ma tran moi:', matrix_cop)
    return matrix_cop

set_status(matrix)