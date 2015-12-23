"""Tests for puzzle 11."""

import unittest
import puzzle11

class TestPuzzle11(unittest.TestCase):
    """Tests for puzzle 11."""

    def test_valid_password(self):
        """Tests for valid_password()."""
        self.assertFalse(puzzle11.valid_password('hijklmmn'))
        self.assertFalse(puzzle11.valid_password('abbceffg'))
        self.assertFalse(puzzle11.valid_password('bbcegjkj'))
        self.assertFalse(puzzle11.valid_password('abcdefgh'))
        self.assertTrue(puzzle11.valid_password('abcdffaa'))
        self.assertFalse(puzzle11.valid_password('ghijklmn'))
        self.assertTrue(puzzle11.valid_password('ghjaabcc'))

    def test_increment_password(self):
        """Tests for increment_password()."""
        self.assertRaises(puzzle11.PasswordException, \
                          puzzle11.increment_password, 'z')
        self.assertRaises(puzzle11.PasswordException, \
                          puzzle11.increment_password, 'zzzzzz')
        self.assertEquals('b', puzzle11.increment_password('a'))
        self.assertEquals('ba', puzzle11.increment_password('az'))

    def test_next_password(self):
        """Tests for next_password()."""
        self.assertEquals('abcdffaa', puzzle11.next_password('abcdefgh'))
        self.assertEquals('ghjaabcc', puzzle11.next_password('ghijklmn'))

if __name__ == '__main__':
    unittest.main()
