class WeatherApi:
    """Client for a live weather data service.

    In production this class would make a network request.

    Methods:
        get_conditions(city) — return a dict with keys "temp_c" (float)
                               and "condition" (str, e.g. "sunny")
    """

    def get_conditions(self, city: str) -> dict:
        """Return current weather conditions for the given city.

        parameters:
            city -- the name of the city to look up

        returns:
            a dict with keys:
                "temp_c"    -- float, the current temperature in Celsius
                "condition" -- str, a description such as "sunny"

        note:
            This method is intentionally not implemented.
        """
        raise NotImplementedError("WeatherApi requires a live connection")
