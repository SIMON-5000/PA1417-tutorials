from unittest.mock import MagicMock
from src.integration.mocking_injected.risk_database import RiskDatabase
from src.integration.mocking_injected.fraud_detector import FraudDetector
from src.integration.mocking_injected.payment_processor import PaymentProcessor


def test_high_risk_customer_is_blocked():
    # Arrange
    mock_db = MagicMock(spec=RiskDatabase)
    mock_db.get_score.return_value = 95       # above both thresholds
    detector = FraudDetector(mock_db)         # real — both methods tested
    processor = PaymentProcessor(detector)    # real
    # Act
    result = processor.process("cust-1", 500.0)
    # Assert: score > 90 -> blocked
    assert result == "blocked"


def test_elevated_risk_customer_is_flagged():
    mock_db = MagicMock(spec=RiskDatabase)
    mock_db.get_score.return_value = 80       # above 70 but not above 90
    detector = FraudDetector(mock_db)
    processor = PaymentProcessor(detector)
    # score > 70 but <= 90 -> flagged
    assert processor.process("cust-2", 200.0) == "flagged"


def test_low_risk_customer_is_approved():
    mock_db = MagicMock(spec=RiskDatabase)
    mock_db.get_score.return_value = 30       # below both thresholds
    detector = FraudDetector(mock_db)
    processor = PaymentProcessor(detector)
    assert processor.process("cust-3", 150.0) == "approved: 150.0 SEK"


def test_boundary_score_70_is_approved():
    mock_db = MagicMock(spec=RiskDatabase)
    mock_db.get_score.return_value = 70       # boundary: not > 70, so clear
    detector = FraudDetector(mock_db)
    processor = PaymentProcessor(detector)
    assert processor.process("cust-4", 100.0) == "approved: 100.0 SEK"
