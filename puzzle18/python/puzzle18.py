"""Day 18 Puzzle"""

class Grid(object):
    """Class to represent the grid."""
    def __init__(self, height, width, broken_corner_lights=False):
        self.height = height
        self.width = width
        self.broken_corner_lights = broken_corner_lights
        self.str_rep = ['.', '#']
        self.str_dct = {'.' : 0, '#': 1}

        self.grid = []
        self.init_grid()

    def init_grid(self):
        """
        Intitializes an empty grid of size
        self.height x self.width.
        """
        for dummy_index in range(self.height):
            self.grid.append([0] * self.width)

        # for part two of the puzzle
        # the 4 lights in the corner are
        # always on
        if self.broken_corner_lights:
            self.turn_on_corner_lights()

    def __str__(self):
        result = ''
        for row in self.grid:
            row_str = [self.str_rep[i] for i in row]
            result += "".join(row_str) + "\n"
        return result

    def __eq__(self, other_grid):
        return self.grid == other_grid.grid

    def from_string(self, grid_string):
        """Loads grid from string."""
        row_strings = grid_string.split("\n")
        self.height = len(row_strings)
        self.width = len(row_strings[0])
        self.grid = []
        for row_s in row_strings:
            self.grid.append([self.str_dct[c] for c in row_s])
        if self.broken_corner_lights:
            self.turn_on_corner_lights()

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

    def get_future_state(self, row, col):
        """Returns the future state for a given cell."""

        # The state a light should have next is based on its
        # current state (on or off) plus the number of neighbors
        # that are on:
        #
        #   A light which is on stays on when 2 or 3 neighbors
        #   are on, and turns off otherwise.
        #
        #   A light which is off turns on if exactly 3 neighbors are
        #   on, and stays off otherwise.

        neighbors_on = self.count_neighbors_on(row, col)
        if self.grid[row][col] == 1:
            if neighbors_on == 2 or neighbors_on == 3:
                return 1
            else:
                return 0
        else:
            if neighbors_on == 3:
                return 1
            else:
                return 0

    def count_lights_on(self):
        """Returns a count of the lights that are on."""
        return sum([sum(row) for row in self.grid])

    def tick(self, tick_count=1):
        """Execute the given number of round of the game of life."""
        for dummy_index in range(tick_count):
            future_grid = []
            for row in range(self.height):
                future_row = []
                for col in range(self.width):
                    future_row.append(self.get_future_state(row, col))
                future_grid.append(future_row)
            self.grid = future_grid

            if self.broken_corner_lights:
                self.turn_on_corner_lights()

    def turn_on_corner_lights(self):
        """Turn the lights in the four corners on."""
        # for part two of the puzzle
        # the 4 lights in the corner are
        # always on
        if not self.grid == []:
            self.grid[0][0] = 1
            self.grid[0][-1] = 1
            self.grid[-1][-1] = 1
            self.grid[-1][0] = 1


def read_data():
    """Read data from input file."""
    with open('../input.txt', 'r') as input_file:
        data = input_file.read().strip()
    return data

def main():
    """Main program."""
    grid = Grid(0, 0)
    grid.from_string(read_data())
    grid.tick(100)
    print "There are", grid.count_lights_on(), "after 100 steps."

if __name__ == '__main__':
    main()
