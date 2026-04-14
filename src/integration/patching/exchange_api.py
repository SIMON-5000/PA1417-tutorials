class ExchangeApi:
    """Fetches live currency exchange rates from an external service.

    methods:
        get_rate(from_currency, to_currency) -- return the exchange rate as a float
    """

    def get_rate(self, from_currency: str, to_currency: str) -> float:
        """Return the exchange rate from one currency to another.

        parameters:
            from_currency -- the ISO currency code to convert from (e.g. "SEK")
            to_currency   -- the ISO currency code to convert to (e.g. "EUR")

        returns:
            the exchange rate as a float

        note:
            This method is intentionally not implemented.
        """
        raise NotImplementedError("ExchangeApi requires a live network connection.")
