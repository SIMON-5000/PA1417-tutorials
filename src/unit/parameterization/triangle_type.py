def triangle_type(a: float, b: float, c: float) -> str:
    """Classify a triangle by its three side lengths.

    parameters:
        a -- the first side length (must be positive)
        b -- the second side length (must be positive)
        c -- the third side length (must be positive)

    returns:
        "equilateral" -- if all three sides are equal
        "isosceles"   -- if exactly two sides are equal
        "scalene"     -- if no two sides are equal

    raises:
        ValueError -- if any side is non-positive, or if the sides do not
                     satisfy the triangle inequality
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError(
            f"Sides {a}, {b}, {c} do not satisfy the triangle inequality"
        )
    if a == b == c:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    return "scalene"
