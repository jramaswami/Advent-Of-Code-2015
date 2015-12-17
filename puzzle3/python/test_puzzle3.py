"""Tests for puzzle 3."""

import unittest
import puzzle3

class TestPuzzle3(unittest.TestCase):
    """Tests for puzzle 3."""

    def test_puzzle3a(self):
        """Tests for puzzle 3, part 1."""
        self.assertEquals(2, puzzle3.santa_alone_delivers('>'))
        self.assertEquals(4, puzzle3.santa_alone_delivers('^>v<'))
        self.assertEquals(2, puzzle3.santa_alone_delivers('^v^v^v^v^v'))

    def test_puzzle3b(self):
        """Tests for puzzle 3, part 1."""
        self.assertEquals(3, puzzle3.santa_with_robot_delivers('^v'))
        self.assertEquals(3, puzzle3.santa_with_robot_delivers('^>v<'))
        self.assertEquals(11, puzzle3.santa_with_robot_delivers('^v^v^v^v^v'))

if __name__ == '__main__':
    unittest.main()
