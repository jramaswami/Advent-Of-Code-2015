"""Day 23 Puzzle"""

def hlf_r(registers, values, line_pointer):
    """Half r"""
    registers[values[0]] = registers[values[0]] / 2
    return line_pointer + 1

def tpl_r(registers, values, line_pointer):
    """Triple r"""
    registers[values[0]] = registers[values[0]] * 3
    return line_pointer + 1

def inc_r(registers, values, line_pointer):
    """Increment r"""
    registers[values[0]] = registers[values[0]] + 1
    return line_pointer + 1

def jmp_offset(registers, values, line_pointer):
    """Jump offset"""
    return line_pointer + int(values[0])

def jie_r(registers, values, line_pointer):
    """Jump offset if even"""
    if registers[values[0][:-1]] > 0 \
    and registers[values[0][:-1]] % 2 == 0:
        return line_pointer + int(values[1])
    else:
        return line_pointer + 1

def jio_r(registers, values, line_pointer):
    """Jump offset if even"""
    if registers[values[0][:-1]] == 1:
        return line_pointer + int(values[1])
    else:
        return line_pointer + 1

def read_data():
    """Read data from input file."""
    data = []
    with open("../input.txt", "r") as input_file:
        for line in input_file:
            line = line.strip()
            data.append(line)

    return data

def run_program(program, registers):
    """Run a program"""
    line_pointer = 0
    while line_pointer < len(program):
        tokens = program[line_pointer].split()
        if tokens[0] == 'hlf':
            line_pointer = hlf_r(registers, tokens[1:], line_pointer)
        elif tokens[0] == 'tpl':
            line_pointer = tpl_r(registers, tokens[1:], line_pointer)
        elif tokens[0] == 'inc':
            line_pointer = inc_r(registers, tokens[1:], line_pointer)
        elif tokens[0] == 'jmp':
            line_pointer = jmp_offset(registers, tokens[1:], line_pointer)
        elif tokens[0] == 'jio':
            line_pointer = jio_r(registers, tokens[1:], line_pointer)
        elif tokens[0] == 'jie':
            line_pointer = jie_r(registers, tokens[1:], line_pointer)

def main():
    """Main program."""
    data = read_data()
    registers = {'a': 0, 'b': 0}
    run_program(data, registers)
    print 'The value of register b if a starts at 0 is %d.' % registers['b']
    registers = {'a': 1, 'b': 0}
    run_program(data, registers)
    print 'The value of register b if a starts at 1 is %d.' % registers['b']

if __name__ == "__main__":
    main()
