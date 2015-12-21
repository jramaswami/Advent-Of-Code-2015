"""Tests for puzzle 8."""

import unittest
import puzzle8

class TestPuzzle8(unittest.TestCase):
    """Tests for puzzle 8."""

    def test_count_chars(self):
        """Tests for puzzle 8, part 1."""
        self.assertEquals(0, puzzle8.count_chars("\"\""))
        self.assertEquals(3, puzzle8.count_chars("\"abc\""))
        self.assertEquals(7, puzzle8.count_chars("aaa\\\"aaa"))
        self.assertEquals(1, puzzle8.count_chars("\\x27"))

    def test_encode_chars(self):
        """Tests for puzzle 8, part 2."""
        self.assertEquals('"\\"\\""', puzzle8.encode('""'))
        self.assertEquals('"\\"abc\\""', puzzle8.encode('"abc"'))
        self.assertEquals('"\\"aaa\\\\\\"aaa\\""', puzzle8.encode('"aaa\\"aaa"'))
        self.assertEquals('"\\"\\\\x27\\""', puzzle8.encode('"\\x27"'))

if __name__ == '__main__':
    unittest.main()
