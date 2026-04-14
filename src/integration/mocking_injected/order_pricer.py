from src.integration.mocking_injected.discount_engine import DiscountEngine


class OrderPricer:
    """Calculates the final price of an order after any applicable discount.

    parameters:
        discount_engine -- a DiscountEngine used to determine the discount

    methods:
        price(customer_id, base_amount) -- return the final price in SEK
    """

    def __init__(self, discount_engine: DiscountEngine):
        """Initialise an OrderPricer with the given discount engine.

        parameters:
            discount_engine -- a DiscountEngine used to determine the discount

        returns:
            none
        """
        self._engine = discount_engine

    def price(self, customer_id: str, base_amount: float) -> float:
        """Return the final price of an order after any applicable discount.

        parameters:
            customer_id -- the unique identifier of the customer
            base_amount -- the order amount before discount in SEK

        returns:
            the final price as a float rounded to two decimal places
        """
        discount = self._engine.get_discount(customer_id, base_amount)
        return round(base_amount - discount, 2)
