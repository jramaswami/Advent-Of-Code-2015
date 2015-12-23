"""Day 11 Puzzle"""

class PasswordException(Exception):
    """Exception for passwords."""
    def __init__(self, value):
        Exception.__init__(self, value)
        self.value = value
    def __str__(self):
        return repr(self.value)

def increment_password(password):
    """Function to increment password."""
    # recursion ending case 1: we've run out
    # of passwords because password is all z's
    if 'z' * len(password) == password:
        raise PasswordException('Unable to increment ' + password)
    # recursion ending case 2: we successfully
    # increment the last letter of the password
    if ord(password[-1]) < ord('z'):
        return password[:-1] + chr(ord(password[-1]) + 1)
    # recursion case
    # set last letter of password to 'a' and
    # increment the but-last of the password
    else:
        return increment_password(password[:-1]) + 'a'

def next_password(password):
    """Function to return the next password."""
    new_password = increment_password(password)
    while not valid_password(new_password):
        new_password = increment_password(new_password)
    return new_password

def valid_password(password):
    """Function to test validity of password according to rules."""
    has_straight_letter_sequence = False
    count_of_letter_pairs = 0

    for index in range(len(password)):
        # no i, o, or l
        if password[index] in ['i', 'o', 'l']:
            # print 'Password', password, \
                  # 'includes invalid char:', password[index]
            return False

        # one straight letter sequence of letter
        if index < len(password) - 2:
            if ord(password[index]) + 1 == ord(password[index + 1]) \
            and ord(password[index]) + 2 == ord(password[index + 2]):
                has_straight_letter_sequence = True

        # two different non-overlapping two letter pairs
        if index < len(password) - 1:
            if password[index] == password[index + 1]:
                if index > 1:
                    # don't count if previous letter is the same
                    # because we can't have overlapping pairs
                    if password[index] == password[index - 1]:
                        pass
                    else:
                        count_of_letter_pairs += 1
                else:
                    count_of_letter_pairs += 1

    if has_straight_letter_sequence and count_of_letter_pairs > 1:
        return True
    else:
        # if not has_straight_letter_sequence:
            # print 'Password', password, \
                  # 'does not have straight letter sequence.'
        # elif count_of_letter_pairs < 2:
            # print 'Password', password, \
                  # 'does not have two or more letter pairs.'
        return False

def main():
    """Main program."""
    input_string = 'hepxcrrq'
    password_1 = next_password(input_string)
    password_2 = next_password(password_1)
    print 'The next password after', input_string, 'is', password_1
    print 'The next password after', password_1, 'is', password_2

if __name__ == '__main__':
    main()
