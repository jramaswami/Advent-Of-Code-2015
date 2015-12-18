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

    def test_moore_neighborhood(self):
        """Tests for Grid.moore_neighborhood()"""
        grid = p18.Grid(4, 4)
        expected = [(0, 1), (1, 1), (1, 0)]
        self.assertEquals(grid.moore_neighborhood(0, 0), expected)

        expected = [(0, 1), (0, 2), (0, 3), (1, 3),
                    (2, 3), (2, 2), (2, 1), (1, 1)]
        self.assertEquals(grid.moore_neighborhood(1, 2), expected)

        expected = [(2, 0), (2, 1), (2, 2), (3, 2), (3, 0)]
        self.assertEquals(grid.moore_neighborhood(3, 1), expected)

    def test_count_neighbors_on(self):
        """Tests for Grid.count_neighbors_on()"""
        grid = p18.Grid(4, 4)
        grid_string = "##..\n..#.\n#...\n##.#"
        grid.from_string(grid_string)
        self.assertEquals(1, grid.count_neighbors_on(0, 0))
        self.assertEquals(2, grid.count_neighbors_on(3, 0))
        self.assertEquals(0, grid.count_neighbors_on(3, 3))
        self.assertEquals(4, grid.count_neighbors_on(2, 1))

if __name__ == '__main__':
    unittest.main()
