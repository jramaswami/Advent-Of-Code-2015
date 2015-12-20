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
        self.assertEquals(7, len(new_molecules))

    def test_steps_to_build_molecule(self):
        """Tests for steps_to_build_molecule()"""
        transformations = {'e': ['H', 'O'], 'H': ['HO', 'OH'], 'O': ['HH']}
        self.assertEquals(3, p19.steps_to_build_molecule('HOH', \
                                                         transformations))
        self.assertEquals(6, p19.steps_to_build_molecule('HOHOHO', \
                                                         transformations))

    def test_reverse_transformations(self):
        """Tests for reverse_transformations()"""
        transformations = {'e': ['H', 'O'], 'H': ['HO', 'OH'], 'O': ['HH']}
        reverse = p19.reverse_transformations(transformations)
        self.assertIn('e', reverse['H'])
        self.assertIn('e', reverse['O'])
        self.assertIn('H', reverse['HO'])
        self.assertIn('H', reverse['OH'])
        self.assertIn('O', reverse['HH'])

    def test_steps_reverse_molecule(self):
        """Tests for reverse_engineer_molecule()"""
        transformations = {'e': ['H', 'O'], 'H': ['HO', 'OH'], 'O': ['HH']}
        reverse = p19.reverse_transformations(transformations)
        self.assertEquals(3, p19.steps_to_reverse_molecule('HOH', reverse))
        self.assertEquals(6, p19.steps_to_reverse_molecule('HOHOHO', reverse))

    def test_random_choice(self):
        """Tests for trials()"""
        transformations = {'e': ['H', 'O'], 'H': ['HO', 'OH'], 'O': ['HH']}
        self.assertEquals(3, p19.trials('HOH', transformations))
        self.assertEquals(6, p19.trials('HOHOHO', transformations))

    def test_greedy_reversal(self):
        """Tests for greedy_reversal()"""
        transformations = {'e': ['H', 'O'], 'H': ['HO', 'OH'], 'O': ['HH']}
        reverse = p19.reverse_transformations(transformations)
        self.assertEquals(3, p19.greedy_reversal('HOH', reverse))
        self.assertEquals(6, p19.greedy_reversal('HOHOHO', reverse))

if __name__ == '__main__':
    unittest.main()
