"""Puzzle 1"""

def when_is_basement_entered(input_text):
    """
    Function to find when 'basement' is entered.
    That is, when the level reaches -1.
    """
    level = 0
    char_number = 0
    for char in input_text:
        char_number = char_number + 1
        if char == '(':
            level = level + 1
        elif char == ')':
            level = level - 1
        # Have we reached basement
        if level == -1:
            return char_number

    return None


def process_input_text(input_text):
    """
    Function to process an input string
    and determine what level Santa will
    be on at the end.
    """
    level = 0
    for char in input_text:
        if char == '(':
            level = level + 1
        elif char == ')':
            level = level - 1
    return level

def process_input_file(file_name, process_to_apply):
    """Process on input file."""
    input_file = open(file_name, 'r')
    result = process_to_apply(input_file.read())
    input_file.close()
    return result

if __name__ == '__main__':
    print 'input.txt produces level', \
          process_input_file('../input.txt', process_input_text)
    print 'input2.txt enters basement on char #', \
          process_input_file('../input2.txt', when_is_basement_entered)
