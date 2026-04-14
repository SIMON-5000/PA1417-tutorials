from src.unit.mocking_patching.stock_checker import StockChecker
from src.unit.mocking_patching.price_fetcher import PriceFetcher


class ShopAssistant:
    """Answers customer queries about item availability and pricing.

    methods:
        describe(item) -- return a description of the item's availability and price
    """

    def describe(self, item: str) -> str:
        """Return a human-readable description of an item's availability and price.

        parameters:
            item -- the name of the item to describe

        returns:
            a string of the form "<item>: available at <price> SEK." or
            "<item>: out of stock at <price> SEK."
        """
        checker = StockChecker()
        fetcher = PriceFetcher()
        in_stock = checker.is_in_stock(item)
        price = fetcher.get_price(item)
        status = "available" if in_stock else "out of stock"
        return f"{item}: {status} at {price} SEK."
