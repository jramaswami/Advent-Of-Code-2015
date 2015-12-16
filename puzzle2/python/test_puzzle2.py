"""Tests for puzzle 2."""

import unittest
import puzzle2
import puzzle2b

class TestPuzzle2(unittest.TestCase):
    """Tests for puzzle 2."""

    def test_puzzle2(self):
        """Tests for puzzle 2."""
        box1 = '2x3x4'
        box2 = '1x1x10'
        self.assertEquals(58, puzzle2.square_feet_for_box(box1))
        self.assertEquals(43, puzzle2.square_feet_for_box(box2))
        self.assertEquals((58 + 43), puzzle2.process_box_list([box1, box2]))

    def test_puzzle2b(self):
        """Tests for puzzle 2b."""
        box1 = '2x3x4'
        box2 = '1x1x10'
        self.assertEquals(34, puzzle2b.ribbon_required_for_box(box1))
        self.assertEquals(14, puzzle2b.ribbon_required_for_box(box2))
        self.assertEquals((34 + 14), puzzle2b.process_box_list([box1, box2]))

if __name__ == '__main__':
    unittest.main()

