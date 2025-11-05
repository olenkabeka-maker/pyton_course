# Task_1   
"""Pick your solution to one of the exercises in this module. Design tests for this solution and write tests using unittest library.
функція міститься в модулі function_example.py"""

# ТЕСТИ

import unittest
from function_example import a_b

class TestABFunction(unittest.TestCase):

    def test_valid_input(self):
        result = a_b(4, 2)
        self.assertEqual(result, 8.0)

    def test_value_error(self):
        result = a_b("abc", 2)
        self.assertEqual(result, "Помилка! Вводь лише числа!")

    def test_zero_division(self):
        result = a_b(4, 0)
        self.assertEqual(result, "Не можна ділити на нуль!")

unittest.main()