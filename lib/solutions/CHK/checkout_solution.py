

# noinspection PyUnusedLocal
# skus = unicode string
import re
from collections import namedtuple

ItemCombination = namedtuple('ItemCombination', ['price', 'discount', 'combination'])

def prime_iter():
    """iterate over prime numbers, does not end"""
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    current = 1
    while True:
        current += 1
        if is_prime(current):
            yield current
        

class Checkout:
    """Class to interact with price table
    Example Table:
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
    
    def __init__(self, price_table:str):
        """initialise the price table

        Args:
            price_table (str): price table as string
        """
        
        def parse_offers(offer:str) -> None:
            
            def parse_for_offer(offer:str) -> None:
                offer = offer.split(' for ')
                # assumes offer is always same item as item in that row
                offer_count = int(offer[0].strip().replace(item, ''))
                offer_price = int(offer[1].strip())
            
            def parse_get_offer(offer:str) -> None:
                pass
            
            offers = offer.split(',')
            for offer in offers:
                if 'for' in offer:
                    parse_for_offer(offer)
                elif 'get' in offer:
                    parse_get_offer(offer)
                else:
                    raise NotImplementedError('Unknown offer type')
            
        price_table = price_table.strip()
        
        self.prices: list[ItemCombination] = []
        
        items: dict[str, int] = {}
        offers: list[str] =[]
        
        for line in price_table.splitlines()[3:-1]:
            item, price, offer = line.split('|')[1:4]
            item = item.strip()
            price = int(price.strip())
            offer = offer.strip()
            items[item] = price
            self.prices.append
            offers.append(offer)
            
            
    def get_price(self, skus:str) -> int:
        """Return total price for all SKUs"""
        # split skus into individual SKUs for commas or spaces
        # skus = re.split(r'[,\s]+', skus) # actually allows for more than 
        # one char sku
        
        # remove whitespace and commas
        skus = re.sub(r'[,\s]+', '', skus)
        skus = list(skus)
        if not skus:
            return 0
        if any(sku not in self.prices for sku in skus):
            return -1
        unique_skus = set(skus)
        res = 0
        for sku in unique_skus:
            count = skus.count(sku)
            best_offer_count = max(self.prices[sku].keys())
            # first attempt to get best deal, get full price for the remaider
            if count >= best_offer_count:
                res += self.prices[sku][best_offer_count] * (count // best_offer_count)
            res += self.prices[sku][1] * (count % best_offer_count)
        return res
        
DEFAULT_PRICE_TABLE = """
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
DEFAULT_CHECKOUT_CLASS = Checkout(DEFAULT_PRICE_TABLE)

def checkout(skus, checkout_class=DEFAULT_CHECKOUT_CLASS):
    return checkout_class.get_price(skus)
