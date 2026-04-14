def classify_age(age: int) -> str:
    """Classify a person's life stage based on their age.

    parameters:
        age -- a non-negative integer representing age in years

    returns:
        "infant"   -- if age is 0 to 2
        "child"    -- if age is 3 to 12
        "teenager" -- if age is 13 to 17
        "adult"    -- if age is 18 to 64
        "senior"   -- if age is 65 or above

    raises:
        ValueError -- if age is negative
    """
    if age < 0:
        raise ValueError(f"Age cannot be negative, got {age}")
    if age <= 2:
        return "infant"
    if age <= 12:
        return "child"
    if age <= 17:
        return "teenager"
    if age <= 64:
        return "adult"
    return "senior"
