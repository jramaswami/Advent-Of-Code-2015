"""Day 6 Puzzle"""

import re

class LightGrid(object):
    """Represents a grid of lights."""

    def __init__(self, width, height):
        """Constructor."""
        self._grid = []
        self._width = width
        self._height = height
        self.clear_grid()

    def clear_grid(self):
        """Make grid all zeros."""
        self._grid = []
        for dummy_index in range(self._height):
            self._grid.append([0 for dummy_kndex in range(self._width)])

    def __str__(self):
        """__str__ method."""
        result = ""
        for row in self._grid:
            result = result + str(row) + "\n"
        return result

    def toggle_light(self, row, col):
        """Toggles lights on and off."""
        if self._grid[row][col] == 1:
            self._grid[row][col] = 0
        else:
            self._grid[row][col] = 1

    def toggle_rectangle_of_lights(self, row1, col1, row2, col2):
        """Toggles lights from [row1, col1] to [row2, col2] inclusive."""
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.toggle_light(row, col)

    def turn_on_light(self, row, col):
        """Turns on light."""
        self._grid[row][col] = 1

    def turn_on_rectangle_of_lights(self, row1, col1, row2, col2):
        """Turns on lights from [row1, col1] to [row2, col2] inclusive."""
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.turn_on_light(row, col)

    def turn_off_light(self, row, col):
        """Turns off light."""
        self._grid[row][col] = 0

    def turn_off_rectangle_of_lights(self, row1, col1, row2, col2):
        """Turns off lights from [row1, col1] to [row2, col2] inclusive."""
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.turn_off_light(row, col)

    def get_grid(self):
        """Returns the list of lists that is the grid."""
        return self._grid

    def count_lights_on(self):
        """Returns the number of lights on."""
        return sum([sum(row) for row in self._grid])

    def process_instruction(self, line):
        """Process a text instruction."""
        tokens = [item for item in re.split(r'(\W+)', line) \
                  if item not in [' ', ',']]
        if tokens[0] == 'turn':
            if tokens[1] == 'on':
                self.turn_on_rectangle_of_lights(int(tokens[2]), int(tokens[3]),
                                                 int(tokens[5]), int(tokens[6]))
            elif tokens[1] == 'off':
                self.turn_off_rectangle_of_lights(int(tokens[2]), int(tokens[3]),
                                                  int(tokens[5]), int(tokens[6]))
        elif tokens[0] == 'toggle':
            self.toggle_rectangle_of_lights(int(tokens[1]), int(tokens[2]),
                                            int(tokens[4]), int(tokens[5]))



class AdjustableLightGrid(LightGrid):
    """Represents grid of lights with adjustable brightness."""

    def __init__(self, width, height):
        """Constructor."""
        LightGrid.__init__(self, width, height)

    def toggle_light(self, row, col):
        self._grid[row][col] += 2

    def turn_off_light(self, row, col):
        if self._grid[row][col] > 0:
            self._grid[row][col] -= 1

    def turn_on_light(self, row, col):
        self._grid[row][col] += 1


def process_input_file(file_name, grid):
    """Process an input file."""
    input_file = open(file_name, 'r')
    for line in input_file:
        grid.process_instruction(line.strip())
    input_file.close()
    return grid.count_lights_on()

if __name__ == '__main__':
    print 'There are', \
          process_input_file('../input.txt', LightGrid(1000, 1000)), \
          'lights on'
    print 'The total brightness is', \
          process_input_file('../input.txt', AdjustableLightGrid(1000, 1000))
