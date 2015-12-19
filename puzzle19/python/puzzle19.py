"""Day 19 Puzzle"""

def transform_molecule(molecule, atomic_transformations):
    """
    Returns a Set of possible transformations
    of the given molecule using the given dict
    of possible atomic transformations.
    """
    transformations = []
    for index in range(len(molecule)):
        atom = molecule[index]

        if atom not in atomic_transformations:
            continue

        for new_atom in atomic_transformations[atom]:
            possible_molecule = molecule[:index] + new_atom + molecule[index + 1:]
            transformations.append(possible_molecule)

    return set(transformations)

def main():
    """Main application."""
    pass

if __name__ == '__main__':
    main()
