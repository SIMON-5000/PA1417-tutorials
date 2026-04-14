class CartPricer:
    """Calculates the total price for a cart item.

    parameters:
        price_service -- a service with a get_price(item) method

    methods:
        total(item, quantity) -- return the total cost for quantity units of item
    """

    def __init__(self, price_service):
        """Initialise a CartPricer with the given price service.

        parameters:
            price_service -- a service with a get_price(item) method

        returns:
            none
        """
        self._price_service = price_service

    def total(self, item: str, quantity: int) -> float:
        """Return the total cost for a given quantity of an item.

        parameters:
            item     -- the name of the item to price
            quantity -- the number of units

        returns:
            the total cost as a float (unit price multiplied by quantity)
        """
        unit_price = self._price_service.get_price(item)
        return unit_price * quantity
