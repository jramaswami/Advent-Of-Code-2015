"""Day 13 puzzle"""

import re
import itertools

def find_happiest_arrangement(scored_arrangments):
    """Returns arrangement with max happiness"""
    max_score = 0
    max_arrangement = None
    for arrangement, score in scored_arrangments.items():
        if max_arrangement == None:
            max_score = score
            max_arrangement = arrangement
        elif score > max_score:
            max_score = score
            max_arrangment = arrangement
    return max_arrangment

def swap_pair(pair):
    """Returns pair with items swapped."""
    return (pair[1], pair[0])

def get_happiness_score(pair, happiness):
    """Returns the happiness score of the given pair."""
    if pair in happiness:
        return happiness[pair]
    else:
        raise Exception(str(pair) + ' has no happiness score.')

def score_seating_arrangements(arrangements, happiness):
    """Scores the seating arrangments."""
    seating_scores = {}
    for arrangement in arrangements:
        score = 0
        for index in range(len(arrangement)):
            if index == len(arrangement) - 1:
                score += get_happiness_score((arrangement[index], \
                                              arrangement[0]), \
                                              happiness)
                score += get_happiness_score((arrangement[0], \
                                              arrangement[index]), \
                                              happiness)
            else:
                score += get_happiness_score((arrangement[index], \
                                              arrangement[index + 1]), \
                                              happiness)
                score += get_happiness_score((arrangement[index + 1], \
                                              arrangement[index]), \
                                              happiness)
        seating_scores[arrangement] = score
    return seating_scores

def possible_seating_arrangements(people):
    """Returns list of possible seating arrangments."""
    arrangements = [arr for arr in itertools.permutations(people)]
    return arrangements

def load_input_file(file_name):
    """Loads input file."""
    happiness = {}
    people = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            tokens = re.split(r'\s+', line.strip())
            left = tokens[0]
            right = tokens[-1][:-1] # strip of trailing '.'
            units = int(tokens[3])
            coefficient = -1 if tokens[2] == 'lose' else 1
            happiness[(left, right)] = units * coefficient
            if left not in people:
                people.append(left)
    return happiness, set(people)

def main():
    """Main program."""
    happiness, people = load_input_file('../input.txt')
    arrangements = possible_seating_arrangements(people)
    scored_arrangements = score_seating_arrangements(arrangements, happiness)
    happiest_arrangement = find_happiest_arrangement(scored_arrangements)
    print 'Max happiness change is', scored_arrangements[happiest_arrangement]

    # Part 2
    # Add zero happiness score for me and each person
    for person in people:
        happiness[('Joseph', person)] = 0
        happiness[(person, 'Joseph')] = 0
    # Add me to list of people
    people = list(people)
    people.append('Joseph')
    people = set(people)
    arrangements = possible_seating_arrangements(people)
    scored_arrangements = score_seating_arrangements(arrangements, happiness)
    happiest_arrangement = find_happiest_arrangement(scored_arrangements)
    print 'Max happiness change with me is', scored_arrangements[happiest_arrangement]

if __name__ == '__main__':
    main()
