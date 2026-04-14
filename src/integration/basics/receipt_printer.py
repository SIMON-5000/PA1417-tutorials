from src.integration.basics.price_formatter import PriceFormatter


class ReceiptPrinter:
    """Builds a list of formatted receipt lines from a list of items.

    Each line combines the item name and its formatted price.
    The PriceFormatter dependency is injected via the constructor.

    Methods:
        print_receipt(items) — return a list of formatted strings,
                               one per item
    """

    def __init__(self, formatter: PriceFormatter) -> None:
        """Initialise a ReceiptPrinter with the given price formatter.

        parameters:
            formatter -- a PriceFormatter used to format each item's price

        returns:
            none
        """
        self._formatter = formatter

    def print_receipt(self, items: list[tuple[str, float]]) -> list[str]:
        """Return a formatted receipt line for each item in the list.

        parameters:
            items -- a list of (name, price) tuples

        returns:
            a list of strings, each of the form "  <name>: <formatted price>";
            returns an empty list if items is empty
        """
        return [f"  {name}: {self._formatter.format(price)}" for name, price in items]
