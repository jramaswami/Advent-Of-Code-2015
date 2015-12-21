"""Day 9 Puzzle"""

import itertools

def calculate_distance(route, distances):
    """Calculates distance for route using dict of distances between cities."""
    total_distance = 0
    for index in range(len(route) - 1):
        # Get distance from distances dict
        # Remember key could be reversed
        key = tuple([route[index], route[index + 1]])
        if key not in distances:
            key = tuple([route[index + 1], route[index]])
            if key not in distances:
                raise Exception("Unable to find distance for " + key)
        total_distance = total_distance + distances[key]
    return total_distance

def process_file(file_name):
    """Process input file."""
    cities = []
    distances = {}
    with open(file_name) as input_file:
        for line in input_file:
            line = line.strip()
            tokens = line.split(' ')
            if tokens[0] not in cities:
                cities.append(tokens[0])
            if tokens[2] not in cities:
                cities.append(tokens[2])
            if tuple([tokens[0], tokens[2]]) not in distances:
                distances[tuple([tokens[0], tokens[2]])] = int(tokens[-1])

    cities = set(cities)

    shortest_route = None
    shortest_distance = 0
    longest_route = None
    longest_distance = 0
    for route in itertools.permutations(cities, len(cities)):
        distance = calculate_distance(route, distances)
        # Initialize when there isn't a value
        if shortest_route == None:
            shortest_route = route
            shortest_distance = distance
        if longest_route == None:
            longest_route = route
            longest_distance = distance
        if distance < shortest_distance:
            shortest_route = route
            shortest_distance = distance
        if distance > longest_distance:
            longest_route = route
            longest_distance = distance

    print 'Shortest distance is', "->".join(shortest_route), \
          '@', shortest_distance
    print 'Longest distance is', "->".join(longest_route), \
          '@', longest_distance

def main():
    """Main program."""
    process_file('../input.txt')

if __name__ == '__main__':
    main()
