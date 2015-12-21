"""Tests Day 9 Puzzle."""

import unittest
import puzzle9

class TestPuzzle9(unittest.TestCase):
    """Tests for puzzle 9."""

    def test_calculate_distance(self):
        """Tests for puzzle9.calculate_distance()"""
        distances = {('London', 'Dublin') : 464,
                     ('London', 'Belfast') : 518,
                     ('Dublin', 'Belfast') : 141}
        route = ('Dublin', 'London', 'Belfast')
        self.assertEquals(982, puzzle9.calculate_distance(route, distances))
        route = ('London', 'Dublin', 'Belfast')
        self.assertEquals(605, puzzle9.calculate_distance(route, distances))
        route = ('Belfast', 'Dublin', 'London')
        self.assertEquals(605, puzzle9.calculate_distance(route, distances))
        route = ('Dublin', 'Belfast', 'London')
        self.assertEquals(659, puzzle9.calculate_distance(route, distances))
        route = ('Belfast', 'Dublin', 'London')
        self.assertEquals(605, puzzle9.calculate_distance(route, distances))
        route = ('Belfast', 'London', 'Dublin')
        self.assertEquals(982, puzzle9.calculate_distance(route, distances))

if __name__ == '__main__':
    unittest.main()
