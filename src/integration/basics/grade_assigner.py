from src.integration.basics.score_normalizer import ScoreNormalizer


class GradeAssigner:
    """Assigns a letter grade based on a normalised percentage.

    Grade boundaries:
        A — 90 % and above
        B — 75 % to 89 %
        C — 60 % to 74 %
        D — 50 % to 59 %
        F — below 50 %

    Methods:
        assign(score, max_score) — return the letter grade for the given score
    """

    def __init__(self, normalizer: ScoreNormalizer) -> None:
        """Initialise a GradeAssigner with the given score normalizer.

        parameters:
            normalizer -- a ScoreNormalizer used to convert scores to percentages

        returns:
            none
        """
        self._normalizer = normalizer

    def assign(self, score: int, max_score: int) -> str:
        """Return the letter grade for a score out of a maximum possible score.

        parameters:
            score     -- marks awarded
            max_score -- maximum possible marks

        returns:
            "A" -- if the percentage is 90 or above
            "B" -- if the percentage is 75 to 89
            "C" -- if the percentage is 60 to 74
            "D" -- if the percentage is 50 to 59
            "F" -- if the percentage is below 50
        """
        pct = self._normalizer.percentage(score, max_score)
        if pct >= 90:
            return "A"
        if pct >= 75:
            return "B"
        if pct >= 60:
            return "C"
        if pct >= 50:
            return "D"
        return "F"
