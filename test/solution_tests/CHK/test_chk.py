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
        self.assertEqual(self.checkout.get_price('A   B C,,, D,    D'), 130)
        self.assertEqual(self.checkout.get_price('ABC'), 100)
        self.assertEqual(self.checkout.get_price('ABCx'), -1)
        self.assertEqual(self.checkout.get_price(''), 0)
        
class TestCheckoutSecond(unittest.TestCase):
    
    def setUp(self):
        price_table = """
        +------+-------+------------------------+
        | Item | Price | Special offers         |
        +------+-------+------------------------+
        | A    | 50    | 3A for 130, 5A for 200 |
        | B    | 30    | 2B for 45              |
        | C    | 20    |                        |
        | D    | 15    |                        |
        | E    | 40    | 2E get one B free      |
        +------+-------+------------------------+
        """
        
        self.checkout = checkout_solution.Checkout(price_table)
        
    def test_second_prices(self):
        self.assertEqual(self.checkout.get_price('A'), 50)
        self.assertEqual(self.checkout.get_price('ABCx'), -1)
        self.assertEqual(self.checkout.get_price('AAAAAA'), 250)
        self.assertEqual(self.checkout.get_price('EEB'), 80)
        self.assertEqual(self.checkout.get_price('AAAAA'), 200)
        self.assertEqual(self.checkout.get_price('AAAA'), 180)
        self.assertEqual(self.checkout.get_price('EEEEBB'), 160)

class TestPrime(unittest.TestCase):
    
    def test_first_primes(self):
        self.assertEqual([2, 3, 5, 7, 11] == list(checkout_solution.prime_iter()[:5]))
        
    
        
        
        
class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        price_table = """
        +------+-------+----------------+
        | Item | Price | Special offers |
        +------+-------+----------------+
        | A    | 60    | 3A for 130     |
        | B    | 30    | 2B for 45      |
        | C    | 20    |                |
        | D    | 15    |                |
        +------+-------+----------------+
        """
        
        self.checkout = checkout_solution.Checkout(price_table)
        
    def test_solution_default(self):
        self.assertEqual(checkout_solution.checkout('A A A A'), 180)
        
    def test_solution_custom(self):
        self.assertEqual(checkout_solution.checkout('A A A A', self.checkout), 190)
        
    

if __name__ == '__main__':
    unittest.main()
