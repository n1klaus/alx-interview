#!/usr/bin/python3
"""
Solving pascal's triangle with O(log n) time complexity
and O(n) space complexity
"""


def pascal_triangle(n):
    """
    Function to create a pascal's triangle

    Returns:
        a list of list of integers

    """
    triangle: list = []
    if n <= 0:
        return triangle

    try:
        for row in range(n):
            # create a list of integers for every row
            new_row = [None] * (row + 1)
            new_row[0] = 1
            if row >= 2:
                # Add values which fall in range of 1 to -2 if there are any
                for col in range(1, n - 1):
                    if col < row:
                        new_row[col] = triangle[row - 1][col] + \
                            triangle[row - 1][col - 1]
            if n >= 2:
                new_row[-1] = 1
            triangle.append(new_row)
        return triangle
    except BaseException:
        raise
