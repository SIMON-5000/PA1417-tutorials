from src.unit.asserts.fizzbuzz import fizzbuzz


def test_fizzbuzz():
    # Arrange
    # (nothing to set up)
    # Act
    result = fizzbuzz(15)
    # Assert
    assert result == "FizzBuzz"


def test_fizz():
    # Arrange
    # (nothing to set up)
    # Act
    result = fizzbuzz(9)
    # Assert
    assert result == "Fizz"


def test_buzz():
    # Arrange
    # (nothing to set up)
    # Act
    result = fizzbuzz(10)
    # Assert
    assert result == "Buzz"


def test_number():
    # Arrange
    # (nothing to set up)
    # Act
    result = fizzbuzz(7)
    # Assert
    assert result == "7"
