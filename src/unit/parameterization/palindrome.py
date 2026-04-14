def is_palindrome(s: str) -> bool:
    """Return True if the string reads the same forwards and backwards.

    parameters:
        s -- the string to check

    returns:
        True  -- if s is a palindrome
        False -- if s is not a palindrome

    note:
        The check is case-sensitive. "Racecar" is not a palindrome
        because the capital R does not match the lowercase r.
    """
    return s == s[::-1]
