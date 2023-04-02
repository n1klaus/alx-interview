#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid: list):
    """
    Args:
        grid (list): a list of list of integers representing
                     land or water cells
    Returns:
        (int): The total perimeter of the island
    """
    # check if our argument is undefined
    if not isinstance(grid, list) or \
        not all(list(map(lambda x: True if isinstance(x, list)
                         else False, grid))):
        return 0

    # create our variables
    row_index = 0
    perimeter = 0
    landed_on_water = False

    # Iterate each row
    while row_index < len(grid):
        # Start from first column if not landed on water, 0
        if not landed_on_water:
            col_index = 0
        # Reset the check
        landed_on_water = False

        # Iterate each column
        while col_index < len(grid[row_index]):
            # If cell is land
            if grid[row_index][col_index] == 1:
                # Add perimeter of current cell
                perimeter += 1 * 4
            # if connected to land on top, substract shared connection
            if grid[row_index - 1][col_index] == 1:
                perimeter -= 1
            # if connected to land on left, substract shared connection
            if grid[row_index][col_index - 1] == 1:
                perimeter -= 1
            # if connected to land on right, substract shared connection
            if col_index + 1 < len(grid[row_index]) and \
                    grid[row_index][col_index + 1] == 1:
                perimeter -= 1
            else:
                # move to the next row to search vertically
                landed_on_water = True
                break
            # if connected to land on bottom, substract shared connection
            if row_index + 1 < len(grid) and \
                    grid[row_index + 1][col_index] == 1:
                perimeter -= 1

            # Move to the next column
            col_index += 1
        # Move to the next row
        row_index += 1

    return perimeter
