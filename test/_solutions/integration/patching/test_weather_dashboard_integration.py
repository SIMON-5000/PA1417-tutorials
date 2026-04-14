from unittest.mock import patch
from src.integration.patching.weather_formatter import WeatherFormatter
from src.integration.patching.weather_dashboard import WeatherDashboard


def test_sunny_weather_report():
    with patch("src.integration.patching.weather_formatter.WeatherApi") as MockApi:
        mock_api = MockApi.return_value
        mock_api.get_conditions.return_value = {"temp_c": 24, "condition": "sunny"}
        formatter = WeatherFormatter()        # real
        dashboard = WeatherDashboard(formatter)  # real
        # Act
        result = dashboard.display("Karlskrona")
        # Assert
        assert result == "Weather report — Karlskrona: sunny, 24°C"


def test_rainy_weather_report():
    with patch("src.integration.patching.weather_formatter.WeatherApi") as MockApi:
        mock_api = MockApi.return_value
        mock_api.get_conditions.return_value = {"temp_c": 10, "condition": "rainy"}
        formatter = WeatherFormatter()
        dashboard = WeatherDashboard(formatter)
        assert dashboard.display("Gothenburg") == "Weather report — Gothenburg: rainy, 10°C"


def test_snowy_weather_report():
    with patch("src.integration.patching.weather_formatter.WeatherApi") as MockApi:
        mock_api = MockApi.return_value
        mock_api.get_conditions.return_value = {"temp_c": -5, "condition": "snowy"}
        formatter = WeatherFormatter()
        dashboard = WeatherDashboard(formatter)
        assert dashboard.display("Stockholm") == "Weather report — Stockholm: snowy, -5°C"
