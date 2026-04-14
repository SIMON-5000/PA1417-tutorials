class EmailClient:
    """Sends emails over a real mail server connection.

    methods:
        send(to, subject, body) -- send an email; returns True on success, False on failure
    """

    def send(self, to: str, subject: str, body: str) -> bool:
        """Send an email to the given address.

        parameters:
            to      -- the recipient's email address
            subject -- the email subject line
            body    -- the email body text

        returns:
            True  -- if the email was sent successfully
            False -- if the email failed to send

        note:
            This method is intentionally not implemented.
        """
        raise NotImplementedError("requires a live mail server connection")
