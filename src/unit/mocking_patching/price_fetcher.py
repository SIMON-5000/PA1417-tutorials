class PriceFetcher:
    """Fetches current prices from a pricing service.

    methods:
        get_price(item) -- return the current price of the item in SEK
    """

    def get_price(self, item: str) -> float:
        """Return the current price of the given item in SEK.

        parameters:
            item -- the name of the item to look up

        returns:
            the current price as a float in SEK

        note:
            This method is intentionally not implemented.
        """
        raise NotImplementedError("requires a live pricing service connection")
