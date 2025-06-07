
class OutOfStockError(Exception):
    """Raised when an item is out of stock."""
    pass

def buy_item(stock):
    if stock == 0:
        raise OutOfStockError("Item is out of stock.")

status = buy_item(0)
print(status)  

# Raises OutOfStockError: Item is out of stock.
