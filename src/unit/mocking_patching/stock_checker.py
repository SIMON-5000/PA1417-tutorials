class StockChecker:
    """Checks live inventory for items.

    methods:
        is_in_stock(item) -- return True if the item is currently available
    """

    def is_in_stock(self, item: str) -> bool:
        """Return True if the given item is currently available in inventory.

        parameters:
            item -- the name of the item to check

        returns:
            True  -- if the item is currently available
            False -- if the item is out of stock

        note:
            This method is intentionally not implemented.
        """
        raise NotImplementedError("requires a live inventory system connection")
