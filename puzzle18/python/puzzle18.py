"""Day 18 Puzzle"""

class Grid(object):
    """Class to represent the grid."""
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = []
        self.str_rep = ['.', '#']
        self.str_dct = {'.' : 0, '#': 1}
        self.init_grid()
        self.future = []

    def init_grid(self):
        """
        Intitializes an empty grid of size
        self.height x self.width.
        """
        for dummy_index in range(self.height):
            self.grid.append([0] * self.width)

    def init_future(self):
        """
        Intitializes an empty grid of size
        self.height x self.width.
        """
        for dummy_index in range(self.height):
            self.future.append([0] * self.width)

    def get_offset_coords(self, row, col, row_off, col_off):
        """
        If the cell is in the grid, returns the
        coordinates of the cell.  If the cell
        is not on the grid, returns None.
        """
        row_d = row + row_off
        col_d = col + col_off
        if row_d >= 0 and row_d < self.height \
        and col_d >= 0 and col_d < self.height:
            return (row_d, col_d)
        else:
            return None

    def moore_neighborhood(self, row, col):
        """
        Returns a list of the states of the
        cells in the Moore neighborhood of
        the cell at [row, col].
        """
        moore_n = []
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
                   (1, 1), (1, 0), (1, -1), (0, -1)]

        for off in offsets:
            neighbor = self.get_offset_coords(row, col, off[0], off[1])
            if neighbor != None:
                moore_n.append(neighbor)

        return moore_n

    def count_neighbors_on(self, row, col):
        """Returns the number of neighbors that are on."""
        moore_n = self.moore_neighborhood(row, col)
        result = sum([self.grid[n[0]][n[1]] for n in moore_n])
        return result

    def __str__(self):
        result = ''
        for row in self.grid:
            row_str = [self.str_rep[i] for i in row]
            result += " ".join(row_str) + "\n"
        return result

    def from_string(self, grid_string):
        """Loads grid from string."""
        row_strings = grid_string.split("\n")
        self.height = len(row_strings)
        self.width = len(row_strings[0])
        self.grid = []
        for row_s in row_strings:
            self.grid.append([self.str_dct[c] for c in row_s])

def main():
    """Main program."""
    grid = Grid(4, 4)
    print grid

if __name__ == '__main__':
    main()
