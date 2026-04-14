import pytest
from src.unit.parameterization.triangle_type import triangle_type


@pytest.mark.parametrize("a, b, c, expected", [
    pytest.param(3, 3, 3, "equilateral", id="all-sides-equal"),
    pytest.param(3, 3, 5, "isosceles",   id="isosceles-first-two-match"),
    pytest.param(3, 5, 3, "isosceles",   id="isosceles-first-last-match"),
    pytest.param(5, 3, 3, "isosceles",   id="isosceles-last-two-match"),
    pytest.param(3, 4, 5, "scalene",     id="scalene-small"),
    pytest.param(7, 10, 5, "scalene",    id="scalene-larger"),
])
def test_triangle_type(a, b, c, expected):
    # Arrange + Act
    result = triangle_type(a, b, c)
    # Assert
    assert result == expected


def test_degenerate_triangle_raises():
    with pytest.raises(ValueError):
        triangle_type(1, 2, 10)


def test_nonpositive_side_raises():
    with pytest.raises(ValueError):
        triangle_type(0, 3, 3)
