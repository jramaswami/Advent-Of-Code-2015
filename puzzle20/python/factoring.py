"""
Functions to factor a number; get the sum of a numbers divisors;
and a list of a number divisors.

References:
    http://rosettacode.org/wiki/Prime_decomposition
    http://mathschallenge.net/library/number/sum_of_divisors
"""

from math import floor, sqrt
import itertools as it
import operator as op

# try:
    # long
# except NameError:
    # long = int

def prime_factors(number):
    """
    Returns the prime factors of the given number.

    See http://rosettacode.org/wiki/Prime_decomposition#Python:_Using_floating_point
    """
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = long(floor(sqrt(number)))
    d = 1
    q = number % 2 == 0 and 2 or 3
    while q <= maxq and number % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + prime_factors(number//q) or [number]

def sum_divisors(number):
    """Gets the sum of divisors for given number"""
    total = 1
    for factor, group in it.groupby(prime_factors(number)):
        factor_count = len(list(group))
        subtotal = ((factor ** (factor_count + 1)) - 1) / (factor - 1)
        total = total * subtotal
    return total

def get_divisors(number):
    """Returns the divisors of a number."""
    factors = prime_factors(number)
    powerset = set(it.chain.from_iterable(it.combinations(factors, r) \
                                          for r in range(1, len(factors) + 1)))
    powerset.add((1, ))
    return sorted([reduce(op.mul, x) for x in powerset])

def main():
    """Main program."""
    # import time
    # start = time.time()
    # tocalc =  2**59-1
    # print("%s = %s" % (tocalc, fac(tocalc)))
    # print("Needed %ss" % (time.time() - start))

    print 72, [2, 2, 2, 3, 3], 195
    print 72, prime_factors(72), sum_divisors(72)
    rho = sum_divisors(2259441)
    print 2259441, rho, 34000000, rho * 10 == 34000000

    print get_divisors(100)
    print get_divisors(1000000)

if __name__ == '__main__':
    main()
