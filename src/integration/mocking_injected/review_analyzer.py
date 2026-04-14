from src.integration.mocking_injected.sentiment_api import SentimentApi


class ReviewAnalyzer:
    """Classifies a text review as positive, neutral, or negative.

    Delegates sentiment scoring to an injected SentimentApi. The
    classification thresholds are:
        score > 0  -> "positive"
        score == 0 -> "neutral"
        score < 0  -> "negative"

    Methods:
        classify(text) — return the sentiment category for text
    """

    def __init__(self, sentiment_api: SentimentApi) -> None:
        """Initialise a ReviewAnalyzer with the given sentiment API.

        parameters:
            sentiment_api -- a SentimentApi used to score text

        returns:
            none
        """
        self._api = sentiment_api

    def classify(self, text: str) -> str:
        """Return the sentiment category for a review text.

        parameters:
            text -- the review text to classify

        returns:
            "positive" -- if the sentiment score is greater than 0
            "neutral"  -- if the sentiment score is exactly 0
            "negative" -- if the sentiment score is less than 0
        """
        score = self._api.analyze(text)
        if score > 0:
            return "positive"
        if score < 0:
            return "negative"
        return "neutral"
