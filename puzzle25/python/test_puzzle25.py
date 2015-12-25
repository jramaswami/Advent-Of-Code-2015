"""Tests for Day 25 Puzzle"""
import unittest
import puzzle25 as p25

class TestPuzzle25(unittest.TestCase):
    """Test for Day 25 Puzzle"""

    def test_diagonals(self):
        """Test diagonals()"""
        # result = p25.diagonals(1, 6, 1, lambda x: x + 1)
        # self.assertEquals(21, result)

        p25.DEBUG = False
        grid = [[1, 3, 6, 10, 15, 21],
                [2, 5, 9, 14, 20],
                [4, 8, 13, 19],
                [7, 12, 18],
                [11, 17],
                [16],]
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                # row, col addressed from 1 instead of 0 in diagonals
                # so add one to row and col to get correct result
                result = p25.diagonals(row + 1, col + 1, 1, lambda x: x + 1)
                self.assertEquals(grid[row][col], result, \
                                  "%d, %d: %d != %d" % \
                                  (row + 1, col + 1, grid[row][col], result))

        grid = [[20151125, 18749137, 17289845, 30943339, 10071777, 33511524],
                [31916031, 21629792, 16929656, 7726640, 15514188, 4041754],
                [16080970, 8057251, 1601130, 7981243, 11661866, 16474243],
                [24592653, 32451966, 21345942, 9380097, 10600672, 31527494],
                [77061, 17552253, 28094349, 6899651, 9250759, 31663883],
                [33071741, 6796745, 25397450, 24659492, 1534922, 27995004],]
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                # row, col addressed from 1 instead of 0 in diagonals
                # so add one to row and col to get correct result
                result = p25.diagonals(row + 1, col + 1, \
                                       20151125, p25.calculate_code)
                self.assertEquals(grid[row][col], result, \
                                  "%d, %d: %d != %d" % \
                                  (row + 1, col + 1, grid[row][col], result))

    def test_calculate_code(self):
        """Test calculate_code()"""
        initial_value = 20151125
        self.assertEquals(31916031, p25.calculate_code(initial_value))

if __name__ == "__main__":
    unittest.main()
