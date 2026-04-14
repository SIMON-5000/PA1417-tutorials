class StockApi:
    """Client for a live inventory stock service.

    In production this class would query a warehouse system.

    Methods:
        in_stock(sku) — return True if the product SKU is currently in stock
    """

    def in_stock(self, sku: str) -> bool:
        """Return True if the given product SKU is currently in stock.

        parameters:
            sku -- the product identifier to check

        returns:
            True  -- if the product is currently in stock
            False -- if the product is out of stock

        note:
            This method is intentionally not implemented.
        """
        raise NotImplementedError("StockApi requires a live connection")
