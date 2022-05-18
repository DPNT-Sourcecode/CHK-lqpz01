

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
        # prices are stored in a dict holding sku as key pointing to a dict
        # key-value pairs of count, price self.prices['A'] = {1: 50, 3: 130}
        self.prices: dict[str, tuple[int, int]] = {}
        for line in price_table.splitlines()[3:-1]:
            item, price, offer = line.split('|')[1:4]
            item = item.strip()
            price = int(price.strip())
            offer = offer.strip()
            self.prices[item] = {1: price}
            if offer:
                offer = offer.split(' for ')
                # assumes offer is always same item as item in that row
                offer_count = int(offer[0].strip().replace(item, ''))
                offer_price = int(offer[1].strip())
                self.prices[item][offer_count] = offer_price
            
    def get_price(self, skus:str) -> int:
        """Return total price for all SKUs"""
        skus = skus
            

def checkout(skus):
    raise NotImplementedError()

