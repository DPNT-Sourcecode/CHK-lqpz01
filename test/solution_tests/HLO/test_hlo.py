from lib.solutions.SUM import sum_solution
import unittest

class TestSum(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(sum_solution.compute(1, 2), 3)


if __name__ == '__main__':
    unittest.main()