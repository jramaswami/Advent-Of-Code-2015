"""Tests for puzzle 14"""

import unittest
import puzzle14

class TestPuzzle14(unittest.TestCase):
    """Tests for puzzle 14"""

    def test_puzzle14(self):
        """Tests for puzzle 14"""
        comet = puzzle14.Reindeer('comet', 14, 10, 127)
        dancer = puzzle14.Reindeer('dancer', 16, 11, 162)

        comet.tick()
        dancer.tick()
        self.assertEquals(comet.distance_traveled, 14)
        self.assertEquals(dancer.distance_traveled, 16)

        comet.tick_until(10)
        dancer.tick_until(10)
        self.assertEquals(comet.distance_traveled, 140)
        self.assertEquals(dancer.distance_traveled, 160)

        comet.tick()
        dancer.tick()
        self.assertEquals(comet.distance_traveled, 140)
        self.assertEquals(comet.state, puzzle14.Reindeer.RESTING)
        self.assertEquals(dancer.distance_traveled, 176)

        comet.tick()
        dancer.tick()
        self.assertEquals(comet.state, puzzle14.Reindeer.RESTING)
        self.assertEquals(dancer.state, puzzle14.Reindeer.RESTING)

        comet.tick_until(1000)
        dancer.tick_until(1000)
        self.assertEquals(comet.state, puzzle14.Reindeer.RESTING)
        self.assertEquals(dancer.state, puzzle14.Reindeer.RESTING)
        self.assertEquals(comet.distance_traveled, 1120)
        self.assertEquals(dancer.distance_traveled, 1056)

        comet = puzzle14.Reindeer('comet', 14, 10, 127)
        dancer = puzzle14.Reindeer('dancer', 16, 11, 162)
        comet.tick_until(1000)
        dancer.tick_until(1000)
        self.assertEquals(comet.state, puzzle14.Reindeer.RESTING)
        self.assertEquals(dancer.state, puzzle14.Reindeer.RESTING)
        self.assertEquals(comet.distance_traveled, 1120)
        self.assertEquals(dancer.distance_traveled, 1056)

    def test_puzzle14_part2(self):
        """Tests for puzzle 14."""
        comet = puzzle14.Reindeer('comet', 14, 10, 127)
        dancer = puzzle14.Reindeer('dancer', 16, 11, 162)
        race = puzzle14.ReindeerRace()
        race.add_reindeer(comet, dancer)
        race.race(140)
        self.assertEquals(139, dancer.points)
        self.assertEquals(1, comet.points)


if __name__ == '__main__':
    unittest.main()
