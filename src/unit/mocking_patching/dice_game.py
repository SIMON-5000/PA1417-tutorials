import random


class DiceGame:
    """A simple dice game using a six-sided die.

    methods:
        roll()            -- roll the die and return the result (1-6)
        is_winner(target) -- return True if the roll meets or exceeds target
    """

    def roll(self) -> int:
        """Roll a six-sided die and return the result.

        parameters:
            none

        returns:
            an integer from 1 to 6 inclusive
        """
        return random.randint(1, 6)

    def is_winner(self, target: int) -> bool:
        """Return True if a fresh die roll meets or exceeds the target value.

        parameters:
            target -- the minimum roll value needed to win

        returns:
            True  -- if the roll result is greater than or equal to target
            False -- if the roll result is less than target
        """
        return self.roll() >= target
