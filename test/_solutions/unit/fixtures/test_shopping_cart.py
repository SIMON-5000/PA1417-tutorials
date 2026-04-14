import pytest
from src.unit.fixtures.shopping_cart import ShoppingCart


@pytest.fixture
def empty_cart():
    return ShoppingCart()


@pytest.fixture
def stocked_cart():
    cart = ShoppingCart()
    cart.add_item("apple", 1.50)
    cart.add_item("bread", 2.00)
    cart.add_item("milk", 0.99)
    return cart


# --- tests that need an empty cart ---

def test_new_cart_is_empty(empty_cart):
    assert empty_cart.is_empty() is True


def test_new_cart_total_is_zero(empty_cart):
    assert empty_cart.total() == 0.0


def test_new_cart_item_count_is_zero(empty_cart):
    assert empty_cart.item_count() == 0


def test_add_item_cart_is_no_longer_empty(empty_cart):
    empty_cart.add_item("apple", 1.50)
    assert empty_cart.is_empty() is False


def test_add_item_increases_count(empty_cart):
    empty_cart.add_item("apple", 1.50)
    assert empty_cart.item_count() == 1


# --- tests that need a pre-populated cart ---

def test_stocked_cart_item_count(stocked_cart):
    assert stocked_cart.item_count() == 3


def test_stocked_cart_total(stocked_cart):
    assert stocked_cart.total() == pytest.approx(4.49)


def test_remove_item_decreases_count(stocked_cart):
    stocked_cart.remove_item("apple")
    assert stocked_cart.item_count() == 2


def test_remove_item_adjusts_total(stocked_cart):
    stocked_cart.remove_item("apple")
    assert stocked_cart.total() == pytest.approx(2.99)


def test_remove_nonexistent_item_raises(stocked_cart):
    with pytest.raises(ValueError):
        stocked_cart.remove_item("banana")
