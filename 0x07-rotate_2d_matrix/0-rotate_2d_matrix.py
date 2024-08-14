#!/usr/bin/python3
""" Rotate a 2D matrix"""


def rotate_2d_matrix(matrix):
    """
    rotate 2D matrix
    [1, 2, 3]       [7, 4, 1]
    [4, 5, 6] ===>  [8, 5, 2]
    [7, 8. 9]       [9, 6, 3]
    """
    # Step 1: Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
