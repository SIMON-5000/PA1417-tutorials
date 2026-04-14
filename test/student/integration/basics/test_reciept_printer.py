from src.integration.basics.price_formatter import PriceFormatter
from src.integration.basics.receipt_printer import ReceiptPrinter
import pytest

@pytest.mark.integ
def test_receipt_printer():
    price_formatter = PriceFormatter()
    reciept_printer = ReceiptPrinter(price_formatter)

    RECIEPTS = [("Kladdkaka", 55), ("Chokladpudding", 28),
                ("Äppelpaj", 74.99), ("Bullar", 28.995)]
    
    result = reciept_printer.print_receipt(RECIEPTS)

    assert result == ["  Kladdkaka: 55.00 SEK",
                      "  Chokladpudding: 28.00 SEK", "  Äppelpaj: 74.99 SEK", "  Bullar: 29.00 SEK"]
