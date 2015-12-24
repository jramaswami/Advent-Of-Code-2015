"""Day 24 Puzzle"""

# Knapsack problem
#
# C(P, n) is function to choose combinations of length n from set P
# S <-- empty list
# P <-- list of packages
# W <-- sum(P) / length(P)
# for n <-- 1 to length(P)
#       for cm in C(P, n)
#           if sum(cm) equals W then
#               add cm to S
#           end if
#       end for
#       if len(S) is not 0 then
#           break
#       end if
# end for

DEBUG = True

def log(message):
    """Prints message if DEBUG is True."""
    if DEBUG:
        print message

import itertools as it
def find_groups(packages, total_weight, early_exit=True):
    """Find a group from packages with a given total weight."""
    solutions = []
    # Starting from a length of 1, iterate through all the
    # combinations of packages of the given length.
    for group_length in xrange(1, len(packages)):
        log('Checking groups of length %d that have total weight of %d' \
                % (group_length, total_weight))
        for group in it.combinations(packages, group_length):
            # If a group of packages has a weight equal to
            # required weight, verify that you can split
            # the remaining packages into a groups of
            # the required weight.
            if sum(group) == total_weight:
                log('Found potential solution: %s' % str(group))
                log('Verifiying remaining packages ...')
                remaining_packages = [p for p in packages if p not in group]
                # If there is a group within the remaining packages
                # that is of the required weight, then the third
                # package must be of the required weight because the
                # required weight is the weight of all the packages
                # divided by three. So if thre is at least one
                # group of the required weight, initial group to
                # our list of solutions.
                if len(find_groups(remaining_packages, total_weight)) > 0:
                    solutions.append(group)

        # If an early exit has been requested and
        # if we have solutions then we have found the
        # smallest number of packages that will fit, as
        # required, so stop and return the solutions.
        if early_exit and len(solutions) > 0:
            return solutions

    return solutions

def main():
    """Main program."""
    data = [1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41,
            43, 47, 53, 59, 67, 71, 73, 79, 83, 89, 97,
            101, 103, 107, 109, 113]


if __name__ == "__main__":
    main()
