class SentimentApi:
    """Client for a remote sentiment-analysis service.

    In production this class would make a network request.

    Methods:
        analyze(text) — return a sentiment score in the range -1.0 to 1.0
                        (negative = negative sentiment, positive = positive)
    """

    def analyze(self, text: str) -> float:
        """Return a sentiment score for the given text.

        parameters:
            text -- the text to analyse

        returns:
            a float from -1.0 (most negative) to 1.0 (most positive)

        note:
            This method is intentionally not implemented.
        """
        raise NotImplementedError("SentimentApi requires a live connection")
