from src.integration.mocking_injected.loyalty_service import LoyaltyService


class DiscountEngine:
    """Determines the discount a customer is entitled to based on loyalty points.

    parameters:
        loyalty_service -- a LoyaltyService used to look up the customer's points

    methods:
        get_discount(customer_id, amount) -- return the discount amount in SEK
    """

    POINTS_THRESHOLD = 100  # minimum points required for a discount
    DISCOUNT_RATE = 0.10    # 10 % off when threshold is met

    def __init__(self, loyalty_service: LoyaltyService):
        """Initialise a DiscountEngine with the given loyalty service.

        parameters:
            loyalty_service -- a LoyaltyService used to look up the customer's points

        returns:
            none
        """
        self._service = loyalty_service

    def get_discount(self, customer_id: str, amount: float) -> float:
        """Return the discount amount the customer is entitled to.

        parameters:
            customer_id -- the unique identifier of the customer
            amount      -- the order amount before discount in SEK

        returns:
            the discount as a float; 0.0 if the customer has fewer than
            100 loyalty points, or 10% of amount if they have 100 or more
        """
        points = self._service.get_points(customer_id)
        if points >= self.POINTS_THRESHOLD:
            return round(amount * self.DISCOUNT_RATE, 2)
        return 0.0
