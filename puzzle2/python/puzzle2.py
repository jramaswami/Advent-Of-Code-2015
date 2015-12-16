"""Day 2 Puzzle, Part 1"""

def extra_required(dimensions):
    """Determine the smallest side which is the required extra."""
    possible_extras = []
    for index in range(len(dimensions)):
        first = index
        second = index + 1
        if second >= len(dimensions):
            second = 0
        possible_extras.append(dimensions[first] * dimensions[second])
    return min(possible_extras)

def square_feet_for_box(box):
    """Returns the square feet required for given box."""
    dimensions = [int(dim) for dim in box.split('x')]
    # first determine surface area
    height, length, width = dimensions
    square_feet_required = (2 * length * width) + \
                           (2 * width * height) + \
                           (2 * height * length)
    return square_feet_required + extra_required(dimensions)

def process_box_list(box_list):
    """Processes a list of boxes to determine total space required."""
    total_square_feet = 0
    for box in box_list:
        total_square_feet = total_square_feet + square_feet_for_box(box)
    return total_square_feet

def process_input_file(file_name):
    """Turns input file into a list of box dimensions."""
    input_file = open(file_name, 'r')
    box_list = []
    for line in input_file:
        box_list.append(line.strip())
    return process_box_list(box_list)

if __name__ == '__main__':
    print process_input_file('../input.txt')
