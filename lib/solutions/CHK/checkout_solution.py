

# noinspection PyUnusedLocal
# skus = unicode string
import re
from collections import namedtuple
from functools import reduce
import operator
from itertools import combinations_with_replacement

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
                
            def parse_buy_any(offer:str) -> None:
                # perhaps not the most efficient way, but keeps with the theme
                # of the implementation without adding a seperate ItemCombination class
                offer = offer.split(' ')
                offer_count = int(offer[2].strip())
                offer_items = list(re.sub(r'[^a-zA-Z]', '', offer[4]))
                offer_price = int(offer[-1].strip())
                for item_combination in combinations_with_replacement(offer_items, offer_count):
                    offer_discount = sum([self.items[item].price for item in item_combination]) - offer_price
                    offer_combination = reduce(operator.mul, [self.items[item].prime for item in item_combination], 1)
                    self.prices.append(ItemCombination(
                        price=offer_price,
                        discount=offer_discount,
                        combination=offer_combination
                    ))
                
            offers = offer.split(', ')
            for offer in offers:
                if not offer:
                    continue
                
                elif 'get one' in offer:
                    parse_one_free_offer(offer)
                elif 'buy any' in offer:
                    parse_buy_any(offer)
                elif 'for' in offer:
                    parse_for_offer(offer)
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
            
            
            
    def get_price(self, skus:str) -> int:
        """Return total price for all SKUs"""
        
        # remove whitespace and commas
        skus = re.sub(r'[,\s]+', '', skus)
        skus = list(skus)
        if not skus:
            return 0
        if any(sku not in self.items for sku in skus):
            return -1
        res = 0
        combination = reduce(operator.mul, [self.items[sku].prime for sku in skus], 1)
        potential_offers = list(filter(
            lambda x: combination % x.combination == 0, 
            self.prices
            ))
        #sort is stable
        potential_offers.sort(key=lambda x: x.combination)
        potential_offers.sort(key=lambda x: x.discount, reverse=True)
        for offer in potential_offers:
            while combination > 1 and combination % offer.combination == 0:
                res += offer.price
                # rounding down is important for large numbers,
                # // negates the need for a special case for LARGE numbers in 
                # python3 
                combination //= offer.combination
            
                    
        return res
        
DEFAULT_PRICE_TABLE = """
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
DEFAULT_CHECKOUT_CLASS = Checkout(DEFAULT_PRICE_TABLE)

def checkout(skus, checkout_class=DEFAULT_CHECKOUT_CLASS):
    return checkout_class.get_price(skus)

if __name__ == '__main__':
    print(checkout('STXX'))