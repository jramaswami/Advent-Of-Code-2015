"""Day 8 Puzzle"""

DEBUG = False

def log(*messages):
    """Prints debug messages to console if DEBUG == True."""
    if DEBUG:
        for msg in messages:
            print msg,
        print

def encode(chars):
    """Encodes characters."""
    return '"' + chars.replace("\\", "\\\\").replace('"', '\\"') + '"'

def count_chars(line):
    """Counts chars in line after applying escape sequences."""
    char_count = 0
    index = 0
    while index < len(line):
        if line[index] == '\\':
            # escape sequence
            if line[index + 1] == 'x':
                # hex escape sequence; increment count
                char_count = char_count + 1
                # then move to end of escape sequence
                index = index + 4
            else:
                # either \\ or \"; increment count
                char_count = char_count + 1
                # then move to end of escape sequence
                index = index + 2
        elif line[index] == '"':
            # do not count quotes; just move on
            index = index + 1
        else:
            # normal character, increment count
            char_count = char_count + 1
            # move to next char
            index = index + 1
    log('Line', line, 'has', char_count, 'characters', \
        'from', len(line), 'of code.')
    return char_count

def main():
    """Main."""
    with open('../input.txt', 'r') as input_file:
        total_chars = 0
        total_code = 0
        total_encoded = 0
        for line in input_file:
            total_chars = total_chars + count_chars(line.strip())
            total_code = total_code + len(line.strip())
            total_encoded = total_encoded + len(encode(line.strip()))
    print 'The code - chars is:', total_code - total_chars
    print 'The encoded - code is:', total_encoded - total_code

if __name__ == '__main__':
    main()
