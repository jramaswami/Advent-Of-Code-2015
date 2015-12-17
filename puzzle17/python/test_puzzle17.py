"""Tests for Day 17 Puzzle"""

import unittest
import puzzle17 as p17

class TestPuzzle17(unittest.TestCase):
    """Tests for Day 17 Puzzle."""

    def test_filter_permutations(self):
        """Tests for filter_permutations()"""
        containers = [20, 15, 10, 5, 5]
        combos = p17.container_combinations(containers)
        filt_combos = [fp for fp in p17.filter_combinations(combos, 25)]
        self.assertEquals(4, len(filt_combos))

    def test_min_length(self):
        """Tests for find_min_length()"""
        containers = [20, 15, 10, 5, 5]
        combos = p17.container_combinations(containers)
        filt_combos = [fp for fp in p17.filter_combinations(combos, 25)]
        self.assertEquals(2, p17.find_min_length(filt_combos))

    def test_select_smallest_combos(self):
        """Tests for select_smallest_combinations()"""
        containers = [20, 15, 10, 5, 5]
        combos = p17.container_combinations(containers)
        filt_combos = [fp for fp in p17.filter_combinations(combos, 25)]
        self.assertEquals(3, len(p17.select_smallest_combinations(filt_combos)))

if __name__ == '__main__':
    unittest.main()

