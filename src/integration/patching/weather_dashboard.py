from src.integration.patching.weather_formatter import WeatherFormatter


class WeatherDashboard:
    """Displays weather information for a city.

    Delegates formatting to an injected WeatherFormatter.

    Methods:
        display(city) — return the dashboard line for the city
    """

    def __init__(self, formatter: WeatherFormatter) -> None:
        """Initialise a WeatherDashboard with the given weather formatter.

        parameters:
            formatter -- a WeatherFormatter used to generate weather summaries

        returns:
            none
        """
        self._formatter = formatter

    def display(self, city: str) -> str:
        """Return the dashboard weather line for the given city.

        parameters:
            city -- the name of the city to display weather for

        returns:
            a string of the form "Weather report — <formatted summary>"
        """
        return f"Weather report — {self._formatter.format(city)}"
