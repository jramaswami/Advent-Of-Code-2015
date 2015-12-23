"""Day 22 Puzzle"""

import tqdm
import magic
import rpg
import itertools

def do_permutations(choose):
    """Use permutations"""
    spell_list = ['Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge']
    boss = rpg.Character('Boss', hit_points=71, damage=10)
    player = rpg.Character('Player', hit_points=50, mana=500)

    possible_permutations = len(spell_list) ** choose
    permutations = itertools.product(spell_list, repeat=choose)
    tqdm_perms = tqdm.tqdm(permutations, total=possible_permutations)

    min_cost = 999999999
    winner = []

    for battle_spell_list in tqdm_perms:
        spell_cost = magic.score_spell_list(battle_spell_list)
        if spell_cost < min_cost:
            # simulate battle
            player.reset()
            boss.reset()
            effects = {}

            # simulate the combat
            try:
                result = rpg.simulate_combat(player, boss, \
                                             iter(battle_spell_list), \
                                             effects)
            except rpg.SpellCastingException:
                result = -1

            if result == 1:
                # winner
                min_cost = spell_cost
                winner = battle_spell_list
                # return min_cost, winner

    return min_cost, winner

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
                current_winner = battle_spell_list
                min_cost = cost
        elif result == -1:
            pass
        else:
            # combat not resolved
            for spell in master_spell_list:
                new_battle_spell_list = list(battle_spell_list)
                new_battle_spell_list.append(spell)
                # only bother to keep looking if it beats our current min
                if magic.score_spell_list(new_battle_spell_list) < min_cost:
                    stack.append(new_battle_spell_list)
    return current_winner, min_cost

def do_monte_carlo(limit):
    """Monte Carlo simulation of random spells."""
    import random

    spell_list = ['Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge']
    min_cost = 999999999999999999
    min_spell_list = []

    for dummy_index in tqdm.tqdm(range(limit)):
        boss = rpg.Character('Boss', hit_points=71, damage=10)
        player = rpg.Character('Player', hit_points=50, mana=500)
        effects = {}
        battle_spell_list = []
        next_spell = random.choice(spell_list)
        battle_spell_list.append(next_spell)
        try:
            result = rpg.simulate_combat(player, boss, \
                                         iter([next_spell]), effects)
        except rpg.SpellCastingException:
            result = -1
        while result == 0:
            next_spell = random.choice(spell_list)
            battle_spell_list.append(next_spell)
            try:
                result = rpg.simulate_combat(player, boss, \
                                             iter([next_spell]), effects)
            except rpg.SpellCastingException:
                result = -1

        if result == 1:
            spell_list_cost = magic.score_spell_list(battle_spell_list)
            if spell_list_cost < min_cost:
                min_cost = spell_list_cost
                min_spell_list = battle_spell_list

    return min_cost, min_spell_list

def do_dfs():
    """Does depth first search for solutions."""
    spell_list = ['Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge']
    boss = rpg.Character('Boss', hit_points=71, damage=10)
    player = rpg.Character('Player', hit_points=50, mana=500)
    return dfs_iterative(spell_list, player, boss)

def main():
    """Main program."""
    # Random
    # trials = 1000000
    # cost, winner = do_monte_carlo(trials)
    # print 'Random, easy mode,', trials, 'trials', cost, winner
    # rpg.HARDMODE = True
    # cost, winner = do_monte_carlo(trials)
    # print 'Random, hard mode,', trials, 'trials', cost, winner

    # choose = 12
    # cost, winner = do_permutations(choose)
    # print 'Permutations, easy mode,', cost, winner
    # rpg.HARDMODE = True
    # cost, winner = do_permutations(choose)
    # print 'Permutations, hard mode,', cost, winner

    cost, winner = do_dfs()
    print 'DFS, easy mode,', cost, winner
    rpg.HARDMODE = True
    cost, winner = do_dfs()
    print 'DFS, hard mode,', cost, winner

if __name__ == "__main__":
    main()
