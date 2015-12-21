"""Day 21 Puzzle."""

import collections
import re
import itertools as it
import operator
import copy

def simulate_combat_turn(attacker, defender, verbose=False):
    """Simulates a single turn of combat."""
    defender['Hit Points'] -= (attacker['Damage'] - defender['Armor'])
    if verbose:
        print attacker['Name'], 'attacks', defender['Name'], \
              'for', attacker['Damage'], '; ', defender['Name'], \
              'now has', defender['Hit Points']

def simulate_combat(player, boss, verbose=False):
    """
    Simulate combat between player and boss.
    Returns 1 if player wins.  Returns 0 if boss wins.
    """
    while boss['Hit Points'] > 0 and player['Hit Points'] > 0:
        # player attacks first
        simulate_combat_turn(player, boss, verbose)
        if boss['Hit Points'] <= 0:
            return 1

        # boss attacks second
        simulate_combat_turn(boss, player, verbose)
        if player['Hit Points'] <= 0:
            return 0

def get_ring_combinations(store, max_rings=2):
    """
    Returns the list of ring combinations up
    to the maximum number of rings.
    """
    rings = [t for t in store['Rings'].values()]
    ring_combos = []
    for index in range(1, max_rings + 1):
        ring_combos.extend([c for c in it.combinations(rings, index)])
    # Add the possiblity of having no rings
    ring_combos.append(({'Name': 'No Rings', 'Cost': 0,
                         'Damage': 0, 'Armor': 0}, ))
    return ring_combos

def possible_loadouts(store):
    """Returns list of possible player loadouts."""
    # First add possibility of having no armor
    store['Armor']['No Armor'] = {'Name': 'No Armor', 'Cost': 0,
                                  'Damage': 0, 'Armor': 0}
    loadouts = []
    for dummy_key, weapon in store['Weapons'].items():
        for dummy_key, armor in store['Armor'].items():
            for ring_combo in get_ring_combinations(store, 2):
                # build items
                items = [weapon, armor]
                for ring in ring_combo:
                    items.append(ring)

                cost = sum([t['Cost'] for t in items])
                damage = sum([t['Damage'] for t in items])
                defense = sum([t['Armor'] for t in items])
                names = [t['Name'] for t in items]
                loadout = {'Items': names, 'Cost': cost, \
                               'Damage': damage, 'Armor': defense}
                loadouts.append(loadout)
    return loadouts

def read_store_data():
    """Reads and returns store data as dict."""
    store = collections.defaultdict(dict)
    with open('../store.txt', 'r') as input_file:
        current_category = ''
        properties = []
        splitp = re.compile(r'\s{2,}')

        for line in input_file:
            line = line.strip()
            if line == '':
                # blank line
                pass
            elif line.find(':') >= 0:
                # title line
                tokens = splitp.split(line)
                current_category = tokens[0][:-1]
                properties = ['Name']
                properties.extend(tokens[1:])
            else:
                # item line
                tokens = splitp.split(line)
                item_dict = {}
                for index in range(len(tokens)):
                    if index != 0:
                        item_dict[properties[index]] = int(tokens[index])
                    else:
                        item_dict[properties[index]] = tokens[index]
                store[current_category][tokens[0]] = item_dict
    return store

def read_boss_data():
    """Reads boss data and returns boss as a dict"""
    boss = {}
    with open('../boss.txt', 'r') as input_file:
        for line in input_file:
            tokens = line.split(':')
            boss[tokens[0]] = int(tokens[1].strip())
    return boss

def main():
    """Main program."""
    store = read_store_data()
    boss_master_copy = read_boss_data()
    boss_master_copy['Name'] = 'boss'
    loadouts = sorted(possible_loadouts(store), \
                      key=operator.itemgetter('Cost'))

    min_win_loadout = []
    max_lose_loadout = []

    for loadout in loadouts:
        boss = copy.deepcopy(boss_master_copy)
        player = {'Hit Points': 100, 'Name' : 'player'}
        player['Armor'] = loadout['Armor']
        player['Damage'] = loadout['Damage']
        winner = simulate_combat(player, boss, verbose=False)
        if winner == 1 and min_win_loadout == []:
            min_win_loadout = loadout
        elif winner == 0:
            max_lose_loadout = loadout

    print 'Winner with the least cost', min_win_loadout['Cost'], \
          ':', min_win_loadout['Items']
    print 'Loser with the most cost', max_lose_loadout['Cost'], \
          ':', max_lose_loadout['Items']

if __name__ == '__main__':
    main()
