from src.integration.patching.exchange_api import ExchangeApi


class CurrencyConverter:
    """Converts a monetary amount from one currency to another.

    methods:
        convert(amount, from_currency, to_currency) -- return the converted amount
    """

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """Convert an amount from one currency to another using the live exchange rate.

        parameters:
            amount        -- the monetary amount to convert
            from_currency -- the ISO currency code to convert from (e.g. "SEK")
            to_currency   -- the ISO currency code to convert to (e.g. "EUR")

        returns:
            the converted amount as a float rounded to two decimal places
        """
        api = ExchangeApi()
        rate = api.get_rate(from_currency, to_currency)
        return round(amount * rate, 2)
