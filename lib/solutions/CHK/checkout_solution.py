

# noinspection PyUnusedLocal
# skus = unicode string
import re
from collections import namedtuple
import math

Item = namedtuple('Item', ['price', 'prime'])
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
        
        def parse_offer(offer:str) -> None:
            
            def parse_for_offer(offer:str) -> None:
                offer = offer.split(' for ')
                # assumes offer is always same item as item in that row
                offer_count = int(re.sub(r'[^\d]', '', offer[0]))
                offer_item = re.sub(r'[^a-zA-Z]', '', offer[0])
                offer_price = int(offer[1].strip())
                offer_discount = self.items[offer_item].price * offer_count - offer_price
                offer_combination = self.items[offer_item].prime ** offer_count
                self.prices.append(ItemCombination(
                    price=offer_price,
                    discount=offer_discount,
                    combination=offer_combination
                ))
                
            
            def parse_one_free_offer(offer:str) -> None:
                offer = offer.split(' ')
                # assumes offer is always same item as item in that row
                offer_count = int(re.sub(r'[^\d]', '', offer[0]))
                offer_item = re.sub(r'[^a-zA-Z]', '', offer[0])
                offer_free_item = offer[3].strip()
                offer_price = self.items[offer_item].price * offer_count
                offer_discount = self.items[offer_free_item].price
                offer_combination = (self.items[offer_item].prime ** offer_count) * self.items[offer_free_item].prime
                self.prices.append(ItemCombination(
                    price=offer_price,
                    discount=offer_discount,
                    combination=offer_combination
                ))
            
            offers = offer.split(',')
            for offer in offers:
                if not offer:
                    continue
                if 'for' in offer:
                    parse_for_offer(offer)
                elif 'get one' in offer:
                    parse_one_free_offer(offer)
                else:
                    raise NotImplementedError('Unknown offer type')
            
        self.prices: list[ItemCombination] = []
        self.items: dict[str, Item] = {}
        
        offers: list[str] =[]
        primes = prime_iter()
        for line in price_table.strip().splitlines()[3:-1]:
            item, price, offer = line.split('|')[1:4]
            item = item.strip()
            price = int(price.strip())
            offer = offer.strip()
            self.items[item] = Item(price, next(primes))
            self.prices.append(ItemCombination(
                price=price, 
                discount=0, 
                combination=self.items[item].prime))
            offers.append(offer)
        for offer in offers:
            parse_offer(offer)
            
        self.prices.sort(key=lambda x: x.discount)
        # sort is stable
        self.prices.sort(key=lambda x: x.combination)
            
            
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
        if any(sku not in self.items for sku in skus):
            return -1
        res = 0
        combination = math.prod(self.items[sku].prime for sku in skus)
        i = 0
        while combination > 1:
            
            if combination >= self.prices[i].combination and combination % self.prices[i].combination == 0:
                res += self.prices[i].price
                combination /= self.prices[i].combination
            else:
                i += 1
                    
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

if __name__ == '__main__':
    print(checkout('A A A A', checkout))

