"""Day 10 Puzzle"""

def look_and_say(sequence):
    """Turn sequence into new sequence given look-and-say rules."""
    new_sequence = ''
    prev_char = sequence[0]
    subseq_len = 0
    for index in range(len(sequence)):
        if sequence[index] != prev_char:
            new_sequence += str(subseq_len)
            new_sequence += prev_char
            prev_char = sequence[index]
            subseq_len = 1
        else:
            subseq_len += 1
    # Get last subsequence
    new_sequence += str(subseq_len)
    new_sequence += prev_char

    return new_sequence

def main():
    """Main program."""
    seq = '3113322113'
    for dummy_index in range(40):
        seq = look_and_say(seq)
    print 'The length of the sequence when applied 40 times is ', len(seq)

    seq = '3113322113'
    for dummy_index in range(50):
        seq = look_and_say(seq)
    print 'The length of the sequence when applied 50 times is ', len(seq)

if __name__ == '__main__':
    main()
