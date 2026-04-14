from src.integration.mocking_injected.review_analyzer import ReviewAnalyzer


class RatingEngine:
    """Converts a text review into a 1–5 star rating.

    Delegates classification to an injected ReviewAnalyzer. The mapping is:
        "positive" -> 5 stars
        "neutral"  -> 3 stars
        "negative" -> 1 star

    Methods:
        star_rating(text) — return the integer star rating for text
    """

    def __init__(self, analyzer: ReviewAnalyzer) -> None:
        """Initialise a RatingEngine with the given review analyzer.

        parameters:
            analyzer -- a ReviewAnalyzer used to classify review text

        returns:
            none
        """
        self._analyzer = analyzer

    def star_rating(self, text: str) -> int:
        """Return the star rating for a review text.

        parameters:
            text -- the review text to rate

        returns:
            5 -- if the review is positive
            3 -- if the review is neutral
            1 -- if the review is negative
        """
        category = self._analyzer.classify(text)
        return {"positive": 5, "neutral": 3, "negative": 1}[category]
