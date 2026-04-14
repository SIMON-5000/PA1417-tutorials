import pytest
from unittest.mock import MagicMock
from src.unit.mocking_basics.cart_pricer import CartPricer


# When multiple tests need the same mock configured the same way,
# put the mock inside a @pytest.fixture — exactly like shared object
# setup from the unit test fixtures tutorial.

@pytest.fixture
def price_service():
    mock = MagicMock()
    mock.get_price.return_value = 5.0
    return mock


def test_total_single_item(price_service):
    # Arrange
    pricer = CartPricer(price_service)
    # Act
    result = pricer.total("apple", 1)
    # Assert
    assert result == 5.0


def test_total_multiple_items(price_service):
    # Arrange
    pricer = CartPricer(price_service)
    # Act
    result = pricer.total("apple", 3)
    # Assert
    assert result == 15.0


def test_total_zero_quantity(price_service):
    # Arrange
    pricer = CartPricer(price_service)
    # Act
    result = pricer.total("apple", 0)
    # Assert
    assert result == 0.0
