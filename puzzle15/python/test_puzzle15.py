"""Tests for puzzle 15."""

import unittest
import puzzle15 as p15

class TestPuzzle15(unittest.TestCase):
    """Tests for puzzle 15."""

    def test_scoring_proportions(self):
        """Tests for scoring proportions."""
        butterscotch = ('Butterscotch', -1, -2, 6, 3, 8)
        cinnamon = ('Cinnamon', 2, 3, -2, -1, 3)
        ingredients = [butterscotch, cinnamon]
        proportions = [p for p in p15.ingredient_proportions(len(ingredients), 100)]
        prop_scores = p15.score_properties_for_proportion(ingredients, (44, 56))
        expected = [[44 * -1, 44* -2, 44 * 6, 44 * 3],
                    [56 * 2, 56 * 3, 56 * -2, 56 * -1]]
        self.assertEquals(prop_scores, expected)
        expected = [68, 80, 152, 76]
        sum_prop_scores = p15.sum_properties_scores(prop_scores)
        self.assertEquals(sum_prop_scores, expected)
        best_score = max([p15.score_proportion(ingredients, p) for p in proportions])
        self.assertEquals(best_score, 62842880)

    def test_calorie_filter(self):
        """Tests for filtering by calories."""
        butterscotch = ('Butterscotch', -1, -2, 6, 3, 8)
        cinnamon = ('Cinnamon', 2, 3, -2, -1, 3)
        ingredients = [butterscotch, cinnamon]
        self.assertEquals(500, p15.calculate_calories(ingredients, (40, 60)))
        proportions = [p for p in p15.ingredient_proportions(len(ingredients), 100)]
        calorie_filter = lambda x: p15.calculate_calories(ingredients, x) == 500
        proportions_500_cal = [p for p in proportions if calorie_filter(p)]
        best_score = max([p15.score_proportion(ingredients, p) for p in proportions_500_cal])
        self.assertEquals(best_score, 57600000)

if __name__ == '__main__':
    unittest.main()
