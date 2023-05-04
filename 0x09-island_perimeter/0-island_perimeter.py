#!/usr/bin/python3
""" Island Perimeter """


class Cell(object):
    """Class definition for cells"""
    perimeter = 4
    is_land = False

    def __init__(self, row_index: int, col_index: int):
        """Instantiates new cell objects"""
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
    """Class definition for rows"""
    perimeter = 0

    def __init__(self, index: int):
        """Instantiates new row objects"""
        self.index = index
        self.cells = []

    def get_land_cells(self):
        """Returns only cells with land"""
        return [cell for cell in self.cells if cell.is_land]


class Grid(object):
    """Class definition for grid"""
    perimeter = 0

    def __init__(self, grid: list):
        """Instantiates new grid objects"""
        self.rows = []
        self.linked_cells = set()
        self.create_grid(grid)

    def create_grid(self, grid: list):
        """Creates our grid"""
        if isinstance(grid, list):
            rows = []
            for row_index in range(len(grid)):
                columns = []
                for col_index in range(len(grid[row_index])):
                    cell = Cell(row_index, col_index)
                    # print(repr(cell))
                    # create links if it a land cell
                    if grid[row_index][col_index] == 1:
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
                    # Ignore cells with no links
                    if len(cell.links) > 0:
                        cell.is_land = True
                    # print(repr(cell))
                    columns.append(cell)
                row = Row(row_index)
                row.cells = columns
                rows.append(row)
            self.rows = rows

    def get_linked_cells(self) -> set:
        """Returns a set of all linked cells"""
        if self.rows:
            valid_cells = set()
            for row in self.rows:
                valid_cells.update(row.get_land_cells())
            # Do the pruning
            valid_locations = set()
            for cell in valid_cells:
                valid_locations.update([cell.location for cell in cell.links])
            for cell in valid_cells:
                if cell.location in valid_locations:
                    self.linked_cells.add(cell)
        return self.linked_cells

    def get_linked_cells_perimeter(self) -> int:
        """Returns the perimeter of all the linked cells"""
        if self.rows:
            for cell in self.get_linked_cells():
                self.perimeter += cell.perimeter
        return self.perimeter

    def __str__(self):
        """Overrides the default string representation of the object"""
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
    # check if our argument is undefined
    if not isinstance(grid, list) or \
        not all(list(map(lambda x: True if isinstance(x, list)
                         else False, grid))):
        return 0

    # create a new grid
    my_grid = Grid(grid)

    print(my_grid)
    # Get all linked cells and calculate the perimeter
    return my_grid.get_linked_cells_perimeter()
