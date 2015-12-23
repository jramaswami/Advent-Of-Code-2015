"""Tests for puzzle 12."""

import puzzle12
import unittest

class TestPuzzle12(unittest.TestCase):
    """Tests for puzzle 12."""

    def test_sum_text(self):
        """Tests for sum_text()"""
        self.assertEqual(6, puzzle12.sum_text("[1,2,3]"))
        self.assertEquals(6, puzzle12.sum_text('{"a":2,"b":4}'))
        self.assertEquals(3, puzzle12.sum_text('[[[3]]]'))
        self.assertEquals(3, puzzle12.sum_text('{"a":{"b":4},"c":-1}'))
        self.assertEquals(0, puzzle12.sum_text('"a":[-1,1]}'))
        self.assertEquals(0, puzzle12.sum_text('[-1,{"a":1}]'))
        self.assertEquals(0, puzzle12.sum_text('[]'))
        self.assertEquals(0, puzzle12.sum_text('{}'))

    def test_sum_obj(self):
        """Tests for sum_obj()"""
        self.assertEqual(6, puzzle12.sum_obj([1, 2, 3]))
        self.assertEquals(6, puzzle12.sum_obj({"a":2, "b":4}))
        self.assertEquals(3, puzzle12.sum_obj([[[3]]]))
        self.assertEquals(3, puzzle12.sum_obj({"a":{"b":4}, "c":-1}))
        self.assertEquals(0, puzzle12.sum_obj({"a":[-1, 1]}))
        self.assertEquals(0, puzzle12.sum_obj([-1, {"a":1}]))
        self.assertEquals(0, puzzle12.sum_obj([]))
        self.assertEquals(0, puzzle12.sum_obj({}))
        self.assertEqual(6, puzzle12.sum_obj([1, 2, 3], ['red']))
        obj = [1, {"c":"red", "b":2}, 3]
        self.assertEquals(4, puzzle12.sum_obj(obj, ['red']))
        obj = {"d":"red", "e":[1, 2, 3, 4], "f":5}
        self.assertEquals(0, puzzle12.sum_obj(obj, ['red']))
        obj = [1, "red", 5]
        self.assertEquals(6, puzzle12.sum_obj(obj, ['red']))

if __name__ == '__main__':
    unittest.main()
