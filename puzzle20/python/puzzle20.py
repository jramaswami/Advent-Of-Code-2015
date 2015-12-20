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

def release_the_elves(target_present_count, stop_house=1000000):
    """
    Deliver presents until you find a house where the
    target number of presents gets delivered.

    Limit can be the house number to stop at.
    """
    if stop_house == 0:
        return -1, -1

    house = 1
    while True:
        presents = sum(factoring.get_divisors(house)) * 10

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

    house_number = by_summing_divisors(target_present_count)
    print 'House number', house_number, 'got', target_present_count, \
          'presents (by summing divisors).'

    house_number, dummy_presents = release_the_elves(target_present_count)
    print 'House number', house_number, 'got', target_present_count, \
          'presents (factoring).'

if __name__ == '__main__':
    main()

