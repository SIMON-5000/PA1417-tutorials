def sign(n: int) -> str:
    """Return the sign of an integer as a string.

    parameters:
        n -- an integer value

    returns:
        "negative" -- if n is less than 0
        "zero"     -- if n is equal to 0
        "positive" -- if n is greater than 0
    """
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
