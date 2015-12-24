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
def find_groups(packages, total_weight, group_number=1, early_exit=True):
    """Find a group from packages with a given total weight."""
    solutions = []
    # Starting from a length of 1, iterate through all the
    # combinations of packages of the given length.
    for group_length in xrange(1, len(packages)):
        # log('Checking groups of length %d that have total weight of %d' \
                # % (group_length, total_weight))
        for group in it.combinations(packages, group_length):

            # If group weighs the required amount, we have a
            # potential solution ...
            if sum(group) == total_weight:
                # If we are in group 1, then we must verify that
                # the remaining packages can be split into groups
                # of the required weight.
                if group_number == 1:
                    log('Found potential group %d: %s --> %d' \
                        % (group_number, str(group), sum(group)))
                    log('Verifiying remaining packages ...')
                    remaining_packages = [p for p in packages if p not in group]
                    remaining_groups = find_groups(remaining_packages, \
                                                   total_weight, \
                                                   group_number=group_number+1)
                    if len(remaining_groups) > 0:
                        # There are solutions in the remaining packages
                        # so, append the group to the list of solutions
                        solutions.append(sorted(list(group), reverse=True))
                # We are verifying that there are solutions for group 2
                # and group 3.  If there is a solution to group 2, then
                # there must be a solution to group 3 since the required
                # weight is total weight divided by 3 and we have found
                # two groups of the required weight:
                #       total_weight = 3 * group_weight
                # We can just return the single solution because we
                # just want to verify.
                else:
                    log('Verified group %d solution: %s --> %d' \
                        % (group_number, str(group), sum(group)))
                    remaining_packages = [p for p in packages if p not in group]
                    log('Verified group %d solution: %s --> %d' \
                        % (group_number + 1, str(remaining_packages), \
                           sum(remaining_packages)))
                    log("*" * 20)
                    return [group, tuple(remaining_packages)]

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
