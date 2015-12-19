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
        new_molecule = p19.transform_molecule('H2O', transformations)
        self.assertEquals(set(['OO2O']), new_molecule)

        # Same tests after string to list
        transformations = {'H': ['HO', 'OH'], 'O': ['HH']}
        molecule = p19.molecule_string_to_list('HOH')
        new_molecules = p19.transform_molecule(molecule, transformations)
        expected = set(['HOOH', 'HOHO', 'OHOH', 'HOOH', 'HHHH'])
        self.assertEquals(expected, new_molecules)

        molecule = p19.molecule_string_to_list('HOHOHO')
        new_molecules = p19.transform_molecule(molecule, transformations)
        self.assertEquals(7, len(new_molecules))

        transformations = {'H': ['OO']}
        molecule = p19.molecule_string_to_list('H2O')
        new_molecule = p19.transform_molecule(molecule, transformations)
        self.assertEquals(set(['OO2O']), new_molecule)

    def test_molecule_string_to_list(self):
        """Tests for molecule_string_to_list()"""
        self.assertEquals(['H', 'O', 'H'], p19.molecule_string_to_list("HOH"))
        self.assertEquals(['H', 'O', 'H', 'O', 'H', 'O'], \
                          p19.molecule_string_to_list("HOHOHO"))

if __name__ == '__main__':
    unittest.main()
