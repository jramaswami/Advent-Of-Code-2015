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

DEBUG = False

import operator

def log(message):
    """Prints message if DEBUG is True."""
    if DEBUG:
        print message

import itertools as it
def find_groups(packages, total_weight, group_number=1, groups_of=3, early_exit=True):
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
                else:
                    log('Verified group %d solution: %s --> %d' \
                        % (group_number, str(group), sum(group)))

                    if group_number == groups_of - 1:
                        # If we are down to two groups, verify them both
                        remaining_packages = [p for p in packages if p not in group]
                        log('Verified group %d solution: %s --> %d' \
                            % (group_number + 1, str(remaining_packages), \
                               sum(remaining_packages)))
                        log("*" * 20)
                        return [group, tuple(remaining_packages)]
                    else:
                        # More subsequent groups, recurse
                        remaining_packages = [p for p in packages if p not in group]
                        subgroups = find_groups(remaining_packages, \
                                                total_weight, \
                                                group_number=group_number+1)
                        # If there are solutions in subsequent groups
                        # then we can add this group and return the
                        # subgroups.
                        if len(subgroups) > 0:
                            return [group] + subgroups
            else:
                if group_number > 1:
                    log('Failed to verify groups %s; sum %d = %d' \
                        % (group, sum(group), total_weight))


        # If an early exit has been requested and
        # if we have solutions then we have found the
        # smallest number of packages that will fit, as
        # required, so stop and return the solutions.
        if early_exit and len(solutions) > 0:
            return solutions

    return solutions

def do_puzzle(data, groups_of):
    """Do the puzzle."""

    weight = sum(data) / groups_of
    solutions = find_groups(data, weight, groups_of=groups_of, early_exit=True)

    winner = solutions[0]
    min_qe = reduce(operator.mul, solutions[0])

    for solution in solutions:
        quantum_entanglement = reduce(operator.mul, solution)
        if quantum_entanglement < min_qe:
            min_qe = quantum_entanglement
            winner = solution
    return min_qe, winner

def main():
    """Main program."""
    data = [1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41,
            43, 47, 53, 59, 67, 71, 73, 79, 83, 89, 97,
            101, 103, 107, 109, 113]
    min_qe, winner = do_puzzle(data, 3)
    print 'Minimum QE for groups of 3 is %d for solution %s' % (min_qe, winner)

    min_qe, winner = do_puzzle(data, 4)
    print 'Minimum QE for groups of 4 is %d for solution %s' % (min_qe, winner)

if __name__ == "__main__":
    main()
