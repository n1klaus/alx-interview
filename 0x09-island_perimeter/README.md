# Island Perimeter

# Problem
Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in grid:

grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

# Requirements
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water
There is only one island (or nothing).

# Solution
- Find the Island (Interconnection of land cells (1) )
    - Get one land cell(1) and connect to other land cells(1) interconnected horizontally (in same row)
      or vertically (in same column) while calculating the total perimeter
        - add perimeter for each cell where perimeter = (length of a side) 1 * 4 (all sides)
        - check if the current cell shares a connection with another cell
            - if it shares a connection with another cell on its top side (previous row)
                - subtract the length (1) from the total perimeter
            - if it shares a connection with another cell on its left side (previous column)
                - subtract the length (1) from the total perimeter
            - if it shares a connection with another cell on its bottom side (next row)
                - subtract the length (1) from the total perimeter
            - if it shares a connection with another cell on its right side (next column)
                - subtract the length (1) from the total perimeter
    - return the total perimeter
- if there is no land cell(1) found, there is no island present

