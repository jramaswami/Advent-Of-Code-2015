"""Tests for puzzle 7."""

import unittest
import puzzle7
import numpy as np

class TestPuzzle7(unittest.TestCase):
    """Tests for puzzle 7."""

    def test_puzzle_7a(self):
        """Tests for puzzle 7, part 1."""
        circuit = puzzle7.Circuit()
        circuit.process_instruction('123 -> x')
        self.assertEquals(123, circuit.get_wire_signal('x'))
        circuit.process_instruction('456 -> y')
        self.assertEquals(456, circuit.get_wire_signal('y'))
        circuit.process_instruction('x AND y -> d')
        self.assertEquals(np.bitwise_and(123, 456), circuit.get_wire_signal('d'))
        circuit.process_instruction('x OR y -> e')
        circuit.process_instruction('x LSHIFT 2 -> f')
        circuit.process_instruction('y RSHIFT 2 -> g')
        circuit.process_instruction('NOT x -> h')
        circuit.process_instruction('NOT y -> i')

        print circuit.get_wires()

if __name__ == '__main__':
    unittest.main()
