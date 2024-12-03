import unittest
from func import *
class TestFunctions(unittest.TestCase):

    # Test case for Problem 1
    def test_func01(self):
        self.assertEqual(func01([1, 2, 3, 4, 5]), 6)  # Sum of evens: 2 + 4 = 6
        self.assertEqual(func01([1, 3, 5, 7]), 0)     # No evens
        self.assertEqual(func01([2, 4, 6, 8]), 20)    # Sum of evens: 2 + 4 + 6 + 8 = 20
        self.assertEqual(func01([10, 20, 30, 40]), 100)  # Sum of evens: 10 + 20 + 30 + 40 = 100
        self.assertEqual(func01([1, 3, 5, 7, 9]), 0)   # No evens, all odd numbers
        self.assertEqual(func01([]), 0)                # Empty list

    # Test case for Problem 2
    def test_func02(self):
        self.assertEqual(func02(['cat', 'dog', 'elephant', 'bat']), ['elephant'])  # Strings with more than 3 chars
        self.assertEqual(func02(['one', 'two', 'three', 'four']), ['three', 'four'])
        self.assertEqual(func02(['a', 'bc', 'deff']), ['deff'])  # Only 'def' is longer than 3 chars
        self.assertEqual(func02(['aaaa', 'bb', 'cccc', 'ddd']), ['aaaa', 'cccc'])  # Only 'aaa' and 'cccc' have length > 3
        self.assertEqual(func02(['apple', 'pie']), ['apple'])  # 'pie' has less than 3 characters
        self.assertEqual(func02([]), [])                   # Empty list

    # Test case for Problem 3
    def test_func03(self):
        self.assertEqual(func03([1, -2, 3, -4, 5]), [1, 3, 5])  # Positive integers
        self.assertEqual(func03([0, -1, -2]), [0])  # Only 0 is positive
        self.assertEqual(func03([-5, -6, -7]), [])  # No positive integers
        self.assertEqual(func03([10, -5, 3, -2, 5]), [10, 3, 5])  # Positive integers only
        self.assertEqual(func03([0]), [0])  # List with 0 as the only element
        self.assertEqual(func03([]), [])  # Empty list

    # Test case for Problem 4
    def test_func04(self):
        self.assertEqual(func04([1, 2, 3, 4]), [1, 4, 9, 16])  # Squares of the integers
        self.assertEqual(func04([0, -1, -2]), [0, 1, 4])
        self.assertEqual(func04([5]), [25])  # Square of 5 is 25
        self.assertEqual(func04([2, 3, 4]), [4, 9, 16])  # Squares of 2, 3, 4
        self.assertEqual(func04([10, 15]), [100, 225])  # Squares of 10 and 15
        self.assertEqual(func04([]), [])  # Empty list

    # Test case for Problem 5
    def test_func05(self):
        self.assertEqual(func05([1, 2, 3, 4]), 24)  # Product of all integers: 1*2*3*4 = 24
        self.assertEqual(func05([2, 3, 5]), 30)     # Product: 2*3*5 = 30
        self.assertEqual(func05([]), 1)             # Empty list, return 1
        self.assertEqual(func05([10, 0, 5]), 0)     # Product with 0: 10*0*5 = 0
        self.assertEqual(func05([1, 2, 3]), 6)      # Product of 1*2*3 = 6
        self.assertEqual(func05([0]), 0)            # Product with 0: 0
        self.assertEqual(func05([7, 8, 9]), 504)    # Product of 7*8*9 = 504

    # Test case for Problem 6
    def test_func06(self):
        self.assertEqual(func06(['one', 'two', 'three', 'four', 'five']), ['one', 'two', 'three', 'four', 'five'])  # Sorted by length
        self.assertEqual(func06(['a', 'abc', 'ab', 'abcd']), ['a', 'ab', 'abc', 'abcd'])
        self.assertEqual(func06(['dog', 'cat', 'elephant', 'ant']), ['ant', 'dog', 'cat', 'elephant'])  # Sorted by length
        self.assertEqual(func06(['banana', 'apple', 'cherry']), ['apple', 'banana', 'cherry'])
        self.assertEqual(func06(['x', 'xy', 'xyz', 'abcd', 'abc']), ['x', 'xy', 'xyz', 'abc', 'abcd'])  # Alphabetically sorted by length
        self.assertEqual(func06([]), [])  # Empty list

    # Test case for Problem 7
    def test_func07(self):
        self.assertEqual(func07(['apple', 'banana', 'cherry', 'date'], lambda s: len(s) > 5), 2)  # Strings with length > 5
        self.assertEqual(func07(['cat', 'dog', 'elephant'], lambda s: s.startswith('e')), 1)  # Starts with 'e'
        self.assertEqual(func07(['a', 'b', 'c'], lambda s: s == 'a'), 1)  # Only 'a' matches
        self.assertEqual(func07(['cat', 'dog', 'elephant'], lambda s: 'a' in s), 2)  # 'cat' and 'elephant' contain 'a'
        self.assertEqual(func07(['one', 'two', 'three', 'four'], lambda s: 'o' in s), 3)  # 'one' and 'two' contain 'o'
        self.assertEqual(func07([], lambda s: len(s) > 3), 0)  # Empty list, no matches
        self.assertEqual(func07(['apple', 'pie', 'orange', 'banana'], lambda s: s.startswith('b')), 1)  # 'banana' and 'pie' start with 'b'


if __name__ == '__main__':
    unittest.main()
