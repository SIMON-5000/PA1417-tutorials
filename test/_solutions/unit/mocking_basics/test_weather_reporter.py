from unittest.mock import MagicMock
from src.unit.mocking_basics.weather_reporter import WeatherReporter


def test_get_report_formats_string():
    # Arrange
    mock_service = MagicMock()
    mock_service.get_temperature.return_value = 22
    reporter = WeatherReporter(mock_service)
    # Act
    result = reporter.get_report("Karlskrona")
    # Assert
    assert result == "The temperature in Karlskrona is 22°C."


def test_get_report_uses_correct_city():
    # Arrange
    mock_service = MagicMock()
    mock_service.get_temperature.return_value = -5
    reporter = WeatherReporter(mock_service)
    # Act
    result = reporter.get_report("Stockholm")
    # Assert
    assert result == "The temperature in Stockholm is -5°C."
