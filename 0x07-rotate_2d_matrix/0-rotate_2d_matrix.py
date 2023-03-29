#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix: list) -> None:
    """Rotates a 2d matrix in-place"""
    # create index pointers
    col_idx: int = 0
    row_idx: int = 0
    last_idx: int = 0

    # Transpose the matrix rows and columns
    while row_idx < len(matrix):
        while col_idx < len(matrix[row_idx]):
            # swap values with xor
            current: int = matrix[row_idx][col_idx]
            replacement: int = matrix[col_idx][row_idx]
            temp: int = current ^ replacement
            replacement = matrix[col_idx][row_idx] = temp ^ replacement
            current = matrix[row_idx][col_idx] = temp ^ current
            # move to the next column
            col_idx += 1
        # if reached end of the row
        if col_idx == len(matrix[row_idx]):
            last_idx += 1
            col_idx = last_idx
        # move to the next row
        row_idx += 1

    # Reverse each row in the matrix
    for row_index in range(len(matrix)):
        row_size: int = len(matrix[row_index])
        for col_index in range(row_size // 2):
            # swap values with xor
            last_col_index: int = row_size - 1 - col_index
            current: int = matrix[row_index][col_index]
            replacement: int = matrix[row_index][last_col_index]
            temp: int = current ^ replacement
            replacement = matrix[row_index][last_col_index] = \
                temp ^ replacement
            current = matrix[row_index][col_index] = temp ^ current
