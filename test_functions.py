import unittest

from palindrome import is_palindrome
from binary_search import binary_search


class TestPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))

    def test_empty_and_single(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))


class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        data = [1, 3, 5, 7, 9, 11]
        self.assertEqual(binary_search(data, 7), 3)
        self.assertEqual(binary_search(data, 1), 0)
        self.assertEqual(binary_search(data, 11), 5)

    def test_not_found(self):
        data = [1, 3, 5, 7, 9, 11]
        self.assertEqual(binary_search(data, 4), -1)
        self.assertEqual(binary_search(data, 100), -1)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 5), -1)


if __name__ == "__main__":
    unittest.main()
