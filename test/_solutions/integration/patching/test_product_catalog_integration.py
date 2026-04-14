from unittest.mock import patch
from src.integration.patching.store_inventory import StoreInventory
from src.integration.patching.product_catalog import ProductCatalog


def test_item_in_stock_at_normal_price():
    with patch("src.integration.patching.store_inventory.PriceApi") as MockPriceApi, \
         patch("src.integration.patching.store_inventory.StockApi") as MockStockApi:
        MockPriceApi.return_value.get_price.return_value = 49.99
        MockStockApi.return_value.in_stock.return_value = True
        inventory = StoreInventory()           # real
        catalog = ProductCatalog(inventory)    # real
        # Act
        result = catalog.describe("SKU-001")
        # Assert
        assert result == "SKU-001: 49.99 SEK, in stock"


def test_item_out_of_stock():
    with patch("src.integration.patching.store_inventory.PriceApi") as MockPriceApi, \
         patch("src.integration.patching.store_inventory.StockApi") as MockStockApi:
        MockPriceApi.return_value.get_price.return_value = 199.0
        MockStockApi.return_value.in_stock.return_value = False
        inventory = StoreInventory()
        catalog = ProductCatalog(inventory)
        assert catalog.describe("SKU-002") == "SKU-002: 199.0 SEK, out of stock"


def test_expensive_item_in_stock():
    with patch("src.integration.patching.store_inventory.PriceApi") as MockPriceApi, \
         patch("src.integration.patching.store_inventory.StockApi") as MockStockApi:
        MockPriceApi.return_value.get_price.return_value = 2499.0
        MockStockApi.return_value.in_stock.return_value = True
        inventory = StoreInventory()
        catalog = ProductCatalog(inventory)
        assert catalog.describe("SKU-003") == "SKU-003: 2499.0 SEK, in stock"
