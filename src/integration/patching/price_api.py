class PriceApi:
    """Client for a live product pricing service.

    In production this class would query a pricing database.

    Methods:
        get_price(sku) — return the current price for a product SKU
    """

    def get_price(self, sku: str) -> float:
        """Return the current price for the given product SKU.

        parameters:
            sku -- the product identifier to look up

        returns:
            the current price as a float

        note:
            This method is intentionally not implemented.
        """
        raise NotImplementedError("PriceApi requires a live connection")
