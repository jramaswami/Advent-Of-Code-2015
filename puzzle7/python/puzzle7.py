"""Day 7 Puzzle"""

import numpy as np
import re

class Circuit(object):
    """Represents Bobby's circuit."""

    def __init__(self):
        self._wires = {}
        self._unevaluated = []

    def evaluate_token(self, token):
        """Convert token to number."""
        if token.isdigit():
            return int(token)
        elif token in self._wires:
            return self._wires[token]
        else:
            raise Exception('Unable to evaluate token ' + token)

    def token_is_evaluatable(self, token):
        """Determine if token is evaluatable."""
        if token.isdigit():
            return True
        elif token in self._wires:
            return True
        else:
            return False

    def get_binary_operation(self, token):
        """Determines appropriate binary operation."""
        if token == 'AND':
            return np.bitwise_and
        elif token == 'OR':
            return np.bitwise_or
        elif token == 'LSHIFT':
            return np.left_shift
        elif token == 'RSHIFT':
            return np.right_shift
        elif token == 'XOR':
            return np.bitwise_xor
        else:
            raise Exception('Unknown operation: ' + token)

    def can_process_tokens(self, tokens):
        """Determines if all tokens are evaluatable."""
        if tokens[0] == 'NOT':
            # not
            if self.token_is_evaluatable(tokens[1]):
                return True
            else:
                return False
        elif len(tokens) == 3:
            # assignment
            if self.token_is_evaluatable(tokens[0]) \
            and tokens[1] == '->':
                return True
        elif len(tokens) == 5:
            # binary operation
            if self.token_is_evaluatable(tokens[0]) \
            and self.token_is_evaluatable(tokens[2]):
                return True
            else:
                return False

    def process_instruction(self, instruction):
        """Process an instruction."""
        tokens = re.split(r'\s+', instruction)
        if self.can_process_tokens(tokens):
            self.process_tokens(tokens)
        else:
            self._unevaluated.append(tokens)

    def process_tokens(self, tokens):
        """Process tokens by evaluating or storing."""
        if tokens[0] == 'NOT':
            # not
            signal = np.bitwise_not(self.evaluate_token(tokens[1]))
            self.set_wire_signal(tokens[-1], signal)
        elif len(tokens) == 3 and tokens[1] == '->':
            # assignment
            self.set_wire_signal(tokens[-1], self.evaluate_token(tokens[0]))
        elif len(tokens) == 5:
            # binary operation
            left = self.evaluate_token(tokens[0])
            right = self.evaluate_token(tokens[2])
            operation = self.get_binary_operation(tokens[1])
            signal = operation(left, right)
            self.set_wire_signal(tokens[-1], signal)

    def evaluation_loop(self, limit=1000):
        """Loop over and over to evaluate tokens."""
        passes = 0
        while True:
            for tokens in self._unevaluated:
                if self.can_process_tokens(tokens):
                    self._unevaluated.remove(tokens)
                    self.process_tokens(tokens)
            passes += 1
            if len(self._unevaluated) < 1:
                return True
            if passes > limit:
                print 'Reached evaluation_loop limit!'
                return False

    def set_wire_signal(self, wire_id, value):
        """Set the value of the signal on the given wire."""
        if wire_id in self._wires:
            # raise Exception('Trying to reassign signal to wire ' + wire_id)
            print 'Ignoring reassignment of signal to wire', wire_id
        else:
            self._wires[wire_id] = int(value)

    def get_wire_signal(self, wire_id):
        """Returns the value of the signal on the given wire."""
        return self._wires[wire_id]

    def get_wires(self):
        """Returns the dict of wires."""
        return self._wires

    def get_unevaluated(self):
        """Returns the dict of wires."""
        return self._unevaluated

def main():
    """Main program."""
    circuit = Circuit()
    input_file = open('../input.txt')
    for line in input_file:
        circuit.process_instruction(line.strip())
    input_file.close()
    circuit.evaluation_loop()
    print 'The value of wire a in circuit 1 is:', circuit.get_wire_signal('a')

    circuit2 = Circuit()
    circuit2.set_wire_signal('b', circuit.get_wire_signal('a'))
    input_file = open('../input.txt')
    for line in input_file:
        circuit2.process_instruction(line.strip())
    input_file.close()
    circuit2.evaluation_loop()
    print 'The value of wire a in circuit 2 is:', circuit2.get_wire_signal('a')

if __name__ == '__main__':
    main()

