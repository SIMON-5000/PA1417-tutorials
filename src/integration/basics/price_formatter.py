class PriceFormatter:
    """Formats a monetary amount as a human-readable string.

    Methods:
        format(amount) — return the amount formatted as "X.XX SEK"
    """

    def format(self, amount: float) -> str:
        """Return a monetary amount formatted as a SEK price string.

        parameters:
            amount -- the monetary value to format

        returns:
            a string of the form "<amount> SEK" with two decimal places
            (e.g. "12.50 SEK" for 12.5)
        """
        return f"{amount:.2f} SEK"
