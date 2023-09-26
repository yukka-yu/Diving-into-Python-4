# 1. Напишите функцию для транспонирования матрицы


def transponeering(matrix):
    m = len(matrix)  #2
    n = len(matrix[0]) #3
    new_matrix = [[0 for i in range(m)] for j in range(n)]
    for i in range(m): # 0, 1
        for j in range(n): # 0, 1, 2
            new_matrix[j][i] = matrix[i][j] # new_matrix[0][1] = matrix[1][0] new_matrix[1][1] = matrix[1][1]
    return new_matrix
    
print(transponeering([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))