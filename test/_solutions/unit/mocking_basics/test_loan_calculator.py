from unittest.mock import MagicMock
from src.unit.mocking_basics.loan_calculator import LoanCalculator


def test_total_repayment_includes_interest_and_fee():
    # Arrange
    mock_rate_service = MagicMock()
    mock_rate_service.get_rate.return_value = 0.1  # 10%
    mock_fee_service = MagicMock()
    mock_fee_service.get_fee.return_value = 50.0
    calculator = LoanCalculator(mock_rate_service, mock_fee_service)
    # Act
    result = calculator.total_repayment(1000.0)
    # Assert
    assert result == 1150.0  # 1000 + 100 interest + 50 fee


def test_total_repayment_zero_interest():
    # Arrange
    mock_rate_service = MagicMock()
    mock_rate_service.get_rate.return_value = 0.0
    mock_fee_service = MagicMock()
    mock_fee_service.get_fee.return_value = 25.0
    calculator = LoanCalculator(mock_rate_service, mock_fee_service)
    # Act
    result = calculator.total_repayment(500.0)
    # Assert
    assert result == 525.0  # 500 + 0 interest + 25 fee


def test_total_repayment_zero_fee():
    # Arrange
    mock_rate_service = MagicMock()
    mock_rate_service.get_rate.return_value = 0.05
    mock_fee_service = MagicMock()
    mock_fee_service.get_fee.return_value = 0.0
    calculator = LoanCalculator(mock_rate_service, mock_fee_service)
    # Act
    result = calculator.total_repayment(200.0)
    # Assert
    assert result == 210.0  # 200 + 10 interest + 0 fee
