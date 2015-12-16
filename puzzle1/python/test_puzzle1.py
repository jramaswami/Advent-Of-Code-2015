"""
Test for puzzle1.py
"""

import unittest
import puzzle1

class TestPuzzle1(unittest.TestCase):
    """Test for puzzle1.py"""

    def test_puzzle1_part1(self):
        """Test for puzzle1.py"""
        self.assertEquals(puzzle1.process_input_text('(())'), 0)
        self.assertEquals(puzzle1.process_input_text('()()'), 0)
        self.assertEquals(puzzle1.process_input_text('((('), 3)
        self.assertEquals(puzzle1.process_input_text('(()(()('), 3)
        self.assertEquals(puzzle1.process_input_text('())'), -1)
        self.assertEquals(puzzle1.process_input_text('))('), -1)
        self.assertEquals(puzzle1.process_input_text(')))'), -3)
        self.assertEquals(puzzle1.process_input_text(')())())'), -3)

    def test_puzzle1_part2(self):
        """Test for puzzle1.py"""
        self.assertEquals(puzzle1.when_is_basement_entered(')'), 1)
        self.assertEquals(puzzle1.when_is_basement_entered('()())'), 5)

if __name__ == '__main__':
    unittest.main()

