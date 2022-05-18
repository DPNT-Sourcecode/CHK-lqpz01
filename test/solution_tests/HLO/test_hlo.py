from lib.solutions.HLO import hello_solution
import unittest

class TestHLO(unittest.TestCase):
    
    def test_hello(self):
        self.assertEqual(hello_solution.hello(''), 'Hello, World!')
        
    def test_name_input(self):
        self.assertEqual(hello_solution.hello('John'), 'Hello, John!')


if __name__ == '__main__':
    unittest.main()


