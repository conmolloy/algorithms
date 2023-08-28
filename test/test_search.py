import unittest
import random

from search.linear_search import linear_search
from search.binary_search import binary_search


class TestLinearSearch(unittest.TestCase):
    def test_linear_search(self):
        result = linear_search(["A", "B", "C", "fggg", "wow"], "B")
        self.assertEqual(result, True)

    def test_linear_search_fail(self):
        result = linear_search(["A", "B", "C", "fggg", "wow"], "3")
        self.assertEqual(result, False)


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9)
        self.assertEqual(result, True)

    def test_linear_search_fail(self):
        result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)
        self.assertEqual(result, False)

    def test_random_number(self):
        for _ in range(10):
            random_integers = [random.randint(1, 1000) for _ in range(20)]
            random_number = random.randint(0, 19)
            random_integers.sort()
            result = binary_search(random_integers, random_integers[random_number])
            self.assertEqual(
                result,
                True,
                f"list used = {random_integers}, and searched for {random_integers[random_number]}",
            )


if __name__ == "__main__":
    unittest.main()
