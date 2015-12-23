"""Day 22 Puzzle"""

import magic
import strategy
import rpg

def dfs_iterative(master_spell_list, player, boss):
    """Depth first iteratively."""
    stack = []
    winners = []
    losers = []
    for spell in master_spell_list:
        stack.append([spell])

    while len(stack) > 0:
        # get spell list for battle
        battle_spell_list = stack.pop()

        # reset characters and effects
        player.reset()
        boss.reset()
        effects = []

        # simulate the combat
        result = rpg.simulate_combat(player, boss, \
                                     iter(battle_spell_list), effects)

        if result == 1:
            # winner
            cost = sum([player.spell_book.get_spell_cost(s) \
                        for s in battle_spell_list])
            winners.append((battle_spell_list, cost))
            print 'Winner(', cost, '):', battle_spell_list
        elif result == -1:
            # loser
            print 'Loser:', battle_spell_list
            losers.append(battle_spell_list)
        else:
            # combat not resolved
            for spell in master_spell_list:
                if rpg.spell_can_be_cast(spell, player, effects):
                    new_battle_spell_list = list(battle_spell_list)
                    new_battle_spell_list.append(spell)
                    stack.append(new_battle_spell_list)
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
    spell_list = ['Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge']
    spell_list.reverse()
    boss = rpg.Character('Boss', hit_points=71, damage=10)
    player = rpg.Character('Player', hit_points=50, mana=500)
    winners, dummy_losers = dfs_iterative(spell_list, player, boss)
    min_cost = 999999999
    min_spell_list = []
    for spell_list, cost in winners:
        if cost < min_cost:
            min_cost = cost
            min_spell_list = spell_list

    print "*" * 80
    print 'Best Spell List:', min_spell_list
    print 'Minimum Cost:', min_cost

if __name__ == "__main__":
    main()
