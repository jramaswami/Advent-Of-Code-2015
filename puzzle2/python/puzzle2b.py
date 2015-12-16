"""Day 2 Puzzle, Part 2"""

def ribbon_required_around_box(dimensions):
    """
    Determine the amount of ribbon to go around the box
    by choosing the side with the smallest perimeter.
    """
    possible_perimeters = []
    for index in range(len(dimensions)):
        first = index
        second = index + 1
        if second >= len(dimensions):
            second = 0
        possible_perimeters.append((2 * dimensions[first]) + \
                                   (2 * dimensions[second]))
    return min(possible_perimeters)

def ribbon_required_for_box(box):
    """Determine ribbon required to wrap box."""
    # Split string into list of dimensions.
    dimensions = [int(dim) for dim in box.split('x')]
    height, length, width = dimensions
    # Find the number of feet of ribbon to wrap the
    # smallest perimeter of the box.
    feet_required = ribbon_required_around_box(dimensions)
    # Now determine the extra needed for the bow.
    feet_required = feet_required + (length * width * height)
    return feet_required

def process_box_list(box_list):
    """Processes a list of boxes to determine total space required."""
    total_ribbon_required = 0
    for box in box_list:
        total_ribbon_required = total_ribbon_required + \
                                ribbon_required_for_box(box)
    return total_ribbon_required

def process_input_file(file_name):
    """Turns input file into a list of box dimensions."""
    input_file = open(file_name, 'r')
    box_list = []
    for line in input_file:
        box_list.append(line.strip())
    return process_box_list(box_list)

if __name__ == '__main__':
    print process_input_file('../input.txt')

