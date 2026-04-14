def fizzbuzz(n: int) -> str:
    """Return the FizzBuzz result for a positive integer.

    parameters:
        n -- a positive integer

    returns:
        "FizzBuzz" -- if n is divisible by both 3 and 5
        "Fizz"     -- if n is divisible by 3 only
        "Buzz"     -- if n is divisible by 5 only
        str(n)     -- if n is not divisible by 3 or 5
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
