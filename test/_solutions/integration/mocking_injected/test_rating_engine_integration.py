from unittest.mock import MagicMock
from src.integration.mocking_injected.sentiment_api import SentimentApi
from src.integration.mocking_injected.review_analyzer import ReviewAnalyzer
from src.integration.mocking_injected.rating_engine import RatingEngine


def test_positive_review_gets_five_stars():
    # Arrange
    mock_api = MagicMock(spec=SentimentApi)
    mock_api.analyze.return_value = 0.8       # strong positive
    analyzer = ReviewAnalyzer(mock_api)        # real
    engine = RatingEngine(analyzer)            # real
    # Act
    result = engine.star_rating("Great product!")
    # Assert: positive -> "positive" -> 5 stars
    assert result == 5


def test_neutral_review_gets_three_stars():
    mock_api = MagicMock(spec=SentimentApi)
    mock_api.analyze.return_value = 0.0        # exactly neutral
    analyzer = ReviewAnalyzer(mock_api)
    engine = RatingEngine(analyzer)
    assert engine.star_rating("It is a product.") == 3


def test_negative_review_gets_one_star():
    mock_api = MagicMock(spec=SentimentApi)
    mock_api.analyze.return_value = -0.6       # negative
    analyzer = ReviewAnalyzer(mock_api)
    engine = RatingEngine(analyzer)
    assert engine.star_rating("Terrible experience.") == 1
