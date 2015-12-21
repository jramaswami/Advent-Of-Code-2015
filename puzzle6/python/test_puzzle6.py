"""Tests for puzzle 6."""

import unittest
import puzzle6

class TestPuzzle6(unittest.TestCase):
    """Tests for puzzle 6."""

    def test_grid(self):
        """Tests for grid class."""
        grid = puzzle6.LightGrid(3, 3)
        expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEquals(grid.get_grid(), expected)
        self.assertEquals(grid.count_lights_on(), 0)
        grid.toggle_light(0, 0)
        grid.toggle_light(1, 1)
        grid.toggle_light(2, 2)
        expected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEquals(grid.get_grid(), expected)
        grid.clear_grid()
        expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEquals(grid.get_grid(), expected)
        grid.toggle_rectangle_of_lights(1, 1, 2, 2)
        expected = [[0, 0, 0], [0, 1, 1], [0, 1, 1]]
        self.assertEquals(grid.get_grid(), expected)
        expected = [[1, 1, 0], [0, 0, 0], [0, 1, 1]]
        grid.turn_on_light(0, 0)
        grid.turn_on_light(0, 1)
        grid.turn_off_light(1, 1)
        grid.turn_off_light(1, 2)
        self.assertEquals(grid.get_grid(), expected)
        grid.clear_grid()
        grid.turn_on_rectangle_of_lights(0, 0, 2, 2)
        expected = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEquals(grid.get_grid(), expected)
        grid.turn_off_rectangle_of_lights(1, 1, 2, 2)
        expected = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
        self.assertEquals(grid.get_grid(), expected)

    def test_instruction_processing(self):
        """Tests for processing text instructions."""
        grid = puzzle6.LightGrid(1000, 1000)
        grid.process_instruction("turn on 0,0 through 999,999")
        self.assertEquals((1000 * 1000), grid.count_lights_on())
        grid.process_instruction("toggle 0,0 through 999,0")
        self.assertEquals(((1000 * 1000) - 1000), grid.count_lights_on())
        grid.process_instruction("turn off 0,999 through 999,999")
        self.assertEquals(((1000 * 1000) - 2000), grid.count_lights_on())

    def test_adjustable_light_grid(self):
        """Tests for adjustbale light grid."""
        grid = puzzle6.AdjustableLightGrid(3, 3)
        expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEquals(grid.get_grid(), expected)
        grid.turn_on_light(0, 0)
        expected = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEquals(grid.get_grid(), expected)
        grid.toggle_light(0, 0)
        expected = [[3, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEquals(grid.get_grid(), expected)
        grid.turn_off_light(0, 0)
        expected = [[2, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEquals(grid.get_grid(), expected)

if __name__ == '__main__':
    unittest.main()

