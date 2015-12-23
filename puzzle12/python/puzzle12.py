"""Day 12 Puzzle"""

import types
import json

def sum_text(text):
    """Sum of numbers contained in text."""
    number_text = ''
    current_sum = 0
    for index in range(len(text)):
        if text[index].isdigit() or text[index] == '-':
            number_text += text[index]
        else:
            if len(number_text) > 0:
                current_sum += int(number_text)
                number_text = ''
    return current_sum

def sum_obj(obj, exclusions=None):
    """Sum list or dict"""
    obj_type = type(obj)
    if obj_type == types.IntType:
        return obj
    elif obj_type == types.ListType:
        return sum([sum_obj(leaves, exclusions) for leaves in obj])
    elif obj_type == types.DictType:
        # total = 0
        # for key, value in obj.items():
            # if key not in exclusions:
                # total += sum_obj(value)
        # return total
        # build list of atomic items from obj
        items = []
        for item in obj.values():
            if isinstance(item, dict) or isinstance(item, list):
                pass
            else:
                items.append(item)
        # turn list of exclusions into a set
        if exclusions == None:
            exclusions = []
        exclusion_set = set(exclusions)
        # make sure excluded items are not in keys or atomic values
        # any non-atomic items will be evaluated recursively for
        # exclusions
        if exclusion_set.isdisjoint(obj.keys()) \
        and exclusion_set.isdisjoint(items):
            return sum([sum_obj(leaves, exclusions) for leaves in obj.values()])
        else:
            return 0
    else:
        return 0

def main():
    """Main program."""
    total = 0
    with open('../input.txt', 'r') as input_file:
        for line in input_file:
            total = total + sum_text(line.strip())
    print 'Total for input file is:', total
    with open('../input.txt', 'r') as input_file:
        obj = json.loads(input_file.read())
        print 'Total by summing objects is:', sum_obj(obj)
        print 'Total excluding red is:', sum_obj(obj, exclusions=['red'])

if __name__ == '__main__':
    main()
