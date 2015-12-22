"""Day 22 Puzzle"""

import magic
import strategy
import rpg
import copy

def dfs(spell_list, player, boss, effects, accumulator, winners, losers):
    """Depth first search with backtracking."""
    for spell in spell_list:
        if rpg.spell_can_be_cast(spell, player, effects):
            # copy objects
            player_clone = copy.copy(player)
            boss_clone = copy.copy(boss)
            effects_clone = copy.deepcopy(effects)
            accumulator = list(accumulator)

            # simulate combat
            rpg.simulate_combat_round(player_clone, boss_clone,
                                      effects_clone, spell)

            if boss_clone.is_dead():
                # win, record it and then pop up to next level
                accumulator.append(spell)
                winners.append(accumulator)

            if player_clone.is_dead():
                # backtrack and try again
                accumulator.append(spell)
                losers.append(accumulator)

            # if boss and player are alive, continue on one level down
            dfs(spell_list, player, boss, effects, \
                accumulator, winners, losers)


class SpellBattle(object):
    """A spell battle."""
    def __init__(self, spell_list, player, boss, effects, result=0):
        self.spell_list = spell_list
        self.result = result
        self.effects = []
        self.player = player
        self.boss = boss

    def add_spell(self, spell):
        """Add a spell."""
        self.spell_list.append(spell)

    def simulate_combat_round(self):
        """Simulate a round of combat."""
        rpg.simulate_combat_round(self.player, self.boss, \
                                  self.effects, self.spell_list[-1])
        if self.boss.is_dead():
            return 1
        elif self.player.is_dead():
            return -1
        else:
            return 0

def dfs_iterative(spell_list, player, boss):
    """Depth first iteratively."""
    stack = []
    winners = []
    losers = []
    for spell in spell_list:
        stack.append(SpellBattle([spell], player, boss, []))

    while len(stack) > 0:
        spell_battle = stack.pop()
        result = spell_battle.simulate_combat_round()
        if result == 1:
            # winner
            winners.append(spell_battle.spell_list)
        elif result == -1:
            # loser
            losers.append(spell_battle.spell_list)
        else:
            for spell in spell_list:
                if rpg.spell_can_be_cast(spell, spell_battle.player, \
                        spell_battle.effects):
                    new_spell_battle = copy.deepcopy(spell_battle)
                    new_spell_battle.add_spell(spell)
                    stack.append(new_spell_battle)
    return winners, losers

def monte_carlo(limit):
    """Monte Carlo simulation of random spells."""
    import sys

    min_cost = 999999999999999999
    min_spell_list = []

    for dummy_index in range(limit):
        boss = rpg.Character('Boss', hit_points=71, damage=10)
        player = rpg.Character('Player', hit_points=50, mana=500)
        spell_list = strategy.RandomSpellList(magic.SpellBook())
        result = rpg.simulate_combat(player, boss, spell_list)

        if result == 1:
            print
            print spell_list.cost, spell_list.spells_cast
            if spell_list.cost < min_cost:
                min_cost = spell_list.cost
                min_spell_list = spell_list.spells_cast
            print
        else:
            if dummy_index % 1000 == 0:
                print dummy_index
                print spell_list.spells_cast
            else:
                print '.',
            sys.stdout.flush()

    return min_cost, min_spell_list

def main():
    """Main program."""
    # Random
    # min_cost, min_spell_list = monte_carlo(100000)
    # print "Best spell list:", min_spell_list
    # print "Minimum cost is:", min_cost

    # Max Cost
    # boss = Character('Boss', hit_points=71, damage=10)
    # player = Character('Player', hit_points=50, mana=500)
    # spell_list = strategy.MaxCostSpellList(magic.SpellBook())
    # result = simulate_combat(player, boss, spell_list)
    # print "*" * 80
    # print 'MAX COST SPELL:'
    # if result == 1:
        # print 'Player wins!'
    # else:
        # print 'Player loses.'
    # print boss, player

    # Max Damage
    # boss = Character('Boss', hit_points=71, damage=10)
    # player = Character('Player', hit_points=50, mana=500)
    # spell_list = strategy.MaxDamageSpellList(magic.SpellBook())
    # result = simulate_combat(player, boss, spell_list)
    # print "*" * 80
    # print 'MAX DAMAGE SPELL:'
    # if result == 1:
        # print 'Player wins!'
    # else:
        # print 'Player loses.'
    # print boss, player

    # Shields Up
    # boss = Character('Boss', hit_points=71, damage=10)
    # player = Character('Player', hit_points=50, mana=500)
    # spell_list = strategy.ShieldsUpSpellList(magic.SpellBook())
    # result = simulate_combat(player, boss, spell_list)
    # print "*" * 80
    # print 'SHIELDS UP'
    # if result == 1:
        # print 'Player wins!'
    # else:
        # print 'Player loses.'
    # print boss, player

    spell_list = ['Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge']
    boss = rpg.Character('Boss', hit_points=71, damage=10)
    player = rpg.Character('Player', hit_points=50, mana=500)
    winners, losers = dfs_iterative(spell_list, player, boss)
    print 'winners:\n'
    for item in winners:
        print item

if __name__ == "__main__":
    main()
