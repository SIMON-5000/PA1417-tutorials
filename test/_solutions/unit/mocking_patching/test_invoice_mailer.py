from unittest.mock import patch
from src.unit.mocking_patching.invoice_mailer import InvoiceMailer


# InvoiceMailer creates an EmailClient() *inside* send_invoice — we cannot
# inject a mock via the constructor. patch() temporarily replaces EmailClient
# in the invoice_mailer module's namespace for the duration of the test.
#
# Namespace rule: patch where the name is *used* (src.invoice_mailer.EmailClient),
# not where it is defined (src.email_client.EmailClient).


def test_send_invoice_returns_true_on_success():
    # Arrange
    with patch("src.unit.mocking_patching.invoice_mailer.EmailClient") as MockEmailClient:
        mock_client = MockEmailClient.return_value
        mock_client.send.return_value = True
        mailer = InvoiceMailer()
        # Act
        result = mailer.send_invoice("customer@example.com", 499.0)
        # Assert
        assert result is True


def test_send_invoice_returns_false_on_failure():
    # Arrange
    with patch("src.unit.mocking_patching.invoice_mailer.EmailClient") as MockEmailClient:
        mock_client = MockEmailClient.return_value
        mock_client.send.return_value = False
        mailer = InvoiceMailer()
        # Act
        result = mailer.send_invoice("customer@example.com", 499.0)
        # Assert
        assert result is False
