from src.integration.patching.weather_api import WeatherApi


class WeatherFormatter:
    """Produces a human-readable weather summary for a city.

    Creates its own WeatherApi internally — the dependency is hard-coded,
    not injected. To test this class without a live connection, patch
    WeatherApi in this module's namespace:
        patch("src.integration.patching.weather_formatter.WeatherApi")

    Methods:
        format(city) — return a formatted weather string for the city
    """

    def format(self, city: str) -> str:
        """Return a formatted weather summary string for the given city.

        parameters:
            city -- the name of the city to look up

        returns:
            a string of the form "<city>: <condition>, <temp_c>°C"
            (e.g. "Karlskrona: sunny, 22°C")
        """
        api = WeatherApi()
        data = api.get_conditions(city)
        return f"{city}: {data['condition']}, {data['temp_c']}°C"
