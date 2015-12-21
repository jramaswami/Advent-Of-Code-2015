"""Day 5 Puzzle"""

DEBUG = False

def log(*messages):
    """Function to print messages."""
    if DEBUG:
        for msg in messages:
            print msg,
        print

def string_is_nice2(string):
    """Determines if string qualifies as nice according to definition 2."""
    doublets = {}
    splits = 0
    index = 0
    while index < len(string) - 1:
        # doublets
        # if index > 1 \
        # and (string[index - 1] == string[index] == string[index + 1]):
            # # don't double count something like 'aaa'
            # pass
        # else:
            # if string[index:index+2] in doublets:
                # doublets[string[index:index+2]] += 1
            # else:
                # doublets[string[index:index+2]] = 1

        if string[index:index+2] in doublets:
            doublets[string[index:index+2]] += 1
        else:
            doublets[string[index:index+2]] = 1

        # move forward until we find a character that
        # isn't the same to avoid counting continuous
        # chars as doublets
        second_letter = string[min([index + 1, len(string) - 1])]
        third_letter = string[min([index + 2, len(string) - 1])]
        while index < len(string) \
        and string[index] == second_letter == third_letter:
            log('moving to', index, string[index])
            index = index + 1


        # splits
        if index < len(string) - 3:
            if string[index] != string[index + 1] \
            and string[index] == string[index + 2]:
                splits = splits + 1

        index = index + 1

    # now check last three for split
    if string[-3] == string[-1] and string[-3] != string[-2]:
        splits = splits + 1

    pair_of_doublets = False
    for key in doublets.keys():
        if doublets[key] > 1:
            pair_of_doublets = True

    if pair_of_doublets and splits > 0:
        log(string, 'is nice!')
        return True
    elif not pair_of_doublets:
        log(string, 'does not contain a doublet pair.')
        log(str(doublets))
    elif splits < 1:
        log(string, 'contains', splits, 'split(s).')

    return False


def string_is_nice(string):
    """Determines if string qualifies as nice."""
    vowels = ['a', 'e', 'i', 'o', 'u']
    number_of_vowels = 0
    doublet = False
    for index in range(len(string) - 1):
        # check for ab, cd, pq, or xy
        if string[index:index + 2] in ['ab', 'cd', 'pq', 'xy']:
            log(string, 'contains forbidden string.')
            return False
        # doublet
        if string[index] == string[index + 1]:
            doublet = True
        # vowels
        if string[index] in vowels:
            number_of_vowels = number_of_vowels + 1
    # be sure to check the last letter for vowelship
    if string[-1] in vowels:
        number_of_vowels = number_of_vowels + 1

    if doublet and number_of_vowels > 2:
        log(string, 'is nice!')
        return True
    else:
        if not doublet:
            log(string, 'does not contain a doublet.')

        if number_of_vowels < 3:
            log(string, 'has', number_of_vowels, 'vowel(s).')

        return False

def input_string_to_list(input_string):
    """Returns a list of input strings split by newline."""
    return [s.strip() for s in input_string.split('\n')]

def count_nice_strings(input_string):
    """Count the number of nice strings."""
    nice_strings = 0
    list_of_strings = input_string_to_list(input_string)
    for string in list_of_strings:
        if len(string) > 2:
            if string_is_nice(string):
                nice_strings = nice_strings + 1
    return nice_strings

def count_nice_strings2(input_string):
    """Count the number of nice strings according to definition 2."""
    nice_strings = 0
    list_of_strings = input_string_to_list(input_string)
    for string in list_of_strings:
        if len(string) > 2:
            if string_is_nice2(string):
                nice_strings = nice_strings + 1
    return nice_strings

def process_file(file_name, process_to_apply):
    """Process input file."""
    input_file = open(file_name, 'r')
    input_string = input_file.read()
    input_file.close()
    return process_to_apply(input_string)

if __name__ == '__main__':
    print "\nFile contains", process_file('../input.txt', count_nice_strings), \
          "nice strings according to definition 1."
    print "\nFile contains", process_file('../input.txt', count_nice_strings2), \
          "nice strings according to definition 2."
