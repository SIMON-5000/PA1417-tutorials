class WeatherReporter:
    """Reports current weather for a city.

    parameters:
        weather_service -- a service with a get_temperature(city) method

    methods:
        get_report(city) -- return a formatted weather report string
    """

    def __init__(self, weather_service):
        """Initialise a WeatherReporter with the given weather service.

        parameters:
            weather_service -- a service with a get_temperature(city) method

        returns:
            none
        """
        self._weather_service = weather_service

    def get_report(self, city: str) -> str:
        """Return a formatted weather report for the given city.

        parameters:
            city -- the name of the city to report on

        returns:
            a string of the form "The temperature in <city> is <temp>°C."
        """
        temperature = self._weather_service.get_temperature(city)
        return f"The temperature in {city} is {temperature}°C."
