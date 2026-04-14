from src.unit.asserts.sign import sign


def test_negative():
    # Arrange
    # (nothing to set up)
    # Act
    result = sign(-1)
    # Assert
    assert result == "negative"


def test_zero():
    # Arrange
    # (nothing to set up)
    # Act
    result = sign(0)
    # Assert
    assert result == "zero"


def test_positive():
    # Arrange
    # (nothing to set up)
    # Act
    result = sign(1)
    # Assert
    assert result == "positive"
