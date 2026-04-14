def day_type(day: str) -> str:
    """Return whether a day name is a weekday or weekend.

    parameters:
        day -- the name of the day (e.g. "Monday")

    returns:
        "weekday" -- if day is Monday through Friday
        "weekend" -- if day is Saturday or Sunday

    raises:
        ValueError -- if day is not a recognised day name
    """
    weekdays = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
    weekend = {"Saturday", "Sunday"}
    if day in weekdays:
        return "weekday"
    if day in weekend:
        return "weekend"
    raise ValueError(f"Unrecognised day: {day}")
