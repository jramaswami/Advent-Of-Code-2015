"""Day 14 Puzzle"""

class ReindeerRace(object):
    """Represents reindeer race."""
    def __init__(self):
        self.reindeer = []

    def add_reindeer(self, *reindeer):
        """Add reindeer to race."""
        for deer in reindeer:
            self.reindeer.append(deer)

    def race(self, seconds=2503):
        """Race!"""
        for dummy_index in range(seconds):
            for deer in self.reindeer:
                deer.tick()

            for leader in self.current_leaders():
                leader.award_point()

    def current_leaders(self):
        """Get the current leader in distance."""
        max_dist = 0
        leaders = []
        for deer in self.reindeer:
            if deer.distance_traveled > max_dist:
                leaders = [deer]
                max_dist = deer.distance_traveled
            elif deer.distance_traveled == max_dist:
                leaders.append(deer)
        return leaders

class Reindeer(object):
    """Class to represent reindeer."""

    # constancts
    MOVING = 1
    RESTING = 0

    # pylint: disable-msg=too-many-instance-attributes

    def __init__(self, name, speed, endurance, recovery):
        """
        speed = speed of reindeer in km/sec.
        endurance = time in secs that reindeer can maintain speed.
        recovery = time in secs reindeer must rest before moving again.
        """
        self.name = name
        self.speed = int(speed)
        self.endurance = int(endurance)
        self.recovery = int(recovery)
        self.reset()

    def __str__(self):
        return self.name + " has gone " + str(self.distance_traveled) + \
               ' and has ' + str(self.points) +  ' points.'

    def reset(self):
        """Reset, i.e. go back to starting line."""
        self.distance_traveled = 0
        self.state = Reindeer.MOVING
        self.internal_clock = 0
        self.total_ticks = 0
        self.points = 0

    def tick(self):
        """Represents one second of state"""
        self.total_ticks += 1

        # if reindeer is moving ...
        if self.state == Reindeer.MOVING:
            # if internal clock has exceeded the reindeer's endurance
            # then change state to RESTING and reset internal clock
            if self.internal_clock >= self.endurance:
                self.state = Reindeer.RESTING
                self.internal_clock = 1
            # if reindeer can still move, move and increment internal
            # clock
            else:
                self.internal_clock += 1
                self.distance_traveled += self.speed
        # if reindeer is resting ...
        else:
            # if reindeer can move again, do so
            if self.internal_clock >= self.recovery:
                self.internal_clock = 1
                self.state = Reindeer.MOVING
                self.distance_traveled += self.speed
            # otherwise, continue resting
            else:
                self.internal_clock += 1

    def many_ticks(self, ticks):
        """Tick the given number of ticks"""
        for dummy_index in range(ticks):
            self.tick()

    def tick_until(self, tick_to):
        """Tick to given number of total ticks"""
        while self.total_ticks < tick_to:
            self.tick()

    def description(self):
        """Returns description of reindeer."""
        return self.name + " can fly " + str(self.speed) + " km/s for " + \
               str(self.endurance) + " seconds, but then must rest for " + \
               str(self.recovery) + " seconds."

    def award_point(self):
        """Give reindeer a point for leading race."""
        self.points += 1

def calculate_distance(speed, endurance, recovery, seconds):
    """Calculates distance."""
    interval_time = endurance + recovery
    intervals = seconds / interval_time
    remainder = seconds % interval_time
    intervals_distance = intervals * speed * endurance
    remainder_distance = min(remainder, endurance) * speed
    return intervals_distance + remainder_distance

def main2():
    """Alternative main."""
    import re
    max_dist = 0
    with open('../input.txt', 'r') as input_file:
        for line in input_file:
            pattern = r"(\S+) can fly (\d+) km/s for (\d+) seconds, " + \
                      r"but then must rest for (\d+) seconds\."
            matches = re.match(pattern, line.strip())
            name, speed, endurance, recovery = matches.group(1, 2, 3, 4)
            distance = calculate_distance(int(speed), int(endurance), \
                                          int(recovery), 2503)
            # print name, 'went', distance
            if distance > max_dist:
                max_dist = distance
    print 'Winning distance is', max_dist

def main():
    """Main program."""
    import re

    with open('../input.txt', 'r') as input_file:
        reindeer = []
        for line in input_file:
            pattern = r"(\S+) can fly (\d+) km/s for (\d+) seconds, " + \
                      r"but then must rest for (\d+) seconds\."
            matches = re.match(pattern, line.strip())
            name, speed, endurance, recovery = matches.group(1, 2, 3, 4)
            reindeer.append(Reindeer(name, speed, endurance, recovery))

        max_distance = 0
        winner = None
        for deer in reindeer:
            deer.tick_until(2503)
            if deer.distance_traveled > max_distance:
                max_distance = deer.distance_traveled
                winner = deer

        print winner.name, 'won by travelling', max_distance, 'km', \
              'in', winner.total_ticks, 'seconds.'

        # Part 2
        race = ReindeerRace()
        # reset and add to race
        for deer in reindeer:
            deer.reset()
            race.add_reindeer(deer)
        race.race()
        max_points = 0
        winner = None
        for deer in reindeer:
            if deer.points > max_points:
                winner = deer
                max_points = deer.points
        print winner.name, 'has', winner.points, 'points and went', \
              winner.distance_traveled, 'km in', winner.total_ticks, \
              'seconds.'

if __name__ == '__main__':
    main()
    print
    print "*" * 80
    print
    main2()
