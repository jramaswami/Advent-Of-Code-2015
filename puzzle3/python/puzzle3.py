"""Day 3 Puzzle"""

def move(location, vector):
    """Function to add vector to given location to move santa or robot."""
    return tuple([(location[0] + vector[0]), (location[1] + vector[1])])

def direction_to_vector(direction):
    """Function to turn character direction into a vector."""
    if direction == '<':
        return [-1, 0]
    elif direction == '>':
        return [1, 0]
    elif direction == 'v':
        return [0, -1]
    elif direction == '^':
        return [0, 1]
    else:
        return [0, 0]

def deliver_present(houses, location):
    """Deliver a present to the house at the given location."""
    if location in houses:
        houses[location] = houses[location] + 1
    else:
        houses[location] = 1

def santa_alone_delivers(input_string):
    """
    Determine the number of houses that receive a present
    when santa delivers alone.
    """
    current_location = (0, 0)
    houses_with_presents = {}
    deliver_present(houses_with_presents, current_location)
    for direction in input_string:
        vector = direction_to_vector(direction)
        current_location = move(current_location, vector)
        deliver_present(houses_with_presents, current_location)
    return len(houses_with_presents)

def santa_with_robot_delivers(input_string):
    """
    Determine the number of houses that receive a present
    when santa delivers along with the robot.
    """

    santa_location = (0, 0)
    robot_location = (0, 0)
    deliverer = 'santa'

    houses_with_presents = {}
    deliver_present(houses_with_presents, santa_location)
    for direction in input_string:
        vector = direction_to_vector(direction)
        if deliverer == 'santa':
            deliverer = 'robot'
            santa_location = move(santa_location, vector)
            deliver_present(houses_with_presents, santa_location)
        else:
            deliverer = 'santa'
            robot_location = move(robot_location, vector)
            deliver_present(houses_with_presents, robot_location)

    return len(houses_with_presents)


def process_input_file(file_name, process_to_apply):
    """Process the input file for the answer to the puzzle."""
    input_file = open(file_name, 'r')
    input_string = input_file.read()
    input_file.close()
    return process_to_apply(input_string)

if __name__ == '__main__':
    print 'Santa alone delivers', \
          process_input_file('../input.txt', santa_alone_delivers), \
          'presents.'
    print 'Santa and the robot deliver', \
          process_input_file('../input.txt', santa_with_robot_delivers), \
          'presents.'

