from unittest.mock import patch
from src.unit.mocking_patching.shop_assistant import ShopAssistant


# ShopAssistant creates both StockChecker() and PriceFetcher() internally.
# We need to patch both. Stacked @patch decorators are applied bottom-up,
# and their mock parameters arrive in the same bottom-up order:
#
#   @patch("...PriceFetcher")    # outermost  ->  second parameter
#   @patch("...StockChecker")    # innermost  ->  first parameter
#   def test_...(MockStockChecker, MockPriceFetcher):


@patch("src.unit.mocking_patching.shop_assistant.PriceFetcher")
@patch("src.unit.mocking_patching.shop_assistant.StockChecker")
def test_describe_available_item(MockStockChecker, MockPriceFetcher):
    # Arrange
    MockStockChecker.return_value.is_in_stock.return_value = True
    MockPriceFetcher.return_value.get_price.return_value = 199.0
    assistant = ShopAssistant()
    # Act
    result = assistant.describe("Headphones")
    # Assert
    assert result == "Headphones: available at 199.0 SEK."


@patch("src.unit.mocking_patching.shop_assistant.PriceFetcher")
@patch("src.unit.mocking_patching.shop_assistant.StockChecker")
def test_describe_out_of_stock_item(MockStockChecker, MockPriceFetcher):
    # Arrange
    MockStockChecker.return_value.is_in_stock.return_value = False
    MockPriceFetcher.return_value.get_price.return_value = 89.0
    assistant = ShopAssistant()
    # Act
    result = assistant.describe("USB Cable")
    # Assert
    assert result == "USB Cable: out of stock at 89.0 SEK."
