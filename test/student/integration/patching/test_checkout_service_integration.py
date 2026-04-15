from unittest.mock import patch
from src.integration.patching.currency_converter import CurrencyConverter, ExchangeApi  
from src.integration.patching.checkout_service import CheckoutService
import pytest
from unittest import mock

# TODO: Write integration tests for CheckoutService + CurrencyConverter,
#       with ExchangeApi patched.

@pytest.fixture
def checkout_service():
    with patch("src.integration.patching.currency_converter.ExchangeApi") as mock_api_class:
        
        mock_api = mock.MagicMock()
        mock_api.get_rate.return_value = 2.0

        print("\n\n PRINTS INCOMMING: ")
        print(type(mock_api_class))
        print(type(mock_api), mock_api.get_rate())
        print("\nEND\n")

        mock_api_class.return_value = mock_api
        
        currency_converter = CurrencyConverter()
        checkout_service = CheckoutService(currency_converter)        
        # We use YIELD to 'keep the mock alive' in the tests.
        # It is only active inside the 'with patch'-scope
        yield checkout_service

@pytest.mark.integ
def test_checkout_service_integration(checkout_service):
    result = checkout_service.total_in(10.0, "SEK")
    assert result == 20.00