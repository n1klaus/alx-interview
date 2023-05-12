#!/usr/bin/python3
""" Island Perimeter """


class Cell(object):
    """Class definition for a grid land cell"""
    perimeter = 4
    is_land = False

    def __init__(self, row_index: int, col_index: int):
        """Instantiates a new cell object"""
        self.location = (row_index, col_index)
        self.links = set()

    def __str__(self):
        """Returns the default string representation of the object"""
        return "{0}".format("1" if self.is_land else "0")

    def __repr__(self):
        """Returns the canonical representation of the object"""
        return "Cell {0} with perimeter {2} links to {1}" \
            .format(self.location, [cell.location for cell in self.links],
                    self.perimeter)


class Row(object):
    """Class definition for a grid row"""
    perimeter = 0

    def __init__(self, index: int):
        """Instantiates a new row object"""
        self.index = index
        self.cells = []

    def get_land_cells(self):
        """Returns only land cells in a grid row"""
        return [cell for cell in self.cells if cell.is_land]


class Grid(object):
    """Class definition for a grid"""
    perimeter = 0

    def __init__(self, grid: list):
        """Instantiates a new grid object"""
        self.rows = []
        self.valid_cells = set()
        self.create_grid(grid)

    def create_grid(self, grid: list):
        """Creates our grid land matrix"""
        if isinstance(grid, list):
            rows = []
            for row_index in range(len(grid)):
                columns = []
                for col_index in range(len(grid[row_index])):
                    cell = Cell(row_index, col_index)
                    # create links to other cells if it a land cell
                    if grid[row_index][col_index] == 1:
                        cell.is_land = True
                        if col_index > 0:
                            # Add link to left cell
                            if grid[row_index][col_index - 1] == 1:
                                cell.links.add(Cell(row_index, col_index - 1))
                                # Deduct the perimeter
                                cell.perimeter -= 1
                        if col_index < len(grid[row_index]) - 1:
                            # Add link to right cell
                            if grid[row_index][col_index + 1] == 1:
                                cell.links.add(Cell(row_index, col_index + 1))
                                # Deduct the perimeter
                                cell.perimeter -= 1
                        if row_index > 0:
                            # Add link to top cell
                            if grid[row_index - 1][col_index] == 1:
                                cell.links.add(Cell(row_index - 1, col_index))
                                # Deduct the perimeter
                                cell.perimeter -= 1
                        if row_index < len(grid) - 1:
                            # Add link to bottom cell
                            if grid[row_index + 1][col_index] == 1:
                                cell.links.add(Cell(row_index + 1, col_index))
                                # Deduct the perimeter
                                cell.perimeter -= 1
                    columns.append(cell)
                # Create and fill our row with the cells
                row = Row(row_index)
                row.cells = columns
                rows.append(row)
            # Fill our grid with the rows
            self.rows = rows

    def get_valid_cells(self) -> set:
        """
        Returns a set of land cells which have a link to other cells
        otherwise return single cell in a case of a lonely cell
        """
        if self.rows:
            valid_cells = set()
            # Add all land cells from each row
            for row in self.rows:
                valid_cells.update(row.get_land_cells())

            # Do the pruning
            if len(valid_cells) > 1:
                # Store all locations of linked cells
                valid_locations = set()
                # Add land cells which have been linked by other cells
                for cell in valid_cells:
                    valid_locations.update(
                        {cell.location for cell in cell.links})

                # Only add land cells which have been linked to by other cells
                # in our final set of land cells
                for cell in valid_cells:
                    if cell.location in valid_locations:
                        self.valid_cells.add(cell)
            else:
                # No need for pruning
                new_cell = next(iter(valid_cells), None)
                self.valid_cells.add(new_cell)
        return self.valid_cells

    def get_valid_cells_perimeter(self) -> int:
        """Returns the perimeter of all the valid cells"""
        if self.rows:
            # Get all valid land cells
            for cell in self.get_valid_cells():
                if cell:
                    # Add their perimeter
                    self.perimeter += cell.perimeter
        return self.perimeter

    def __str__(self):
        """Returns the default string representation of the object"""
        result = ""
        for row in self.rows:
            result += "["
            result += " ".join([str(cell) for cell in row.cells])
            result += "]"
            result += "\n"
        return result


def island_perimeter(grid: list) -> int:
    """
    Args:
        grid (list): a list of list of integers representing
                     land or water cells
    Returns:
        (int): The total perimeter of the island
    """
    # validate our arguments
    if not isinstance(grid, list) or \
        not all(list(map(lambda x: True if isinstance(x, list)
                         else False, grid))):
        return 0

    # create a new grid
    my_grid = Grid(grid)

    # Get all valid land cells and calculate the perimeter
    return my_grid.get_valid_cells_perimeter()
