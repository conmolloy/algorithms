import unittest

from search.linear_search import linear_search

class TestLinearSearch(unittest.TestCase):

    def test_linear_search(self):
        result = linear_search(["A", "B", "C", "fggg", "wow"], "B")
        self.assertEqual(result, True)  

    def test_linear_search_fail(self):
        result = linear_search(["A", "B", "C", "fggg", "wow"], "3")
        self.assertEqual(result, False) 

if __name__ == '__main__':
    unittest.main()