"""Tests for puzzle13"""

import unittest
import puzzle13

class TestPuzzle13(unittest.TestCase):
    """Tests for puzzle13."""

    def test_load_input_file(self):
        """Tests for load_input_file()"""
        happiness, people = puzzle13.load_input_file('../test_input.txt')
        self.assertEquals(54, happiness[('Alice', 'Bob')])
        self.assertEquals(-7, happiness[('Bob', 'Carol')])

        self.assertEquals(4, len(people))
        self.assertTrue('Alice' in people)
        self.assertTrue('Bob' in people)
        self.assertTrue('Carol' in people)
        self.assertTrue('David' in people)

    def test_find_happiest_arrangement(self):
        """Tests find_happiest_arrangment()."""
        happiness, people = puzzle13.load_input_file('../test_input.txt')
        arrangements = puzzle13.possible_seating_arrangements(people)
        scored_arrangements = puzzle13.score_seating_arrangements(arrangements, \
                                                                  happiness)
        happiest_arrangement = puzzle13.find_happiest_arrangement(scored_arrangements)
        self.assertEquals(330, scored_arrangements[happiest_arrangement])

if __name__ == '__main__':
    unittest.main()
