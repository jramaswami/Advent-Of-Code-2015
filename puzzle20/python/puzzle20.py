"""Day 20 Puzzle"""

import factoring

class Elf(object):
    """Represents an elf delivering presents."""

    def __init__(self, number):
        self.number = number

    def deliver_presents(self, house):
        """Deliver presents to a house."""
        if house.number % self.number == 0:
            house.receive_presents(10 * self.number)

class House(object):
    """Represents a house receiving presents."""
    def __init__(self, number):
        self.number = number
        self.presents = 0

    def receive_presents(self, presents):
        """Receive presents from an elf."""
        self.presents = self.presents + presents


def deliver_until_present_count(target_number_of_presents, limit=1000000):
    """
    Deliver presents until you find a house where the
    target number of presents gets delivered.
    """
    elves = []
    index = 1
    while True:
        # add elf
        elf = Elf(index)
        elves.append(elf)

        # deliver presents to the new house
        house = House(index)
        for elf in elves:
            elf.deliver_presents(house)

        # are we there yet
        if house.presents >= target_number_of_presents:
            return house.number

        index = index + 1

        # safety
        if index == limit:
            return -1

def release_the_elves(target_present_count, stop_house=10000000, lazy=False):
    """
    Deliver presents until you find a house where the
    target number of presents gets delivered.

    Limit can be the house number to stop at.
    """
    if stop_house == 0:
        return -1, -1

    house = 1
    while True:
        divisors = factoring.get_divisors(house)

        # If the elves are lazy then filter divisors because
        # elves won't deliver to more than 50 houses, but they
        # will deliver 11 instead of 10 presents
        if lazy:
            presents = sum([d for d in divisors if (d * 50) > house]) * 11
        else:
            presents = sum(divisors) * 10

        if presents >= target_present_count:
            return house, presents

        # safety
        if house == stop_house:
            return house, presents

        house = house + 1

def by_summing_divisors(target_number):
    """Attempt to solve problem using prime factoring."""
    for index in range(2, target_number / 10):
        rho = factoring.sum_divisors(index)
        if rho >= target_number / 10:
            return index

def main():
    """Main program."""
    target_present_count = 34000000

    # Naive solution using objects doesn't really work.  My computer
    # very quickly ran out of memory.
    # house_number = deliver_until_present_count(target_present_count)
    # print 'House number', house_number, 'got', target_present_count, \
          # 'presents (object oriented).'

    import time
    start = time.time()
    house_number = by_summing_divisors(target_present_count)
    print 'House number', house_number, 'got', target_present_count, \
          'presents (by calculating sum of divisors from prime factors).'
    print time.time() - start, 'seconds elapsed'

    start = time.time()
    house_number, dummy_presents = release_the_elves(target_present_count)
    print 'House number', house_number, 'got', target_present_count, \
          'presents (by summing actual divisors).'
    print time.time() - start, 'seconds elapsed'

    start = time.time()
    house_number, presents = release_the_elves(target_present_count, lazy=True)
    print 'House number', house_number, 'got', presents, \
          'presents when the elves were lazy (by summing actual divisors).'
    print time.time() - start, 'seconds elapsed'

if __name__ == '__main__':
    main()

