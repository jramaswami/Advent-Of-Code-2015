"""Day 16 Puzzle"""

import copy

def auntie_filter(aunt, key, value):
    """Filter for list of aunties"""
    if key not in aunt[1]:
        return True
    if key in aunt[1]:
        if aunt[1][key] == value:
            return True
        else:
            return False

def retroencabulator_filter(aunt, key, value):
    """
    New filter to wrap around old filter to account for the
    fact that the MFCSAM is a retroencabulator.
    """
    if key in ('cats', 'trees') and key in aunt[1]:
        if aunt[1][key] > value:
            return True
        else:
            return False
    elif key in ('pomeranians', 'goldfish') and key in aunt[1]:
        if aunt[1][key] < value:
            return True
        else:
            return False
    else:
        return auntie_filter(aunt, key, value)

def clean_number(number):
    """Cleans up the number in the aunt's properties."""
    if number.find(',') >= 0:
        number = number[:-1]
    return int(number)

def main():
    """Main program."""
    aunts = []
    with open('../input.txt', 'r') as input_file:
        for line in input_file:
            tokens = line.strip().split()
            props = []
            for index in range(2, len(tokens), 2):
                props.append((tokens[index][:-1], clean_number(tokens[index+1])))
            aunts.append((int(tokens[1][:-1]), dict(props)))

    retro_aunts = copy.deepcopy(aunts)

    search = [('children', 3), ('cats', 7), ('samoyeds', 2),
              ('pomeranians', 3), ('akitas', 0), ('vizslas', 0),
              ('goldfish', 5), ('trees', 3), ('cars', 2),
              ('perfumes', 1)]
    for item in search:
        aunts = [aunt for aunt in aunts if auntie_filter(aunt, item[0], item[1])]
    if len(aunts) == 1:
        print 'Aunt Sue #', aunts[0][0], 'gave you the gift.'
    else:
        print 'Oops!'
        print aunts

    for item in search:
        retro_aunts = [aunt for aunt in retro_aunts \
                       if retroencabulator_filter(aunt, item[0], item[1])]
    if len(retro_aunts) == 1:
        print 'Aunt Sue #', retro_aunts[0][0], ' really gave you the gift.'
    else:
        print 'Oops!'
        print retro_aunts

if __name__ == '__main__':
    main()
