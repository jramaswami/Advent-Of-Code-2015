"""Tests for Day 24 Puzzle"""
import unittest
import puzzle24 as p24
import operator

class TestPuzzle24(unittest.TestCase):
    """Test for Day 24 Puzzle"""

    def test_something(self):
        """Test find_groups()"""
        p24.DEBUG = True
        packages = range(1, 6)
        packages.extend(range(7, 12))
        packages.reverse

        weight = sum(packages) / 3
        solutions = p24.find_groups(packages, weight, early_exit=False)
        print "*" * 80
        for t in solutions:
            print t

        possibles = [[11, 9], [10, 9, 1], [10, 8, 2], [10, 7, 3], \
                     [10, 5, 4, 1], [10, 5, 3, 2], [10, 4, 3, 2, 1], \
                     [9, 8, 3], [9, 7, 4], [9, 5, 4, 2], [8, 7, 5], \
                     [8, 5, 4, 3], [7, 5, 4, 3, 1]]
        for poss in possibles:
            self.assertIn(poss, solutions)

if __name__ == "__main__":
    unittest.main()
