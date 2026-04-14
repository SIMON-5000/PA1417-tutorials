from unittest.mock import MagicMock
from src.integration.mocking_injected.loyalty_service import LoyaltyService
from src.integration.mocking_injected.discount_engine import DiscountEngine
from src.integration.mocking_injected.order_pricer import OrderPricer


# This is an integration test — OrderPricer (A) and DiscountEngine (B) both
# run with their real implementations. Only LoyaltyService (C) is mocked,
# because it would require a live network connection.
#
# What distinguishes this from a unit test of OrderPricer?
# In a unit test of OrderPricer you would mock DiscountEngine entirely —
# passing a MagicMock() in place of the real engine. That isolates OrderPricer
# completely but tests nothing about how DiscountEngine behaves. Here we keep
# DiscountEngine real, so the test also covers the logic inside it: the points
# threshold, the discount rate, and the subtraction. If either class has a bug,
# this test will catch it.
#
# Ask yourself: if you replaced the real DiscountEngine with a MagicMock(),
# would this still be an integration test?
# No — you would be testing OrderPricer in isolation, which is a unit test of A.
# The integration between A and B disappears the moment B becomes a mock.


def test_loyal_customer_receives_discount():
    # Arrange
    mock_loyalty = MagicMock(spec=LoyaltyService)
    mock_loyalty.get_points.return_value = 150   # above threshold
    engine = DiscountEngine(mock_loyalty)         # real engine
    pricer = OrderPricer(engine)                  # real pricer
    # Act
    result = pricer.price("cust-1", 200.0)
    # Assert: 10 % off 200 = 20 discount → 180 final
    assert result == 180.0


def test_new_customer_pays_full_price():
    # Arrange
    mock_loyalty = MagicMock(spec=LoyaltyService)
    mock_loyalty.get_points.return_value = 50    # below threshold
    engine = DiscountEngine(mock_loyalty)
    pricer = OrderPricer(engine)
    # Act
    result = pricer.price("cust-2", 200.0)
    # Assert: no discount
    assert result == 200.0


def test_customer_exactly_at_threshold_receives_discount():
    # Arrange
    mock_loyalty = MagicMock(spec=LoyaltyService)
    mock_loyalty.get_points.return_value = 100   # exactly at threshold
    engine = DiscountEngine(mock_loyalty)
    pricer = OrderPricer(engine)
    # Act
    result = pricer.price("cust-3", 500.0)
    # Assert: threshold is inclusive → 10 % off → 450
    assert result == 450.0
