from src.integration.basics.price_formatter import PriceFormatter
import pytest

@pytest.mark.integ
def test_price_formatter():
    formatter = PriceFormatter()

    assert formatter.format(100.001) == "100.00 SEK"