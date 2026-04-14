class RiskDatabase:
    """Client for a remote fraud-risk scoring service.

    In production this class would query an external database.

    Methods:
        get_score(customer_id) — return an integer risk score from 0 (no risk)
                                 to 100 (highest risk)
    """

    def get_score(self, customer_id: str) -> int:
        """Return an integer risk score for the given customer.

        parameters:
            customer_id -- the unique identifier of the customer

        returns:
            an integer from 0 (no risk) to 100 (highest risk)

        note:
            This method is intentionally not implemented.
        """
        raise NotImplementedError("RiskDatabase requires a live connection")
