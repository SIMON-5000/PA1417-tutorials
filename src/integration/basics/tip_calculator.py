class TipCalculator:
    """Calculates the tip amount for a restaurant bill.

    methods:
        calculate(amount, tip_percent) -- return the tip as a monetary amount
    """

    def calculate(self, amount: float, tip_percent: float) -> float:
        """Return the tip amount for a given bill and tip percentage.

        parameters:
            amount      -- the bill amount before tip
            tip_percent -- the desired tip percentage (e.g. 15 for 15%)

        returns:
            the tip as a float rounded to two decimal places
        """
        return round(amount * tip_percent / 100, 2)
