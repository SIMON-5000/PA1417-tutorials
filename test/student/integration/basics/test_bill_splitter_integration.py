from src.integration.basics.tip_calculator import TipCalculator
from src.integration.basics.bill_splitter import BillSplitter
import pytest

# TODO: Write integration tests for BillSplitter.
@pytest.mark.integ
def test_billsplitter():
    """Integration test for billsplitter"""
   
    # Arrange
    tip_calculator = TipCalculator()
    bill_splitter = BillSplitter(tip_calculator)

    # Act
    amount = bill_splitter.split(100.0, 2, 2)

    # Assert
    assert amount == 51.0
