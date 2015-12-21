"""Tests for puzzle 4."""

import unittest
import puzzle4

class TestPuzzle4(unittest.TestCase):
    """Tests for puzzle 4."""

    def test_puzzle4a(self):
        """Tests for puzzle 4, part 1."""
        self.assertEquals(609043, puzzle4.find_first_md5('abcdef', 5))
        self.assertEquals(1048970, puzzle4.find_first_md5('pqrstuv', 5))

if __name__ == '__main__':
    unittest.main()
