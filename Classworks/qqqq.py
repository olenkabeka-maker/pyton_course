#assert sum([1, 2, 3]) == 6, "Should be 6"  # test



"""import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([2, 3, 1]), 6)     #unittest команда -  python qqqq.py

if __name__ == "__main__":
    unittest.main() """

"""def test_sum():
    assert sum([1, 1, 1]) == 6       #pytest (це і команда)"""


def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")               # команда - python qqqq.py 