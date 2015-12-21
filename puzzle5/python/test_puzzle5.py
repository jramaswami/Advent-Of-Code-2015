"""Tests for puzzle 5."""

import unittest
import puzzle5

class TestPuzzle5(unittest.TestCase):
    """Tests for puzzle 5."""

    def test_puzzle5a(self):
        """Tests for puzzle 5, part 1."""
        print "Tests for puzzle 5, part 1."
        self.assertTrue(puzzle5.string_is_nice('ugknbfddgicrmopn'))
        self.assertTrue(puzzle5.string_is_nice('aaa'))
        self.assertFalse(puzzle5.string_is_nice('jchzalrnumimnmhp'))
        self.assertFalse(puzzle5.string_is_nice('haegwjzuvuyypxyu'))
        self.assertFalse(puzzle5.string_is_nice('dvszwmarrgswjxmb'))
        input_string = "ugknbfddgicrmopn\naaa\njchzalrnumimnmhp\n" \
                     + "haegwjzuvuyypxyu\ndvszwmarrgswjxmb"
        self.assertEquals(2, puzzle5.count_nice_strings(input_string))
        print ("*" * 50), "\n"

    def test_puzzle5b(self):
        """Tests for puzzle 5, part 2."""
        print "Tests for puzzle 5, part 2."
        puzzle5.DEBUG = True
        self.assertTrue(puzzle5.string_is_nice2('qjhvhtzxzqqjkmpb'))
        self.assertTrue(puzzle5.string_is_nice2('xxyxx'))
        self.assertTrue(puzzle5.string_is_nice2('xxazxxzyz'))
        self.assertFalse(puzzle5.string_is_nice2('xyxxx'))
        self.assertFalse(puzzle5.string_is_nice2('xxxyx'))
        self.assertFalse(puzzle5.string_is_nice2('uurcxstgmygtbstg'))
        self.assertFalse(puzzle5.string_is_nice2('ieodomkazucvgmuy'))
        input_string = "qjhvhtzxzqqjkmpb\nxxyxx\n" \
                     + "uurcxstgmygtbstg\nieodomkazucvgmuy"
        self.assertEquals(2, puzzle5.count_nice_strings2(input_string))
        print ("*" * 50), "\n"

if __name__ == '__main__':
    unittest.main()
