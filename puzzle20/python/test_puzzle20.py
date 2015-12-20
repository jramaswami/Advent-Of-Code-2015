"""Test for Day 20 Puzzle."""

import unittest
import puzzle20 as p20

class TestPuzzle20(unittest.TestCase):
    """Tests for Day 20 Puzzle."""

    def test_deliveries(self):
        """Tests for part 1 of puzzle."""
        expected = [10, 30, 40, 70, 60, 120, 80, 150, 130]
        elves = []
        houses = []
        for index in range(1, 10):
            # add elf
            elf = p20.Elf(index)
            elves.append(elf)

            # add house
            house = p20.House(index)
            houses.append(house)

            # deliver presents to the new house
            for elf in elves:
                elf.deliver_presents(house)

        # tests
        self.assertEquals(9, len(elves))
        self.assertEquals(9, len(houses))

        for house in houses:
            self.assertEquals(expected[house.number - 1], house.presents)

    def test_deliver_present_count(self):
        """Tests for deliver_until_present_count()"""
        self.assertEquals(6, p20.deliver_until_present_count(120))
        self.assertEquals(8, p20.deliver_until_present_count(150))

    def test_release_the_elves(self):
        """Tests for release the elves()"""
        house, presents = p20.release_the_elves(10)
        self.assertEquals(1, house)
        self.assertEquals(10, presents)

        house, presents = p20.release_the_elves(80)
        self.assertEquals(6, house)
        self.assertEquals(120, presents)

if __name__ == '__main__':
    unittest.main()
