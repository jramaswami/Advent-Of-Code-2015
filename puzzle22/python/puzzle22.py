"""Day 22 Puzzle"""

import magic
import strategy
import rpg

def dfs_iterative(master_spell_list, player, boss):
    """Depth first iteratively."""
    current_winner = None
    min_cost = 9999999999999
    stack = []
    for spell in master_spell_list:
        stack.append([spell])

    while len(stack) > 0:
        # get spell list for battle
        battle_spell_list = stack.pop()

        # reset characters and effects
        player.reset()
        boss.reset()
        effects = {}

        if magic.score_spell_list(battle_spell_list) < min_cost:
            # only simulate if the cost of the spells is less
            # than the current minimum
            try:
                # simulate the combat
                result = rpg.simulate_combat(player, boss, \
                                             iter(battle_spell_list), \
                                             effects)
            except rpg.SpellCastingException:
                result = -1
        else:
            result = -1

        if result == 1:
            # winner
            cost = magic.score_spell_list(battle_spell_list)
            if cost < min_cost:
                print 'Winner(', cost, '):', battle_spell_list
                current_winner = battle_spell_list
                min_cost = cost
        elif result == -1:
            # loser
            # print 'Loser:', battle_spell_list
            pass
        else:
            # combat not resolved
            for spell in master_spell_list:
                new_battle_spell_list = list(battle_spell_list)
                new_battle_spell_list.append(spell)
                # only bother to keep looking if it beats our current min
                if magic.score_spell_list(new_battle_spell_list) < min_cost:
                    stack.append(new_battle_spell_list)
        # print len(stack),
    return current_winner, min_cost

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
    spell_list = ['Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge']
    boss = rpg.Character('Boss', hit_points=71, damage=10)
    player = rpg.Character('Player', hit_points=50, mana=500)
    min_cost, winner = dfs_iterative(spell_list, player, boss)
    print "*" * 80
    print 'Best Spell List:', winner
    print 'Minimum Cost:', min_cost

    rpg.HARDMODE = True
    spell_list = ['Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge']
    boss = rpg.Character('Boss', hit_points=71, damage=10)
    player = rpg.Character('Player', hit_points=50, mana=500)
    min_cost, winner = dfs_iterative(spell_list, player, boss)
    print "*" * 80
    print 'Best Spell List in Hard Mode:', winner
    print 'Minimum Cost in Hard Mode:', min_cost

    # winner = ['Poison', 'Recharge', 'Shield', 'Poison', 'Recharge',
              # 'Shield', 'Poison', 'Recharge', 'Shield', 'Magic Missile',
              # 'Poison', 'Magic Missile']
    # rpg.VERBOSE = True
    # boss = rpg.Character('Boss', hit_points=71, damage=10)
    # player = rpg.Character('Player', hit_points=50, mana=500)
    # result = rpg.simulate_combat(player, boss, iter(winner), {})
    # if result == 1:
        # print 'Player wins!!!'


if __name__ == "__main__":
    main()
