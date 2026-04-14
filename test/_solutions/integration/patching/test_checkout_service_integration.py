from unittest.mock import patch
from src.integration.patching.currency_converter import CurrencyConverter
from src.integration.patching.checkout_service import CheckoutService


# This is an integration test — CheckoutService (A) and CurrencyConverter (B)
# both run with their real implementations. Only ExchangeApi (C) is patched,
# because CurrencyConverter creates it internally and it would require a live
# network connection.
#
# Namespace rule: ExchangeApi is imported inside currency_converter.py, so
# patch it there — src.currency_converter.ExchangeApi — not at its definition
# site (src.exchange_api.ExchangeApi). Once the import has run, the name
# ExchangeApi lives in CurrencyConverter's namespace, and that is the one
# patch must replace.
#
# Compare this to Tutorial 07 (Unit Tests — Mocking Patching), where
# InvoiceMailer was tested in full isolation. Here, CheckoutService is real
# and calls the real CurrencyConverter. The integration between A and B is
# what we are testing; patching C simply removes the network dependency.


def test_total_in_eur_applies_correct_rate():
    # Arrange
    with patch("src.integration.patching.currency_converter.ExchangeApi") as MockApi:
        mock_api = MockApi.return_value
        mock_api.get_rate.return_value = 0.087       # 1 SEK = 0.087 EUR
        converter = CurrencyConverter()              # real converter
        service = CheckoutService(converter)         # real checkout
        # Act
        result = service.total_in(1000.0, "EUR")
        # Assert
        assert result == 87.0


def test_total_in_usd_applies_correct_rate():
    # Arrange
    with patch("src.integration.patching.currency_converter.ExchangeApi") as MockApi:
        mock_api = MockApi.return_value
        mock_api.get_rate.return_value = 0.095       # 1 SEK = 0.095 USD
        converter = CurrencyConverter()
        service = CheckoutService(converter)
        # Act
        result = service.total_in(200.0, "USD")
        # Assert
        assert result == 19.0


def test_total_in_same_currency_uses_rate_of_one():
    # Arrange
    with patch("src.integration.patching.currency_converter.ExchangeApi") as MockApi:
        mock_api = MockApi.return_value
        mock_api.get_rate.return_value = 1.0
        converter = CurrencyConverter()
        service = CheckoutService(converter)
        # Act
        result = service.total_in(500.0, "SEK")
        # Assert
        assert result == 500.0
