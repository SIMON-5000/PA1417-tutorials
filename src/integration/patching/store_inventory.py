from src.integration.patching.price_api import PriceApi
from src.integration.patching.stock_api import StockApi


class StoreInventory:
    """Looks up combined price and stock information for a product.

    Creates both PriceApi and StockApi internally — both dependencies are
    hard-coded, not injected. To test this class without live connections,
    both must be patched in this module's namespace:
        patch("src.integration.patching.store_inventory.PriceApi")
        patch("src.integration.patching.store_inventory.StockApi")

    Methods:
        lookup(sku) — return a dict with "price" and "in_stock" for the SKU
    """

    def lookup(self, sku: str) -> dict:
        """Return pricing and stock data for the given product SKU.

        parameters:
            sku -- the product identifier to look up

        returns:
            a dict with keys:
                "price"    -- float, the current price
                "in_stock" -- bool, whether the item is available
        """
        price_api = PriceApi()
        stock_api = StockApi()
        return {
            "price": price_api.get_price(sku),
            "in_stock": stock_api.in_stock(sku),
        }
