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

    def moore_neighborhood(self, row, col):
        """
        Returns a list of the states of the
        cells in the Moore neighborhood of
        the cell at [row, col].
        """
        moore_n = []
        # up and left
        row_n, col_n = row - 1, col - 1
        if row_n > 0 and col_n > 0:
            moore_n.append((row_n, col_n))
        # up
        row_n, col_n = row - 1, col + 0
        if row_n > 0:
            moore_n.append((row_n, col_n))
        # up and right
        row_n, col_n = row - 1, col + 1
        if row_n > 0 and col_n < self.width:
            moore_n.append((row_n, col_n))
        # right
        row_n, col_n = row + 0, col + 1
        if col_n < self.width:
            moore_n.append((row_n, col_n))
        # down and right
        row_n, col_n = row + 1, col + 1
        if row_n < self.height and col_n < self.width:
            moore_n.append((row_n, col_n))
        # down
        row_n, col_n = row + 1, col + 0
        if row_n < self.height:
            moore_n.append((row_n, col_n))
        # down and left
        row_n, col_n = row + 1, col - 1
        if row_n < self.height and col_n > 0:
            moore_n.append((row_n, col_n))
        # left
        row_n, col_n = row + 0, col - 1
        if col_n > 0:
            moore_n.append((row_n, col_n))

        return moore_n

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
