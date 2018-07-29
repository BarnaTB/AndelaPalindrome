import unittest
# from palindrome import *
# from unittest.mock import patch


class PalindromeTest(unittest.TestCase):
    # @patch('builtins.input', return_value)
    def test_for_digit(self):
        word = 'word'
        self.assertEqual(word.isdigit(), False)

    def test_for_string(self):
        word = 'word'
        self.assertEqual(word.isalpha(), True)

    # def test_for_palindrome(self):
    #     palindrome()
    #     self.assertEqual(palindrome(), True)
