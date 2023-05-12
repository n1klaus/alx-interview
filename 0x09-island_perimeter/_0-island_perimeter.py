#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid: list) -> int:
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
    start_col = 0
    total_perimeter = 0

    # Iterate each row
    while row_index < len(grid):
        # Start from first column, index 0 if not at the island edge
        col_index = 0

        # Iterate each column
        while col_index < len(grid[row_index]):
            # If cell is land
            if grid[row_index][col_index] == 1:
                # Add perimeter of current cell
                total_perimeter += (1 * 4)
                # set it as the starting column
                if col_index < start_col or start_col == 0:
                    start_col = col_index
                # if connected to land on top, subtract shared connection
                if row_index > 0 and grid[row_index - 1][col_index] == 1:
                    total_perimeter -= 1
                # if connected to land on left, subtract shared connection
                if col_index > 0 and grid[row_index][col_index - 1] == 1:
                    total_perimeter -= 1
                # if connected to land on bottom, subtract shared connection
                if row_index + 1 < len(grid) and \
                        grid[row_index + 1][col_index] == 1:
                    total_perimeter -= 1
                # if connected to land on right, subtract shared connection
                if col_index + 1 < len(grid[row_index]):
                    if grid[row_index][col_index + 1] == 1:
                        total_perimeter -= 1
                    else:
                        # move to the next row to search vertically
                        break

            # Move to the next column
            col_index += 1
        # Move to the next row
        row_index += 1

    return total_perimeter
