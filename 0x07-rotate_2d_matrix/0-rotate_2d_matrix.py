#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.
    """
    size = len(matrix)
    for row_idx in range(size):
        for col_idx in range(row_idx, size):
            matrix[row_idx][col_idx], matrix[col_idx][row_idx] = \
                matrix[col_idx][row_idx], matrix[row_idx][col_idx]

    for r in matrix:
        r.reverse()
