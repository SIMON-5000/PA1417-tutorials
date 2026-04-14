from src.integration.patching.currency_converter import CurrencyConverter


class CheckoutService:
    """Converts a SEK order total into the customer's preferred currency.

    parameters:
        converter -- a CurrencyConverter used to perform the conversion

    methods:
        total_in(amount_sek, target_currency) -- return the amount in the target currency
    """

    def __init__(self, converter: CurrencyConverter):
        """Initialise a CheckoutService with the given currency converter.

        parameters:
            converter -- a CurrencyConverter used to perform the conversion

        returns:
            none
        """
        self._converter = converter

    def total_in(self, amount_sek: float, target_currency: str) -> float:
        """Return a SEK order total converted to the target currency.

        parameters:
            amount_sek      -- the order total in Swedish kronor
            target_currency -- the ISO currency code to convert to (e.g. "EUR")

        returns:
            the converted amount as a float
        """
        return self._converter.convert(amount_sek, "SEK", target_currency)
