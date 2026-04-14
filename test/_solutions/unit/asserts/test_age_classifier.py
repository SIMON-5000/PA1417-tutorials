import pytest
from src.unit.asserts.age_classifier import classify_age


def test_infant():
    # Arrange
    # (nothing to set up)
    # Act
    result = classify_age(1)
    # Assert
    assert result == "infant"


def test_child():
    # Arrange
    # (nothing to set up)
    # Act
    result = classify_age(8)
    # Assert
    assert result == "child"


def test_teenager():
    # Arrange
    # (nothing to set up)
    # Act
    result = classify_age(15)
    # Assert
    assert result == "teenager"


def test_adult():
    # Arrange
    # (nothing to set up)
    # Act
    result = classify_age(30)
    # Assert
    assert result == "adult"


def test_senior():
    # Arrange
    # (nothing to set up)
    # Act
    result = classify_age(70)
    # Assert
    assert result == "senior"

# Two ways to test that a function raises an exception.
# Both are correct — v1 is more explicit, v2 is the pytest shorthand.

def test_negative_age_raises_v1():
    # V1: explicit flag variable.
    # We set a flag to False, call the function inside a try/except,
    # and set the flag to True if the expected exception is caught.
    # The final assert checks that the exception actually occurred.
    # Arrange
    exception_was_raised = False
    # Act
    try:
        classify_age(-1)
    except ValueError:
        exception_was_raised = True
    # Assert
    assert exception_was_raised

def test_negative_age_raises_v2():
    # V2: pytest.raises context manager.
    # pytest.raises(ValueError) wraps the call and automatically fails
    # the test if the expected exception is NOT raised — same logic as
    # v1 but written as a single block.
    # Arrange
    # (nothing to set up)
    # Act / Assert
    with pytest.raises(ValueError):
        classify_age(-1)
