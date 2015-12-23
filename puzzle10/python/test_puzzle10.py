"""Tests for puzzle 10."""

import unittest
import puzzle10

class TestPuzzle10(unittest.TestCase):
    """Tests for puzzle 10."""

    def test_look_and_say(self):
        """Tests for look_and_say()."""
        self.assertEquals('11', puzzle10.look_and_say('1'))
        self.assertEquals('21', puzzle10.look_and_say('11'))
        self.assertEquals('1211', puzzle10.look_and_say('21'))
        self.assertEquals('111221', puzzle10.look_and_say('1211'))
        self.assertEquals('312211', puzzle10.look_and_say('111221'))

if __name__ == '__main__':
    unittest.main()
