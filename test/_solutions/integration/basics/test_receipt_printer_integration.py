from src.integration.basics.price_formatter import PriceFormatter
from src.integration.basics.receipt_printer import ReceiptPrinter


def test_empty_items_returns_empty_list():
    # Arrange — both components are real
    formatter = PriceFormatter()
    printer = ReceiptPrinter(formatter)
    # Act
    result = printer.print_receipt([])
    # Assert
    assert result == []


def test_single_item_receipt():
    formatter = PriceFormatter()
    printer = ReceiptPrinter(formatter)
    # Act
    result = printer.print_receipt([("Apple", 1.5)])
    # Assert: formatter is called once, producing the correct line
    assert result == ["  Apple: 1.50 SEK"]


def test_multiple_items_produces_one_line_each():
    formatter = PriceFormatter()
    printer = ReceiptPrinter(formatter)
    # Act
    result = printer.print_receipt([("Apple", 1.5), ("Bread", 2.0), ("Milk", 0.99)])
    # Assert: formatter is called once per item
    assert len(result) == 3
    assert result[0] == "  Apple: 1.50 SEK"
    assert result[1] == "  Bread: 2.00 SEK"
    assert result[2] == "  Milk: 0.99 SEK"


def test_items_appear_in_input_order():
    formatter = PriceFormatter()
    printer = ReceiptPrinter(formatter)
    result = printer.print_receipt([("Z-item", 5.0), ("A-item", 1.0)])
    assert result[0] == "  Z-item: 5.00 SEK"
    assert result[1] == "  A-item: 1.00 SEK"
