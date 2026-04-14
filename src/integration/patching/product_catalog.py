from src.integration.patching.store_inventory import StoreInventory


class ProductCatalog:
    """Produces a human-readable product description for a SKU.

    Delegates inventory lookup to an injected StoreInventory.

    Methods:
        describe(sku) — return a formatted description string for the product
    """

    def __init__(self, inventory: StoreInventory) -> None:
        """Initialise a ProductCatalog with the given store inventory.

        parameters:
            inventory -- a StoreInventory used to look up product data

        returns:
            none
        """
        self._inventory = inventory

    def describe(self, sku: str) -> str:
        """Return a human-readable product description for the given SKU.

        parameters:
            sku -- the product identifier to describe

        returns:
            "<sku>: <price> SEK, in stock"     -- if the item is available
            "<sku>: <price> SEK, out of stock" -- if the item is unavailable
        """
        data = self._inventory.lookup(sku)
        availability = "in stock" if data["in_stock"] else "out of stock"
        return f"{sku}: {data['price']} SEK, {availability}"
