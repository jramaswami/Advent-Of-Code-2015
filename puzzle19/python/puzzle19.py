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
    for index in range(len(molecule)):
        atom = molecule[index]

        if atom not in atomic_transformations:
            continue

        for new_atom in atomic_transformations[atom]:
            possible_molecule = molecule[:index] + new_atom + molecule[index + 1:]
            transformations.append(possible_molecule)

    return set(transformations)

def molecule_string_to_list(molecule_string):
    """
    Takes a molecule in string form and
    returns it as a list of atoms.
    """
    molecule_list = []
    partial = ''
    # For each character in the string
    for character in molecule_string:
        # If the character is upper case then
        # it is a whole molecule
        if character == character.upper():
            if partial != '':
                # Add the previously partial atom,
                # now complete, to the list
                molecule_list.append(partial)
                # Start a new partial atom
                partial = character
            else:
                # This is the first character
                partial = character
        # If the character is lower case then
        # it is part of the partial atom
        else:
            partial += character

    # Don't forget to get the last partial atom
    # that was being built, now complete
    if partial:
        molecule_list.append(partial)

    return molecule_list

def main():
    """Main application."""
    pass

if __name__ == '__main__':
    main()
