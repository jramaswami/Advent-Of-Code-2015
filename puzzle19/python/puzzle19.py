"""Day 19 Puzzle"""

from __future__ import print_function

import collections
import random

def transform_molecule(molecule, atomic_transformations):
    """
    Returns a Set of possible transformations
    of the given molecule, as a list of atoms,
    using the given dict of possible atomic
    transformations, where possible atomic
    transformations should be lists as well.
    """
    transformations = set([])
    index = 0
    while index < len(molecule):
        atom = molecule[index]
        if index < len(molecule) - 1:
            # for some reason 'e' is an atom were every other
            # atom is a cap or a cap + a lower
            if molecule[index + 1] in 'abcdfghijklmnopqrstuvwxyz':
                atom = atom + molecule[index + 1]

        if atom in atomic_transformations:
            for new_atom in atomic_transformations[atom]:
                possible_molecule = molecule[:index] + new_atom \
                                  + molecule[index + len(atom):]
                transformations.add(possible_molecule)

        index = index + len(atom)

    return transformations

def read_data():
    """
    Reads data file and returns molecule as string and
    dictionary of transformations.
    """
    with open('../input.txt', 'r') as input_file:
        lines = input_file.readlines()

    molecule = lines[-1].strip()
    transformations = collections.defaultdict(list)
    for line in lines[:-2]:
        line = line.strip()
        atom, transformation = line.split(' => ')
        transformations[atom].append(transformation)

    return molecule, transformations

def steps_to_build_molecule(target_molecule, transformations, limit=100):
    """
    Returns the minimum number of steps to
    build target molecule.
    """
    steps = 0
    new_molecules = set(['e'])
    for steps in range(1, limit):
        # print("\n", steps, ':', len(new_molecules), 'molecules ...\n')
        temp = set([])
        for molecule in new_molecules:
            # print('.', end="")
            for possible_molecule in transform_molecule(molecule, transformations):
                # Did we find a match?
                if target_molecule == possible_molecule:
                    return steps
                # Don't add the possible molecule to the list of possibles
                # if it is longer than the target molecule because the
                # there are no transformations that reduce the size of the
                # molecule.
                if len(possible_molecule) <= len(target_molecule):
                    temp.add(possible_molecule)
        new_molecules = set(temp)

        # If all the possible molecules have extended past
        # the length of the target molecule so that we
        # are out of new molecules, return -1.
        if len(new_molecules) == 0:
            return -1

    # We fell out without finding the target molecule
    # so return -1.
    return -1

def reverse_transformations(transformations):
    """Returns a dict with the transformations reversed."""
    reverse = collections.defaultdict(list)
    for key, value_list in transformations.items():
        for value in value_list:
            reverse[value].append(key)
    return reverse

def steps_to_reverse_molecule(target_molecule, reverse, limit=100):
    """Returns number of steps required to reverse engineer molecule."""
    new_molecules = set([target_molecule])
    for step in range(1, limit):
        # print('Step', step, ':', len(new_molecules), 'molecules.')
        temp = set([])
        for atom in reverse.keys():
            # print(str(atom), end="")
            for molecule in new_molecules:
                start = 0
                index = molecule.find(atom, start)
                while start < len(molecule) and index >= 0:
                    for reversal in reverse[atom]:
                        new_molecule = molecule[:index] + reversal \
                                     + molecule[index + len(atom):]
                    if new_molecule == 'e':
                        return step

                    # Don't add any molecules that have 'e' in
                    # them.  The only 'e' molecule is the
                    # beginning, a single 'e'.
                    if new_molecule.find('e') < 0:
                        temp.add(new_molecule)
                        # print(new_molecule)

                    start = index + len(atom)
                    index = molecule.find(atom, start)
        # print("\n")
        new_molecules = temp

    return -1

def random_transformation(molecule, transformations):
    """Returns a random transformation of the molecule."""
    possible_molecules = transform_molecule(molecule, transformations)
    return random.choice(list(possible_molecules))

def trials(target_molecule, transformations, success_limit=5):
    """Returns number of steps required through random choice."""
    molecule = 'e'
    steps = 0
    n_trials = 0
    successful_trials = 0
    min_steps = -1
    while molecule != target_molecule:

        steps = steps + 1
        possible_molecules = transform_molecule(molecule, transformations)

        if target_molecule in possible_molecules:
            successful_trials += 1
            print('Successful trial', successful_trials, ':', steps)

            if successful_trials == success_limit:
                return min_steps

            if min_steps == -1:
                min_steps = steps
            elif steps < min_steps:
                min_steps = steps

            molecule = 'e'
            steps = 0
            n_trials = 0

        else:
            molecule = random.choice(list(possible_molecules))
            if len(molecule) > len(target_molecule):
                n_trials = n_trials + 1
                # print("Print starting over", n_trials, "...")
                molecule = 'e'
                steps = 0
    return steps

def greedy_reversal(target_molecule, reverse):
    """Returns number of steps required to reverse engineer molecule."""
    reverse_atoms = sorted(reverse.keys(), key=len, reverse=True)
    molecule = target_molecule

    steps = 0
    while molecule != 'e':
        atom = None
        for atom in reverse_atoms:
            index = molecule.find(atom)
            if index >= 0:
                break

        if atom == None:
            return

        smallest_atom = sorted(reverse[atom], key=len)[0]
        while index >= 0:
            new_molecule = molecule.replace(atom, smallest_atom, 1)
            molecule = new_molecule
            steps = steps + 1
            index = molecule.find(atom)

    return steps

def main():
    """Main application."""
    molecule, transformations = read_data()
    new_molecules = transform_molecule(molecule, transformations)
    print('There are', len(new_molecules), 'different molecules', \
          'produced by one transformation.')

    # The forward method works in the tests but takes up too much
    # memory when I run it on my laptop, leading to system failure.
    # steps = steps_to_build_molecule(molecule, transformations, limit=1000)
    # print('There are', steps, 'to build the target molecule.')

    # Due to the memory requirements of the forward method, I tried
    # a different take, reversing the direction of the transformations.
    # Instead of working forward from 'e' to the target molecule,
    # I work backword from the target molecule to 'e'.
    # reverse = reverse_transformations(transformations)
    # steps = steps_to_reverse_molecule(molecule, reverse, limit=3)
    # print "There are", steps, "to get from 'e' to the target molecule."

    # Unable to get two above solutions, I'm resorting to random tries
    # steps = trials(molecule, transformations)
    # print('It took', steps, 'to produce target molecule.')

    reverse = reverse_transformations(transformations)
    steps = greedy_reversal(molecule, reverse)
    print('It took', steps, 'steps to produce target molecule using', \
          'a greedy algorithm.')



if __name__ == '__main__':
    main()
