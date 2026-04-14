from src.unit.mocking_patching.email_client import EmailClient


class InvoiceMailer:
    """Sends invoice emails to customers.

    methods:
        send_invoice(customer_email, amount) -- send an invoice email; returns True on success
    """

    def send_invoice(self, customer_email: str, amount: float) -> bool:
        """Send an invoice email to a customer for the given amount.

        parameters:
            customer_email -- the email address to send the invoice to
            amount         -- the invoice total in SEK

        returns:
            True  -- if the email was sent successfully
            False -- if the email failed to send
        """
        client = EmailClient()
        subject = "Your Invoice"
        body = f"Your invoice total is {amount} SEK."
        return client.send(customer_email, subject, body)
