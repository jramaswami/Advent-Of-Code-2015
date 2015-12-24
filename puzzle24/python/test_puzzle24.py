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
        print packages
        for t in solutions:
            print t
        self.assertEquals(13, len(solutions))


if __name__ == "__main__":
    unittest.main()
