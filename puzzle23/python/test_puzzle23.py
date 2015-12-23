"""Tests for Day 23 Puzzle"""
import unittest
import puzzle23 as p23

class TestPuzzle23(unittest.TestCase):
    """Test for Day 23 Puzzle"""

    def test_run_program(self):
        """Test run_program()"""
        program = ['inc a', 'jio a, +2', 'tpl a', 'inc a']
        registers = {'a': 0}
        p23.run_program(program, registers)
        self.assertEquals(registers['a'], 2)

if __name__ == "__main__":
    unittest.main()
