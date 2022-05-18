from lib.solutions.CHK import checkout_solution
import unittest

class TestCheckout(unittest.TestCase):
    
    def setUp(self):
        price_table = """
        +------+-------+----------------+
        | Item | Price | Special offers |
        +------+-------+----------------+
        | A    | 50    | 3A for 130     |
        | B    | 30    | 2B for 45      |
        | C    | 20    |                |
        | D    | 15    |                |
        +------+-------+----------------+
        """
        
        self.checkout = checkout_solution.Checkout(price_table)
        
    def test_prices(self):
        self.assertEqual(self.checkout.get_price('A'), 50)
        self.assertEqual(self.checkout.get_price('A B C'), 100)
        self.assertEqual(self.checkout.get_price('A, B, C'), 100)
        self.assertEqual(self.checkout.get_price('A A A A'), 180)
        self.assertEqual(self.checkout.get_price('A A A A A A A'), 130*2 + 50)
        self.assertEqual(self.checkout.get_price('A B F'), -1)
        self.assertEqual(self.checkout.get_price('A B C D, D'), 130)
        

class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        price_table = """
        +------+-------+----------------+
        | Item | Price | Special offers |
        +------+-------+----------------+
        | A    | 50    | 3A for 130     |
        | B    | 30    | 2B for 45      |
        | C    | 20    |                |
        | D    | 15    |                |
        +------+-------+----------------+
        """
        
        self.checkout = checkout_solution.Checkout(price_table)
        
    def test_solution(self):
        self.assertEqual(checkout_solution.checkout('A A A A'), 180)

if __name__ == '__main__':
    unittest.main()

