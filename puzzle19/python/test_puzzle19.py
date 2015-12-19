"""Tests for Day 19 Puzzle."""

import unittest
import puzzle19 as p19

class TestPuzzle19(unittest.TestCase):
    """Tests for Day 19 Puzzle."""

    def test_transform_molecule(self):
        """Tests for transform_molecule()"""
        transformations = {'H': ['HO', 'OH'], 'O': ['HH']}
        new_molecules = p19.transform_molecule('HOH', transformations)
        expected = set(['HOOH', 'HOHO', 'OHOH', 'HOOH', 'HHHH'])
        self.assertEquals(expected, new_molecules)

        new_molecules = p19.transform_molecule('HOHOHO', transformations)
        self.assertEquals(7, len(new_molecules))

        transformations = {'H': ['OO']}
        new_molecules = p19.transform_molecule('H2O', transformations)
        self.assertEquals(set(['OO2O']), new_molecules)

        transformations = {'Ti': ['BP', 'TiTi'], 'e': ['HF', 'NAl', 'OMg']}
        new_molecules = p19.transform_molecule('TieTi', transformations)
        print new_molecules
        self.assertEquals(7, len(new_molecules))

if __name__ == '__main__':
    unittest.main()
