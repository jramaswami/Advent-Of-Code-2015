"""Tests for puzzle 18"""

import unittest
import puzzle18 as p18

class TestPuzzle18(unittest.TestCase):
    """Tests for puzzle 18"""

    def test_from_string(self):
        """Tests for Grid.from_string()"""
        grid = p18.Grid(0, 0)
        grid_string = "...\n###\n..."
        expected = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
        grid.from_string(grid_string)
        self.assertEquals(grid.grid, expected)
        grid_string = "#..\n.#.\n..#"
        grid.from_string(grid_string)
        expected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEquals(grid.grid, expected)

if __name__ == '__main__':
    unittest.main()
