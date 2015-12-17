"""Day 17 Puzzle"""

import itertools

def select_smallest_combinations(combos):
    """Filters by smallest combinations"""
    min_length = find_min_length(combos)
    return [c for c in combos if len(c) == min_length]

def find_min_length(combos):
    """Find the smallest length of combos."""
    min_length = 20
    for combo in combos:
        if len(combo) < min_length:
            min_length = len(combo)
    return min_length

def filter_combinations(combos, target):
    """Filter combinations."""
    return [c for c in combos if sum(c) == target]

def container_combinations(containers):
    """Returns combinations of the containers."""
    combos = []
    for index in range(1, len(containers)):
        combos.extend(itertools.combinations(containers, index))
    return combos

def load_file(file_name):
    """Loads data from file and returns it as a list."""
    with open(file_name) as input_file:
        data = [int(line.strip()) for line in input_file]
    return data

def main():
    """Main program."""
    containers = load_file('../input.txt')
    combos = container_combinations(containers)
    combos_150 = [f for f in filter_combinations(combos, 150)]
    print "There are", len(combos_150), "possible combinations that", \
          "add up to 150."
    small_combos = select_smallest_combinations(combos_150)
    print "There are", len(small_combos), "combinations of length", \
            len(small_combos[0])

if __name__ == '__main__':
    main()
