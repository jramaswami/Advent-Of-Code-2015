"""Day 19 Puzzle"""

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

def main():
    """Main application."""
    pass

if __name__ == '__main__':
    main()
