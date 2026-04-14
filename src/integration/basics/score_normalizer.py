class ScoreNormalizer:
    """Converts a raw score into a percentage.

    Methods:
        percentage(score, max_score) — returns score as a percentage of
                                       max_score, rounded to one decimal place
    """

    def percentage(self, score: int, max_score: int) -> float:
        """Return a score expressed as a percentage of the maximum possible score.

        parameters:
            score     -- the number of marks awarded
            max_score -- the maximum possible marks (must be greater than 0)

        returns:
            a float in the range 0.0 to 100.0, rounded to one decimal place
        """
        return round(score / max_score * 100, 1)
