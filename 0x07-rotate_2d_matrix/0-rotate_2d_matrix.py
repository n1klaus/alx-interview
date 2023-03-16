#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix: list) -> None:
    """Rotates a 2d matrix in-place"""
    # create a temporary reference matrix
    _matrix: list = [row.copy() for row in matrix]

    # create column indexer
    col_idx: int = 0
    for row_index in range(len(matrix)):
        # recreate row indexer for each row
        row_idx: int = len(matrix) - 1
        for col_index in range(len(matrix[row_index])):
            # copy values to desired position
            matrix[row_index][col_index] = _matrix[row_idx][col_idx]
            # decrement the row indexer
            row_idx -= 1
        # increment the column indexer
        col_idx += 1
