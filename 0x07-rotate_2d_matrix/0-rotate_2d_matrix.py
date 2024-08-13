#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """rotate two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Rotate elements in place using tuple unpacking
            (matrix[i][j], matrix[j][n - 1 - i],
             matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i]) = (
                matrix[n - 1 - j][i], matrix[i][j],
                matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j])

