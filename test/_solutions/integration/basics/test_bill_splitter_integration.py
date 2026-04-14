from src.integration.basics.tip_calculator import TipCalculator
from src.integration.basics.bill_splitter import BillSplitter


# This is an integration test — TipCalculator and BillSplitter both run with
# their real implementations. No mocks, no fixtures, no external resources.
#
# What makes this an integration test rather than a unit test of BillSplitter?
# BillSplitter delegates tip calculation to TipCalculator. When we test with a
# real TipCalculator, we verify that the two components work correctly together
# — the integration between them. A unit test of BillSplitter would pass a
# MagicMock() in place of TipCalculator, isolating BillSplitter completely and
# testing its logic independently of TipCalculator's logic.


def test_split_ten_percent_tip_among_two():
    # Arrange — both components are real
    calculator = TipCalculator()
    splitter = BillSplitter(calculator)
    # Act
    result = splitter.split(bill=100.0, tip_percent=10.0, num_people=2)
    # Assert: bill=100, tip=10, total=110, each person owes 55
    assert result == 55.0


def test_split_with_no_tip():
    # Arrange
    calculator = TipCalculator()
    splitter = BillSplitter(calculator)
    # Act
    result = splitter.split(bill=60.0, tip_percent=0.0, num_people=3)
    # Assert: no tip, each person owes 20
    assert result == 20.0


def test_split_uneven_amounts_are_rounded():
    # Arrange
    calculator = TipCalculator()
    splitter = BillSplitter(calculator)
    # Act
    result = splitter.split(bill=100.0, tip_percent=15.0, num_people=3)
    # Assert: bill=100, tip=15, total=115, each person owes 38.33
    assert result == 38.33
