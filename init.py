"""
Python script to initialize a puzzle:
    1.  Make puzzle directory puzzle{n}/python
    2.  Generate puzzle python programs puzzle{n}/puzzle{n}.py
        and puzzle{n}/test_puzzle{n}.py
    3.  Generate puzzle{n}/README.md
"""

import sys
import os

PYTHON = '''"""Day {puzzle_number} Puzzle"""

def read_data():
    """Read data from input file."""
    data = []
    with open("../input.txt", "r") as input_file:
        for line in input_file:
            line = line.strip()
            data.append(line)

    return data

def main():
    """Main program."""
    data = read_data()

if __name__ == "__main__":
    main()
'''

TEST = '''"""Tests for Day {puzzle_number} Puzzle"""
import unittest
import puzzle{puzzle_number} as p{puzzle_number}

class TestPuzzle{puzzle_number}(unittest.TestCase):
    """Test for Day {puzzle_number} Puzzle"""

    def test_something(self):
        """Test ..."""
        pass

if __name__ == "__main__":
    unittest.main()
'''

def init_puzzle():
    """Main program."""
    if len(sys.argv) < 2:
        print 'You must specify the puzzle number'
        return 0

    puzzle_number = sys.argv[1].strip()

    puzzle_dir = "puzzle%s" % puzzle_number
    python_dir = "puzzle%s/python" % puzzle_number
    readme_path = "%s/README.md" % puzzle_dir
    python_path = "%s/puzzle%s.py" % (python_dir, puzzle_number)
    test_path = "%s/test_puzzle%s.py" % (python_dir, puzzle_number)

    if not os.path.exists(puzzle_dir):
        print 'Making %s directory ...' % puzzle_dir
        os.mkdir(puzzle_dir)
    else:
        print '%s already exists ...' % puzzle_dir

    if not os.path.exists(python_dir):
        print 'Making %s directory ...' % python_dir
        os.mkdir(python_dir)
    else:
        print '%s already exists ...' % python_dir

    if not os.path.exists(readme_path):
        print 'Making %s file ...' % readme_path
        readme_file = open(readme_path, 'w')
        readme_file.close()
    else:
        print '%s already exists ...' % readme_path

    if os.path.exists(python_path):
        print '%s already exists ...' % python_path
    else:
        print 'Writing %s ...' % python_path
        with open(python_path, "w") as python_file:
            python_file.write(PYTHON.format(puzzle_number=puzzle_number))

    if os.path.exists(test_path):
        print '%s already exists ...' % test_path
    else:
        print 'Writing %s ...' % test_path
        with open(test_path, "w") as test_file:
            test_file.write(TEST.format(puzzle_number=puzzle_number))


if __name__ == '__main__':
    init_puzzle()
