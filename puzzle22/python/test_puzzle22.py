"""Tests for Day 22 Puzzle"""
import unittest
import rpg
import strategy

class TestPuzzle22(unittest.TestCase):
    """Test for Day 22 Puzzle"""

    def test_simulate_combat(self):
        """Tests for simulate_combat()"""
        rpg.VERBOSE = False

        if rpg.VERBOSE:
            print "*" * 30, 'Battle #1', "*" * 30
        player = rpg.Character('Player', hit_points=10, mana=250)
        boss = rpg.Character('Boss', hit_points=13, damage=8)
        spell_list = strategy.SpellList(['Poison', 'Magic Missile'])
        result = rpg.simulate_combat(player, boss, spell_list, {})
        # Player has 2 hit points, 0 armor, 24 mana
        self.assertEquals(player.hit_points, 2)
        self.assertEquals(player.armor, 0)
        self.assertEquals(player.mana, 24)

        # This kills the boss, and the player wins.
        self.assertTrue(boss.is_dead())
        self.assertFalse(player.is_dead())
        self.assertEquals(result, 1)

        if rpg.VERBOSE:
            print "*" * 30, 'Battle #2', "*" * 30
        player = rpg.Character('Player', hit_points=10, mana=250)
        boss = rpg.Character('Boss', hit_points=14, damage=8)
        spell_list = strategy.SpellList(['Recharge', 'Shield', 'Drain',
                                         'Poison', 'Magic Missile'])
        effects = {}
        result = rpg.simulate_combat(player, boss, spell_list, effects)
        self.assertEquals(result, 1)

    def test_simulate_combat_round(self):
        """Tests simulate_combat_round()"""
        rpg.VERBOSE = False

        player = rpg.Character('Player', hit_points=10, mana=250)
        boss = rpg.Character('Boss', hit_points=13, damage=8)
        effects = {}

        if rpg.VERBOSE:
            print "*" * 80

        # Player has 10 hit points, 0 armor, 250 mana
        self.assertEquals(player.hit_points, 10)
        self.assertEquals(player.armor, 0)
        self.assertEquals(player.mana, 250)
        # Boss has 13 hit points
        self.assertEquals(boss.hit_points, 13)

        rpg.simulate_combat_round(player, boss, effects, 'Poison')

        # Player has 2 hit points, 0 armor, 77 mana
        self.assertEquals(player.hit_points, 2)
        self.assertEquals(player.armor, 0)
        self.assertEquals(player.mana, 77)
        # Boss has 10 hit points
        self.assertEquals(boss.hit_points, 10)
        # Poison timer is now 4.
        self.assertEquals(effects['Poison'], 5)

        # Player casts Magic Missile
        rpg.simulate_combat_round(player, boss, effects, 'Magic Missile')

        # Player has 2 hit points, 0 armor, 24 mana
        self.assertEquals(player.hit_points, 2)
        self.assertEquals(player.armor, 0)
        self.assertEquals(player.mana, 24)
        # Poison its timer is now 3
        self.assertEquals(effects['Poison'], 3)
        # This kills the boss, and the player wins.
        self.assertTrue(boss.is_dead())
        self.assertFalse(player.is_dead())

if __name__ == "__main__":
    unittest.main()
