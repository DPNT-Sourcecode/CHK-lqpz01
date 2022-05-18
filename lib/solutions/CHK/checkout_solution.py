

# noinspection PyUnusedLocal
# skus = unicode string

class Checkout:
    """Class to interact with price table
    Example Table:
    +------+-------+----------------+
    | Item | Price | Special offers |
    +------+-------+----------------+
    | A    | 50    | 3A for 130     |
    | B    | 30    | 2B for 45      |
    | C    | 20    |                |
    | D    | 15    |                |
    +------+-------+----------------+
    """
    
    def __init__(self, price_table:str):
        price_table = price_table.strip()
        # prices are stored in a dict
        self.prices: dict[str, tuple[int, int]] = {}
        for line in price_table.splitlines()[3:-1]:
            item, price, offer = line.split('|')[1:4]
            item = item.strip()
            price = int(price.strip())
            offer = offer.split(' for ')
            offer_count = int(offer[0].strip()[:-1])
            offer_price = int(offer[1].strip())
            self.prices[item] = {1: price, offer_count: offer_price}
            
    def get_price(self, skus:str) -> int:
        """Return total price for all SKUs"""
        skus = skus
            

def checkout(skus):
    raise NotImplementedError()
