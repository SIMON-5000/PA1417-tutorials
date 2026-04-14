from src.integration.basics.tip_calculator import TipCalculator


class BillSplitter:
    """Splits a restaurant bill (including tip) evenly among a group.

    parameters:
        tip_calculator -- a TipCalculator instance used to compute the tip

    methods:
        split(bill, tip_percent, num_people) -- return the amount each person owes
    """

    def __init__(self, tip_calculator: TipCalculator):
        """Initialise a BillSplitter with the given tip calculator.

        parameters:
            tip_calculator -- a TipCalculator instance used to compute the tip

        returns:
            none
        """
        self._calculator = tip_calculator

    def split(self, bill: float, tip_percent: float, num_people: int) -> float:
        """Return the amount each person owes after splitting the bill including tip.

        parameters:
            bill        -- the total bill amount before tip
            tip_percent -- the desired tip percentage (e.g. 15 for 15%)
            num_people  -- the number of people splitting the bill

        returns:
            each person's share as a float rounded to two decimal places
        """
        tip = self._calculator.calculate(bill, tip_percent)
        return round((bill + tip) / num_people, 2)
