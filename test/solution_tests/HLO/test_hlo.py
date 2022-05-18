from lib.solutions.HLO import hello_solution
import unittest

class TestHLO(unittest.TestCase):
    
    def test_hello(self):
        self.assertEqual(hello_solution.hello('Mr. X'), 'Hello, World!')
        
   


if __name__ == '__main__':
    unittest.main()

