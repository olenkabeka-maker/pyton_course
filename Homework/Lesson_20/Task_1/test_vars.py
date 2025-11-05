# test  функція для тестування міститься в модулі vars.py

import unittest
from vars import example

class TestExampleFunction(unittest.TestCase):
    
    def test_sum_result(self):
        result = example()
        self.assertEqual(result, 30)

    def test_return_type(self):
        result = example()
        self.assertIsInstance(result, (int, float))

unittest.main()