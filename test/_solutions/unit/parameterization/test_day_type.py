import pytest
from src.unit.parameterization.day_type import day_type


# Without @pytest.mark.parametrize, every row in the table below would
# need its own test function — seven functions that are identical except
# for the day name and expected output. Any change to the test logic
# (e.g. adding a comment, renaming a variable) would have to be made
# in seven places.
#
# @pytest.mark.parametrize collapses them into one function. pytest
# runs it once for each row, and each run appears as a separate test
# in the output so failures are still easy to pinpoint.
#
# The string "day, expected" names the parameters that pytest will
# inject into each test run. Each tuple in the list is one test case.

@pytest.mark.parametrize("day, expected", [
    ("Monday",    "weekday"),
    ("Tuesday",   "weekday"),
    ("Wednesday", "weekday"),
    ("Thursday",  "weekday"),
    ("Friday",    "weekday"),
    ("Saturday",  "weekend"),
    ("Sunday",    "weekend"),
])
def test_day_type(day, expected):
    # Arrange
    # (handled by parametrize)
    # Act
    result = day_type(day)
    # Assert
    assert result == expected


# Not every test belongs in the parametrize table. This case tests
# different behaviour (an exception), so it stays as its own function.

def test_invalid_day_raises():
    # Arrange
    # (nothing to set up)
    # Act / Assert
    with pytest.raises(ValueError):
        day_type("Funday")
