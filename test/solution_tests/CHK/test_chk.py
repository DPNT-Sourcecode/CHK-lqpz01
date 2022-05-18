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
        
class TestCheckoutFourth(unittest.TestCase):
    
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
        | G    | 20    |                        |
        | H    | 10    | 5H for 45, 10H for 80  |
        | I    | 35    |                        |
        | J    | 60    |                        |
        | K    | 80    | 2K for 150             |
        | L    | 90    |                        |
        | M    | 15    |                        |
        | N    | 40    | 3N get one M free      |
        | O    | 10    |                        |
        | P    | 50    | 5P for 200             |
        | Q    | 30    | 3Q for 80              |
        | R    | 50    | 3R get one Q free      |
        | S    | 30    |                        |
        | T    | 20    |                        |
        | U    | 40    | 3U get one U free      |
        | V    | 50    | 2V for 90, 3V for 130  |
        | W    | 20    |                        |
        | X    | 90    |                        |
        | Y    | 10    |                        |
        | Z    | 50    |                        |
        +------+-------+------------------------+
        """
        
        self.checkout = checkout_solution.Checkout(price_table)
        
    
    def test_larger_list(self):
        self.assertEqual(self.checkout.get_price('H'*11), 80+10)
        self.assertEqual(self.checkout.get_price('H'*11+'U'*4), 90+120)
        self.assertEqual(self.checkout.get_price('ABCDEF'), 165)
        self.assertEqual(self.checkout.get_price('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 965)
        self.assertEqual(self.checkout.get_price('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'), 1880)
        self.assertEqual(self.checkout.get_price('LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH'), 1880)
  
class TestCheckoutFifth(unittest.TestCase):
    
    def setUp(self):
        price_table = """
        +------+-------+---------------------------------+
        | Item | Price | Special offers                  |
        +------+-------+---------------------------------+
        | A    | 50    | 3A for 130, 5A for 200          |
        | B    | 30    | 2B for 45                       |
        | C    | 20    |                                 |
        | D    | 15    |                                 |
        | E    | 40    | 2E get one B free               |
        | F    | 10    | 2F get one F free               |
        | G    | 20    |                                 |
        | H    | 10    | 5H for 45, 10H for 80           |
        | I    | 35    |                                 |
        | J    | 60    |                                 |
        | K    | 70    | 2K for 120                      |
        | L    | 90    |                                 |
        | M    | 15    |                                 |
        | N    | 40    | 3N get one M free               |
        | O    | 10    |                                 |
        | P    | 50    | 5P for 200                      |
        | Q    | 30    | 3Q for 80                       |
        | R    | 50    | 3R get one Q free               |
        | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
        | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
        | U    | 40    | 3U get one U free               |
        | V    | 50    | 2V for 90, 3V for 130           |
        | W    | 20    |                                 |
        | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
        | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
        | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
        +------+-------+---------------------------------+
        """
        
        self.checkout = checkout_solution.Checkout(price_table)
        
    
    def test_any_list(self):
        
        self.assertEqual(self.checkout.get_price('STXX'), 45+17)
        self.assertEqual(self.checkout.get_price('TTXX'), 45+17)
        self.assertEqual(self.checkout.get_price('WXYZ'), 45+20)
        self.assertEqual(self.checkout.get_price('TXYZ'), 45+17)
  
class TestCheckoutFavour(unittest.TestCase):
    
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
        self.assertEqual(next(primes), 11)
        self.assertEqual(next(primes), 13)
        self.assertEqual(next(primes), 17)
        self.assertEqual(next(primes), 19)
    
        
        
        
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