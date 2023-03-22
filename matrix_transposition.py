

def transposition(matrix):
    transposed_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))] 
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix

matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 5, 6]]
print(transposition(matrix))