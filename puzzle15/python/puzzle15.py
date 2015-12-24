"""Day 16 Puzzle"""

import itertools as it
import re
import operator as op

def calculate_calories(ingredients, proportion):
    """Calculates the calories for the cookie of the given proportion."""
    return sum([x[0] * x[1] for x in zip(proportion, [j[-1] for j in ingredients])])

def ingredient_proportions(ingredient_count, max_tblsp):
    """Returns matrix of possible ingredient proportions."""
    return it.ifilter(lambda x: sum(x) == max_tblsp, \
                      it.product(range(max_tblsp + 1), repeat=ingredient_count))

def score_properties_for_proportion(ingredients, proportion):
    """Returns list of scores for ingredients in the given proportion."""
    scores = []
    # for each ingredient multiply its properties by the individual
    # proportion for that ingredient; accumulate them into a list
    # which is then returned
    for index in range(len(proportion)):
        scores.append([proportion[index] * x for x in ingredients[index][1:-1]])
    return scores

def sum_properties_scores(scores):
    """
    Sum the scores for each property, i.e. sum
    the columns of the scores array.
    """
    return [sum(t) for t in [x for x in zip(*scores)]]

def multiply_properties_scores(properties_scores):
    """Return final score for the proportions."""
    return reduce(op.mul, [max(0, p) for p in properties_scores])

def score_proportion(ingredients, proportion):
    """Returns the score for the given proportion of ingredients."""
    # Wrap intermediate functions
    return multiply_properties_scores(
        sum_properties_scores(
            score_properties_for_proportion(ingredients, proportion)))

def main():
    """Main program."""
    # load ingredients
    ingredients = []
    pattern = re.compile(r'^(\w+): capacity (-?\d+), durability (-?\d), ' + \
                         r'flavor (-?\d), texture (-?\d+), calories (\d)')
    with open('../input.txt', 'r') as input_file:
        for line in input_file:
            matches = pattern.match(line.strip())
            ingredient = [matches.group(1)]
            ingredient.extend([int(item) for item in matches.groups()[1:]])
            ingredients.append(ingredient)

    proportions = [p for p in ingredient_proportions(len(ingredients), 100)]
    best_score = max([score_proportion(ingredients, p) for p in proportions])
    print 'Best score is', best_score
    calorie_filter = lambda x: calculate_calories(ingredients, x) == 500
    proportions_500_cal = [p for p in proportions if calorie_filter(p)]
    best_score = max([score_proportion(ingredients, p) for p in proportions_500_cal])
    print 'Best score for 500 calories is', best_score

if __name__ == '__main__':
    main()
