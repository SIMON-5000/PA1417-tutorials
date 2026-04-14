class LoyaltyService:
    """Retrieves a customer's loyalty points from an external system.

    methods:
        get_points(customer_id) -- return the number of loyalty points the customer holds
    """

    def get_points(self, customer_id: str) -> int:
        """Return the number of loyalty points the customer holds.

        parameters:
            customer_id -- the unique identifier of the customer

        returns:
            the number of loyalty points as an integer

        note:
            This method is intentionally not implemented.
        """
        raise NotImplementedError("LoyaltyService requires a live network connection.")
