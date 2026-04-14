import pytest
from src.unit.parameterization.palindrome import is_palindrome


# is_palindrome accepts any string — the input domain is infinite.
# We cannot test every possible string, so we choose a representative
# sample that covers the cases that matter:
#
#   - empty string and single character (boundary cases)
#   - a palindrome with an odd number of characters
#   - a palindrome with an even number of characters
#   - strings that are clearly not palindromes
#   - a case-sensitivity edge case
#
# This is equivalence partitioning applied to an infinite domain.
# Parametrize lets us express all these cases compactly without
# writing a separate function for each one.

@pytest.mark.parametrize("s, expected", [
    ("",        True),   # empty string is trivially a palindrome
    ("a",       True),   # single character is always a palindrome
    ("racecar", True),   # odd-length palindrome
    ("noon",    True),   # even-length palindrome
    ("hello",   False),  # not a palindrome
    ("world",   False),  # not a palindrome
    ("Racecar", False),  # case-sensitive: R ≠ r
])
def test_is_palindrome(s, expected):
    # Arrange
    # (handled by parametrize)
    # Act
    result = is_palindrome(s)
    # Assert
    assert result == expected
