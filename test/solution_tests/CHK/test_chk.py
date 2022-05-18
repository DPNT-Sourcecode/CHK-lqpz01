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
        
        
        
    def test_invalid(self):
        self.assertEqual(self.checkout.get_price('ABCx'), -1)
        
    def test_empty(self):
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
        
        
    def test_free(self):
        self.assertEqual(self.checkout.get_price('EEEEBB'), 160)
        self.assertEqual(self.checkout.get_price('EEEEBBB'), 190)
        
class TestCheckoutThird(unittest.TestCase):
    
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
        | F    | 10    | 2F get one F free      |
        +------+-------+------------------------+
        """
        
        self.checkout = checkout_solution.Checkout(price_table)
        
    
    def test_same_free(self):
        self.assertEqual(self.checkout.get_price('FF'), 20)
        self.assertEqual(self.checkout.get_price('FFF'), 20)
        self.assertEqual(self.checkout.get_price('FFFF'), 30)
        self.assertEqual(self.checkout.get_price('FFFFF'), 40)
        
    
  
class TestFavour(unittest.TestCase):
    
    def setUp(self):
        price_table = """
        +------+-------+------------------------+
        | Item | Price | Special offers         |
        +------+-------+------------------------+
        | A    | 50    | 3A for 100, 5A for 200 |
        | B    | 30    | 2B for 20              |
        | C    | 20    |                        |
        | D    | 15    |                        |
        | E    | 40    | 2E get one B free      |
        | F    | 10    | 2F get one A free      |
        +------+-------+------------------------+
        """
        
        self.checkout = checkout_solution.Checkout(price_table)
        
    def test_favour(self):   
        self.assertEqual(self.checkout.get_price('AAAAAA'), 200)
        self.assertEqual(self.checkout.get_price('AAAAAAFF'), 220)   
        self.assertEqual(self.checkout.get_price('BBEE'), 20+40*2)      

class TestPrime(unittest.TestCase):
    
    def test_first_primes(self):
        primes = checkout_solution.prime_iter()
        self.assertEqual(next(primes), 2)
        self.assertEqual(next(primes), 3)
        self.assertEqual(next(primes), 5)
        self.assertEqual(next(primes), 7)
        
    
        
        
        
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