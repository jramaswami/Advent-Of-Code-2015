"""Tests for Day 21 Puzzle."""

import unittest
import puzzle21 as p21

class TestPuzzle21(unittest.TestCase):
    """Tests for Day 21 Puzzle."""

    def test_combat_simulation(self):
        """
        Tests for simulate_combat()
        and simulate_combat_turn()
        """
        # simulate_combat_turn()
        player = {'Hit Points': 8, 'Damage': 5, 'Armor': 5}
        boss = {'Hit Points': 12, 'Damage': 7, 'Armor': 2}
        p21.simulate_combat_turn(player, boss)
        self.assertEquals(9, boss['Hit Points'])
        p21.simulate_combat_turn(boss, player)
        self.assertEquals(6, player['Hit Points'])
        p21.simulate_combat_turn(player, boss)
        self.assertEquals(6, boss['Hit Points'])
        p21.simulate_combat_turn(boss, player)
        self.assertEquals(4, player['Hit Points'])
        p21.simulate_combat_turn(player, boss)
        self.assertEquals(3, boss['Hit Points'])
        p21.simulate_combat_turn(boss, player)
        self.assertEquals(2, player['Hit Points'])
        p21.simulate_combat_turn(player, boss)
        self.assertEquals(0, boss['Hit Points'])

        # simulate_combat
        player = {'Hit Points': 8, 'Damage': 5, 'Armor': 5}
        boss = {'Hit Points': 12, 'Damage': 7, 'Armor': 2}
        result = p21.simulate_combat(player, boss)
        self.assertEquals(1, result)
        self.assertEquals(2, player['Hit Points'])
        self.assertEquals(0, boss['Hit Points'])

if __name__ == '__main__':
    unittest.main()
