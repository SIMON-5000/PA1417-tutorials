import pytest
from src.unit.fixtures.stack import Stack


@pytest.fixture
def stack():
    s = Stack()
    s.push("first")
    s.push("second")
    s.push("third")
    return s


def test_size(stack):
    # Arrange
    # (handled by fixture)
    # Act
    result = stack.size()
    # Assert
    assert result == 3


def test_is_not_empty(stack):
    # Arrange
    # (handled by fixture)
    # Act
    result = stack.is_empty()
    # Assert
    assert not result


def test_peek_returns_top(stack):
    # Arrange
    # (handled by fixture)
    # Act
    result = stack.peek()
    # Assert
    assert result == "third"


def test_pop_returns_top(stack):
    # Arrange
    # (handled by fixture)
    # Act
    result = stack.pop()
    # Assert
    assert result == "third"


def test_pop_decreases_size(stack):
    # Arrange
    # (handled by fixture)
    # Act
    stack.pop()
    result = stack.size()
    # Assert
    assert result == 2


def test_pop_empty_raises():
    # Arrange
    # This test needs an empty stack, so we create one directly
    # rather than using the pre-populated fixture.
    s = Stack()
    # Act / Assert
    with pytest.raises(ValueError):
        s.pop()


def test_peek_empty_raises():
    # Arrange
    s = Stack()
    # Act / Assert
    with pytest.raises(ValueError):
        s.peek()
