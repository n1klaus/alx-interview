#!/usr/bin/python3
"""Solving pascal's triangle challenge """


def pascal_triangle(n):
    """Function to create a pascal's triangle

    Args:
        n (int): number of rowIndexs in the triangle

    Returns:
        triangle (list): a list of list of integers making up the triangle

    """
    triangle = []
    if n <= 0:
        return triangle

    for row in range(1, n + 1):
        val = 1
        triangle_row = []
        for col in range(1, row + 1):
            # calculate the value to insert using Binomial Coefficient
            if col > 1:
                val = val * (row - col + 1) // (col - 1)
            # insert value in the row
            triangle_row.append(val)
        triangle.append(triangle_row)
    return triangle
