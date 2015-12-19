"""Day 19 Puzzle"""

import collections

def transform_molecule(molecule, atomic_transformations):
    """
    Returns a Set of possible transformations
    of the given molecule, as a list of atoms,
    using the given dict of possible atomic
    transformations, where possible atomic
    transformations should be lists as well.
    """
    transformations = []
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
                transformations.append(possible_molecule)

        index = index + len(atom)

    return set(transformations)

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

def main():
    """Main application."""
    molecule, transformations = read_data()
    new_molecules = transform_molecule(molecule, transformations)
    print 'There are', len(new_molecules), 'different molecules', \
          'produced by one transformation.'

if __name__ == '__main__':
    main()
