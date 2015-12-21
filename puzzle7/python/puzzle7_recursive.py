"""
Recursive solution to puzzle 7.
"""

import sys
import re
import numpy as np
import copy

OPS = {'AND': np.bitwise_and, 'OR': np.bitwise_or,
       'LSHIFT': np.left_shift, 'RSHIFT': np.right_shift,
       'XOR': np.bitwise_xor, 'NOT': np.bitwise_not}

def get_input_file_name():
    """Get file name for input file or default to input.txt"""
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = '../input.txt'
    return file_name

def get_requested_wire():
    """Get requested wire or default to 'a'"""
    if len(sys.argv) > 2:
        wire_requested = sys.argv[2]
    else:
        wire_requested = 'a'
    return wire_requested

def load_wires_from_file(file_name):
    """Loads wires from file into a dict"""
    wires = {}
    with open(file_name, 'r') as input_file:
        for line in input_file:
            tokens = re.split(r'\s+', line.strip())
            # wire id is the last token
            wire_id = tokens[-1]
            signal = tokens[:-2]

            # signal is the tokens before -> and wire id
            if len(tokens) == 3:
                # straight up assignment, if we have a digit
                # then just remember the integer
                if tokens[0].isdigit():
                    signal = int(tokens[0])

            wires[wire_id] = signal
    return wires

def get_signal(wires, wire_id):
    """Gets or evalutes signal for given wire id"""
    # we might be getting a signal instead of a wire id
    # so if wire_id is a number, just return it because
    # it is actually a signal
    if str(wire_id).isdigit():
        return int(wire_id)

    signal = wires[wire_id]
    # return value if we have digit
    if str(signal).isdigit():
        return int(signal)
    # otherwise we have to evaluate signal,
    # which should be a list
    if len(signal) == 1:
        # just one token means an assignment from
        # another wire, just get the value of that
        # wire
        signal = get_signal(wires, signal[0])
    elif len(signal) == 2:
        # unary operation
        operation = OPS[signal[0]]
        lhs = get_signal(wires, signal[1])
        signal = operation(lhs)
    elif len(signal) == 3:
        # binary operation
        lhs = get_signal(wires, signal[0])
        rhs = get_signal(wires, signal[2])
        operation = OPS[signal[1]]
        signal = operation(lhs, rhs)

    wires[wire_id] = int(signal)
    return int(signal)

def main():
    """Main program."""
    input_file_name = get_input_file_name()
    wires = load_wires_from_file(input_file_name)
    if input_file_name == '../input.txt':
        # prepare for second part of puzzle
        wires2 = copy.deepcopy(wires)

    wire_id = get_requested_wire()
    if wire_id == '*':
        for key in wires.keys():
            print key, get_signal(wires, key)
    else:
        print 'wire_id', wire_id, '=', get_signal(wires, wire_id)

    if input_file_name == '../input.txt':
        # part two
        wires2['b'] = get_signal(wires, 'a')
        print 'After overriding a -> b:', wire_id, '=', \
              get_signal(wires2, wire_id)

if __name__ == '__main__':
    main()
