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

    for rowIndex in range(n):
        # fill the row with empty values
        new_row = [None] * (rowIndex + 1)
        # Insert 1 in first index
        new_row[0] = 1
        # Check if there are possible indexes between the first and last index
        if rowIndex >= 2:
            # Fill values which fall in between the first and last index
            for colIndex in range(1, n - 1):
                if colIndex < rowIndex:
                    new_row[colIndex] = triangle[rowIndex - 1][colIndex] + \
                        triangle[rowIndex - 1][colIndex - 1]
                else:
                    break
        # Insert 1 in last index if the rowIndex size is greater than 1
        if n >= 2:
            new_row[-1] = 1
        # finally add the created rowIndex into the triangle
        triangle.append(new_row)
    return triangle
