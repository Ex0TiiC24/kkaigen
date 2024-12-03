import unittest
from mymerge import *
class TestRecursiveFunctionalProblems(unittest.TestCase):

    # Test case for Problem 1
    def test_recursive_sum(self):
        self.assertEqual(recursive_sum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(recursive_sum([10, -5, 6]), 11)
        self.assertEqual(recursive_sum([0, 0, 0, 0]), 0)
        self.assertEqual(recursive_sum([]), 0)

    # Test case for Problem 2
    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_max([10, 20, 5, 7]), 20)
        self.assertEqual(find_max([-1, -2, -3, -4]), -1)
        self.assertEqual(find_max([0]), 0)

    # Test case for Problem 3
    def test_recursive_reverse(self):
        self.assertEqual(recursive_reverse([1, 2, 3, 4]), [4, 3, 2, 1])
        self.assertEqual(recursive_reverse(['a', 'b', 'c']), ['c', 'b', 'a'])
        self.assertEqual(recursive_reverse([]), [])

    # Test case for Problem 4
    def test_count_evens(self):
        self.assertEqual(count_evens([1, 2, 3, 4, 5]), 2)
        self.assertEqual(count_evens([10, 20, 30, 40]), 4)
        self.assertEqual(count_evens([1, 3, 5, 7]), 0)
        self.assertEqual(count_evens([2, 4, 6, 8]), 4)

    # Test case for Problem 5
    def test_count_occurrences(self):
        self.assertEqual(count_occurrences([1, 2, 3, 1, 4], 1), 2)
        self.assertEqual(count_occurrences([1, 2, 2, 2, 3], 2), 3)
        self.assertEqual(count_occurrences([5, 5, 5], 5), 3)
        self.assertEqual(count_occurrences([], 10), 0)

    # Test case for Problem 6
    def test_filter_odds(self):
        self.assertEqual(filter_odds([1, 2, 3, 4, 5]), [1, 3, 5])
        self.assertEqual(filter_odds([10, 20, 30]), [])
        self.assertEqual(filter_odds([7, 9, 11, 13]), [7, 9, 11, 13])
        self.assertEqual(filter_odds([2, 4, 6]), [])

    # Test case for Problem 7
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

    # Test case for Problem 8
    def test_sum_of_squares_of_evens(self):
        self.assertEqual(sum_of_squares_of_evens([1, 2, 3, 4, 5]), 20)
        self.assertEqual(sum_of_squares_of_evens([10, 20, 30, 40]), 4000)
        self.assertEqual(sum_of_squares_of_evens([1, 3, 5, 7]), 0)
        self.assertEqual(sum_of_squares_of_evens([2, 4, 6, 8]), 120)

    # Test case for Problem 9
    def test_recursive_flatten(self):
        self.assertEqual(recursive_flatten([1, [2, 3], [4, [5, 6]]]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(recursive_flatten([[[1]], [2, 3], [4, 5]]), [1, 2, 3, 4, 5])
        self.assertEqual(recursive_flatten([[1], [2], [3]]), [1, 2, 3])
        self.assertEqual(recursive_flatten([[]]), [])

    # Test case for Problem 10
    def test_product_of_positives(self):
        self.assertEqual(product_of_positives([1, 2, 3, 4]), 24)
        self.assertEqual(product_of_positives([-1, -2, -3, 4]), 4)
        self.assertEqual(product_of_positives([0, 1, 2, 3]), 6)
        self.assertEqual(product_of_positives([10, -1, 5, -2]), 50)

if __name__ == "__main__":
    unittest.main()