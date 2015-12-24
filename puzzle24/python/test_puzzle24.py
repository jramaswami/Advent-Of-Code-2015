"""Tests for Day 24 Puzzle"""
import unittest
import puzzle24 as p24

class TestPuzzle24(unittest.TestCase):
    """Test for Day 24 Puzzle"""

    def test_find_groups(self):
        """Test find_groups()"""
        p24.DEBUG = False
        packages = range(1, 6)
        packages.extend(range(7, 12))

        weight = sum(packages) / 3
        solutions = p24.find_groups(packages, weight, early_exit=False)
        possibles = [[11, 9], [10, 9, 1], [10, 8, 2], [10, 7, 3], \
                     [10, 5, 4, 1], [10, 5, 3, 2], [10, 4, 3, 2, 1], \
                     [9, 8, 3], [9, 7, 4], [9, 5, 4, 2], [8, 7, 5], \
                     [8, 5, 4, 3], [7, 5, 4, 3, 1]]

        if p24.DEBUG == True:
            print "*" * 80
        for poss in possibles:
            self.assertIn(poss, solutions)

        solutions = p24.find_groups(packages, weight, early_exit=True)
        self.assertEquals([[11, 9]], solutions)

        weight = sum(packages) / 4
        solutions = p24.find_groups(packages, weight, \
                                    groups_of=4, early_exit=False)
        possibles = [[11, 4], [10, 5], [9, 5, 1], [9, 4, 2], \
                     [9, 3, 2, 1], [8, 7]]
        if p24.DEBUG == True:
            print "*" * 80
        for poss in possibles:
            self.assertIn(poss, solutions)

        solutions = p24.find_groups(packages, weight, \
                                    groups_of=4, early_exit=True)
        self.assertEquals(sorted([[11, 4], [10, 5], [8, 7]]), \
                          sorted(solutions))

    def test_do_puzzle(self):
        """Test do_puzzle()"""
        p24.DEBUG = False
        packages = range(1, 6)
        packages.extend(range(7, 12))

        min_qe, winner = p24.do_puzzle(packages, groups_of=3)
        self.assertEquals([11, 9], winner)
        self.assertEquals(99, min_qe)

        min_qe, winner = p24.do_puzzle(packages, groups_of=4)
        self.assertEquals([11, 4], winner)
        self.assertEquals(44, min_qe)

if __name__ == "__main__":
    unittest.main()
