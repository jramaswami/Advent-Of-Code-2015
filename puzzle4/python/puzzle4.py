"""Day 4 Puzzle"""

import hashlib

def find_first_md5(key, number_of_leading_zeros):
    """Find the first md5 starting with the required number of zeroes."""
    index = 0
    limit = 10000000000
    keep_going = True
    while keep_going:
        digest = hashlib.md5()
        digest.update(key + str(index))
        if str(digest.hexdigest())[:number_of_leading_zeros] == \
           ('0' * number_of_leading_zeros):
            return index
        digest = None
        index = index + 1
        if index > limit:
            keep_going = False
    return None


if __name__ == '__main__':
    print 'The lowest number that combines with iwrupvqb', \
          'to produce a md5 hash with 5 leading zeros is', \
          find_first_md5('iwrupvqb', 5)
    print 'The lowest number that combines with iwrupvqb', \
          'to produce a md5 hash with 6 leading zeros is', \
          find_first_md5('iwrupvqb', 6)
