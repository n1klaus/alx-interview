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
Cells are inter-connected horizontally/vertically (not diagonally) therefore making a rectangular structure
The grid is completely surrounded by water
There is only one island (or nothing).

# [Brute Force Solution 1 - Using neighbouring cells to interconnect the island](./_0-island_perimeter.py)
- Find the Island (Interconnection of land cells (1) )
    - Start scanning from the first row first column to get one land cell(1) 
      and connect to other land cells(1) interconnected horizontally (in same row)
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

Time complexity => O(n ^ 2)
Space complexity => O(1)

=> Faults - Doesn't work with irregular shaped islands with cells in a row separated by water e.g
    [
        [0, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0]
    ]

# [Brute Force Solution 2 - Using rows as collections of cell nodes with each cell having location and links to other cells to map the connection path](./0-island_perimeter.py)
### Base objects
Cell => links: (set) collection of linking cells (horizontally and vertivally only)
        perimeter: (int) total perimeter of the cell minus its shared connections
        location: (tuple) row index, column index
		is_land: (bool) True if cell is land False otherwise

Row => cells: (list) collection of cells with land
       index: (int) row index
       perimeter: (int) total perimeter of the its cells

Grid => rows: (list) collection of non-empty rows
		valid_cells: (set) collection all cells that map a connection path for the island
        perimeter: (int) total perimeter of the its valid_cells

### Operations:
(Row) => get all land cells
(Row) => get the total perimeter of a row
(Grid) => get all valid land cells
(Grid) => get the total perimeter of the grid using the valid land cells
(Grid) => get all cell links to create valid_cells set
(Grid) => prune dangling cells i.e cells with no links
(Grid) => prune orphan cells i.e cells whose locations is not in valid_cells set


### Procedure
- Create our base objects => Cells, Rows and the Grid
- Fill the rows with linked cells while calculating cell perimeter for each cell
- create our set of all linked cells in the grid and prune out cells without links
- with the final set of valid cells get the total perimter

Time complexity => O(n ^ 2)
Space complexity => O(n)
